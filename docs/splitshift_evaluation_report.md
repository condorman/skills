# 💡 SplitShift: Instant Tip Pool Calculator & Payroll-Ready Shift Ledger

**Context Category**: Mobile App (iOS & Android)
**Novelty Level**: Unserved Niche Flank (Native Mobile-First Hours/Points-Weighted Tip Pool Ledger, Flanking Static Excel Lead-Magnets, a Barebones Unrated Single-Feature App, and Heavy POS-Integrated Payroll Platforms)

---

#### 1. Core Problem & Latent Friction

- **Discovered Friction**: At the end of every shift, a bar/restaurant shift lead or manager has to manually split the pooled tip total (cash + card) across everyone who worked, weighted by role and/or hours. This is currently done on a **napkin, phone calculator, or a paper "tip-out sheet"** — Server44's own marketing literally promises to "stop doing tip-out math on napkins." Disputes over fairness are common enough that unfair tip-pool splits have triggered real wage-theft complaints and lawsuits (e.g., the Aspen, CO restaurant tip-pooling case). Larger operators buy static Excel/Google Sheets tip-pool templates as free lead magnets from Toast POS, Kickfin, Connecteam, Agendrix, RestaurantOwner, and Push Operations — proving the arithmetic itself is a widely recognized pain point — but nobody has turned it into a persistent, native mobile, multi-shift tool.
- **Target Audience**: Shift leads, bar managers, and owner-operators at independent restaurants, bars, cafés, and food trucks (1–40 staff) who run informal or semi-formal tip pools every single shift but are too small/price-sensitive for enterprise payroll-integrated tip distribution platforms.

#### 2. The "Why Now?" Factor (Tech Enabler)

- **Recent Tech Breakthrough**: On-device text recognition (Apple VisionKit / Google ML Kit) is now fast, free, and accurate enough for a solo developer to add an optional "scan the register tape / POS summary screen" auto-fill feature with zero backend or per-scan API cost — something that required a paid cloud OCR vendor a few years ago. Separately, short-form video (TikTok/Reels) content from bartenders and servers (#bartender, #serverlife, #restaurantlife) is at an all-time engagement high in 2026, creating an unusually strong organic distribution window for a free niche utility that service-industry creators would genuinely want to show off.
- **Why It Couldn't Be Built Earlier**: The core arithmetic has always been trivial to build; what was previously uneconomical for a solo dev was (a) shipping a *reliable* camera-scan convenience feature without a recurring cloud OCR bill, and (b) reaching this specific audience without paid ads, since TikTok's algorithm-driven niche reach for blue-collar/service-industry micro-tools has only become reliably strong in the last couple of years.

#### 3. Novelty & Prior-Art Verification

- **Prior-Art Search Results**: A 5-pass search surfaced three tiers of prior art, none of which occupies the specific wedge of "persistent, hours/points-weighted, native mobile shift ledger with export":
  1. **Static Excel/web lead magnets** (Toast POS, Kickfin, Connecteam, Agendrix, RestaurantOwner, Push Operations, eTip) — one-off downloadable spreadsheets or web forms, not apps used shift after shift, no history, no team-share.
  2. **A single barebones native app, "Tipout Divider"** (iOS only, free, zero ratings/reviews found) — does a flat role-percentage split of one total, no hours-weighting, no persistent multi-shift ledger, no CSV/payroll export, no team-share link, no Android version.
  3. **Enterprise POS-integrated payroll platforms** (Kickfin, TipHaus, 7shifts, Toast) — require full POS integration, per-employee monthly pricing, and a sales/onboarding process; built for chains and mid-size operators, not a solo shift lead who wants an answer in under a minute.
  4. **Individual tip-tracking apps** (Tip Reports, Tip Tracker – Server44, TipKeepr) — solve a *different* job: one server logging their own tips over time for taxes, not a shift lead splitting one pooled total across the whole team present that night.
  - No Google Patents results were found for tip-pool distribution calculation methods (searched `patents.google.com` for restaurant tip pool distribution; only irrelevant restaurant-ordering and raffle patents surfaced).
- **Originality Verdict**: Confirmed Unserved Niche Flank — the mechanic (weighted split) exists in crude/static form, but no competitor combines native mobile + persistent multi-shift ledger + hours/points-weighted templates + payroll-ready export + 1-tap team share in a single lightweight, standalone tool.

##### 3.1 Feature Delta Matrix

| Feature / Dimension | SplitShift (Candidate) | Tipout Divider (Closest Light Prior Art) | Kickfin / TipHaus (Closest Heavy Prior Art) |
|---|---|---|---|
| **Core Mechanics** | Equal, role-%, hours-weighted, and points-based (e.g. bartender 1.5x, busser 0.5x) split engine | Flat role-percentage split only | Fully automated POS-synced calculation |
| **Persistence** | Running multi-shift ledger per venue, CSV/payroll-ready export | Simple swipe-to-delete list, no export | Full payroll system of record |
| **Distribution / Onboarding** | Instant, no signup, works standalone in <60s | Instant, no signup | Requires POS integration + sales process |
| **Pricing** | Free tier + low-cost pro (~$4.99/mo) for export/multi-venue | Free | Enterprise per-employee/month pricing |
| **Team Communication** | 1-tap SMS/WhatsApp share of the breakdown | None | Direct bank payout (heavier scope) |
| **Innovation Delta / Verdict** | 🟢 Novel combination for this segment | 🟡 Proves demand, zero moat, abandoned-feeling | 🔴 Overbuilt/expensive for a solo shift lead |

##### 3.2 Evidence & Verification Audit Log

- **Dorks / Queries Run**:
  `bartenders servers reddit "tip out" OR "tip pool" calculate by hand end of shift complaint app`,
  `Tiphaus Kickfin 7shifts tip pooling pricing "small restaurant" too expensive complex reviews`,
  `upwork fiverr "tip pool" OR "tip out" spreadsheet calculator custom job restaurant`,
  `site:patents.google.com tip pool distribution calculation method restaurant`
- **Verified URLs Examined**:
  - [Tipout Divider – App Store](https://apps.apple.com/bf/app/tipout-divider/id6479544605) - *Free, unrated, flat role-% split only, no ledger/export, iOS-only.*
  - [Tip Reports / Tip Tracker – Server44 – App Store](https://apps.apple.com/np/app/tip-tracker-server44/id6758269550) - *Individual server tip-logging tool, not a shift-lead pool splitter; own marketing cites "tip-out math on napkins" as the pain it addresses.*
  - [Kickfin Tip Pooling Calculator Template](https://kickfin.com/resources/tip-pooling-calculator-template/) - *Free static Excel/Sheets download, positioned as a lead magnet for Kickfin's paid POS-integrated payout platform.*
  - [Toast POS Tip Pooling Calculator](https://pos.toasttab.com/resources/tip-pooling-calculator) - *Same pattern: static spreadsheet lead magnet tied to a full enterprise POS suite.*
  - [Kickfin vs TipHaus Comparison](https://www.tiphaus.com/blog/tiphaus-vs-tiphaus/) - *Confirms both are enterprise, POS-synced, real-time bank payout platforms — a different, heavier product category.*
  - [Aspen restaurant tip-pooling lawsuit coverage](https://www.aol.com/2012-01-23-aspen-restaurant-alleged-tip-pool.html) - *Evidence that unclear/unfair manual tip-pool splits create real legal and trust exposure for operators.*
  - [Google Patents search](https://patents.google.com) - *No patents found covering restaurant tip-pool distribution calculation methods.*

#### 4. Anti-False-Positive 6-Proof Verification Matrix

- **Proof 1 (Willingness to Pay & Demand Velocity)**: **PASS**. Multiple vendors (Kickfin, TipHaus, Toast, Connecteam, Agendrix, Push Operations, RestaurantOwner) build free tip-pooling calculators specifically as lead magnets to sell paid payroll/POS platforms — proof that solving this exact math problem is valuable enough to fund customer acquisition. Enterprise buyers already pay recurring fees for automated tip distribution (Kickfin/TipHaus), confirming active spend in the category; the gap is a cheap, standalone option for the long tail of small independents who can't justify POS integration.
- **Proof 2 (Zero-CAC Distribution)**: **PASS**. Massive, highly active niche communities (r/bartenders, r/TalesFromYourServer, r/KitchenConfidential) plus a thriving #bartender/#serverlife TikTok/Reels ecosystem where a genuinely useful free shift tool is organically shared; strong long-tail App Store/Play Store ASO terms ("tip out calculator", "tip pool calculator", "tip splitter") with existing but weak-quality competitors to out-rank.
- **Proof 3 (Anti-Churn Retention)**: **PASS**. Used at the literal end of every single shift a venue runs a tip pool — multiple times per week per venue, among the highest-frequency use cases evaluated in this log.
- **Proof 4 (AI Reliability >95%)**: **PASS**. The core split-calculation workflow is deterministic arithmetic (100% reproducible, no LLM/AI in the critical path). The only AI/ML component — optional on-device OCR to auto-fill the pooled total from a photo of the register tape — is a convenience layer with a manual-entry fallback, so any recognition miss costs the user a few seconds of typing rather than breaking the core product.
- **Proof 5 (Micro-Moat)**: **PASS**. Defensibility comes from being first to combine (a) hours/points-weighted split templates, (b) a persistent multi-venue, multi-shift ledger, (c) payroll/FLSA-ready CSV export, and (d) 1-tap team-share — a bundle the free single-feature clone (Tipout Divider) does not offer and the enterprise players (Kickfin/TipHaus) only offer bundled into an expensive, sales-gated POS suite. First-mover ASO rank on "tip pool calculator app" in the App/Play Store is achievable given current competitors are unrated/low-traction.
- **Proof 6 (Status Quo Resistance)**: **PASS**. Replaces manual napkin/calculator math redone from scratch every shift and eliminates the trust/dispute risk of an opaque, undocumented split (a documented real-world failure mode, per the Aspen lawsuit). Saves a shift lead 5–15 minutes of error-prone mental math per shift, multiple times a week, and produces an auditable record the free "good enough" habit does not.
- **Protocol Score**: **6/6 → APPROVED**

#### 5. Solopreneur + AI Feasibility Stack

- **Recommended Tech Stack**: React Native (Expo) for iOS + Android from one codebase, on-device SQLite for the shift ledger (fully offline-first, no backend required for MVP), Apple VisionKit / Google ML Kit for optional receipt-total OCR scan, RevenueCat + Apple/Google IAP for the Pro tier subscription.
- **AI Automation Scope**: Strictly bounded to one optional convenience feature (photo-to-total OCR autofill). All financial calculations remain deterministic, auditable code — zero LLM involvement in money math.
- **Solo Execution Time**: 5–7 days for a fully functional offline MVP (split engine, ledger, CSV export, share sheet); OCR autofill and multi-venue support as a fast-follow in week 2.

#### 6. Legal & Regulatory Safety

- **Legal Risk Level**: Very Low.
- **Notes**: The app is a calculation and record-keeping tool only — it never touches, moves, or holds money, and it does not decide *who* should be in a tip pool or *what* split policy is compliant (the operator configures their own already-decided policy). This sidesteps FLSA tip-pooling eligibility rules (which govern *who* can be included, not how a total is arithmetically divided). A simple in-app disclaimer ("Consult your state/local wage laws and your own tip-pool policy — this tool only performs the calculation you configure") is sufficient. No payment processing, no PCI scope, no licenses required.

#### 7. Monetization Strategy

- **Pricing Model**: Freemium — free tier covers single-shift calculation + basic history (last 5 shifts); Pro tier at **$4.99/month or $39/year** unlocks unlimited ledger history, CSV/payroll export, multi-venue support, and OCR receipt scan.
- **Value Proposition**: Replaces 5–15 minutes of manual math and dispute risk per shift for less than the cost of one round of drinks a month — an easy yes for an owner-operator, and a natural low-friction upsell once a free-tier shift lead hits the 5-shift history cap.

#### 8. Summary Recommendation

- **Status**: **APPROVED**
