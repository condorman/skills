# Evaluation Report

## Step 0: Memory Check Result — ⚠️ CRITICAL DUPLICATE FLAG

`docs/ideas_log.md` (seeded in the target project) already contains an entry dated **2026-07-27**:

> **1. 💡 ExposureFlow AI: Mobile ERP Hierarchy Assistant & Live SUDS Habituation Graph for OCD & Phobias**
> Status: **APPROVED (6/6)**. Features a visual Fear Hierarchy Ladder, a live real-time SUDS habituation decay graph, compulsion response delay timer, and 1-tap encrypted PDF report export for weekly CBT therapy sessions.

The user's new prompt — *"app che guida gli utenti attraverso esercizi ERP per ansia, fobie e OCD, con grafico live SUDS e gerarchia della paura personalizzabile"* — describes the **same core concept**: ERP exercises, live SUDS graph, customizable fear hierarchy, for the same three conditions (anxiety, phobias, OCD).

Per Step 0 of the skill ("DO NOT re-propose or re-analyze concepts already recorded unless specifically instructed"), this would normally be blocked. The user explicitly asked for a full re-evaluation including a legal check, so this report proceeds — but re-runs prior-art research from scratch rather than trusting the prior "APPROVED" verdict, per the user's request for the "protocollo completo."

**Result of the re-run: this report reaches a different verdict than the 2026-07-27 log entry** (see Step 3). The prior run appears not to have surfaced direct free/near-identical competing apps that this session found via live web search (see 3.2 Evidence Log). This discrepancy is flagged explicitly in the Memory Log update.

---

### 💡 ExposureGuide: Guided ERP Exposure Sessions with Live SUDS Graph & Custom Fear Hierarchy

**Context Category**: Mobile App (iOS & Android) — *Category B: Gestionali & Micro-Productivity / Category F: Educational & Behavioral Protocols*
**Novelty Level**: ⚠️ **Prior Art Exists / Commodity Mechanics** (re-classified down from the prior session's "Unserved Niche Flank")

#### 1. Core Problem & Latent Friction
- **Discovered Friction**: OCD/phobia/anxiety patients doing ERP homework between therapy sessions typically use paper SUDS worksheets or generic note apps; therapist-led ERP access (NOCD) is expensive ($149–$349/mo self-pay, or $20–$50/session copay).
- **Target Audience**: People in ERP treatment (in therapy or self-directed) for OCD, specific phobias, panic disorder, social anxiety.

#### 2. The "Why Now?" Factor (Tech Enabler)
- **Recent Tech Breakthrough**: None identified. A live SUDS graph and a fear-hierarchy builder require no AI, no new sensor, and no recent model release — they are simple client-side state/UI (slider + timeline chart).
- **Why It Couldn't Be Built Earlier**: It could have — and was. The core mechanic (self-report anxiety rating + fear hierarchy + live-updating graph) has existed as a shipped, free mobile app since well before the current AI wave (see Evidence Log). There is no "why now" enabler; this weakens the Solopreneur + AI Feasibility Gate in Step 4.

#### 3. Novelty & Prior-Art Verification
- **Prior-Art Search Results**: Direct, functionally-identical prior art found and verified via live search (not merely adjacent competitors). "Exposure – Face Your Fears" (free, iOS) already implements: user-entered fear hierarchy, live-updating anxiety rating during the exposure task, and guidance to continue until anxiety drops to ≤20/100 — i.e., the exact SUDS-graph + hierarchy mechanic described in the prompt. "OCD Tracker – ERP Therapy" and "OCD ERP: Exposure Therapy" (Google Play) both ship custom exposure-hierarchy builders with 1–10 SUDS tracking, positioned specifically at OCD. "FearTools – Anxiety Aid," "Anxiety Coach" ($4.99 one-time), and "Fear Ladder" (fearladder.com) round out a saturated niche.
- **Originality Verdict**: **Flanking Existing Competitors / Commodity Mechanics.** Not unprecedented, not a clean unserved-niche flank — the specific feature bundle in the prompt (hierarchy + live SUDS graph) is already shipped, in some cases for free.

##### 3.1 Feature Delta Matrix
| Feature / Dimension | Candidate Concept (ExposureGuide) | Closest Prior Art #1: *Exposure – Face Your Fears* | Closest Prior Art #2: *NOCD (treatmyocd.com)* | Innovation Delta / Verdict |
|---|---|---|---|---|
| **Core Mechanics** | Guided ERP session, live SUDS graph, custom fear hierarchy | Identical: fear hierarchy + live anxiety rating during exposure, guided until SUDS ≤20 | No self-guided hierarchy tool; delivers ERP via live licensed therapists (video sessions) | 🟡 Reskin vs. Prior Art #1 |
| **Distribution** | App Store ASO, r/OCD / r/AnxietyDisorders | Same channel, already ranking, free | Paid performance marketing + insurance-network referrals | 🔴 Saturated vs. #1 |
| **Tech Enabler** | None (client-side UI/state) | None — same, and shipped years ago | Real licensed clinicians (not tech-enabled) | 🔴 Stale (no "why now") |
| **Monetization & UX** | Implied subscription | **Free**, no IAP | $149–$349/mo self-pay for actual therapist access | 🔴 Commodity vs. #1; underpriced-value gap vs. #2 |

##### 3.2 Evidence & Verification Audit Log
- **Queries Run**: `ERP exposure response prevention app OCD anxiety phobia SUDS tracker`, `fear hierarchy app anxiety exposure therapy mobile app`, `nOCD app fear ladder SUDS scale exposure exercises review`, `NOCD app price per month subscription`, `is a mental health exposure therapy app considered a medical device FDA regulation`, `practicing psychology without a license mental health app legal liability`, `risks of self-guided exposure therapy without therapist supervision panic attack contraindication`, `GDPR special category health data mental health app compliance requirements`.
- **Verified URLs Examined**:
  - [Exposure – Face Your Fears (App Store)](https://apps.apple.com/us/app/exposure-face-your-fears/id1135230491) — Fetched directly. Free app; fear-hierarchy creation; live anxiety-level updating during exposure tasks; explicit "use under guidance of a mental health professional" disclaimer. **Functionally identical core loop to the candidate idea.**
  - [OCD Tracker – ERP Therapy (Google Play)](https://play.google.com/store/apps/details?id=ocd.tracker.test.tools.journal.therapy&hl=en) — Obsession/compulsion tracking, 1–10 SUDS distress rating, ERP exposure hierarchy building. Updated June 2026 (actively maintained).
  - [OCD ERP: Exposure Therapy (Google Play)](https://play.google.com/store/apps/details?id=com.ocdserenity.exposurehierarchy) — Custom exposure-hierarchy builder, guided ERP marketed as "70%+ effectiveness."
  - [FearTools – Anxiety Aid (App Store)](https://apps.apple.com/us/app/feartools-anxiety-aid/id1179843607) — Exposure feature for gradual exposure.
  - [Fear Ladder](https://fearladder.com/) — Dedicated fear-ladder/exposure-hierarchy product.
  - [How much does NOCD cost?](https://www.treatmyocd.com/blog/nocd-costs) — $149–$349/mo self-pay or $20–$50 insurance copay; NOCD's free tier already includes self-help hierarchy tools before a therapist is even engaged, meaning the free component of the market leader overlaps with the candidate's entire paid value proposition.
  - [Fear Ladder / Exposure Hierarchy — Wikipedia](https://en.wikipedia.org/wiki/Exposure_hierarchy) — Confirms the hierarchy+SUDS technique is a decades-old, standardized, non-proprietary clinical worksheet method (further evidence of zero moat).

---

#### 4. Anti-False-Positive 6-Proof Verification Matrix

- **Proof 1 (Willingness to Pay & Demand Velocity)**: **FAIL.** Real financial spend exists in this space, but only for *full teletherapy* (NOCD, $149–$349/mo, buys licensed clinician sessions). The narrow feature set the user described — hierarchy + live SUDS graph — is exactly what "Exposure – Face Your Fears" already gives away for **$0**, and what NOCD gives away for free *before* a paid therapist is engaged. No evidence people pay a standalone subscription for this specific bundle.
- **Proof 2 (Zero-CAC Distribution)**: **PASS.** r/OCD, r/OCDRecovery, r/AnxietyDisorders and App Store ASO for "OCD app" / "exposure therapy app" are real, active, receptive channels.
- **Proof 3 (Anti-Churn Retention)**: **FAIL.** ERP is a bounded course of treatment aimed at habituating and resolving a specific fear; once a user's hierarchy is completed, the tool's job is done and there is no natural recurring reason to keep opening the app (unlike invoicing or daily logging tools). This matches Pitfall #3 ("solves problem once and cancels").
- **Proof 4 (AI Reliability >95%)**: **PASS (trivial)** — no AI/ML pipeline is in the described loop (self-report slider + static hierarchy list), so there is no hallucination/accuracy failure surface. Noted as a double-edged pass: it also means there's no AI-driven differentiation to offset the Proof 5 failure below.
- **Proof 5 (Micro-Moat Defensibility)**: **FAIL.** The hierarchy+SUDS mechanic is a standardized, decades-old clinical worksheet technique (see Wikipedia entry) already shipped, in some cases for free, by multiple existing apps. Zero proprietary workflow, zero deep integration, zero SEO head-start — a generic clone could ship this in a weekend.
- **Proof 6 (Status Quo Resistance)**: **FAIL.** The realistic alternative isn't paper or a spreadsheet — it's a **free app that already does this**, with an explicit "use with a mental health professional" disclaimer already built in. The candidate does not save $200+/month or meaningfully more time than the free incumbent.

**Protocol Score: 2/6 → DISCARDED (Eliminated as a False Positive)**

This directly **contradicts the 6/6 APPROVED verdict already recorded for "ExposureFlow AI"** in the seeded `ideas_log.md`. The most likely explanation is that the prior evaluation session did not execute live prior-art searches that surfaced "Exposure – Face Your Fears" and the two Google Play ERP/SUDS apps found in this session — all of which are near-exact functional matches. This is logged as a discrepancy for future sessions (see Step 6 below).

*Note on a viable pivot (not evaluated further here, out of scope for this report): the already-approved "ExposureFlow AI" log entry differentiates itself with a **1-tap encrypted PDF export for weekly therapy-session review** — a therapist-facing artifact none of the free competitors above offer. That specific delta, not the bare hierarchy+graph loop the user described today, is what could plausibly rescue Proofs 1, 5, and 6. As described in this prompt, without that differentiator, the idea fails the protocol.*

#### 5. Solopreneur + AI Feasibility Stack
- Not applicable — idea did not reach APPROVED status. No blueprint generated per Step 7 (mandatory only for 6/6 APPROVED ideas).

#### 6. Legal & Regulatory Safety

**Legal Risk Level: MODERATE–HIGH** (explicitly *not* "Very Low / Zero" — this idea sits in a materially different risk class than the calculator/utility apps typically logged in this project, because it involves deliberately provoking clinical anxiety/panic/OCD symptoms as its core mechanic.)

- **Practicing psychology/therapy without a license**: State psychology-licensing laws generally define "practice of psychology" as rendering services to diagnose, treat, or prevent mental illness. A self-directed app that avoids diagnostic claims and frames itself as an educational/self-help tool (not "treatment," not "therapy") is generally treated as outside licensed practice — but this is a live, unsettled legal gray zone; sources describe AI/digital mental-health apps as currently "operat[ing] in a regulatory vacuum, too sophisticated to be dismissed as wellness tools, but not licensed or regulated as healthcare providers." Marketing copy that names specific DSM conditions ("treats OCD," "cures phobias") meaningfully raises this risk; the user's own framing ("per ansia, fobie e disturbo ossessivo-compulsivo") already leans toward condition-specific treatment language.
- **FDA Software-as-a-Medical-Device (SaMD) exposure**: The FDA's own stated test is *intended use* — an app "intended to diagnose, treat, cure, mitigate, or prevent a disease" is a regulated medical device requiring premarket review; apps that stay in general-wellness framing (no named-disorder treatment claims) are typically exempt. This is a real, non-trivial compliance requirement, not paperwork that can be waved away — it depends entirely on how the app is marketed, and the user's own idea description already crosses into disorder-specific treatment language.
- **Clinical harm / liability risk unique to this vertical**: This is the most important finding, and the reason this category cannot get a boilerplate "very low risk" verdict. ERP works by deliberately eliciting anxiety/distress. Published clinical sources describe real cases where **unsupervised or poorly-paced exposure worsened symptoms**, triggered panic attacks, and in some reported cases produced "impulses toward self-destructive behavior." Every competing app found in this research (Exposure – Face Your Fears, NOCD) mitigates this either with a prominent "use under the guidance of a mental health professional" disclaimer, or by bundling actual licensed clinicians. A fully self-guided app with no contraindication screening (e.g., active suicidality, severe panic disorder, trauma-related dissociation) inherits this liability without those mitigations. A real build would need: crisis-resource / hotline links, an onboarding contraindication questionnaire, prominent non-treatment disclaimers, an attorney-reviewed ToS/liability waiver, and realistically, professional liability (E&O) insurance before public launch.
- **Data privacy (GDPR / US state health-privacy law)**: SUDS logs and fear-hierarchy content (which will typically name specific OCD obsessions, trauma content, or phobia detail) are "special category" data under GDPR Art. 9, requiring explicit (not bundled) consent, a Data Protection Impact Assessment, and likely a DPO if processing at scale — GDPR penalties reach up to €20M or 4% of global revenue. In the US, this data likely also qualifies as "sensitive" under state laws such as Washington's My Health My Data Act and CCPA's sensitive-PII category even though a consumer app without a clinical partner is not automatically a HIPAA Covered Entity.
- **Minors**: Anxiety, phobias, and OCD commonly onset in adolescence; if minors are foreseeable users, COPPA (US, <13) and app-store health-category child-safety policies attach additional obligations.
- **Net assessment**: None of the above is individually fatal or a lawsuit-in-waiting for a careful, well-disclaimed build — but "fully compliant, zero licenses required" (the template's default boilerplate) would be a materially misleading verdict here. This category requires healthcare-privacy engineering, marketing-language legal review, and a genuine clinical-safety design (screening + crisis resources + disclaimers) before launch, which adds real time/cost to the "solopreneur MVP" timeline and was not accounted for in the prior APPROVED log entry's 7–10 day estimate.

#### 7. Monetization Strategy
- Not evaluated in depth — idea did not reach APPROVED status, and the direct free competitor makes a paid-subscription model for the bare feature set unlikely to convert (see Proof 1).

#### 8. Summary Recommendation
- **Status**: **DISCARDED** (2/6 Proofs Passed — False Positive: saturated commodity mechanic with a free direct competitor, no "why now" tech enabler, and a churn profile driven by treatment completion.)
- **Path forward if revisited**: Do not re-propose the bare hierarchy+SUDS-graph loop. If pursued, pivot toward the differentiator already captured in the log's prior "ExposureFlow AI" entry (therapist-facing encrypted PDF export) or another angle untested by existing free apps — and treat the Legal & Regulatory section above as a hard prerequisite, not a formality.
