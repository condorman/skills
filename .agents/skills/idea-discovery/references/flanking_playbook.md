# Flanking Discovery Playbook (v1.0)

This playbook governs **Flanking Discovery Mode** — the alternative to Original Discovery Mode where, instead of searching for an unserved niche, you search for an *already-validated* product that's vulnerable, and build something that displaces it. Consult this file whenever the user selects Flanking Mode in Step 0 of `SKILL.md`.

---

## Why this mode is different, and why it's not automatically easier

Original Discovery Mode's hardest problem is *demand risk* — you don't know if anyone wants the thing until you build it and the 7 Proofs are mostly there to catch that risk early. Flanking Mode trades demand risk for a different one: the demand is already proven (that's the whole appeal), but you're not entering an empty space — you're trying to take share, ranking, or mindshare away from something that already has it. That's a harder distribution problem, not an easier one: an abandoned app can still sit at #3 in App Store search purely on the strength of a thousand old reviews, and outranking dead weight is not the same as filling a gap nobody occupies. Treat every candidate in this mode with the same anti-false-positive rigor as `evaluation_framework.md` demands elsewhere — "it looks neglected" is an impression, not evidence.

---

## The three patterns

Every Flanking candidate must be classified into exactly one of these, with the evidence bar stated. If a candidate doesn't clearly meet the evidence bar for any of the three, it isn't a Flanking candidate — send it through Original Discovery Mode instead, or discard it.

### Pattern 1 — Abandoned-but-Proven
Had real traction (downloads, revenue, an active user base) at some point, and is now genuinely no longer maintained.

**Required evidence (all of it, not just one signal):**
- **Proof of past traction**: download-count tier or ranking history (App Store/Google Play), a funding/acquisition announcement, or a large, long-running review count.
- **Proof of abandonment**: last update date (visible on every store listing) is 12+ months old *and* recent reviews (last 3-6 months) complain about crashes, broken integrations, or unanswered support requests *and* the developer's other public presence (site, X/Twitter, GitHub) has also gone quiet. One signal alone (e.g. "just an old update date") is not enough — plenty of simple, finished utility apps are stable and intentionally not touched. You need the complaint pattern too.
- **Proof residual demand still exists**: recent reviews or forum posts (last 3-6 months) still reference people actively using it or looking for it, not just historical popularity.

### Pattern 2 — Stagnant-but-Validated
Still alive and maintained (updates do happen), has demonstrated real if modest interest, but has stopped meaningfully innovating — cosmetic updates and bug fixes only, no feature movement, for a long stretch.

**Required evidence:**
- **Proof of validated interest**: a install/visit trend, review volume, or community size that shows real (if not massive) ongoing usage — not just a one-time spike.
- **Proof of innovation stall**: compare changelog entries or release notes across the last 12-18 months — do they add anything beyond bug fixes and minor UI tweaks? Cross-reference with feature-request boards (Canny, GitHub issues, subreddit posts) that have sat unaddressed for a year or more despite visible demand (upvotes, repeated asks).
- **Proof the market moved and they didn't**: name the specific capability enabled by newer tech (an AI feature, a platform API, an integration) that competitors or the ecosystem now expect and this product still lacks.

### Pattern 3 — Good-Foundation-Needs-Innovation
Currently fine — actively maintained, reasonably healthy — but has a specific, nameable gap that a better version could close decisively enough to take meaningful share, not just be "nicer."

**Required evidence:**
- **Proof the foundation really is good**: real traction signals (same as Pattern 1/2), so you're not just picking a random competitor and calling it a flanking play.
- **Proof of a concrete, sourced gap**: pulled from real reviews/support threads/feature-request boards, not invented — the exact feature, UX friction, pricing structure, or integration that recurs across multiple independent sources as the reason people are unhappy or looking elsewhere.
- **Honest self-check**: this pattern is the easiest one to fool yourself with ("I could just make it better") because *every* product has a plausible-sounding improvement story. The bar here is that the gap must be independently corroborated by 3+ separate complaints/requests, not a single review or your own opinion of the product.

---

## Search methodology for candidate mining (replaces Step 1's friction mining in Flanking Mode)

Real, checkable signals — every candidate needs citations the same way Original Discovery Mode does. Start with the miner, which groups its queries by the evidence bar each pattern below demands:

```bash
python scripts/deep_search_miner.py "<target product or category>" <domain> --flanking [--locale=it]
```

**A warning about query wording, learned the expensive way**: queries built on state adjectives — "abandoned", "discontinued", "no longer maintained", "alternative to" — have strong keyword gravity toward whichever category the search engine has most indexed under those words (currently the third-party-client graveyard: Reddit apps, Twitter apps). Two sweeps in a row can return the same cluster and look like a market survey. Anchor the query to the *product or the niche* first and the state second, and if two consecutive queries return the same category, change the anchor rather than rephrasing the adjective.

**Check the platform visibility window before valuing any Play Store target.** Google Play removes discoverability from apps that fall behind the target API level requirement: an out-of-date app stops appearing to new users on newer Android versions, on a published, rolling schedule ([Play Console Help](https://support.google.com/googleplay/android-developer/answer/11926878)). This cuts both ways and both directions belong in the report. It *helps*: the incumbent's review-count ranking inertia — the main obstacle this mode faces — expires on a date you can look up, without you doing anything. It *hurts*: the same expiry is visible to every other builder, and an app about to become invisible is not an incumbent holding a position you can take, it's a vacancy that will open for everyone at once. So record the **target API level and its cutoff date** next to the last-update date, and treat "the target is about to disappear on its own" as a reason the displacement needs a moat of its own, not as the moat.

Useful starting points, run in the target domain (mobile/games/saas/web):

- **Store listing pages directly**: App Store and Google Play both show "Last Updated" plainly on the listing page — this is the single fastest abandonment signal and needs no dork, just opening the page.
- **`site:reddit.com "is [product] still maintained" OR "[product] alternative because" OR "[product] died" OR "[product] shut down"`** — people actively looking for a replacement are your residual-demand evidence.
- **`site:alternativeto.net "[product]"`** — a real site built specifically around "why I switched away from X," often with the switching reason stated.
- **G2 / Capterra reviews filtered to recent, low-star** — B2B tools especially tend to get explicit "hasn't been updated," "support went silent," or "acquired and gutted" complaints in reviews once a vendor stops investing.
- **`site:github.com "archived" "[product/library]"`** for open-source or developer-tool candidates — GitHub shows an explicit "Archived" banner and last-commit date; combine with star count as a rough popularity proxy.
- **Canny / Featurebase / public roadmap boards for the specific product** — feature requests sitting at 50+ votes for 12+ months, unaddressed, are the sharpest evidence for Pattern 2 and 3.
- **Product Hunt comments on the product's original launch, revisited** — often has "whatever happened to this?" threads years later.

---

## The Flanking Eligibility Gate (run before scoring the 7 Proofs)

An idea that hasn't cleared this gate isn't a Flanking candidate at all — it's just a regular competitor analysis with extra steps, and Original Discovery Mode's Step 2 (Prior-Art & Novelty Audit) is the right tool for that instead. Two checks, both mandatory:

1. **Genuine Pattern Match**: state which of the three patterns applies and cite the specific evidence required for that pattern above — with real links. "This app hasn't been updated in a while" is not Genuine Pattern Match; the full evidence bar (traction + abandonment/stagnation + residual demand/gap, as specified per pattern) is.
2. **Displacement Feasibility**: name concretely how a solo builder gets discovered *instead of* the incumbent — not just "build something better." If the incumbent still ranks well in store search or SEO purely on review-count inertia, say so and address it directly (a common answer: target the specific complaint cohort directly — the people already searching "[incumbent] alternative" or leaving 1-star reviews are a more reachable audience than generic keyword ranking). If you can't name a credible path to being found ahead of or alongside the incumbent, this fails the gate regardless of how good the rebuild would be.

**Three disqualifiers that fail the gate outright**, each learned from a candidate that looked textbook until checked:

- **Death by platform policy is structural, not abandonment.** A third-party client of a closed platform that died when the API was priced or closed (Reddit clients, Twitter clients) hands its cause of death to anyone who rebuilds it. Not a Flanking candidate at any pattern.
- **A credible free successor already shipped.** If a fork or alternative — especially an open-source one by an original contributor — already absorbed the dissatisfied cohort, Displacement Feasibility fails no matter how strong the abandonment story is. The cohort is the prize; if it's taken, there's nothing to displace into.
- **Old but finished is not abandoned.** A stable utility with no updates and no complaint pattern is working as intended. Without the complaint evidence, Pattern 1 isn't met.

If either check fails, don't proceed to the 7-Proof Protocol — report back with what's missing (the same way Step 4's legal check can push a candidate straight to PIVOT/DISCARDED before the report is written).

---

## Reading the 7 Proofs in Flanking Mode

The scoring thresholds in `evaluation_framework.md` (7/7 Approved, 6/7 Pivot, ≤5/7 Discarded) are unchanged. What changes is what evidence answers each proof, since some of it is now historical rather than hypothetical:

- **Proof 1 (WTP & Demand Velocity)**: largely pre-answered by the Genuine Pattern Match evidence — the incumbent's own traction/revenue history *is* the willingness-to-pay proof. Don't re-litigate whether people want this; do check whether that demand has decayed (a Pattern 1 candidate with heavy churn away from the whole category, not just the incumbent, doesn't clear this even with a great abandonment story).
- **Proof 2 (Zero-CAC Distribution)**: this is where Displacement Feasibility from the gate above gets scored formally — can you reach the *specific* people already dissatisfied with or searching for an alternative to the incumbent (reviews, forum posts, "alternative to X" searches), not a generic organic channel.
- **Proof 3 (Retention)**: usually inherited from the incumbent's own usage pattern if the job-to-be-done hasn't changed — verify it wasn't already trending toward one-off use before decline.
- **Proof 4 (AI Reliability)**: unchanged — applies to your rebuild's technical approach, not the incumbent's.
- **Proof 5 (Micro-Moat)**: reframe as **the specific, sourced gap** from the pattern evidence (the unaddressed feature requests, the stack the incumbent can't easily adopt, the pricing structure people complain about) — a moat here is "why the incumbent specifically can't or won't close this gap themselves," not just "we'll execute better."
- **Proof 6 (Status Quo Resistance)**: reframe as *why switching away from the incumbent* clears the inertia bar, not switching away from a spreadsheet — people already paying for or using something have a higher switching cost than people using no tool at all; the gap has to be worth that switch, not just an improvement.
- **Proof 7 (Solopreneur Buildability)**: unchanged, applies to the rebuild.

---

## IP, trademark & passing-off guardrail

Flanking means building a better alternative *inspired by* proven demand — it does not mean copying the incumbent's name, logo, branding, marketing copy, or source code. Reusing a confusingly similar name or visual identity risks trademark/passing-off exposure regardless of how different the underlying product is, and copying source code or paid content is a separate, harder line. This is a distinct risk axis from the health/money/minors/biometric tiers in `legal_risk_playbook.md` — see that file's Flanking-Mode Addendum for the concrete check to run before finalizing Section 6 of the report.

---

## Report & log format notes

- The Step 5 report's header must state **Discovery Mode: Flanking** and the pattern used (1/2/3).
- The target product is row **K1** of `docs/<idea-slug>/competitors.md` (Step 6) and gets the fullest treatment in it: its user critiques *are* the displacement thesis, and its praise is the table-stakes list the rebuild has to match. A flanking session that leaves that file thin has recorded the opportunity without recording the evidence for it.
- Section 3 of the report (normally "Novelty & Prior-Art Verification") becomes **"Target Product Status & Displacement Gap"** for Flanking Mode — the Feature Delta Matrix format is unchanged, but "Closest Prior Art #1" is now, explicitly, the product being flanked (named and linked per the global naming rule in `SKILL.md` Step 2), not a coincidental competitor.
- `ideas_log.md` entries for Flanking ideas must record the specific target product (name + link) in the Summary line. This is what lets Step 0's duplicate scan catch "already tried to flank this same product" in a later session — a repeat attempt at the same target without new evidence is a duplicate exactly the way a repeated mechanic is in Original Discovery Mode.
