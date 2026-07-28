# Master Product Ideas Log

This log tracks all product ideas discovered, evaluated, and scored using the `idea-discovery` 6-Proof Verification Protocol for this project.

---

## Log Summary

- **Total Ideas Evaluated**: 1
- **Approved**: 1
- **Pivot Required**: 0
- **Discarded**: 0

---

## Evaluated Ideas

### 1. 💡 MarketLedger MTD: Automated Making Tax Digital Quarterly Filing Engine for Multi-Marketplace UK Sellers
- **Date Evaluated**: 2026-07-28
- **Category**: B2B Micro-SaaS / Reporting & Finance for Small E-Commerce (Compliance Reporting)
- **Novelty**: Novel Combination / Unserved Niche Flank. The general "Shopify profit-tracking dashboard" category (TrueProfit, BeProfit, Lifetimely, Finaloop, Synder, A2X, PayTraQer, Daasity, Polar Analytics, Mipler, GETIDA, ReconPe, AppTrim, Dutify, DutyCalc, Kixmon) proved saturated across margin tracking, landed-cost/tariff, multi-store rollup, app-spend audit, and COD/RTO reconciliation angles — all had direct prior art. The search was redirected toward the UK Making Tax Digital for Income Tax (MTD ITSA) compliance flank, where a real gap was found: no examined competitor (GoSimpleTax, Coconut, Bokio, Countingup, 123 Sheets, MyTaxDigital, VitalTax, CHM, AbraTax, Anna Money) combines automated marketplace-native settlement/payout ingestion (Etsy/eBay/Amazon/Shopify) with automatic mapping to HMRC's MTD ITSA quarterly categories and submission.
- **6-Proof Score**: 6/6 (see caveat below — 3 proofs rest partly on reasoned inference/absence-based evidence, not fully verified data)
- **Status**: **APPROVED**
- **Detailed Report**: [marketledger_evaluation_report.md](file:///Users/alessandromizzoni/Documents/Progetti/skills/idea-discovery-workspace/iteration-2/saas-calibration-check/old_skill/outputs/marketledger_evaluation_report.md)
- **Blueprint Architecture**: [marketledger_blueprint.md](file:///Users/alessandromizzoni/Documents/Progetti/skills/idea-discovery-workspace/iteration-2/saas-calibration-check/old_skill/outputs/marketledger_blueprint.md)
- **Summary**: UK-focused B2B micro-SaaS for sole traders/micro-partnerships selling across 2+ marketplaces (Etsy, eBay, Amazon, Shopify, Vinted/Depop/TikTok Shop) above the MTD ITSA turnover threshold (£50k from April 2026, £30k from 2027, £20k from 2028). Auto-ingests marketplace settlement/payout reports, auto-maps gross sales, fees, refunds, and COGS to HMRC's fixed quarterly income/expense categories, and submits confirm-and-go quarterly updates via an embeddable HMRC-recognised MTD API partner (e.g. untied-class infra) rather than pursuing independent HMRC software-vendor accreditation in v1. Deterministic rules-based categorization core; LLM used only to pre-suggest mappings for ambiguous line items, never to auto-submit without explicit user confirmation.
- **Rejection Reason**: N/A (Approved). **Caveats logged for future sessions**: (1) Proof 2 (Zero-CAC Distribution) — channel-fit for the marketplace-seller long-tail keyword cluster is inferred from GoSimpleTax's own landing-page positioning, not independently verified search-volume data. (2) Proof 4 (AI Reliability) — passes on architectural/determinism reasoning; no real classification-accuracy benchmark was run against actual settlement-report data. (3) Proof 5 (Micro-Moat) — based on an absence-based finding across ~10 of HMRC's 40+ recognised-software vendors sampled, not an exhaustive audit. (4) Legal Risk was rated **MODERATE**, not the default "zero risk" — the product depends on either HMRC software recognition or an embeddable third-party MTD API partner (e.g. untied), plus Etsy/eBay/Amazon developer-program approval, both of which are external dependencies outside solo-founder control. Recommend a keyword-volume check, a small pilot categorization-accuracy test, and confirming the API partner's commercial terms before committing to the full build.
