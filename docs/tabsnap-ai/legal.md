# ⚖️ Legal & Gatekeeper Dossier: TabSnap AI

**Idea**: Instant On-Device OCR Receipt Splitter & Group Expense Auditor · **Target market / jurisdictions**: Global (EU & US first)
**Risk tier**: 🟢 Standard
**Overall exposure**: Very Low · **Blocking findings**: None
**Last updated**: 2026-07-29

---

## 1. Litigation exposure — is there a realistic risk of a dispute?

**Short answer**: Very low litigation exposure. The app functions strictly as a local utility calculator and document parser on the user's phone. It does not store user financial credentials, process money directly, or handle regulated banking transactions. Payment settlement is delegated to official third-party deep-link payment schemes ([Venmo](https://venmo.com), [Revolut](https://revolut.com), [PayPal](https://paypal.com)).

| # | Counterparty | What triggers it | Likelihood | Severity | Avoidable by design? | Source |
|---|---|---|---|---|---|---|
| L1 | Payment Platforms ([Venmo](https://venmo.com), [Revolut](https://revolut.com)) | Deep-linking with custom URI schemes for payment settlement | Low | Low | Yes — use standard public deep-link specifications (`venmo://pay`, `revolut.me`) | [Venmo Developer Docs](https://developer.venmo.com) |
| L2 | Data Subjects / Users | Processing receipt photos containing business names or printed items | Low | Low | Yes — 100% on-device processing via VisionKit/MLKit; zero images uploaded to cloud servers | [GDPR Art. 6(1)(f)](https://gdpr-info.eu/) |

---

## 2. Gatekeepers & non-regulatory blockers

| Actor | Present here? | Does it block us? | Does it protect an incumbent? | Cost / time to clear | Evidence |
|---|---|---|---|---|---|
| **Regulators & authorities** | No | No | No | €0 / 0 days | Financial regulation does not apply to client-side calculators |
| **Government law & current legislation** | No | No | No | €0 / 0 days | Standard consumer utility software |
| **Pending legislation & political instability** | No | No | No | €0 / 0 days | No pending rules affecting mobile calculators |
| **Closed associations & professional registries** | No | No | No | €0 / 0 days | N/A |
| **Local bureaucracy & municipal permits** | No | No | No | €0 / 0 days | N/A |
| **Trade associations & lobbies** | No | No | No | €0 / 0 days | N/A |
| **Citizen committees & NIMBY opposition** | No | No | No | €0 / 0 days | N/A |
| **Ethical or cultural boycott risk** | No | No | No | €0 / 0 days | Clean consumer utility |

---

## 3. Verdict & what to do about it

- **Blocking findings**: None.
- **Design changes adopted as a result**: Deferred all monetary transfer execution to native payment apps via public URI schemes (`venmo://`, `revolut.me/`, `paypal.me/`). 100% local on-device VisionKit/MLKit execution to guarantee total data privacy compliance under GDPR and CCPA.
- **Defensibility gained**: Privacy-first positioning (zero server cloud upload) creates trust advantage over legacy competitors.
- **Open questions for a specialist**: None.

*This dossier is structured research, not legal advice.*
