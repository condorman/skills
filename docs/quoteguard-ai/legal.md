# ⚖️ Legal & Gatekeeper Dossier: QuoteGuard AI

**Idea**: Contractor Quote Auditor & Home Repair Cost Estimator · **Target market / jurisdictions**: US & EU (Italy/Germany/UK)
**Risk tier** (per `legal_risk_playbook.md`): 🟢 Standard
**Overall exposure**: Very Low · **Blocking findings**: None
**Last updated**: 2026-07-29

---

## 1. Litigation exposure — is there a realistic risk of a dispute?

**Short answer**: Very low litigation exposure. The app functions as an independent, parameter-based estimation tool for consumer negotiation support. It does not issue binding contractor contracts or process payments. Standard liability disclaimers on PDF export cover price variances.

| # | Counterparty | What triggers it | Likelihood | Severity | Avoidable by design? | Source |
|---|---|---|---|---|---|---|
| L1 | Contractors / Trade Users | Disagreement with generated fair price benchmark | Low | Low | Yes — clear disclaimer on PDF report | Standard product design |
| L2 | Data Subjects / Users | Local storage of home repair notes | Low | Low | Yes — 100% on-device SQLite storage | GDPR / CCPA compliant by design |

---

## 2. Gatekeepers & non-regulatory blockers

| Actor | Present here? | Does it block us? | Does it protect an incumbent? | Cost / time to clear | Evidence |
|---|---|---|---|---|---|
| **Regulators & authorities** | No | No | No | N/A | Standard consumer utility |
| **Government law & legislation** | No | No | No | N/A | N/A |
| **Pending legislation** | No | No | No | N/A | N/A |
| **Closed associations & registries** | No | No | No | N/A | N/A |
| **Local bureaucracy & permits** | No | No | No | N/A | N/A |
| **Trade associations & lobbies** | No | No | No | N/A | N/A |
| **Citizen committees & NIMBY** | No | No | No | N/A | N/A |
| **Ethical or cultural boycott risk** | No | No | No | N/A | N/A |

---

## 3. Verdict & what to do about it

- **Blocking findings**: None.
- **Design changes adopted as a result**: PDF Audit Certificate includes explicit negotiation disclaimer ("Estimates are for informational negotiation purposes based on regional material & labor indices").
- **Defensibility gained**: None (standard consumer legal surface).
- **Open questions for a specialist**: None needed for v1.

*This dossier is structured research, not legal advice.*
