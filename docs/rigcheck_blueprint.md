# 🏗️ Technical Architecture Blueprint: RigCheck AI

**Status**: APPROVED (7/7 Proofs Passed)  
**Target MVP Build Time**: 7–9 Days (5 days core CRUD/tables + 2 days PDF generator + 2 days VisionKit OCR tag scanner & UI polish)  
**Primary Execution Stack**: Flutter (iOS & Android) + SQLite (`sqflite` / `watermelondb`) + Apple VisionKit / Google ML Kit Text Recognition + `pdf` rendering engine + Supabase (Auth/Cloud Backup)

---

## 1. System Architecture Overview

```mermaid
graph TD
    Client["Mobile Client (Flutter)"] --> LocalDB[("On-Device SQLite DB")]
    Client --> OCR Engine["On-Device Tag Scanner (VisionKit / ML Kit)"]
    Client --> PDF Engine["Local PDF Renderer & Cryptographic Signer"]
    Client --> Supabase["Supabase Cloud Sync (Postgres + Auth)"]
    Client --> StoreKit["In-App Purchase (RevenueCat / Stripe)"]
```

---

## 2. Database Schema (Postgres / Supabase SQL DDL)

```sql
-- Profiles / Inspectors Table
CREATE TABLE public.inspectors (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    full_name TEXT NOT NULL,
    certification_id TEXT,
    company_name TEXT,
    signature_png_base64 TEXT,
    subscription_tier TEXT DEFAULT 'free',
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Equipment / Hardware Assets Table
CREATE TABLE public.rigging_assets (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    inspector_id UUID REFERENCES public.inspectors(id) ON DELETE CASCADE,
    serial_number TEXT NOT NULL,
    asset_type TEXT NOT NULL, -- 'alloy_chain', 'wire_rope', 'synthetic_web', 'shackle', 'hoist_hook'
    wll_lbs INTEGER NOT NULL,
    manufacturer TEXT,
    qr_barcode_raw TEXT,
    status TEXT DEFAULT 'pass', -- 'pass', 'discard_required', 'maintenance_needed'
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Inspection Logs Table
CREATE TABLE public.inspection_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    asset_id UUID REFERENCES public.rigging_assets(id) ON DELETE CASCADE,
    inspector_id UUID REFERENCES public.inspectors(id) ON DELETE CASCADE,
    jobsite_location TEXT,
    gps_lat_long POINT,
    checklist_answers JSONB NOT NULL, -- { "yarn_visible": false, "link_wear_pct": 3, "cracks": false }
    overall_status TEXT NOT NULL, -- 'PASS', 'DISCARD'
    photo_urls JSONB DEFAULT '[]'::jsonb,
    pdf_report_url TEXT,
    inspected_at TIMESTAMPTZ DEFAULT NOW()
);
```

---

## 3. Core API Endpoints & Contract Specs

| Endpoint | Method | Input Payload | Output Response | Purpose |
|---|---|---|---|---|
| `/api/v1/assets/scan` | POST (Local/On-Device) | Base64 Frame Photo | `{ "serial": "SN-94820", "wll_lbs": 6500, "confidence": 0.96 }` | On-Device Tag OCR Parser |
| `/api/v1/certificates/generate` | POST (Local/On-Device) | `{ "log_id": "...", "inspector_sig": "..." }` | PDF File Path + Base64 SHA256 Hash | Cryptographic Inspection PDF |
| `/api/v1/sync` | POST | `{ "logs": [...], "assets": [...] }` | `{ "synced": true, "timestamp": "..." }` | Offline-to-Cloud DB Sync |
| `/api/v1/billing/webhook` | POST | RevenueCat Event | `{ "received": true }` | Subscription Status Sync |

---

## 4. UI/UX Layout Tokens & Screen Hierarchy

- **Screen 1**: Dashboard & Inspection Ledger HUD (Recent Inspections, Discard Alert Counter, Add Asset Action Button)
- **Screen 2**: On-Device Tag Camera OCR HUD (Live Bounding Box Overlay for Serial # & WLL Rating)
- **Screen 3**: ASME B30.9 Interactive Guided Inspection Checklist (Visual Toggles: Red Yarn, Link Wear %, Pin Twist, Frame Cracks)
- **Screen 4**: 1-Tap OSHA Certificate PDF Preview & Competent Person Signature Modal
- **Color Palette Tokens**: Safety Amber `#F59E0B` (Primary Accent), Industrial Slate `#0F172A` (Background Dark HUD), Pass Green `#10B981`, Discard Red `#EF4444`

---

## 5. Solopreneur MVP Implementation Roadmap (Day 1 - Day 9)

- **Day 1–3**: Core SQLite Database Schema, Data Models & ASME B30.9 / OSHA Discard Decision Trees
- **Day 4–5**: Camera HUD Integration with Apple VisionKit / Google ML Kit On-Device Tag OCR
- **Day 6–7**: Local PDF Certificate Generator with Digital Signature Capture & GPS Hash Tagging
- **Day 8–9**: Supabase Auth / Local Storage Sync, RevenueCat In-App Purchase Integration, & App Store Package Prep
