# 🏗️ Technical Architecture Blueprint: CertiMach AI

**Status**: APPROVED (7/7 Proofs Passed)  
**Target MVP Build Time**: 10–12 Days  
**Primary Execution Stack**: Next.js 14 (App Router) + Supabase (Postgres + Auth + Storage) + Tailwind CSS + Stripe Connect + Claude 3.5 Sonnet Vision API

---

## 1. System Architecture Overview

```mermaid
graph TD
    User["Consultant / Company User"] --> WebApp["Next.js 14 App Router"]
    OEMClient["OEM / Industrial Client"] --> WebApp
    
    WebApp --> Auth["Supabase Auth (Magic Link & OAuth)"]
    WebApp --> DB[("PostgreSQL Database (Supabase)")]
    WebApp --> Storage["Supabase Storage (PDF Certificates, Whitepapers, Templates)"]
    
    WebApp --> VisionOCR["Claude 3.5 Sonnet API (Certificate OCR Verification)"]
    WebApp --> Stripe["Stripe Connect (Pro Subscriptions & Digital Product Payouts)"]
    
    ClientProposal["Client Proposal / LinkedIn"] <-- EmbedWidget["Embeddable CE Badge / QR PDF Engine"] --- WebApp
```

---

## 2. Database Schema (Postgres / Supabase SQL DDL)

```sql
-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Profiles (Scheda Professionale: Professionisti & Società)
CREATE TABLE public.profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    account_type TEXT CHECK (account_type IN ('individual', 'company')) DEFAULT 'individual',
    full_name TEXT NOT NULL,
    company_name TEXT,
    vat_number TEXT,
    bio TEXT,
    country_code VARCHAR(2) DEFAULT 'IT',
    city TEXT,
    verified_badge BOOLEAN DEFAULT FALSE,
    verification_hash TEXT,
    badge_embed_token UUID DEFAULT gen_random_uuid(),
    hourly_rate_eur NUMERIC(10,2),
    skills TEXT[] DEFAULT '{}',
    subscription_tier TEXT CHECK (subscription_tier IN ('free', 'pro', 'agency')) DEFAULT 'free',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- 2. Services (Offerta Servizi & RFPs)
CREATE TABLE public.services (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    provider_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    category TEXT CHECK (category IN ('ce_marking', 'iso_13849', 'atex', 'cybersecurity_nis2', 'risk_assessment', 'safety_audit')) NOT NULL,
    description TEXT NOT NULL,
    starting_price_eur NUMERIC(10,2),
    delivery_time_days INT,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 3. Events & Training (Eventi, Seminari, Formazione & Webinars)
CREATE TABLE public.events (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    organizer_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    event_type CHECK (event_type IN ('webinar', 'in_person_workshop', 'certified_course')) NOT NULL,
    description TEXT NOT NULL,
    start_time TIMESTAMPTZ NOT NULL,
    end_time TIMESTAMPTZ NOT NULL,
    location_or_url TEXT NOT NULL,
    ticket_price_eur NUMERIC(10,2) DEFAULT 0,
    max_attendees INT,
    ceu_hours NUMERIC(4,1) DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 4. Articles & Whitepapers (Articoli & Pubblicazioni Tecniche)
CREATE TABLE public.publications (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    author_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    slug TEXT UNIQUE NOT NULL,
    abstract TEXT NOT NULL,
    content_md TEXT NOT NULL,
    pdf_attachment_url TEXT,
    keyphrases TEXT[] DEFAULT '{}',
    view_count INT DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- 5. Digital Products Store (Prodotti Digitali: Librerie SISTEMA, Fogli di Calcolo Excel)
CREATE TABLE public.products (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    seller_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    product_type CHECK (product_type IN ('sistema_library', 'excel_template', 'risk_checklist_pdf', 'cad_safety_blocks')) NOT NULL,
    description TEXT NOT NULL,
    price_eur NUMERIC(10,2) NOT NULL,
    file_storage_path TEXT NOT NULL,
    download_count INT DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Row Level Security (RLS) Policies
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.services ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.events ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.publications ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.products ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Public profiles are viewable by everyone" ON public.profiles FOR SELECT USING (true);
CREATE POLICY "Users can update own profile" ON public.profiles FOR UPDATE USING (auth.uid() = id);

CREATE POLICY "Public services viewable by everyone" ON public.services FOR SELECT USING (true);
CREATE POLICY "Providers manage own services" ON public.services FOR ALL USING (auth.uid() = provider_id);

CREATE POLICY "Public publications viewable by everyone" ON public.publications FOR SELECT USING (true);
CREATE POLICY "Authors manage own publications" ON public.publications FOR ALL USING (auth.uid() = author_id);
```

---

## 3. Core API Endpoints & Contract Specs

| Endpoint | Method | Input Payload | Output Response | Purpose |
|---|---|---|---|---|
| `/api/v1/verify-certificate` | POST | `FormData` (PDF/Image file of TÜV/CMSE badge) | `{ "verified": true, "credentials": { "issuer": "TÜV SÜD", "cert_no": "CMSE-9941", "expiry": "2028-12-31" } }` | OCR Certificate Parser via Claude 3.5 Sonnet Vision |
| `/api/v1/badge/[token]` | GET | None (URL Param token) | SVG / Dynamic HTML Badge Widget | Embedded Verification Badge on external sites |
| `/api/v1/checkout/product` | POST | `{ "product_id": "uuid" }` | `{ "checkout_url": "https://checkout.stripe.com/..." }` | Stripe Connect Payout & Digital Product Purchase |
| `/api/v1/rfp/match` | POST | `{ "scope_text": "...", "category": "iso_13849" }` | `{ "matched_experts": [ { "id": "...", "match_score": 0.94 } ] }` | Automated RFP Scope Expert Matcher |

---

## 4. UI/UX Layout Tokens & Screen Hierarchy

- **Screen 1 (Landing & Directory Hub)**: Search Bar with ISO/CE filter pills, Featured Verified Consultants, Upcoming Webinars, Latest Technical Whitepapers, Top Engineering Downloads.
- **Screen 2 (Scheda Professionale / Company Bio)**: Header with Verified Accreditation Badge, Services Grid, Published Whitepapers, Course List, Digital Store Items, Direct Contact / RFP Request Modal.
- **Screen 3 (Consultant Dashboard)**: Profile & Certificate Verification Upload, Lead Inbox, Digital Product Sales Analytics, Badge Embed Code Generator (`<iframe src="...">`).
- **Screen 4 (Single-Player Credential Badge & PDF Generator)**: Dynamic SVG rendering engine for email signatures and PDF client proposals.
- **Color Palette Tokens**:
  - Primary Brand: `#0284C7` (Industrial Ocean Blue)
  - Accreditation Verified Accent: `#10B981` (Emerald Green)
  - Regulatory Caution / Notice: `#F59E0B` (Safety Amber)
  - Background HUD: `#0F172A` (Slate 900) & Surface `#1E293B` (Slate 800)

---

## 5. Solopreneur MVP Implementation Roadmap (Day 1 - Day 12)

- **Day 1–3**: Next.js 14 project setup, Supabase Auth & PostgreSQL Schema creation (Profiles, Services, Events, Publications, Products).
- **Day 4–6**: Public Directory UI, Scheda Professionale View, Article Markdown Renderer & Event Registration system.
- **Day 7–8**: Claude 3.5 Sonnet Vision OCR pipeline for PDF certificate extraction & embeddable SVG verification badge generator (`/api/v1/badge/[token]`).
- **Day 9–10**: Stripe Connect integration for Pro Subscriptions (€39/mo) and Digital Template Downloads.
- **Day 11–12**: End-to-end testing, seed data creation with 10 sample Machinery Safety profiles/whitepapers, and launch deployment on Vercel.
