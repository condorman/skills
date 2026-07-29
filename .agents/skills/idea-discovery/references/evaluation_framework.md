# Anti-False-Positive Evaluation Framework (7-Proof Verification Protocol v5.1)

This document defines the strict, anti-false-positive evaluation criteria designed to eliminate bad ideas early and ensure that only ideas with verified commercial viability, low churn, organic distribution, high technical reliability, genuine solo-buildability, and status-quo resistance are approved.

---

## Calibration: Approval Is the Exception, Not the Default

The whole point of this protocol is that most candidate ideas SHOULD fail it — that's what makes a PASS meaningful. If you notice yourself approving most of the ideas you evaluate in a session, that's not a sign the ideas are unusually good; it's a sign the protocol is being applied as a rubber stamp instead of a filter. A few concrete habits keep this honest:

- **Steelman the rejection before you accept.** For every proof, write the strongest case for REJECT first — the most skeptical reading of the evidence you gathered — before deciding it's a PASS. If you can't construct a real rejection case (not a token one), that's what makes the PASS trustworthy.
- **Evidence you found via search beats evidence you'd expect to find.** "Companies clearly need this" is a hypothesis, not a proof. Only mark a proof PASS on the strength of something you actually retrieved (a real job post, a real review, a real competitor pricing page) — not on the strength of it sounding plausible.
- **In Vertical Deep-Dive Mode, the calibration inverts.** The 7 Proofs are re-scored there against far better evidence, and the failure mode is the mirror image of this one: not approving too easily, but *reproducing the original verdict* because it's already written down. When re-scoring, state explicitly which proofs changed and why — and treat "nothing moved" as a signal to check whether the new evidence was actually allowed to count, since deep-dive evidence that never overturns anything wasn't worth gathering. See the Calibration section of `vertical_deepdive_playbook.md`.
- **Track your own rate — cumulatively, not per session.** The ~1/3 guideline is a property of `ideas_log.md` over time, not of whatever you just did: a single-idea session ending in APPROVED is a 100% approval rate and carries no information, and treating that as an alarm makes the alarm meaningless when it matters. Read the running **Approval rate** line the Step 8 log update maintains in the Log Summary, and re-audit when either the cumulative rate across ~6+ evaluated ideas sits meaningfully above ~1/3, or a single batch of 3+ candidates approves most of them. When it fires, look specifically for Proof 1 (WTP) and Proof 6 (Status Quo) being passed on vibes rather than retrieved evidence — those are the two easiest to talk yourself into.

---

## The 7 Pitfalls of Idea Evaluation

| Pitfall | Common Delusion | Real-World Failure Reason |
|---------|-----------------|---------------------------|
| **1. Complaining ≠ Paying** | "People complain about this on Reddit, so they will buy my app." | Pain is mild; users prefer free hacky workarounds over paying $15/mo. |
| **2. Distribution Blindspot** | "The app is easy to build in 3 days with AI." | Acquiring 1 customer costs $150 in ads for a $20 tool; solopreneur has no organic reach. |
| **3. High Churn Trap** | "Solves a real problem (e.g. file conversion)." | User solves the problem once and cancels subscription immediately. |
| **4. Zero Moat (Commodity Wrapper)** | "It wraps an LLM API nicely." | 20 identical clones appear on Product Hunt within 7 days; base LLMs add the feature for free. |
| **5. AI Reliability Failure** | "AI will handle 100% of the workflow." | LLM hallucinations or edge-case breaks cause endless support tickets that overwhelm 1 person. |
| **6. Status Quo Inertia** | "An app is slightly cleaner than Excel or paper." | Users prefer their free manual spreadsheet/paper habit over learning a new software tool. |
| **7. Novelty-Complexity Confusion** | "It's unprecedented because on-device FFT/beamforming/pose-estimation has never been combined this way, and modern AI makes any build fast." | The exact thing that makes it novel (custom signal-processing, real-time sensor fusion, calibration against physical variance) is also exactly what makes it slow and unpredictable to build — novelty and build risk usually move together, not apart. |

---

## The 7-Proof Verification Protocol

Every candidate idea MUST be evaluated against all 7 verification proofs:

### Proof 1: Willingness to Pay (WTP & Demand Velocity Test)
- **Criterion**: There MUST be concrete evidence of active financial spend AND rising search momentum addressing this problem today.
- **Verification Indicators**:
  - Companies hiring freelancers on Upwork/Fiverr paying $200–$2,000 for this exact custom task.
  - Existing clunky/bloated competitors charging $30+/mo with active paying user reviews.
  - Rising Google Trends / Exploding Topics search volume momentum.
- **Verdict**: If users only complain but never pay for existing workarounds, or search volume is dead/flat for 3+ years, **REJECT (WTP / Dead Demand Failure)**.

### Proof 2: Zero-CAC Organic Distribution Channel
- **Criterion**: The product MUST have a clear, built-in organic customer acquisition channel that requires **$0 in ad spend** and no direct cold sales calls.
- **Valid Organic Channels**:
  - **Extension Store SEO**: Chrome Web Store, Shopify App Store, Figma Community, Notion Template Marketplace.
  - **Programmatic SEO (pSEO)**: High-intent long-tail search queries (e.g., `"convert [format A] to [format B]"`).
  - **Active Niche Communities**: Specific subreddits, Discord groups, or forums where sharing useful tools is welcomed.
- **Verdict**: If customer acquisition requires paid ads, enterprise sales teams, or cold outreach, **REJECT (Distribution Failure)**.

### Proof 3: High Frequency & Retention (Anti-Churn Test)
- **Criterion**: The product MUST solve a recurring daily or weekly workflow pain point—not a one-off event. For **Game Concepts**, avoid "daily-only" 2-minute puzzles; mandate high multi-session replayability (endless modes, roguelite progression, physics merge loops).
- **Frequency Scale**:
  - *Daily/Weekly Recurring*: Invoicing, social media curation, weekly report generation, daily code review summary -> **PASS**.
  - *Multi-Session Games*: Highly replayable physics, roguelite merges, high-score arcade loops -> **PASS**.
  - *One-off / Rare Event / Single-Play-Per-Day*: Resume formatting, single-daily Wordle clones with no replay mode -> **REJECT (High Churn Risk / Low Engagement)**.

### Proof 4: AI Technical Reliability & Low-Support Threshold
- **Criterion**: The core AI/automation pipeline MUST deliver >95% deterministic accuracy without requiring human-in-the-loop debugging or manual customer support intervention.
- **Checklist**:
  - Does the core capability rely on structured output (JSON/Code) that can be programmatically validated?
  - Does an edge-case failure cause catastrophic business loss for the user (e.g. tax filing) or minor inconvenience?
- **Verdict**: If edge-case failures require human review or create high support liability, **REJECT (High Support Friction)**.

### Proof 5: Micro-Moat & Defensibility Angle
- **Criterion**: The app MUST feature at least one defensible micro-moat that prevents instant copy-pasting by generic AI wrappers.
- **Valid Micro-Moats**:
  - **Proprietary Workflow / Prompt Architecture**: Highly tuned multi-agent workflow for a specific professional niche.
  - **Deep API Integrations**: Complex two-way sync with niche software platforms (e.g. QuickBooks + HubSpot + Notion).
  - **First-Mover SEO / Marketplace Rank**: Dominating search rank in Chrome Store or Google before competitors emerge.
- **Verdict**: If the tool is a simple 1-prompt API wrapper with standard UI, **REJECT (Zero Moat)**.

### Proof 6: Status Quo Resistance & Non-Software Substitute Test
- **Criterion**: The proposed software MUST overcome free human inertia (spreadsheets, paper, pinned notes, basic email).
- **Checklist**:
  - Does the app save at least 2+ hours per week or $200+/month compared to a free spreadsheet or manual routine?
- **Verdict**: If the user's free manual habit is "good enough" (<60s effort), **REJECT (Status Quo Inertia Failure)**.

### Proof 7: True Solopreneur Buildability (Technical Reality Check)
- **Criterion**: A realistic solo developer — not a well-funded team, not a research lab — MUST be able to ship a reliable MVP in the stated timeframe using off-the-shelf frameworks, libraries, and APIs. This is a distinct question from Proof 4 (whether the AI/automation is *accurate enough*): Proof 7 asks whether the *build itself* is tractable at all for one person.
- **Why this proof exists**: It's easy to describe a genuinely novel mechanism (custom acoustic signal processing, multi-mic phase-array beamforming, real-time pose estimation with sub-100ms audio feedback, spatial AR triangulation) and then default to a generic MVP estimate ("5–7 days") that would actually apply to a CRUD app. Novelty in the underlying mechanism is very often *why* an idea passed the prior-art search — but that same novelty means there is no off-the-shelf library to lean on, so the engineering has to be invented and calibrated from scratch. Treat any idea whose core mechanism is "unprecedented" as carrying elevated build risk by default, and require the estimate to justify itself rather than assert itself.
- **Red flags that should trigger hard scrutiny (not automatic rejection, but a mandatory justification)**:
  - Custom signal processing the developer would have to design and tune (FFT-based classification, acoustic impulse response analysis, multi-microphone beamforming/triangulation).
  - Real-time computer vision or pose estimation with a hard latency budget (e.g. "<100ms").
  - Any accuracy claim (e.g. ">95%") for a novel on-device model with no existing pretrained model or dataset — this has to be validated empirically against real physical variance (different phones, mic quality, lighting, materials), which off-the-shelf demos don't capture.
  - Hardware calibration against physical-world variance (device models, ambient noise, lighting conditions) that can't be unit-tested in software alone.
  - Anything requiring novel algorithm design rather than composing existing SDKs/APIs (e.g. Apple VisionKit, ML Kit, MediaPipe, a hosted LLM API) — composing existing tools is low-risk; inventing the core technique yourself is high-risk.
- **Checklist**:
  - Can the core mechanism be built almost entirely by composing existing, well-documented SDKs/APIs (e.g. VisionKit, ML Kit, MediaPipe, Whisper, a hosted LLM) rather than inventing new signal-processing or ML techniques?
  - Is there a graceful, cheap fallback (manual entry, a simpler heuristic) if the novel/AI component underperforms in the field, so the product still works while it's being tuned?
  - Does the stated build estimate explicitly separate "core CRUD/UI work" from "the novel technical component," and does the novel-component estimate include time for real-device calibration and testing against physical variance — not just writing the code?
- **Verdict**: If the core mechanism requires inventing and empirically validating a novel signal-processing/ML technique against real-world physical variance, and the estimate doesn't honestly account for that R&D and calibration time, **REJECT or PIVOT (Buildability Failure)** — recommend either a simpler mechanism, a narrower first version that ships the deterministic parts first, or an honest multi-week-to-multi-month estimate instead of a padded "5–7 day" claim.

---

## Final Anti-False-Positive Decision Matrix

| Proof Passed | Risk Assessment | Final Verdict |
|--------------|-----------------|---------------|
| 7 / 7 | Highly Viable Solopreneur Business | **APPROVED** |
| 6 / 7 | Minor Defect (Fixable with Pivot) | **PIVOT REQUIRED** |
| ≤ 5 / 7 | High Risk of Failure / False Positive | **DISCARDED** |

A healthy session mixes verdicts. If every idea in a session lands at 7/7, treat that as a signal to re-run the Calibration checklist above against your own recent reasoning before logging the results.
