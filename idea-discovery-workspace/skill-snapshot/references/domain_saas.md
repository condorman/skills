# B2B Micro-SaaS Domain Directives & Verification Rules

This reference document contains specialized directives and evaluation criteria for **B2B Micro-SaaS, Web Apps & Developer Tools** analyzed by the `idea-discovery` skill.

---

## 1. Friction & Workaround Mining Protocol

Target high-intent business pain points where companies are currently paying money:

1. **Freelance Job Board Mining**: Search Upwork/Fiverr job listings for recurring custom automation requests ($300–$2,000 budget):
   - `"Custom Python script to automate..."`
   - `"Stripe PayPal CSV reconciliation..."`
   - `"API integration between X and Y..."`
2. **Public Feature Request Boards**: Search Canny.io, Featurebase, and Frill boards for bloated incumbent SaaS platforms (e.g. HubSpot, QuickBooks, Shopify). Unserved requests with 100+ votes that have been pending for >1 year are prime standalone Micro-SaaS candidates.
3. **Enterprise Bloat Flank Strategy**: Identify $99+/month enterprise software (e.g., A2X, Quaderno) where solopreneurs only need 1 core feature for $19/month.

---

## 2. B2B SaaS Search Dorks

- `site:producthunt.com/posts "[workflow_tool_keywords]"`
- `site:canny.io "in progress" OR "under review" "[feature_request]"`
- `site:upwork.com "[automation_task_script]"`
- `site:reddit.com/r/MicroSaaS OR site:reddit.com/r/SaaS "[manual_workflow_complaint]"`
- `site:chromewebstore.google.com "[extension_capability]"`

---

## 3. B2B SaaS Moat & Integration Requirements

- Must feature at least one **Deep API Integration** (e.g. Stripe Webhooks, Shopify GraphQL API, Xero OpenAPI, GitHub Actions).
- Must solve a **recurring monthly/quarterly compliance task** (invoicing, VAT OSS reporting, schema guardrails) to ensure <2% monthly churn.
