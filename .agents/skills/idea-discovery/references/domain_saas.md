# B2B Micro-SaaS Domain Directives & Verification Rules

This reference document contains specialized directives and evaluation criteria for **B2B Micro-SaaS, Web Apps & Developer Tools** analyzed by the `idea-discovery` skill — including verified directories, reference portals, and other two-sided marketplace web apps, which fall under this file's scope even though they don't look like a typical API-integration tool (see Section 5).

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

---

## 4. Workflow-Vertical Rotation & Anti-Fixation Gate

- **CHECK `ideas_log.md`**: Inspect the last 3 B2B SaaS / developer-tool entries.
- **STRICT ROTATION RULE**: If 2+ recent entries cluster on the same workflow vertical (e.g. Stripe/payment reconciliation tools, or dispute/chargeback tools, or schema/API-guardrail tools), **DO NOT propose another tool in that same vertical**. Rotate to a genuinely different workflow category — e.g. from payments/finance-ops to compliance/reporting, from developer-CI tooling to customer-support automation, from e-commerce operations to content/SEO tooling — rather than a differently-named tool solving the same underlying job. Two ideas that both "watch a webhook and auto-generate a document" are the same shape even if one is about chargebacks and the other about VAT filings — only rotate if the actual buyer, workflow, and integration surface are meaningfully different.

---

## 5. Marketplace / Verified-Directory / Reference-Portal Ideas: Template-Reskin Detection & Bootstrap Proof

Ideas shaped like "a verified professional directory + credential check + event/webinar ticketing + content hub + product showcase + an embeddable badge that drives B2C traffic back to the portal" are a recognizable **software template**, not a fresh concept each time. This exact bundle of components can be — and has been — proposed for machinery-safety consultants, holistic-health professionals, acoustics technicians, dog trainers, and art restorers in the same session, each with a different vertical-sounding name and each scored as an independent 7/7 approval. That's the same failure the rotation gate above exists to prevent, just one level more abstract: the *vertical name* changes, but the *architecture and monetization mechanism* doesn't.

- **Before proposing or approving one of these**, check the log for any existing entry built from the same component bundle (verified-credential directory + Stripe Connect ticketing + content publishing + embeddable badge, in any combination of 3+ of those pieces), regardless of what profession it's addressed to. If one exists, treat this as the rotation gate above — pick a genuinely different software shape, not just a different noun.
- **Every two-sided marketplace/directory idea must pass a Bootstrap Proof before Proof 2 (Zero-CAC Distribution) can honestly PASS.** A "professionals share a badge that drives B2C traffic" loop is real once it's running, but it does nothing on day one when zero professionals have joined yet — there's no badge anywhere and no traffic to speak of. State concretely: who are the first ~20-50 professionals, how are they individually recruited (not "via the network effect," which doesn't exist yet), and does the product offer them something valuable in single-player mode (e.g. a free tool they'd want even with zero B2C visitors) so they have a reason to join before the flywheel exists. If the report can't answer this concretely, Proof 2 should not pass on the strength of the eventual flywheel alone.
- **Watch for scope creep disguised as one MVP.** These ideas tend to bundle a directory + ticketing + OCR credential verification + a content/article system + a product store + (sometimes) a companion mobile app — that's several distinct products glued together, not one. Apply Proof 7 accordingly: either the MVP genuinely cuts scope to a thin vertical slice (e.g. directory + one monetization path, nothing else, for the true first version) or the timeline needs to honestly reflect building multiple subsystems, not the same 10-12 days regardless of how much is bundled in.
