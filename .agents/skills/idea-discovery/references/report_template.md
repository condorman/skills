# Standardized Evaluation Report Template (Original & Flanking Modes)

Use this template for every validated idea in Original Discovery and Flanking Discovery Mode (Step 5 of `SKILL.md`), saved as `docs/<idea-slug>/evaluation.md`. **Deep-Dive Mode does not use it** — that mode has its own D0-D8 report structure in `vertical_deepdive_playbook.md`, with the 7-Proof matrix appearing there as a re-scoring at D7.

Two rules that this template depends on and that are easy to lose while filling it in:

- **Omit inapplicable subsections entirely** (3.0 for non-Flanking, 3.3 for non-marketplace ideas) rather than leaving them as empty placeholders — a blank heading reads as "not checked" and costs a reader time to resolve.
- **Every product name is a link at first mention in each section**, not once at the bottom.

```markdown
### 💡 [Idea Name]: [Short Catchy Tagline]

**Discovery Mode**: [Original / Flanking — Pattern 1 (Abandoned-but-Proven) / Pattern 2 (Stagnant-but-Validated) / Pattern 3 (Good-Foundation-Needs-Innovation), if Flanking]
**Context Category**: [Web | Mobile | Micro-Service | AI Tool | Social/Community]
**Novelty Level**: [Unprecedented / Novel Combination / Unserved Niche Flank — Original Mode only; for Flanking Mode, state the pattern instead]

#### 1. Core Problem & Latent Friction
- **Discovered Friction**: [Manual process, hacky workaround, or recurring job posting found — Original Mode. For Flanking Mode: the target product's stagnation/abandonment symptom instead]
- **Target Audience**: [Specific audience willing to pay for automation]

#### 2. The "Why Now?" Factor (Tech Enabler)
- **Recent Tech Breakthrough**: [What AI capability/API makes this possible today]
- **Why It Couldn't Be Built Earlier**: [What bottleneck was eliminated]

#### 3. Novelty & Prior-Art Verification *(Flanking Mode: "Target Product Status & Displacement Gap" — see `flanking_playbook.md`)*
- **Prior-Art Search Results**: [Findings from 5-pass search — Flanking Mode: findings from the Target Product Status audit instead]
- **Originality Verdict**: [Confirmed Original / Adjacent to Existing Competitor — Flanking Mode: state instead whether the Flanking Eligibility Gate was cleared, and on what evidence]

##### 3.0 Target Product Status (Flanking Mode only — omit entirely for Original Discovery Mode)
- **Target Product**: [Name](url)
- **Pattern Claimed**: [1 / 2 / 3, per `flanking_playbook.md`]
- **Evidence for the pattern**: [traction proof + abandonment/stagnation/gap proof + residual-demand proof, each with a real link — the full bar per pattern, not a single signal]
- **Flanking Eligibility Gate result**: [Genuine Pattern Match: PASS/FAIL + evidence — Displacement Feasibility: PASS/FAIL + the specific reachable audience named]

##### 3.1 Feature Delta Matrix
*Every "Closest Prior Art" cell MUST name the specific product as a link — `[App/Tool Name](url)` — followed by the description. A description with no linked name is not acceptable here even if the same name+link appears again in 3.2; this table is what people actually scan. In Flanking Mode, "Closest Prior Art #1" is the target product itself.*

| Feature / Dimension | Candidate Concept | Closest Prior Art #1 | Closest Prior Art #2 | Innovation Delta / Verdict |
|---|---|---|---|---|
| **Core Mechanics** | [Description] | [App/Tool Name](url) — [Description] | [App/Tool Name](url) — [Description] | [🟢 Novel / 🟡 Reskin] |
| **Distribution** | [Zero-CAC Channel] | [App/Tool Name](url) — [Channel] | [App/Tool Name](url) — [Channel] | [🟢 Advantage / 🔴 Saturated] |
| **Tech Enabler** | [Tech] | [App/Tool Name](url) — [Tech] | [App/Tool Name](url) — [Tech] | [🟢 Breakthrough / 🔴 Stale] |

##### 3.2 Evidence & Verification Audit Log
*Every product named in this report — here, in 3.1, and in any narrative mention — also gets a row in [competitors.md](competitors.md) (Step 6), including the ones screened out. That file is the one a future session reads; this log is the audit trail for this session.*
- **Dorks / Queries Run**: `[query string 1]`, `[query string 2]`
- **Verified URLs Examined**:
  - [App / Tool / Patent 1 Name](url_1) - *Findings summary*
  - [App / Tool / Patent 2 Name](url_2) - *Findings summary*

##### 3.3 Bootstrap Proof (Marketplace / Directory / Two-Sided ideas only — see `domain_saas.md` §5)
*Omit this subsection entirely for non-marketplace ideas; don't leave it as a blank placeholder.*
- **First 20–50 supply-side participants**: [Who specifically, and how are they individually recruited — not "via the network effect," which doesn't exist yet]
- **Single-player value before the flywheel exists**: [What a solo early joiner gets even with zero demand-side visibility]
- **Effect on Proof 2**: [Proof 2 cannot honestly PASS on the strength of the eventual flywheel alone if this subsection can't be answered concretely]

#### 4. Anti-False-Positive 7-Proof Verification Matrix

Before marking any proof PASS, write the strongest REJECT case first (the most skeptical reading of what you actually found) — a PASS that survives its own steelman is the only kind worth trusting. Proofs 1 and 6 are the two easiest to wave through on vibes, so give those two the most scrutiny.

- **Proof 1 (Willingness to Pay & Demand Velocity)**: [PASS / FAIL + Evidence + the steelman rejection case considered]
- **Proof 2 (Zero-CAC Distribution)**: [PASS / FAIL + Specific Channel + the steelman rejection case considered]
- **Proof 3 (Anti-Churn Retention)**: [PASS / FAIL + Frequency Rate + the steelman rejection case considered]
- **Proof 4 (AI Reliability >95%)**: [PASS / FAIL + Risk Mitigation + the steelman rejection case considered]
- **Proof 5 (Micro-Moat)**: [PASS / FAIL + Defensibility Factor + the steelman rejection case considered]
- **Proof 6 (Status Quo Resistance)**: [PASS / FAIL + Non-Software Inertia Check + the steelman rejection case considered]
- **Proof 7 (True Solopreneur Buildability)**: [PASS / FAIL + What in the mechanism is composed-from-existing-SDKs vs. novel-and-uncalibrated, and whether the timeline honestly reflects that split]
- **Protocol Score**: [7/7 -> APPROVED]
- **Approval rate (cumulative, from `ideas_log.md`)**: [X approved / Y evaluated = Z%; plus the batch rate if this session produced 3+ candidates. Apply the re-audit triggers in the Approval-Rate Calibration section — not the raw rate of a one- or two-idea session, which carries no signal.]

#### 5. Solopreneur + AI Feasibility Stack
- **Recommended Tech Stack**: [e.g. Next.js / Vite + Tailwind + LLM/Vision API + Supabase]
- **AI Automation Scope**: [What AI handles automatically]
- **Solo Execution Time**: [MVP estimate, split into ordinary CRUD/UI work vs. novel-component R&D + real-device calibration — e.g. "3 days core app + 4-6 days calibrating on-device acoustic classification across 5+ phone models", not a single undifferentiated number]

#### 6. Legal & Regulatory Safety
*Summary only — the full analysis lives in [legal.md](legal.md) (Step 7). Summarize here, link there, don't duplicate.*
- **Risk Tier**: [🟢 Standard / 🔴 Elevated — see legal_risk_playbook.md]
- **Legal Risk Level**: [Very Low / Low / Moderate — "Very Low" for an 🔴 Elevated-tier idea requires cited research in the dossier to justify it]
- **Blocking findings**: [none / the ones that must be resolved before building]
- **Gatekeepers that matter**: [the actors from the dossier's Axis 2 that actually apply — orders/registries, permits, lobbies, local opposition, boycott risk — or "none, because [reason]"]
- **Notes**: [🟢 Standard tier: a short paragraph is enough. 🔴 Elevated tier: name the specific regulatory/policy surface found, how the closest real competitors scope their claims/disclaimers, and the concrete mitigation this idea adopts.]
- **IP/Trademark check (Flanking Mode only)**: [Confirm the candidate's name/branding/assets are distinct from the target product — see `legal_risk_playbook.md`'s Flanking-Mode Addendum. Omit this line for Original Discovery Mode.]

#### 7. Monetization Strategy
- **Pricing Model**: [e.g. $19/month or $49 one-time]
- **Value Proposition**: [Clear ROI for buyer]

#### 8. Summary Recommendation
- **Status**: [APPROVED / PIVOT REQUIRED / DISCARDED]
```
