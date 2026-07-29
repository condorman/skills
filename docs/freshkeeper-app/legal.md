# ⚖️ Legal & Gatekeeper Dossier: FreshKeeper AI

**Idea**: Household Food Expiration Tracker & Zero-Waste Chef · **Target market / jurisdictions**: Italy / EU / US
**Risk tier**: 🟢 Standard
**Overall exposure**: Very Low · **Blocking findings**: None
**Last updated**: 2026-07-29

---

## 1. Litigation exposure — is there a realistic risk of a dispute?

**Short answer**: Very low litigation exposure. The application operates as a private household utility for organizing personal grocery inventory and receiving shelf-life reminder alerts. All receipt OCR processing occurs on-device or via secure API calls without storing sensitive payment data or biometric information.

| # | Counterparty | What triggers it | Likelihood | Severity | Avoidable by design? | Source |
|---|---|---|---|---|---|---|
| L1 | Supermarket Retailers | Receipt OCR scanning of store receipts | Low | Low | Yes — Receipts are user-owned proof of purchase; no scraping of store websites required | [EU Consumer Rights Directive](https://eur-lex.europa.eu/) |
| L2 | End Users | Food spoilage occurring before estimated date | Low | Med | Yes — Clear app disclaimer: "Expiration dates are estimates. Always inspect food visually and smell before consuming" | Standard Product Terms |
| L3 | Users with Allergies | AI-generated recipes including potential allergens | Low | High | Yes — Mandatory allergy onboarding filter + explicit recipe disclaimer | [EU Food Information Regulation 1169/2011](https://eur-lex.europa.eu/) |

---

## 2. Gatekeepers & non-regulatory blockers

| Actor | Present here? | Does it block us? | Does it protect an incumbent? | Cost / time to clear | Evidence |
|---|---|---|---|---|---|
| **Regulators & authorities** (Data Protection / GDPR, Consumer Protection) | Yes | No | No | 0 days (standard privacy policy + local storage) | [GDPR Art 6](https://gdpr-info.eu/) |
| **Government law & current legislation** (EU Food Waste Reduction Targets 2026/2030) | Yes | No — Favorable tailwind | No | 0 days | [EU Green Deal Strategy](https://ec.europa.eu/) |
| **Pending legislation & political instability** | No | No | No | N/A | N/A |
| **Closed associations, professional orders & registries** | No | No | No | N/A | N/A |
| **Local bureaucracy, municipal permits & building concessions** | No | No | No | N/A | N/A |
| **Trade associations & lobbies** | No | No | No | N/A | N/A |
| **Citizen committees & NIMBY opposition** | No | No | No | N/A | N/A |
| **Ethical or cultural boycott risk** | No | No | No | N/A | N/A |

### Reading the gates honestly

- **Data Privacy (GDPR)**: Household inventory data is stored locally in device SQLite database. If sync is enabled, Firebase / Apple iCloud private database is used. No selling of user purchase behavior to third-party data brokers.
- **Apple App Store & Google Play Guidelines**: Full compliance with App Store Guideline 5.1.1 (Data Collection & Storage) and Guideline 3.1.1 (In-App Purchases).

---

## 3. Verdict & what to do about it

- **Blocking findings**: None.
- **Design changes adopted as a result**: Added mandatory food safety & allergy disclaimer modal during onboarding and on recipe generation cards.
- **Defensibility gained**: Privacy-first, local-first storage architecture appeals to security-conscious consumers compared to cloud-mandatory competitors.
- **Open questions for a specialist**: None required for 🟢 Standard tier launch.

*This dossier is structured research, not legal advice. Standard mobile application disclaimers apply.*
