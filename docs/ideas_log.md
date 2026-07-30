# Ideas Log

## Log Summary
- Total evaluated: 5 | Approved: 4 | Pivot Required: 0 | Discarded: 1
- Approval rate: 4/5 = 80%

## Category Red Flags
_(structural causes of death found by deep-dives — read this before committing to any candidate)_

## Evaluated Ideas

### 1. FreshKeeper AI: Household Food Expiration Tracker & Zero-Waste Chef

- **Date**: 2026-07-29
- **Discovery Mode**: Original Discovery
- **Domain**: Mobile (iOS & Android)
- **Status**: **APPROVED (7/7)**
- **Novelty Factor**: Novel Combination (On-device receipt OCR + predictive shelf-life DB + 1-tap anti-waste recipes)
- **7-Proof Score**: 7/7
- **Summary**: Solves the €600–$700 annual household food waste problem caused by forgotten fridge/pantry groceries. Unlike legacy market leader [NoWaste](https://apps.apple.com/app/id1112404094) (which requires slow manual item entry), FreshKeeper scans printed supermarket receipts in 2 seconds, populates an auto-expiring color-coded inventory, sends smart <48h notifications, and generates dinner recipes using expiring items.
- **Artifacts**: [evaluation](docs/freshkeeper-app/evaluation.md) · [competitors](docs/freshkeeper-app/competitors.md) · [legal](docs/freshkeeper-app/legal.md) · [blueprint](docs/freshkeeper-app/blueprint.md)

### 2. TabSnap AI: Instant On-Device OCR Bill Splitter & Group Expense Auditor

- **Date**: 2026-07-29
- **Discovery Mode**: Original Discovery
- **Domain**: Mobile Utility (iOS & Android)
- **Status**: **APPROVED (7/7)**
- **Novelty Factor**: Novel Combination (On-device neural receipt OCR + zero-account instant QR/AirDrop bill share + proportional tax/tip calculator + direct payment deep links)
- **7-Proof Score**: 7/7
- **Summary**: Solves the awkward friction of splitting group restaurant bills (4–12 diners) in under 10 seconds. In response to [Splitwise](https://www.splitwise.com)'s restrictive paywalls and legacy server dropouts on [Tab App](https://tabapp.co), TabSnap AI performs 100% on-device VisionKit/MLKit line-item OCR, allows friends to claim items via an instant QR web bridge without downloading an app, calculates proportional tax and tip down to the cent, and generates direct payment links ([Venmo](https://venmo.com), [Revolut](https://revolut.com), [PayPal](https://paypal.com)).
- **Artifacts**: [evaluation](docs/tabsnap-ai/evaluation.md) · [competitors](docs/tabsnap-ai/competitors.md) · [legal](docs/tabsnap-ai/legal.md) · [blueprint](docs/tabsnap-ai/blueprint.md)

### 3. RentShield AI: Room-by-Room Tenant Move-In Inspection & Security Deposit Vault

- **Date**: 2026-07-29
- **Discovery Mode**: Original Discovery
- **Domain**: Mobile Utility (iOS & Android)
- **Status**: **APPROVED (7/7)**
- **Novelty Factor**: Novel Combination (On-device Vision defect auto-tagging + local SHA-256 cryptographic EXIF metadata stamping + comparative room-by-room diff PDF generator + instant landlord delivery receipt)
- **7-Proof Score**: 7/7
- **Summary**: Solves the severe problem where 40%+ of apartment renters lose $500–$2,000 (€500–€1,500) of their security deposit over pre-existing property defects. Unlike B2B landlord portals ([RentCheck](https://apps.apple.com/us/app/rentcheck/id1134017691), [zTenant](https://apps.apple.com/us/app/ztenant/id1491039980)) or expensive $19.99 paid utility apps ([Tenant Inspect](https://apps.apple.com/us/app/tenant-inspect-rental-report/id6450515110)), RentShield AI provides a tenant-first guided room walkthrough, auto-detects scratches and stains via on-device AI, stamps photos with SHA-256 cryptographic EXIF proof, and generates an official signed legal PDF report delivered directly to the landlord on move-in day.
- **Artifacts**: [evaluation](docs/rentshield-ai/evaluation.md) · [competitors](docs/rentshield-ai/competitors.md) · [legal](docs/rentshield-ai/legal.md) · [blueprint](docs/rentshield-ai/blueprint.md)

### 4. QuoteGuard AI: Contractor Quote Auditor & Home Repair Cost Estimator

- **Date**: 2026-07-29
- **Discovery Mode**: Original Discovery
- **Domain**: Mobile Utility (iOS & Android) - Category A (Calculation & Estimation Tools)
- **Status**: **APPROVED (7/7)**
- **Novelty Factor**: Novel Combination (Parametric home repair material & labor formula engine + regional cost index benchmark + instant contractor quote audit PDF report)
- **7-Proof Score**: 7/7
- **Summary**: Solves the severe problem where 68% of homeowners face 30%–80% price variance and quote inflation when hiring contractors for home repairs (painting, tiling, plumbing, electrical). Unlike generic renovation trackers ([Renovise](https://apps.apple.com/app/renovise-remodel-tracker/id6475701878), [Re:Build](https://apps.apple.com/app/rebuild-renovation-planner/id6444855219)) or expensive enterprise tools, QuoteGuard AI allows homeowners to enter room specs via clean sliders, calculates exact material quantities & regional labor hour averages, and generates an exportable "Contractor Quote Audit Certificate" with line-item benchmarks to negotiate fair pricing.
- **Artifacts**: [evaluation](docs/quoteguard-ai/evaluation.md) · [competitors](docs/quoteguard-ai/competitors.md) · [legal](docs/quoteguard-ai/legal.md) · [blueprint](docs/quoteguard-ai/blueprint.md)

### 5. FamilyShield AI: Family Anti-Scam Protocol, Code Word Vault & Scam Radar

- **Date**: 2026-07-30
- **Discovery Mode**: Original Discovery
- **Domain**: Mobile Consumer Safety (iOS & Android) — cross-generational family circles
- **Status**: **DISCARDED (4/7)** — False Positive
- **Novelty Factor**: Novel Combination on paper, but every component individually owned by free or telco-scale incumbents
- **7-Proof Score**: 4/7 (FAIL on Proof 2 Zero-CAC, Proof 5 Moat, Proof 6 Status Quo)
- **Summary**: Demand anchors were real and strong — [FBI IC3 2025](https://www.ic3.gov/Outreach/Brochures/Elder_Fraud_Tri-fold.pdf): $7.7B elder-fraud losses, +37% YoY; AI voice-cloning "grandparent scams" flagged by FTC/FBI. But the space is a sandwich with no middle: free brand-backed message checkers below ([Bitdefender Scamio](https://www.bitdefender.com/en-us/consumer/scamio), [Norton Genie](https://www.malwarebytes.com/solutions/best-scam-detection-tools), indie [ZeroScam](https://zeroscam.io/) already running the IC3-pattern pSEO play), paid telco-scale call-blockers above ([Robokiller](https://apprank.io/robokiller-spam-call-blocker) at ~$2.0M/mo, [Truecaller](https://mashable.com/roundup/best-robocall-blocking-apps) at $9.99/mo), bank-channel senior finance monitoring on the flank ([Carefull × Edward Jones](https://www.prnewswire.com/news-releases/edward-jones-introduces-carefull-financial-safety-platform-to-help-families-protect-what-matters-most-302808126.html)). The unowned residue (family code-word manager) is a feature, and the free status quo (verbal code word + family WhatsApp group + free paste-check) wins.
- **Rejection Reason**: Distribution (Proof 2), moat (Proof 5) and status-quo resistance (Proof 6) all fail — consumer scam-defense monetizes only as a vendor loss-leader or via institutional distribution; no standalone direct-to-consumer middle exists at solopreneur scale.
- **Batch note (screened out at prior-art, not evaluated)**: 5 candidates killed on first pass — read-it-later/personal digest (post-[Pocket shutdown](https://www.shelf-extension.com/why-pocket-shut-down) wave already harvested by [Readwise Reader](https://www.mailist.app/blog/best-pocket-alternatives), Raindrop.io + 5 entrants), family story keeper ([StoryWorth](https://welcome.storyworth.com/blog/remento---how-it-works-pricing-reviews-top-alternatives)/[Remento](https://www.memorymurals.com/journal/storyworth-vs-remento-vs-memory-murals) + 4 clones at identical $99/yr), event QR photo sharing ([Pix Wedding](https://www.pix.wedding/disposable-camera-app-for-parties), [Scene](https://scenedisposable.com/qr-code-for-wedding-pictures) + 8 near-identicals), caregiver/sibling coordination ([SplitKin](https://splitkin.com/guides/best-sibling-caregiving-coordination-app-2026), [TendLog](https://tendlog.com/blog/best-caregiver-app-for-families-how-to-coordinate-care-for-an-aging-parent) et al.), "Letterboxd for concerts" ([Encore](https://encorearchives.com/best-concert-apps), [Concerts Remembered](https://concertsremembered.com/blogs/news/concerts-remembered-app-complete-guide) already exist).
- **Artifacts**: [evaluation](docs/familyshield-ai/evaluation.md) · [competitors](docs/familyshield-ai/competitors.md) · [legal](docs/familyshield-ai/legal.md)
