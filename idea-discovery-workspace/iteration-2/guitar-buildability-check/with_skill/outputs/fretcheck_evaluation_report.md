# Standardized Original Idea Evaluation Report: FretCheck AI (Guitar Setup Diagnostic App)

> **Memory Check Flag (Step 0)**: This candidate is a **near-exact semantic duplicate** of an already-logged idea. See "Duplicate Check" note before Section 1.

### 💡 FretCheck AI: Mic-and-Camera Guitar Setup Diagnostician (Buzz, Action, Truss Rod)

**Context Category**: Mobile App (iOS & Android) — *Category G: Hardware/Sensor-Based Apps*
**Novelty Level**: Novel Combination (externally original — no shipped competitor found — but **internally a duplicate** of an already-evaluated concept in this project's own memory log)

---

## ⚠️ Duplicate Check (Step 0 — Semantic Duplicate Scan)

`docs/ideas_log.md` already contains **Entry #11 — "FretPulse AI: On-Device Acoustic & Vision Guitar Fret Buzz, Action & Truss Rod Setup Assistant"** (evaluated 2026-07-27, logged as APPROVED 6/6). Comparing core mechanics:

| | User's request (this session) | Entry #11 — FretPulse AI (already logged) |
|---|---|---|
| Buzz detection | Microphone analyzes the sound of each plucked fret | 1-second audio pluck per fret, FFT non-harmonic rattle transient detection (2.5–8kHz) |
| Action measurement | Camera measures string height | Camera macro calibration at the 12th fret |
| Truss rod | Regulazione del truss rod | Exact 1/8-turn truss rod directions |

This is the same core mechanic, same sensors, same three symptoms (buzz / action / truss rod), same instrument category. Per the Step 0 duplicate-handling rule, this should not be re-proposed as a fresh, independent discovery. Because the user explicitly asked for this exact idea to be evaluated (not for a new idea to be generated), this report proceeds — but as an **audit/re-evaluation of the existing FretPulse AI entry**, not as a new original concept. The prior entry was scored under an older, less strict internal rubric (a "6-Proof" protocol with **no Proof 7 buildability check at all**, and a Proof 4 verdict of "PASS" with no supporting reliability evidence). This session re-runs the idea through the current v5.0 7-Proof protocol, with real external research, and the result differs materially from the original log entry — see Section 4 and 5.

**Recommendation for the log**: this entry should be appended as a cross-referenced re-audit of #11, not as an independent #26 idea competing for the "Total Ideas Evaluated" count as if it were novel.

---

#### 1. Core Problem & Latent Friction
- **Discovered Friction**: Guitarists diagnosing fret buzz, uncomfortable string action, or truss rod issues currently rely on physical tools (feeler gauges, fret rockers, string-action rulers, $10–$60 on Amazon/StewMac/D'Addario) or a luthier shop visit ($50–$100+ plus multi-day turnaround).
- **Target Audience**: Hobbyist and gigging electric guitarists who want to self-diagnose setup issues at home rather than pay a shop or guess with a feeler gauge.

#### 2. The "Why Now?" Factor (Tech Enabler)
- **Recent Tech Breakthrough**: On-device high-sample-rate audio capture + FFT/onset-detection libraries make isolating a non-harmonic rattle transient from a clean pluck computationally tractable on a phone. Camera-based AR measurement APIs (ARKit/ARCore) exist for general-purpose distance estimation.
- **Why It Couldn't Be Built Earlier**: Mobile CPUs previously couldn't do real-time spectral-flux transient analysis; general tuner apps explicitly filter out non-harmonic noise rather than classify it.
- **Caveat surfaced by this session's research** (not addressed in the original log entry): the "why now" story covers the *audio* half convincingly, but general-purpose phone AR measurement APIs were **not designed for, and are not accurate enough for**, the *camera* half as literally proposed — see Proof 4.

#### 3. Novelty & Prior-Art Verification

**External prior-art search results** (real web searches run this session):
- *Pass 1 (Mechanics-first, App Stores)*: `site:apps.apple.com guitar setup buzz action truss` — no app found doing automated mic-based per-fret buzz classification or camera-based action measurement. One real, relevant competitor surfaced: **Suede Guitar Tuner & Studio** (App Store) — a polyphonic strobe tuner that includes a "Bench Diagnostics" feature offering "guided walkthroughs for buzz, action, relief, and intonation." This appears to be a **manual Q&A/decision-tree wizard** (interactive checklist with a "Dr. Suede" guide persona), not automated sensor classification — the App Store listing gives no indication it analyzes microphone audio per-fret or measures string height via camera. It is the closest real prior art found and should be tracked as a competitor to watch, not dismissed.
- *Pass 2 (GitHub / dev ecosystem)*: `site:github.com guitar fret buzz detection audio OR string action camera measurement` — found adjacent-but-not-identical prior art: **GS-Detector** (inharmonicity-based guitar string/fret detection for tablature transcription) and **Guitar-Chord-Analyzer** (OpenCV/MediaPipe finger tracking on a webcam). Neither targets buzz classification or action measurement, but both confirm the underlying audio/vision techniques are established enough to be composable — useful signal for feasibility, not for prior art of the exact product.
- *Pass 4 (Patents)*: `patents.google.com` search for guitar string height / fret buzz sensing returned only hardware-sensor patents (piezo/ultrasonic pickup systems, CNC fret-slot milling specs, an "optical guitar" fiber-sensing design) — none cover a smartphone camera+mic diagnostic workflow.
- **Camera measurement feasibility check** (new research this session, not present in the original FretPulse report): searched smartphone AR/camera measurement accuracy literature. Findings consistently report **smartphone camera/AR distance measurement accuracy on the order of 1–2 cm without a physical reference object in frame** — two to three orders of magnitude coarser than the ~0.1–0.5 mm increments that distinguish meaningful guitar action settings (typical 12th-fret action ranges ~1.2–2.5mm). This is a material feasibility finding that directly affects Proof 4 below.
- **Originality Verdict (external)**: Novel Combination / Unserved Niche Flank — no shipped competitor automates both halves of this workflow. **Originality Verdict (internal)**: Duplicate of logged Entry #11.

##### 3.1 Feature Delta Matrix
| Feature / Dimension | Candidate Concept (FretCheck AI) | Closest Prior Art #1 (Suede Guitar Tuner & Studio) | Closest Prior Art #2 (Physical gauges: StewMac/D'Addario action ruler + fret rocker) | Innovation Delta / Verdict |
|---|---|---|---|---|
| **Core Mechanics** | Per-fret mic pluck → FFT buzz classification + camera-based action height measurement | Guided Q&A diagnostic wizard (no sensor automation) | Manual metal ruler/feeler-gauge reading, human-interpreted | 🟢 Novel automation angle / 🔴 camera-measurement precision not yet proven feasible on bare phone hardware |
| **Distribution** | App Store SEO + #GuitarTok demo clips | Existing tuner-app install base / App Store SEO | Amazon/Guitar Center retail | 🟢 Advantage (viral demo potential) |
| **Tech Enabler** | On-device FFT transient analysis (established technique) + camera AR measurement (not built for sub-mm precision) | N/A (manual wizard) | N/A (physical tool) | 🟡 Mixed — audio side is a real breakthrough; camera side needs a redesign (see Proof 4) |

##### 3.2 Evidence & Verification Audit Log
- **Dorks / Queries Run**: `app measure guitar string action height camera smartphone`, `app detect fret buzz microphone guitar setup diagnosis`, `"truss rod" app guitar setup assistant iOS Android`, `site:apps.apple.com guitar setup buzz action truss`, `patents.google.com guitar string height measurement camera OR fret buzz acoustic detection`, `site:github.com guitar fret buzz detection audio OR string action camera measurement`, `"StewMac" OR "luthier" app AI guitar setup diagnosis smartphone 2025 2026`, `smartphone camera macro measurement accuracy sub-millimeter AR ruler limitations`
- **Verified URLs Examined**:
  - [Suede Guitar Tuner & Studio – App Store](https://apps.apple.com/us/app/suede-guitar-tuner-studio/id6767552764) – *Real, shipped competitor with a "Bench Diagnostics" guided walkthrough for buzz/action/relief/intonation; appears to be Q&A-based, not sensor-automated.*
  - [GS-Detector (GitHub)](https://github.com/mogeadis/GS-Detector) – *Confirms inharmonicity-based guitar string/fret audio analysis is an established, working technique — supports feasibility of the acoustic half.*
  - [Guitar-Chord-Analyzer (GitHub)](https://github.com/tjross28/Guitar-Chord-Analyzer) – *OpenCV/MediaPipe fretboard camera tracking exists, but for finger/chord tracking, not sub-mm height measurement.*
  - [Turning Your Smartphone Into a Ruler (CMU)](https://www.scs.cmu.edu/news/2015/turning-your-smartphone-ruler-camera-and-imu-combine-accurate-measurements) and related AR-ruler accuracy coverage – *Confirms phone camera/AR measurement is generally only accurate to ~1–2cm without a physical reference object in frame, informing the Proof 4 feasibility concern below.*
  - Google Patents results (US5033353A, US4653376A, CN112466269A, US7728210B2) – *All hardware-sensor or manufacturing-tolerance patents; none describe a smartphone camera/mic diagnostic app.*

---

#### 4. Anti-False-Positive 7-Proof Verification Matrix

- **Proof 1 (Willingness to Pay & Demand Velocity)**: **PASS** — Verified real spend: physical action gauges and fret rockers are actively sold ($10–$60, StewMac/D'Addario/Amazon listings found in search), and professional setups run $50–$100+ at shops. Steelman rejection considered: is this spend "dying," i.e., are guitarists happy paying the shop and not looking for a DIY alternative? Evidence found (active forum/how-to content volume on fret buzz diagnosis, dedicated retail SKUs for the manual tools) suggests ongoing real demand for self-diagnosis, not a vanished market. No explicit Google Trends growth curve was pulled this session — flagging that momentum (rising vs. flat) is asserted from indirect evidence (active retail + content), not a directly verified trend chart.
- **Proof 2 (Zero-CAC Distribution)**: **PASS** — Short-form video (#GuitarTok/Reels/Shorts) showing a "before/after" 60-second fret-buzz fix is a strong, cheap organic hook; App Store search terms ("guitar action app", "fret buzz") are unclaimed by a dedicated automated tool today (only the Q&A-style Suede app half-covers this niche).
- **Proof 3 (Anti-Churn Retention)**: **PASS (borderline)** — Steelman rejection: for a single-guitar casual player, this is close to a "once or twice a year" utility (string changes, seasonal humidity shifts), which risks the Proof 3 "rare event" failure pattern. It passes on the strength of two mitigating facts found in this domain: (a) the average serious guitarist owns 2–4 instruments, multiplying touch-points, and (b) seasonal truss-rod relief drift is a real, recurring (not one-time) phenomenon. This is weaker than a true daily/weekly workflow tool and should be watched, not assumed.
- **Proof 4 (AI Technical Reliability >95%)**: **FAIL as literally specified.** Splitting the mechanism in two:
  - *Microphone/buzz half*: Plausible. Per-fret transient/onset detection is an established DSP technique (confirmed via GS-Detector prior art), though a >95% accuracy claim generalized across guitar types (acoustic/electric/bass), pickup types, string gauges, and ambient noise still has no existing pretrained model or public dataset to lean on — it would need to be built and validated from scratch.
  - *Camera/action-height half*: **Not currently reliable as described.** This session's research found smartphone camera/AR measurement is accurate to roughly 1–2cm without a physical reference object in the frame, while meaningful guitar action adjustments are made in ~0.1–0.5mm increments — two to three orders of magnitude too coarse. "The camera measures string height" as stated in the user's brief is not achievable with a bare phone camera and no calibration object.
  - **Required mitigation to reach PASS**: redesign the camera step to require a physical reference object of known size in-frame (e.g. a credit card, a printed calibration card, or a cheap $5 companion action-gauge card held against the strings) so the measurement becomes a scaled photogrammetry problem instead of raw absolute distance estimation — plus a confidence score and "measurement uncertain, please re-shoot" fallback rather than presenting an unqualified number.
- **Proof 5 (Micro-Moat Defensibility)**: **PASS** — the combination of a tuned per-fret acoustic classifier, a photogrammetry-with-reference-object measurement pipeline, and a deterministic truss-rod turn-direction engine is not a 1-day AI-wrapper clone; each piece requires real tuning work.
- **Proof 6 (Status Quo Resistance)**: **PASS (with a caveat the original log entry didn't surface)** — the non-software substitute isn't quite "free": it's a cheap ($10–$60) physical toolkit that, once purchased, is actually **more precise** than the proposed camera measurement (a $15 action ruler reads to ~0.1mm directly; the app's camera cannot, unmitigated). The app's real value-add is *not* raw measurement accuracy — it's automated per-fret buzz localization across 22 frets (tedious and skill-dependent to do manually with a fret rocker) and plain-English truss-rod guidance that removes the "fear of breaking the neck." That's a genuine time/confidence saving (avoiding a $75+, multi-day shop trip) even if the camera-measurement claim needs to be scoped down.
- **Proof 7 (True Solopreneur Buildability)**: **PASS — but only with an honest, non-padded timeline (see Section 5).** Checklist run:
  - Custom signal processing the developer must design/tune? **Yes** (per-fret FFT transient classifier) — red flag present.
  - Real-time CV/measurement with a precision budget? **Yes** (camera action-height measurement) — red flag present.
  - >95% accuracy claim for a novel on-device model with no existing dataset? **Yes** (buzz classifier) — red flag present.
  - Hardware calibration against physical-world variance (device models, ambient noise, lighting, guitar types)? **Yes, substantial** — red flag present.
  - Can the core mechanism mostly compose existing SDKs rather than invent new techniques? **Partially.** The camera half can be redesigned to compose ARKit/ARCore + a reference-object algorithm (lower risk once redesigned); the acoustic half is closer to genuine custom DSP (higher risk, no off-the-shelf "guitar buzz classifier" library exists).
  - Graceful, cheap fallback if the novel component underperforms? Needs to be designed in explicitly (confidence-gated results + manual "does it still buzz? yes/no" override) — not present in the original brief, but straightforward to add.
  - **Verdict on the estimate**: the *original logged entry's* "5-7 days" MVP claim does not survive this checklist — it is exactly the padded generic-CRUD estimate the v5.0 framework's calibration section warns against. See Section 5 for the honest breakdown.
- **Protocol Score**: **6/7 → PIVOT REQUIRED** (missing proof: Proof 4, AI Technical Reliability — specifically the camera-based action-height measurement as literally specified).

---

#### 5. Solopreneur + AI Feasibility Stack
- **Recommended Tech Stack**: React Native or native (Swift/Kotlin) + iOS AVAudioEngine / Android AAudio for capture + a custom on-device FFT/onset-detection pipeline (not a pre-built SDK) + ARKit/ARCore (redesigned around a physical reference object) for the camera step + local SQLite/Core Data for the multi-guitar "garage" log.
- **AI Automation Scope**: On-device only (no cloud inference needed) — per-fret spectral transient classification for buzz, and reference-object-scaled photogrammetry for action height. Deterministic rule engine (not AI) for truss-rod turn-direction guidance.
- **Solo Execution Time — honest breakdown (this is the key finding this session adds versus the original log entry's undifferentiated "5-7 days")**:
  - **Ordinary CRUD/UI work** (onboarding, multi-guitar profile "garage", results screens, PDF/heatmap export, settings): **~5 days**.
  - **Novel-component R&D: acoustic buzz classifier** — initial FFT/onset-detection algorithm: 3-4 days; **real-device calibration across ≥5 guitars (acoustic, electric-magnetic-pickup, electric-piezo, different string gauges) and ≥5 phone models in varied ambient noise, iterating on false-positive/negative rates toward a defensible accuracy number**: **10-15 additional days**.
  - **Novel-component R&D: camera action-height measurement redesign** — building the reference-object-based photogrammetry flow (not the originally-proposed unmitigated camera measurement) plus UX for correct photo capture: 4-5 days; **calibration/validation across device cameras, focal lengths, and lighting conditions**: **5-7 additional days**.
  - **Deterministic truss-rod guidance engine**: low risk, ~2 days.
  - **Integration, cross-device QA, App Store submission assets**: ~5 days.
  - **Total realistic solo MVP estimate: roughly 6-9 weeks (≈30-45 working days)**, not the "5-7 days" figure carried in the existing log entry. The gap is almost entirely the acoustic-classifier and camera-calibration R&D, exactly the kind of work the current framework's Proof 7 calibration section flags as commonly underestimated.

---

#### 6. Legal & Regulatory Safety
- **Risk Tier**: 🟢 Standard — this is a hobbyist diagnostic/calculation tool operating on audio/photo data of an instrument (not the user's body), captured and processed for the user's own benefit. It does not move money, does not give health/medical/financial/legal advice, has no plausible child-directed use case, and does not capture biometric data about a person (voice/face/gait) — it captures acoustic and visual data about a guitar.
- **Legal Risk Level**: Low.
- **Notes**: No payment/PCI scope for the core diagnostic feature (a later Stripe-based Pro unlock would be standard IAP handling, not a regulatory concern). Recommended good practice regardless of tier: keep audio clips and fretboard photos processed on-device and not uploaded/retained on a server by default, since guitar photos could incidentally capture bystanders or private spaces in the background — a privacy-hygiene note, not a regulatory blocker.

---

#### 7. Monetization Strategy
- **Pricing Model**: Free single-guitar diagnostic; $4.99 one-time "Pro" unlock or $2.99/mo for unlimited multi-guitar garage + PDF setup certificates.
- **Value Proposition**: Replaces a $75+, multi-day shop setup visit with an at-home diagnostic that localizes which of 22 frets is causing buzz and gives plain-English truss-rod direction — positioned around diagnosis + guidance, not raw measurement precision (see Proof 6 caveat).

---

#### 8. Summary Recommendation
- **Status**: **PIVOT REQUIRED (6/7)**
- **What needs to change**: (1) Redesign the camera-based action-height measurement to require a physical reference object in-frame rather than an unmitigated camera estimate — the current framing is not achievable at the precision guitarists need. (2) Ship the buzz classifier with a visible confidence score and a manual "still buzzing? yes/no" override so a misclassification doesn't read as an authoritative diagnosis. (3) Correct the buildability estimate this idea would otherwise inherit from the log's existing FretPulse entry: budget **6-9 weeks**, not "5-7 days," and treat the acoustic-classifier and camera-calibration work as genuine R&D milestones with their own testing checkpoints, not a subtask of general app-building.
- **Duplicate note for the record**: this concept and Entry #11 (FretPulse AI) are the same underlying product. Recommend the project's log treat this report as a **re-audit that supersedes #11's Proof 4/Proof 7 findings**, rather than logging a new, independently-numbered idea.
