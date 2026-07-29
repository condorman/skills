# 📐 Functional Blueprint: QuoteGuard AI

**Status**: APPROVED (7/7) — Original Discovery 2026-07-29
**One-line pitch**: Parametric home repair cost estimator & contractor quote auditor that helps homeowners audit estimates, calculate material waste, and negotiate fair prices.
**Companion artifacts**: [evaluation](evaluation.md) · [competitors](competitors.md) · [legal](legal.md)

---

## 1. Product Definition & Scope

- **Job-to-be-done**: Audit contractor renovation quotes to verify line-item material requirements and regional labor hour benchmarks before signing a repair agreement.
- **Primary user**: Homeowners, renters preparing for move-out fixes, and DIYers hiring trade contractors.
- **The moment of use**: Opened when receiving a contractor's written estimate or while preparing room specifications prior to calling contractors.
- **Success for the user**: Obtaining a clear, itemized breakdown of materials needed + estimated labor hours + a shareable PDF "Contractor Audit Certificate" to negotiate price reductions.
- **Explicitly out of scope for v1**: Contractor invoicing/CRM features, direct in-app contractor hiring marketplace, 3D LiDAR spatial scanning.

---

## 2. Functional Specification

### 2.1 Capabilities

| # | Capability | What the user can do | Rules & constraints | Priority |
|---|---|---|---|---|
| F1 | Multi-Trade Room Specifier | Select trade (Painting, Tiling, Drywall, Flooring) and set room dimensions using interactive sliders | Enforces physical limits (e.g. positive dimensions, window/door deduction subtractions) | MVP |
| F2 | Material & Labor Calculator | Calculate exact material quantities (liters of paint, tile boxes, grout kg) with trade-specific waste factors (5%–15%) | Deterministic formulas based on trade standard coverage tables | MVP |
| F3 | Regional Cost Benchmark | Select ZIP code / Region to pull localized hourly labor rates ($45–$95/hr) | Stored locally in SQLite with quarterly update triggers | MVP |
| F4 | Contractor Quote Auditor | Input contractor's lump-sum estimate to view variance analysis (% over/under fair market range) | Highlights markup flags on labor vs materials | MVP |
| F5 | PDF Audit Certificate Generator | Export a clean 1-page line-item audit PDF to share with contractors during negotiation | Includes legal disclaimer & itemized negotiation talking points | MVP |
| F6 | Home Asset Care Schedule | Set recurring annual upkeep reminders (HVAC filter change, deck sealing, gutter cleaning) | Local push notifications | v1.1 |

### 2.2 Core user stories

- As a homeowner, I want to calculate exact tile and grout requirements for my bathroom including herringbone pattern waste, so that I don't get overcharged for extra material boxes. **Done when**: Tile box count, grout weight, and material price range display on screen.
- As a tenant hiring a painter, I want to input the contractor's $2,500 quote into QuoteGuard AI, so that I can see how many hours of labor they are billing for. **Done when**: The audit screen displays estimated labor hours (12-16 hrs) vs contractor markup percentage.

### 2.3 States, transitions & edge cases

- **Empty state**: Clean visual screen displaying trade selection cards (Painting, Tiling, Flooring, Drywall) with a prompt: "Select a trade to estimate repair cost or audit a quote."
- **Error & failure states**: Invalid zero or negative dimensions show inline field validation.
- **Edge cases**: Zero window/door deductions defaulted safely; offline mode functions 100% using local SQLite tables.

### 2.4 Functional constraints

- 100% offline-first calculations (zero network dependency for core estimation).
- Instant UI slider reactivity (<16ms calculation update on dimension changes).

### 2.5 Non-goals & explicit trade-offs

- Deliberately omits camera scanning/OCR in v1 to keep inputs 100% deterministic and eliminate vision AI hallucinations.

---

## 3. UI/UX Concept

### 3.1 Screen hierarchy

- **Home Screen** — Select Trade (Painting, Tiling, Drywall, Flooring) or Audit Existing Quote.
  - **Room Specifier Sheet** — Sliders for length, width, height, door/window count, material tier.
  - **Audit Results Screen** — Material breakdown, estimated labor hours, fair cost price band gauge.
  - **PDF Export Preview Modal** — 1-page "Contractor Audit Certificate" preview & share button.

### 3.2 Primary flow (end to end)

1. User opens app and taps "Audit a Quote" -> 2. Selects "Tiling" -> 3. Adjusts room sliders (3m x 4m, 1 door, 1 window) -> 4. Chooses tile pattern ("Herringbone") -> 5. Enters contractor quote ($3,200) -> 6. Taps "Generate Audit".
**Total taps**: 6 taps to complete line-item breakdown.

### 3.3 The signature interaction

**The Quote Fairness Gauge**: An interactive visual dial that animates from green ("Fair Price") to amber ("Slightly High") to red ("Overcharged +35%"), instantly showing the user where their contractor's estimate lands relative to regional material and labor benchmarks.

### 3.4 Visual direction

- **Tone**: Professional, trustworthy, precise, clean.
- **Reference points**: Apple Weather, Splitwise, Robinhood clean charts.
- **Colour tokens**: Primary `#1E3A8A` (Deep Slate Blue), Surface `#F8FAFC`, Accent `#10B981` (Fair Green), Danger `#EF4444` (Overcharged Red).
- **Typography**: Inter / System SF Pro. Dense readable data tables.

---

## 4. Implementation Roadmap

| Phase | Goal | Delivers | Riskiest assumption tested |
|---|---|---|---|
| **0 — De-risk** | Test parametric formulas against real contractor quotes | Python script + 10 sample renovation quotes | Formula accuracy verification |
| **1 — Walking skeleton** | Build UI sliders + calculation engine | F1, F2, F3 | SwiftUI/Compose slider reactivity |
| **2 — MVP** | Audit Gauge + PDF Kit Generator | F4, F5 | Shareable PDF export rendering |
| **3 — First iteration** | Home Asset Care Schedule | F6 | Retention notification loops |

- **Realistic solo build estimate**: 3 weeks (2 weeks core app & calculations + 1 week PDF export & UI polish).
- **First-users plan**: Launch on Reddit `r/HomeImprovement`, `r/DIY`, and App Store ASO for "renovation cost calculator".
- **What would make me stop**: If parametric formula estimates differ by >25% from verified local contractor cost sheets during Phase 0 testing.
