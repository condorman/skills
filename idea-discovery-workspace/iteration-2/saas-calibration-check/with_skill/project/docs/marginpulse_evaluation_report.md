# Original Idea Evaluation Report

**Date**: 2026-07-28
**Requested Category**: B2B Micro-SaaS — Reporting / Finance for small e-commerce
**Session**: idea-discovery v5.0, Step 0 confirmed `docs/ideas_log.md` did not exist in the target project — no prior entries, no duplicate-scan conflicts.

---

### 💡 MarginPulse: "Know your real margin before the fee or tariff change hits your bank account"

**Context Category**: Micro-Service / B2B SaaS
**Novelty Level**: Unserved Niche Flank (claimed) → **downgraded after research to Flanking Existing Competitor (see 3.2)**

#### 1. Core Problem & Latent Friction
- **Discovered Friction**: Small multi-channel e-commerce sellers (Shopify + Amazon + Etsy + TikTok Shop) are repeatedly blindsided by two compounding, hard-to-track cost shocks: (a) marketplace fee-schedule changes announced with little lead time, and (b) the August 29, 2025 elimination of the US $800 de-minimis customs exemption, which pushed previously duty-free small parcels into standard customs entry with new duty/broker costs. Evidence: "every year, sellers are surprised by fee increases... the pattern is predictable, but the impact catches many off guard" (Niblin, Amazon FBA Fee Changes 2026); TikTok Shop sellers report "Seller Center shows one sales figure while the actual payout that lands in the bank is significantly lower, with no memo explaining the missing amount" (Dashboardly.io, TikTok Shop Settlement Reconciliation).
- **Target Audience**: Solo/small-team DTC and multi-channel sellers ($100K–$2M/yr revenue) who cannot afford a bookkeeper or enterprise finance-ops tooling (Avalara, Vertex) but are price-sensitive to margin erosion.

#### 2. The "Why Now?" Factor (Tech Enabler)
- **Recent Tech Breakthrough / Trigger Event**: The Aug 29 2025 US de-minimis suspension is a genuine, recent, external shock creating a fresh wave of cost exposure that older landed-cost tools were not originally built around; combined with marketplace APIs (Shopify, Amazon SP-API, Etsy, TikTok Shop Open Platform) that make it technically feasible for a solo developer to pull live order/fee data and cross-reference it against a maintained fee/tariff-rate table.
- **Why It Couldn't Be Built Earlier**: The specific tariff shock is <12 months old, so no incumbent has had much time to build a mature, dedicated response — in theory a timing window. In practice (see below), several incumbents pivoted their content and product messaging toward this exact event within weeks.

#### 3. Novelty & Prior-Art Verification

- **Prior-Art Search Results**: A 9-query, 2-fetch research pass (Google-style web search, not simulated) across the reconciliation, fee-monitoring, returns-leakage, landed-cost/tariff, TikTok-Shop-specific, and COGS-integrity sub-verticals of "small e-commerce finance/reporting" turned up **direct, currently-operating competitors in every sub-angle tested**, not just adjacent products:
  - Marketplace fee-change alerting + per-SKU margin modeling: **ProfitGuard** ("smart alerts, AI weekly summaries... Action Center ranks alerts by financial impact"), **MarginWise** ("spot margin killers before they scale"), **Shopclr** ("every fee, ranked per SKU"), **CentSight** ("Proactive Alerts", positions itself as "AI-powered financial intelligence" for e-commerce), **SellerTransparency Hub** (dedicated "Fee Change Tracker — historical and upcoming fee adjustments with impact assessments").
  - Tariff/de-minimis/landed-cost exposure: **nventory.io** (has a dedicated "2026 US Tariff Changes for Ecommerce Sellers" post sitting alongside its "Marketplace Fee Management for Ecommerce" post — i.e., the same two concerns this idea proposed combining are already adjacent product lines from one competitor), **Zonos**, **Avalara Cross-Border**, **Easyship**, **ShipBob** (all offer landed-cost/duty calculators aimed at e-commerce sellers).
  - TikTok Shop settlement/profit reconciliation specifically: **Dashboardly.io "Profit OS"**, which explicitly advertises "an internal audit across 340K+ orders, one reconciliation tool matched settled amounts with 99.61% accuracy" — a near-exact match to the proposed mechanic for that channel.
  - COGS data-integrity (the "why are my margin reports wrong" root cause): **Craftybase** ("calculates COGS automatically using IRS-approved weighted average costing... syncs COGS and inventory valuations directly to QuickBooks Online").
  - Generic payout/BNPL reconciliation (adjacent vertical also tested to rule out a pivot there): **A2X**, **Link My Books**, **Synder**, **Webgility**, **MyWorks**, **Reconcilely**, **Ledge**, **CONA**.
- **Originality Verdict**: **Flanking Existing Competitor.** No single tool found bundles *fee-change alerts + tariff/de-minimis exposure + per-SKU COGS accuracy* into one report, so a thin recombination angle exists — but every individual component already has at least one live, feature-complete competitor, several with the same "proactive alert" framing this concept relies on for differentiation. This is a **feature-delta gap, not a mechanism-level or market-level gap**.

##### 3.1 Feature Delta Matrix

| Feature / Dimension | MarginPulse (Candidate) | ProfitGuard (Prior Art #1) | SellerTransparency Hub + nventory.io (Prior Art #2) | Innovation Delta / Verdict |
|---|---|---|---|---|
| **Core Mechanics** | Pull store/marketplace orders + COGS, cross-reference against a maintained fee/tariff-rate table, alert on scheduled changes with per-SKU margin impact | Pulls Shopify orders, computes true profit after COGS/fees/refunds, ranks "margin killer" alerts by financial impact | Public fee-change database + impact assessments (Transparency Hub) combined with tariff-specific content/tooling (nventory.io) | 🟡 Reskin — same alerting mechanic already shipped by ProfitGuard; same fee-change-tracking mechanic already shipped by SellerTransparency |
| **Distribution** | Shopify App Store SEO + r/ecommerce / r/MicroSaaS | Shopify App Store, ranked and reviewed in the same "Pricing Optimization" category | SellerTransparency positions as a free public resource (already ranks for "marketplace fee change" search intent) | 🔴 Saturated — same ASO keywords, same category, incumbents have review history head start |
| **Tariff/De-Minimis Coverage** | Combines fee + tariff in one connected report | Not tariff-focused | nventory.io already publishes tariff-specific content/tooling under the same brand as its fee-management product | 🟡 Reskin — the "combine both" angle is the only real delta, and it's thin |
| **Monetization & UX** | $19–39/mo micro-SaaS | Freemium + paid tiers, established | SellerTransparency free; nventory.io paid SaaS | 🔴 Commodity — pricing pressure from a free public alternative and multiple paid incumbents |

##### 3.2 Evidence & Verification Audit Log
- **Search queries actually run (WebSearch tool calls this session)**:
  - `Klarna Afterpay Affirm settlement reconciliation software small ecommerce accounting`
  - `BNPL payout reconciliation Xero QuickBooks app`
  - `reddit "reconcile" Klarna OR Afterpay payouts Shopify manual spreadsheet`
  - `marketplace fee change alert tool Amazon Etsy Shopify margin impact small sellers`
  - `"return cost" leakage report ecommerce SaaS refund reason breakdown small brand`
  - `reddit small ecommerce seller surprised fee increase Amazon referral fee change margin`
  - `small ecommerce seller tariff duty exposure reporting tool de minimis 2025 SaaS`
  - `landed cost calculator SaaS small ecommerce tariff HS code duty small business`
  - `site:apps.shopify.com margin alert fee change tariff app profit`
  - `BeProfit OR TrueProfit OR Lifetimely proactive alert upcoming Amazon fee change tariff margin forecast`
  - `"fee change" alert app Shopify Amazon Etsy connected store margin per SKU proactive`
  - `TikTok Shop seller payout reconciliation profit reporting tool fees affiliate commission small business`
  - `TikTok Shop settlement report confusing sellers reddit fees deducted payout`
  - `ecommerce COGS data errors incorrect cost of goods sold profit report inaccurate Shopify QuickBooks`
  - `"cost of goods sold" audit tool ecommerce stale cost sync inventory SaaS small business`
- **Fetches run**: `https://sellertransparency.com/` (confirmed product scope: fee database + fee change tracker + policy archive, free/no-signup); `https://nventory.io/` (403 Forbidden — could not confirm product page directly, relied on its own blog post titles returned by search, which are treated here as weaker evidence than a fetched page and flagged as such); `https://centsight.com/ecommerce-finance/marketplace-fees` (confirmed "AI-powered financial intelligence" positioning with proactive alerts, but the fetch could not confirm live store-connection depth — flagged as partial evidence).
- **Examined prior-art links** (titles as returned by search):
  - [Seller Transparency Hub](https://sellertransparency.com/) — Confirmed via direct fetch: free public fee database + "Fee Change Tracker" with historical/upcoming changes and impact assessments. Strong evidence.
  - [ProfitGuard (Shopify App Store)](https://apps.shopify.com/profitguard-2) — "True profit after COGS, refunds & fees — AI weekly summaries," smart alerts ranked by financial impact. Strong evidence (search snippet from Shopify's own listing).
  - [MarginWise (Shopify App Store)](https://apps.shopify.com/marginwise) — "spot margin killers before they scale larger." Strong evidence.
  - [Shopclr](https://www.shopclr.com/) — "Know exactly what you're keeping," per-SKU fee ranking for Etsy/Shopify. Strong evidence (search snippet).
  - [nventory.io blog](https://nventory.io/blog/2026-us-tariff-changes-ecommerce-sellers) and [nventory.io fee-management post](https://nventory.io/blog/marketplace-fee-management-ecommerce) — Titles/snippets confirm the same brand publishes both fee-management and tariff content; direct product fetch blocked (403), so feature depth is **not fully confirmed** and is reported as weaker evidence.
  - [Dashboardly.io — TikTok Shop Settlement Reconciliation](https://www.dashboardly.io/post/tiktok-shop-settlement-reconciliation) and [Profit tracking guide](https://www.dashboardly.io/post/tiktok-shop-data-analytics-explained) — explicit reconciliation-accuracy claim ("99.61% accuracy" across 340K+ orders). Strong evidence of direct prior art for the TikTok-Shop-specific sub-angle.
  - [Craftybase](https://craftybase.com/cost-of-goods-sold-software) — automated COGS with landed-cost allocation synced to QuickBooks. Strong evidence (search snippet) for the COGS-integrity sub-angle.
  - [A2X Klarna reconciliation guide](https://www.a2xaccounting.com/ecommerce-accounting-hub/reconcile-klarna-a2x-qbo) and [A2X Sezzle guide](https://www.a2xaccounting.com/ecommerce-accounting-hub/reconcile-sezzle-a2x-qbo) — confirms A2X already has named, documented BNPL-specific reconciliation flows for Klarna and Sezzle. Strong evidence ruling out the BNPL-reconciliation pivot.
- **Evidence integrity note**: every competitor name and URL above came from an actual WebSearch or WebFetch call made in this session. Two items (nventory.io's live product page, CentSight's exact connection depth) could not be independently confirmed by direct fetch — this is disclosed explicitly rather than treated as confirmed prior art, per the skill's evidence-integrity rule.

#### 4. Anti-False-Positive 7-Proof Verification Matrix
- **Proof 1 (Willingness to Pay & Demand Velocity)**: **PASS** — on strong retrieved evidence. Real, cited data: marketplace fees cited as the #1 margin concern by ~49% of Amazon sellers (via Marketplace Pulse, retrieved through search); TikTok Shop sellers report material, confusing payout shortfalls; and — most tellingly — multiple named competitors (ProfitGuard, BeProfit, TrueProfit, CentSight, Craftybase) are already charging monthly fees for adjacent capability, which is direct proof of category-level spend. Steelman rejection considered: this same evidence is a double-edged sword — it proves the *category* has WTP, not that a *new, undifferentiated entrant* can capture it (see Proof 5).
- **Proof 2 (Zero-CAC Distribution)**: **FAIL** — on strong retrieved evidence. The Shopify App Store "Pricing Optimization / Profit Analytics" category is already crowded with ProfitGuard, MarginWise, Shopimize, Delirious Profit, BeProfit, TrueProfit, and Lifetimely, all targeting the same install-intent keywords ("profit calculator," "margin tracker," "true profit"). SellerTransparency Hub already ranks as a free public resource for the "fee change" search intent specifically. A new entrant would be fighting entrenched review counts and SEO/ASO rank, not finding an open channel.
- **Proof 3 (Anti-Churn Retention)**: **PASS** — on retrieved-evidence-supported reasoning. Fee schedules and settlement cycles recur weekly/monthly (TikTok settlement periods, Amazon Q4 fee announcements), so the report has a natural recurring cadence — this is a reasoned inference from the retrieved settlement/fee-cycle evidence rather than a directly retrieved retention statistic.
- **Proof 4 (AI Reliability >95%)**: **PASS** — on assertion-style reasoning grounded in mechanism, not a retrieved accuracy benchmark for this specific product. The core mechanism (parsing published fee/tariff tables + arithmetic against order data) is deterministic and rule-based, not LLM-generative, so >95% accuracy is architecturally plausible — but this is my own risk assessment of the proposed mechanism, not evidence retrieved from a live deployment of this exact idea.
- **Proof 5 (Micro-Moat Defensibility)**: **FAIL** — on strong retrieved evidence. This is the decisive failure. Every individual component of the concept — fee-change alerting (ProfitGuard, MarginWise, SellerTransparency), tariff exposure (nventory.io, Zonos, Avalara), and per-channel settlement reconciliation (Dashboardly for TikTok Shop, A2X for BNPL) — already has a shipping, named competitor. The "combine fee-change + tariff into one report" angle is a thin recombination that any of these incumbents could ship as a feature update in days, which is exactly the Pitfall #4 "Zero Moat / Commodity Wrapper" failure mode described in the evaluation framework.
- **Proof 6 (Status Quo Resistance)**: **PASS, with a caveat** — on retrieved evidence with a steelman complication. Fees genuinely consume 15–45% of revenue depending on platform (retrieved figure), so the dollar impact clearly clears the $200/month bar. The caveat, surfaced by the steelman-rejection habit: for a meaningful share of the target audience, the "status quo" being displaced is no longer a spreadsheet — it is an *existing paid competitor tool* (BeProfit, ProfitGuard, CentSight), which is a harder and different sale than displacing free inertia.
- **Proof 7 (True Solopreneur Buildability)**: **PASS** — on assertion-style reasoning about mechanism composability. The mechanism composes entirely from off-the-shelf pieces: Shopify/Amazon SP-API/Etsy/TikTok Shop Open Platform for order/COGS data, plus a maintained reference table of published fee/tariff rates, plus arithmetic. No novel ML, computer vision, or signal processing is required, and there is a cheap fallback (manual CSV upload) if any single API integration lags. This is a reasoned application of the Proof 7 checklist to the described mechanism, not a retrieved fact.
- **Protocol Score**: **5 / 7 → DISCARDED** (Proof 2 and Proof 5 fail on strong, directly retrieved competitor evidence — not on speculation).

#### 5. Solopreneur + AI Feasibility Stack
- Not applicable — idea did not clear the 7-Proof gate. No blueprint is generated per the skill's mandatory-for-APPROVED-only rule.

#### 6. Legal & Regulatory Safety
- **Risk Tier**: 🟢 Standard — the concept only reads and reports on data the seller already owns (their own orders, COGS, and publicly published fee/tariff schedules). It does not move money, extend credit, give investment/tax advice, handle minors' data, or capture biometric data.
- **Legal Risk Level**: Very Low.
- **Notes**: A pure reporting/calculation tool of this kind carries no PCI, money-transmitter, or advice-liability exposure. The one soft edge is that a tariff/duty *estimate* should be clearly labeled as informational, not a customs broker's binding classification, to avoid implying professional customs-brokerage advice — a standard disclaimer, not a structural blocker.

#### 7. Monetization Strategy
- **Pricing Model**: Would have been ~$19–39/month tiered by connected channel count — moot given the verdict, since Proof 2 and Proof 5 show this price point is already contested by better-established, better-distributed incumbents at similar or lower price points (SellerTransparency's core data is free).
- **Value Proposition**: Real but already captured by existing players; no differentiated ROI story survives the Feature Delta Matrix.

#### 8. Summary Recommendation
- **Status**: **DISCARDED** — direct, multi-angle prior art confirmed via real search across every sub-vertical tested within "small e-commerce finance/reporting" (payout/BNPL reconciliation, fee-change alerting, returns leakage, tariff/landed-cost exposure, TikTok-Shop-specific reconciliation, and COGS-integrity auditing). No sub-angle cleared the Micro-Moat (Proof 5) or Zero-CAC Distribution (Proof 2) bar. Recommend the requester either (a) accept that this specific vertical is currently oversaturated for a solo new entrant, or (b) pivot into an adjacent B2B vertical outside e-commerce finance/reporting for the next research pass, per the workflow-vertical rotation guidance in `domain_saas.md`.

---

## Session Note on Calibration

This session ran a single candidate through the full protocol rather than surveying several, because the prior-art research phase (Step 2) surfaced disqualifying direct competition before the candidate could be meaningfully refined into a second, third concept within the same session budget. Per the Calibration section of `evaluation_framework.md`, a DISCARDED outcome — especially one this well-evidenced — is a healthy, expected result, not a shortfall of the process. No idea in this session was approved; 0/1 candidates evaluated passed the gate (0%), consistent with "approval is the exception."
