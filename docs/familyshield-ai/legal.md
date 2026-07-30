# ⚖️ Legal & Gatekeeper Dossier: FamilyShield AI

**Idea**: family anti-scam shield — code-word protocol vault, LLM suspicious-message check, scam radar, family-circle alerts · **Target market / jurisdictions**: US-first (where the loss statistics and paid call-blocking WTP are), EU/Italy as secondary
**Risk tier** (per `legal_risk_playbook.md`): 🟢 **Standard** — no health content, no money movement, no minors as users, no biometric storage (voice-print matching was deliberately excluded from the design), no professional-advice substitution
**Overall exposure**: **Low–Moderate** · **Blocking findings**: none
**Last updated**: 2026-07-30

---

## 1. Litigation exposure — is there a realistic risk of a dispute?

**Short answer**: the only material exposure is **liability for output**: an elderly user relies on a "no risk indicators found" verdict and then loses money to the message the app cleared. Everything else is routine consumer-app hygiene. The exposure is avoidable by design — never output "safe", only "risk indicators + verification steps" — which is exactly how the real competitors scope it.

| # | Counterparty | What triggers it | Likelihood | Severity | Avoidable by design? | Source |
|---|---|---|---|---|---|---|
| L1 | User harmed by a wrong output | A false-negative classification ("looks fine") relied on for a payment decision; average elder-fraud loss is >$38k per victim | Med | High | Yes — three-state output (risk indicators / no indicators / uncertain + verify), never a "safe" verdict; the pattern [Scamio](https://www.bitdefender.com/en-us/consumer/scamio) and [Genie](https://www.malwarebytes.com/solutions/best-scam-detection-tools) already use | [IC3 Elder Fraud brochure](https://www.ic3.gov/Outreach/Brochures/Elder_Fraud_Tri-fold.pdf) |
| L2 | Data subjects (third parties) | Scam messages forwarded into the app contain other people's personal data (names, numbers, links); processing/storage without their basis | Low | Low | Yes — process transiently, don't retain message content, store only classification metadata; publish a plain-language privacy notice | design choice |
| L3 | Platform operators (Apple/Google) | Call Directory / SMS filter extensions misuse; claiming "call recording" or "deepfake detection" capabilities the OS doesn't permit | Low | Med | Yes — the design uses only documented extension points and makes no live-call claims | design choice |
| L4 | Scam victims' family members as data subjects | Adult children see parents' forwarded messages — intra-family processing, consent flows must cover the protected person, not just the subscriber | Low | Low | Yes — onboarding consent from the protected family member, plain-language (elderly users) | design choice |

Surfaces checked and found clear:
- **Third-party ToS**: the radar ingests public government feeds (FTC/IC3/AARP alerts); no scraping of gated sources.
- **IP & trademark**: "FamilyShield" as a working name would need a mark search before launch (generic-sounding, likely collisions in the security category) — moot given the verdict.
- **Money movement / PCI**: none — subscriptions via app-store billing only.
- **Minors**: the user base is adults protecting elderly parents; no children's data.
- **Biometric**: explicitly excluded — no voice prints, no audio storage (this is also what keeps Proof 7 honest).
- **EU AI Act**: the LLM classification is a chatbot-style interaction → transparency duty ("you are talking to an AI") applies; no higher-risk use case triggered.

---

## 2. Gatekeepers & non-regulatory blockers

This is a pure digital product with no local, professional, or physical footprint, so the axis is close to empty — with reasons, not blanks.

| Actor | Present here? | Does it block us? | Does it protect an incumbent? | Cost / time to clear | Evidence |
|---|---|---|---|---|---|
| **Regulators & authorities** | FTC/FBI appear only as *publishers of the demand anchors and free consumer advice* — they don't regulate this product category | No | Mildly — their free advice ([NCA Safe Word campaign](https://www.staysafeonline.org/campaigns/safeword)) is part of the status quo that beats the product (Proof 6), but that's competition, not a gate | — | [NCA](https://www.staysafeonline.org/campaigns/safeword) |
| **Government law & current legislation** | Consumer/subscription law applies (auto-renewal disclosure, cancellation flow) — routine | No | No | App-store billing handles most of it | — |
| **Pending legislation & political instability** | Scam/robocall regulation (STIR/SHAKEN enforcement, AI-voice rules) is *demand-positive* for the category; nothing pending threatens the mechanic | No | No | — | [Vorp Labs tracker](https://vorplabs.com/ai-threat-monitoring) |
| **Closed associations, professional orders & registries** | Not applicable — no licensed profession involved; consumer self-help tooling | — | — | — | — |
| **Local bureaucracy, municipal permits** | Not applicable — no physical footprint anywhere | — | — | — | — |
| **Trade associations & lobbies** | Telcos and security vendors are competitors, not gatekeepers; no association controls access to users | No | Their *products* are the barrier (free loss-leaders), not their lobbying | — | [competitors.md](competitors.md) |
| **Citizen committees & NIMBY** | Not applicable | — | — | — | — |
| **Ethical / cultural boycott risk** | One plausible bad headline: "App told grandma a message was safe; she lost $40k." This is a launch/PR risk, not a legal one — and it maps to row L1 and the never-say-safe design | Low likelihood, high damage if it happens | No | Handled by output design + not overclaiming in marketing | — |

---

## 4. Verdict & what to do about it

- **Blocking findings**: none. Nothing legal would have stopped this product; the market does that on its own (see [evaluation.md](evaluation.md), Proof 2/5/6).
- **Design changes adopted as a result of this dossier**: (1) no voice-print or audio storage — kills the biometric tier and keeps Proof 7 honest; (2) never-say-safe output contract — kills most of L1; (3) transient processing of forwarded messages — kills L2.
- **Defensibility gained**: none — no gate exists that would stay shut behind us; the absence of gates is precisely why the space is flooded with free vendor tools.
- **Open questions for a specialist**: none worth paying for at this verdict. If ever revisited: whether the three-state output + disclaimer genuinely caps L1 exposure in US state consumer-protection law, and a trademark screen for the product name.
- **Effect on the idea's status**: none — the DISCARDED verdict rests on market grounds (Proofs 2, 5, 6), not legal ones.

*This dossier is structured research, not legal advice.*
