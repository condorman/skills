# 🏗️ Technical Architecture Blueprint: ExposureFlow AI

**Status**: APPROVED (6/6 Proofs Passed)  
**Target MVP Build Time**: 7–10 Days (1 Solopreneur Developer)  
**Primary Execution Stack**: Flutter (iOS & Android) + On-Device Encrypted SQLite (sqflite_sqlcipher) + FLChart + PDF Engine

---

## 1. System Architecture Overview

```mermaid
graph TD
    subgraph Mobile App (iOS / Android)
        UI["Flutter UI Layer (Fear Hierarchy / Exposure HUD)"]
        TimerEngine["Exposure & Compulsion Timer Engine"]
        HabituationMath["Habituation Decay Calculator & FLChart"]
        EncryptedDB[("On-Device SQLite DB (AES-256 SQLCipher)")]
        PDFGen["Local PDF Generator (Therapist Report)"]
    end

    subgraph Client System & Purchases
        IAP["StoreKit 2 / Google Play Billing"]
        ExportShare["iOS Share Sheet / Android Intent (PDF)"]
    end

    UI --> TimerEngine
    TimerEngine --> HabituationMath
    HabituationMath --> EncryptedDB
    UI --> PDFGen
    PDFGen --> ExportShare
    UI --> IAP
```

> **Architecture Note**: 100% Offline-First Architecture. Zero external API calls required for core functionality. Maximum HIPAA/GDPR privacy compliance by default.

---

## 2. Database Schema (Local SQLite / SQLCipher DDL)

```sql
-- Fear Hierarchy Items (Exposure Ladder)
CREATE TABLE fear_hierarchy_items (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    category TEXT DEFAULT 'OCD', -- OCD, Phobia, Panic, Social
    target_suds INTEGER NOT NULL CHECK (target_suds BETWEEN 0 AND 100),
    description TEXT,
    step_order INTEGER NOT NULL,
    is_completed INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Exposure Sessions
CREATE TABLE exposure_sessions (
    id TEXT PRIMARY KEY,
    hierarchy_item_id TEXT NOT NULL REFERENCES fear_hierarchy_items(id) ON DELETE CASCADE,
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP,
    initial_suds INTEGER NOT NULL CHECK (initial_suds BETWEEN 0 AND 100),
    peak_suds INTEGER NOT NULL CHECK (peak_suds BETWEEN 0 AND 100),
    final_suds INTEGER NOT NULL CHECK (final_suds BETWEEN 0 AND 100),
    compulsion_resisted INTEGER DEFAULT 1, -- 1 = Resisted, 0 = Yielded
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Real-Time SUDS Data Points (For Live Decay Graphing)
CREATE TABLE suds_datapoints (
    id TEXT PRIMARY KEY,
    session_id TEXT NOT NULL REFERENCES exposure_sessions(id) ON DELETE CASCADE,
    elapsed_seconds INTEGER NOT NULL,
    suds_rating INTEGER NOT NULL CHECK (suds_rating BETWEEN 0 AND 100),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- App Settings & IAP Status
CREATE TABLE app_preferences (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL
);
```

---

## 3. Core Local API / Business Logic Contracts

| Module / Function | Input Parameters | Output Return | Purpose |
|---|---|---|---|
| `startExposureSession(itemId, initialSuds)` | `itemId: String`, `initialSuds: int` | `SessionModel` | Initializes compulsion timer and records $t_0$ distress baseline |
| `logSudsPoint(sessionId, elapsedSec, suds)` | `sessionId: String`, `elapsedSec: int`, `suds: int` | `DataPointModel` | Records real-time distress point and recalculates habituation velocity |
| `calculateHabituationRate(sessionId)` | `sessionId: String` | `{ dropPercent: double, decaySlope: double }` | Computes logarithmic anxiety drop over time |
| `generateTherapistPdfReport(dateRange)` | `startDate: DateTime`, `endDate: DateTime` | `File (Encrypted PDF)` | Renders clean 1-page clinical summary with SUDS decay charts |

---

## 4. UI/UX Layout Tokens & Screen Hierarchy

### Screen Hierarchy
- **Screen 1: Fear Hierarchy Ladder (Dashboard)**  
  Shows steps 1–10 ranked by SUDS (0–100). Clear "Start Exposure" CTA per step. Cumulative exposure minutes & streak counter.
- **Screen 2: Live Exposure HUD & Compulsion Timer**  
  Large live timer, prominent 1-tap SUDS slider (0–100), real-time FLChart displaying live anxiety decay curve ($SUDS_{t0} \to SUDS_{tn}$), audio micro-grounding toggle.
- **Screen 3: Session Complete & Habituation Summary**  
  Summary card showing total drop (e.g., "Anxiety dropped from 85 to 30 in 16 mins!"), compulsion resistance badge, notes section.
- **Screen 4: Therapist PDF Export & Analytics**  
  Weekly habituation graph, average session duration, 1-tap button to share encrypted PDF with CBT therapist.

### Color Tokens & Design System
- **Background**: `#0F172A` (Slate 900 - Dark Calm)
- **Primary Accent**: `#3B82F6` (Electric Blue - Focus & Trust)
- **Calming Habituation Accent**: `#10B981` (Emerald Green - Recovery & Relief)
- **Anxiety Spike Accent**: `#EF4444` (Soft Red - High SUDS Warning)
- **Card Surface**: `#1E293B` (Slate 800)
- **Typography**: Inter / SF Pro (Clean, high readability)

---

## 5. Solopreneur MVP Implementation Roadmap (Day 1 - Day 14)

- **Day 1–2**: Setup Flutter project, SQLCipher local encrypted database models, and fear hierarchy CRUD logic.
- **Day 3–4**: Build Exposure HUD timer engine and FLChart real-time SUDS decay graph rendering.
- **Day 5–6**: Implement session completion logic, habituation rate math, and local PDF report generator.
- **Day 7–8**: Design sleek dark slate UI with micro-animations and sound cues.
- **Day 9–10**: Integrate In-App Purchases (RevenueCat / StoreKit 2) for Pro unlock.
- **Day 11–12**: Conduct internal testing, verify offline security, and prepare App Store / Google Play screenshots & ASO description.
- **Day 13–14**: Launch on App Store, Google Play, Reddit (`r/OCD`, `r/Anxiety`), and submit to therapy product catalogs.
