# ⚖️ Legal & Gatekeeper Dossier: RentShield AI

**Idea**: Room-by-room tenant move-in inspection & security deposit protection vault  
**Target market / jurisdictions**: US, UK, EU (Italy, Germany, France)  
**Risk tier**: 🟢 Standard  
**Overall exposure**: Very Low  
**Blocking findings**: None  
**Last updated**: 2026-07-29

---

## 1. Litigation exposure — is there a realistic risk of a dispute?

**Short answer**: Very low litigation exposure. The app serves as a personal evidentiary compiler and photo document organizer for the tenant. It does not provide legal advice, issue binding legal verdicts, or act as an escrow agent. Standard disclaimers clarify that reports represent factual photographic records compiled by the user.

| # | Counterparty | What triggers it | Likelihood | Severity | Avoidable by design? | Source |
|---|---|---|---|---|---|---|
| L1 | Landlord / Property Manager | Disagreeing with tenant's recorded photo condition | Low | Low | Yes — Cryptographic SHA-256 metadata timestamps & clear room labeling ensure objective proof | Standard evidence rules |
| L2 | User / Tenant | Deposit dispute loss despite using the app | Low | Low | Yes — Explicit disclaimer that app compile records & does not guarantee small-claims court outcomes | In-app Terms of Service |
| L3 | Data Privacy Regulators | Local photo storage & EXIF metadata handling | Low | Low | Yes — 100% local-first storage model; zero personal photos sent to third-party cloud without user export | GDPR Art 6 / CCPA |

### Key Regulatory & Policy Considerations
- **Third-Party ToS**: Zero third-party web scraping required. Photos and metadata are captured natively on the device camera.
- **Data & Privacy (GDPR / CCPA)**: App operates on a local-first privacy model. Photos, EXIF tags, and generated PDFs remain strictly on user's device storage unless explicitly shared by the user via email or PDF export.
- **Legal Advice Disclaimers**: App explicitly displays a clear notice: *"RentShield AI provides digital photo auditing tools and metadata verification. It does not provide formal legal advice or guarantee specific dispute resolutions."*

---

## 2. Gatekeepers & non-regulatory blockers

| Actor | Present here? | Does it block us? | Does it protect an incumbent? | Cost / time to clear | Evidence |
|---|---|---|---|---|---|
| **Regulators & authorities** | No | No | No | N/A | Local-first utility app |
| **Government law & current legislation** | No | No | No | N/A | Tenant evidence is admissible in small-claims deposit disputes |
| **Pending legislation** | No | No | No | N/A | Rental deposit protection laws (e.g. UK Tenancy Deposit Scheme, US State Security Deposit Acts) enforce tenant evidence rights |
| **Closed associations & registries** | No | No | No | N/A | No professional realtor/landlord registry needed |
| **Local bureaucracy & municipal permits** | No | No | No | N/A | Consumer software app |
| **Trade associations & lobbies** | No | No | No | N/A | Landlord associations cannot restrict tenants from taking photos of their rental unit |
| **Citizen committees & NIMBY opposition** | No | No | No | N/A | N/A |
| **Ethical or cultural boycott risk** | No | No | No | N/A | Pro-consumer & anti-waste alignment |

---

## 3. Verdict & what to do about it

- **Blocking findings**: None.
- **Design changes adopted as a result**:
  1. Local-first storage architecture (zero mandatory cloud account setup) to maximize privacy and remove GDPR DPA requirements.
  2. Cryptographic SHA-256 local signature embedded directly into generated PDF metadata for tamper-evident proof.
  3. Clear legal disclaimer displayed prior to PDF export.
- **Defensibility gained**: SHA-256 cryptographic verification creates a trusted evidentiary standard for small-claims disputes.
- **Open questions for a specialist**: None for MVP launch. Standard terms of use cover record-keeping disclaimers.

*This dossier is structured research, not legal advice. Elevated-tier findings warrant review by a qualified professional in the target jurisdiction before launch.*
