# Anti-False-Positive Evaluation Framework (5-Proof Verification Protocol)

This document defines the strict, anti-false-positive evaluation criteria designed to eliminate bad ideas early and ensure that only ideas with verified commercial viability, low churn, organic distribution, and high technical reliability are approved.

---

## The 5 Pitfalls of Idea Evaluation

| Pitfall | Common Delusion | Real-World Failure Reason |
|---------|-----------------|---------------------------|
| **1. Complaining ≠ Paying** | "People complain about this on Reddit, so they will buy my app." | Pain is mild; users prefer free hacky workarounds over paying $15/mo. |
| **2. Distribution Blindspot** | "The app is easy to build in 3 days with AI." | Acquiring 1 customer costs $150 in ads for a $20 tool; solopreneur has no organic reach. |
| **3. High Churn Trap** | "Solves a real problem (e.g. file conversion)." | User solves the problem once and cancels subscription immediately. |
| **4. Zero Moat (Commodity Wrapper)** | "It wraps an LLM API nicely." | 20 identical clones appear on Product Hunt within 7 days; base LLMs add the feature for free. |
| **5. AI Reliability Failure** | "AI will handle 100% of the workflow." | LLM hallucinations or edge-case breaks cause endless support tickets that overwhelm 1 person. |

---

## The 5-Proof Verification Protocol

Every idea MUST pass all 5 verification proofs to receive an **APPROVED** status.

### Proof 1: Willingness to Pay (WTP Test)
- **Criterion**: There MUST be concrete evidence of active financial spend addressing this problem today.
- **Verification Indicators**:
  - Companies hiring freelancers on Upwork/Fiverr paying $200–$2,000 for this exact custom task.
  - Existing clunky/bloated competitors charging $30+/mo with active paying user reviews.
  - Active search volume for `"buy [tool name]"` or `"paid alternative to [tool]"`.
- **Verdict**: If users only complain but never pay for existing workarounds, **REJECT (WTP Failure)**.

### Proof 2: Zero-CAC Organic Distribution Channel
- **Criterion**: The product MUST have a clear, built-in organic customer acquisition channel that requires **$0 in ad spend** and no direct cold sales calls.
- **Valid Organic Channels**:
  - **Extension Store SEO**: Chrome Web Store, Shopify App Store, Figma Community, Notion Template Marketplace.
  - **Programmatic SEO (pSEO)**: High-intent long-tail search queries (e.g., `"convert [format A] to [format B]"`).
  - **Active Niche Communities**: Specific subreddits, Discord groups, or forums where sharing useful tools is welcomed.
- **Verdict**: If customer acquisition requires paid ads, enterprise sales teams, or cold outreach, **REJECT (Distribution Failure)**.

### Proof 3: High Frequency & Retention (Anti-Churn Test)
- **Criterion**: The product MUST solve a recurring daily or weekly workflow pain point—not a one-off event.
- **Frequency Scale**:
  - *Daily/Weekly Recurring*: Invoicing, social media curation, weekly report generation, daily code review summary -> **PASS**.
  - *One-off / Rare Event*: Resume formatting, wedding planner tool, domain name generator -> **REJECT (High Churn Risk)**.

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

---

## Final Anti-False-Positive Decision Matrix

| Proof Passed | Risk Assessment | Final Verdict |
|--------------|-----------------|---------------|
| 5 / 5 | Highly Viable Solopreneur Business | **APPROVED** |
| 4 / 5 | Minor Defect (Fixable with Pivot) | **PIVOT REQUIRED** |
| ≤ 3 / 5 | High Risk of Failure / False Positive | **DISCARDED** |
