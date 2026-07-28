# Technical Architecture Blueprint: CarePedia AI

## 1. System Architecture Diagram

```mermaid
graph TD
    subgraph B2C Users / End Consumers
        ClientBrowser[Next.js B2C Web Portal / PWA]
        SEOEngine[Search Engines / Organic pSEO Traffic]
    end

    subgraph B2B Professionals & Consultancies
        ProDashboard[Professional Portal & Content Studio]
        EmbedWidget[Embeddable Verified Badge & Media Kit Widget JS]
    end

    subgraph CarePedia AI Core Engine (Vercel Serverless)
        APIRoutes[Next.js 15 App Router API Routes]
        AuthGuard[Supabase RLS & Auth Service]
        AIPipeline[AI Content & OCR Processing Pipeline]
        PaymentEngine[Stripe Connect Gateway]
    end

    subgraph Data & Storage Layer (Supabase)
        DB[(PostgreSQL Database)]
        StorageBucket[Supabase Storage - Document & Media Vault]
    end

    subgraph External Services
        OpenAI[OpenAI GPT-4o Multimodal Vision & Speech API]
        Stripe[Stripe Connect API]
    end

    SEOEngine -->|Direct / Local Search| ClientBrowser
    ClientBrowser -->|Browse Profiles, Events, Articles, Products| APIRoutes
    EmbedWidget -->|Loads Verified Badge & Direct Link| APIRoutes
    ProDashboard -->|Manage Scheda, Publish Events/Articles, Verification| APIRoutes

    APIRoutes --> AuthGuard
    AuthGuard --> DB
    APIRoutes --> StorageBucket
    APIRoutes --> PaymentEngine
    APIRoutes --> AIPipeline

    AIPipeline -->|OCR Certificate Check & Voice-to-Article| OpenAI
    PaymentEngine -->|Ticketing & Sales Checkout| Stripe
```

---

## 2. Database DDL Schema (PostgreSQL / Supabase)

```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Profiles (B2C Users and B2B Professionals)
CREATE TABLE public.profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    email TEXT NOT NULL UNIQUE,
    full_name TEXT NOT NULL,
    account_type TEXT NOT NULL CHECK (account_type IN ('consumer', 'professional', 'company')),
    avatar_url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 2. Professional & Company Profiles (Scheda Professionale / Società)
CREATE TABLE public.professional_listings (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES public.profiles(id) ON DELETE CASCADE,
    entity_type TEXT NOT NULL CHECK (entity_type IN ('individual', 'company')),
    company_name TEXT,
    title_prefix TEXT, -- e.g. Dr., Dott.ssa, Ostetrica, Prof.
    headline TEXT NOT NULL,
    bio TEXT NOT NULL,
    specialties TEXT[] NOT NULL, -- e.g. ['Ostetricia', 'Allattamento IBCLC', 'Nutrizione Funzionale']
    address TEXT,
    city TEXT NOT NULL,
    postal_code TEXT,
    latitude DOUBLE PRECISION,
    longitude DOUBLE PRECISION,
    phone TEXT,
    website_url TEXT,
    verification_status TEXT NOT NULL DEFAULT 'pending' CHECK (verification_status IN ('pending', 'verified', 'rejected')),
    verified_at TIMESTAMP WITH TIME ZONE,
    verification_notes TEXT,
    stripe_account_id TEXT,
    is_pro BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 3. Professional Credentials & Diplomas (Verifica Titoli)
CREATE TABLE public.professional_credentials (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    listing_id UUID NOT NULL REFERENCES public.professional_listings(id) ON DELETE CASCADE,
    credential_title TEXT NOT NULL, -- e.g. Iscrizione Albo FNOPO #1234, Certificazione IBCLC
    issuing_body TEXT NOT NULL,
    document_url TEXT NOT NULL,
    ocr_extracted_data JSONB,
    verified_by_ai BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 4. Offered Services (Servizi)
CREATE TABLE public.services (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    listing_id UUID NOT NULL REFERENCES public.professional_listings(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    service_type TEXT NOT NULL CHECK (service_type IN ('in_person', 'online', 'home_visit')),
    duration_minutes INT NOT NULL,
    price_cents INT NOT NULL, -- Price in cents (EUR)
    currency TEXT DEFAULT 'EUR',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 5. Events, Seminars & Workshops (Eventi, Seminari, Formazione)
CREATE TABLE public.events (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    listing_id UUID NOT NULL REFERENCES public.professional_listings(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    slug TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL,
    event_type TEXT NOT NULL CHECK (event_type IN ('webinar_online', 'workshop_presence', 'course_series')),
    location_name TEXT,
    city TEXT,
    start_time TIMESTAMP WITH TIME ZONE NOT NULL,
    end_time TIMESTAMP WITH TIME ZONE NOT NULL,
    max_attendees INT,
    current_attendees INT DEFAULT 0,
    price_cents INT NOT NULL DEFAULT 0,
    ticket_stripe_price_id TEXT,
    is_published BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 6. Articles & Scientific Publications (Articoli e Pubblicazioni)
CREATE TABLE public.articles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    listing_id UUID NOT NULL REFERENCES public.professional_listings(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    slug TEXT NOT NULL UNIQUE,
    excerpt TEXT NOT NULL,
    content_markdown TEXT NOT NULL,
    category TEXT NOT NULL,
    tags TEXT[],
    cover_image_url TEXT,
    read_time_minutes INT DEFAULT 5,
    views_count INT DEFAULT 0,
    is_published BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 7. Products, Books & Materials (Prodotti e Pubblicazioni)
CREATE TABLE public.products (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    listing_id UUID NOT NULL REFERENCES public.professional_listings(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    product_type TEXT NOT NULL CHECK (product_type IN ('digital_ebook', 'physical_good', 'recommended_item')),
    price_cents INT NOT NULL,
    external_url TEXT, -- Link to third party if recommended item, or Stripe direct link if digital download
    image_url TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 8. Event Bookings & Orders (Prenotazioni Eventi e Acquisti)
CREATE TABLE public.orders (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES public.profiles(id),
    listing_id UUID NOT NULL REFERENCES public.professional_listings(id),
    event_id UUID REFERENCES public.events(id),
    product_id UUID REFERENCES public.products(id),
    stripe_session_id TEXT NOT NULL,
    amount_total_cents INT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('pending', 'completed', 'refunded')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Row Level Security (RLS) Policies
ALTER TABLE public.professional_listings ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.events ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.articles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.products ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Public profiles are viewable by everyone" ON public.professional_listings FOR SELECT USING (true);
CREATE POLICY "Public events are viewable by everyone" ON public.events FOR SELECT USING (is_published = true);
CREATE POLICY "Public articles are viewable by everyone" ON public.articles FOR SELECT USING (is_published = true);
CREATE POLICY "Public products are viewable by everyone" ON public.products FOR SELECT USING (is_active = true);

CREATE POLICY "Professionals can edit own listing" ON public.professional_listings FOR ALL USING (auth.uid() = user_id);
```

---

## 3. Core API Endpoints & Data Contracts

### 3.1 OCR Verification & Certification Upload (`POST /api/pro/verify-credential`)
- **Request Payload**:
  ```json
  {
    "listingId": "uuid",
    "credentialTitle": "Iscrizione Albo FNOPO #4521",
    "issuingBody": "Ordine delle Ostetriche",
    "documentBase64": "data:image/png;base64,..."
  }
  ```
- **Response Payload**:
  ```json
  {
    "success": true,
    "ocrVerified": true,
    "extractedDetails": {
      "nameOnDocument": "Maria Rossi",
      "registryNumber": "4521",
      "expirationDate": "2027-12-31"
    },
    "status": "verified"
  }
  ```

### 3.2 Voice-to-Article AI Drafting (`POST /api/pro/generate-article`)
- **Request Payload**:
  ```json
  {
    "audioVoiceNoteUrl": "https://supabase.storage/.../audio.mp3",
    "topicCategory": "Perinatal Health",
    "targetKeywords": ["svezzamento fisiologico", "consulenza nutrizionale"]
  }
  ```
- **Response Payload**:
  ```json
  {
    "title": "Guida allo Svezzamento Fisiologico: Quando e Come Iniziare",
    "excerpt": "I segnali di prontezza del neonato e i primi alimenti consigliati dalla nutrizionista.",
    "contentMarkdown": "# Guida allo Svezzamento Fisiologico...\n\n...",
    "estimatedReadTime": 6
  }
  ```

---

## 4. UI/UX Screen Hierarchy & Color Tokens

### Color Tokens
- **Primary Teal**: `#0D9488` (Trust, Health, Professionalism)
- **Primary Emerald**: `#059669` (Wellness, Vitality)
- **Background Light**: `#FAFAF9` (Warm Warm-White background)
- **Text Primary**: `#1C1917` (Slate Black for contrast)
- **Accent Coral**: `#F43F5E` (Event Highlights & Action Badges)

### Hierarchy
1. **Public B2C Portal Homepage**: Search bar (Specialty + City), Featured Verified Specialists, Upcoming Seminars & Webinars, Trending Articles, Recommended Curated Products.
2. **Specialist Public Profile Page (`/p/[slug]`)**: Hero Header with Verified Badge, Tab Navigation (Informazioni & Servizi, Eventi & Seminari, Articoli & Pubblicazioni, Prodotti & Risorse), Direct Contact & Booking Modal.
3. **Event Detail & Booking Page (`/eventi/[slug]`)**: Event overview, Speaker profile card, Date/Time/Location map, Stripe Checkout Ticket Modal.
4. **Professional Dashboard (`/pro/dashboard`)**: Scheda Management, Event Studio, Voice-to-Article AI CMS, Stripe Payouts & Earnings.

---

## 5. Day 1 - Day 14 Solopreneur MVP Implementation Roadmap

- **Days 1–3**: Database Schema & Auth Setup in Supabase. Next.js 15 App Router setup, Landing Page & B2C Search Layout.
- **Days 4–6**: Professional Scheda Management & Public Profile View. Implementation of Services, Events, Articles, and Products CRUD endpoints.
- **Days 7–8**: Stripe Connect Express integration for Event Ticketing and Digital Product Checkout.
- **Days 9–10**: AI OCR Credential Verification Pipeline & AI Voice-to-Article Transformer via OpenAI API.
- **Days 11–12**: Embeddable Verified Badge Widget (`badge.js`) & pSEO Dynamic Route Generation (`/citta/[specializzazione]`).
- **Days 13–14**: End-to-End Testing, Responsive UI Audit, and Production Deployment to Vercel.
