# Vertical Deep-Dive Playbook (v1.1)

This playbook governs **Vertical Deep-Dive Mode** — the third mode of `SKILL.md`, used when the goal is no longer *finding* an idea but **stress-testing one specific idea that already exists** (usually one that came out of a previous Original or Flanking session and is recorded in `docs/ideas_log.md`).

Consult this file whenever Step 0's intent router selects Deep-Dive Mode.

---

## What makes this mode different

Original and Flanking modes answer *"is there something here worth building?"* on thin, fast evidence — deliberately thin, because most candidates die and deep research on all of them would be wasted. Deep-Dive Mode answers a different and much more expensive question: **"if I commit the next 3-6 months to this specific idea, what kills me?"**

Three consequences follow, and they're the whole reason this mode needs its own playbook:

1. **The unit of judgment is the component, not the idea.** In discovery, an idea passes or fails as a whole. Here it almost never does — the realistic outcome is "the core holds, feature 3 is a legal liability, feature 5 is what killed two dead competitors, and feature 7 should be cut because it doubles the build for a complaint nobody actually voiced." A single global verdict at the end of a deep-dive is usually a sign the analysis stayed shallow.
2. **Confirmation bias is the primary threat, not false positives.** By the time an idea reaches this mode the user likes it, has probably already told someone about it, and is looking for a green light. Discovery mode's job was to be a filter; this mode's job is to be an *adversary*, and it fails if it turns into an elaborate way of restating the original report with more links.
3. **The deep-dive is allowed — and expected — to overturn a previous APPROVED.** An idea that passed 7/7 on discovery-grade evidence can absolutely die here. If deep-dives never change a verdict, they're a ritual. See the Calibration note at the bottom.

---

## Depth Contract (what "deep" concretely means here)

"Use deep research" is not measurable, and an analysis that *feels* thorough is exactly the failure this mode exists to prevent. So depth is defined as a floor of concrete artifacts, all of which must come from real tool calls (the evidence-integrity rule in `SKILL.md` Step 2 applies here in full, unchanged):

| Artifact | Minimum bar | Where it lands |
|---|---|---|
| Competitor census | 8+ named & linked products across tiers 1-4 below (or an explicit, argued statement of why fewer exist — an empty category is itself a major finding) | D1 |
| Instrumented baseline | For sensor/accuracy-claim ideas: what the literature achieves and on what hardware | D1 (tier 5) |
| Search vocabularies | 3+ genuinely different vocabularies + 1 non-English pass | D1 |
| Voice-of-customer sources | 15+ distinct real user statements (reviews, forum posts, issue threads) across 5+ competitors, each tagged product-specific or category-inherent, plus any independent third-party test | D2 |
| Failed/dead predecessors | 2+ investigated with a cause of death, or a stated finding that none were found and what that implies | D4 |
| Revenue model | Bottom-up, with per-user COGS, usage window/seasonality, and a break-even figure — never a top-down TAM slice | D5 |
| Legal surfaces | One row per idea component, EU/Italy first | D6 |
| Disconfirming evidence | A written "strongest case against building this" produced **before** the verdict | D7 |

**When a minimum bar can't be reached**: sometimes the evidence simply isn't reachable with the tools available — review bodies behind logins, a category with no public forum, a market that doesn't post. That is a normal outcome and it has a defined handling, because the alternative (quietly padding to the number, or stopping dead) is worse than either. Do all three:

1. **State the shortfall in the report header**, in the same line as the research depth (`VoC: 8 of 15 minimum — G2/Capterra reviews not retrievable without an account`).
2. **Try one substitution before conceding it.** Most bars have a second-best surface: reviews → community threads and vendor changelogs; dead predecessors → trademark abandonments, archived repos, Wayback-visible pricing pages; independent tests → the instrumented literature in tier 5.
3. **Cap the verdict's confidence rather than the verdict itself.** A deep-dive that missed a bar can still return KILL — negative evidence found early is not weakened by the evidence you couldn't reach. What it cannot return is a clean **GO**: if the bar that fell short is the one that would have tested the surviving assumption, the honest ceiling is **GO WITH CUTS, pending <the missing evidence>**, naming what would have to be checked before committing. An unreachable bar constrains optimism, not pessimism.

**On tooling and model depth**: if the environment offers a long-running research/deep-research capability, extended thinking, or parallel subagents, use them here — this is the mode that justifies the cost, and per-competitor research parallelizes cleanly (one investigation thread per competitor in D1/D2). If those capabilities are not available, say so plainly in the report header (`Research depth: standard web search only`) instead of implying a depth that wasn't reached. A skill cannot switch the underlying model itself; what it can do is refuse to call a shallow pass "deep."

---

## D0 — Idea Intake & Component Decomposition

Never start searching against the idea's *name*. Start by writing it out as a numbered **Component Ledger**, because every later step returns a verdict per row, and rows that were never written down can never be cut.

Sources for intake, in order of preference: the existing `ideas_log.md` entry and everything in `docs/<idea-slug>/` — `evaluation.md`, `competitors.md`, `legal.md`, `blueprint.md` (if the idea came from a previous session), then whatever the user pasted or described. If the idea exists in the log, **read the original report first** — the point of the deep-dive is to go past it, which requires knowing what it already claimed.

```markdown
### Component Ledger (initial)
| # | Component | Type | Why it's in the idea (user's stated rationale) |
|---|---|---|---|
| C1 | [e.g. OCR intake of supplier invoices] | Core mechanic | [rationale] |
| C2 | [e.g. multi-currency reconciliation] | Supporting feature | |
| C3 | [e.g. shared team workspace] | Nice-to-have | |
| C4 | [e.g. AI-generated dispute letters] | Differentiator | |
```

Also record explicitly, in one line each: **the core job-to-be-done**, **the target user**, and **the assumed monetization**. These three are what the rest of the deep-dive tests; leaving them implicit is how a deep-dive ends up validating a slightly different idea than the one the user has in mind.

Finally, write the **Kill Criteria** *before* researching: 3-5 findings that, if true, would end this idea (e.g. "if 2+ well-funded competitors already ship C1 and C4 together at <€15/mo", "if the dominant complaint about existing tools is price rather than capability", "if the data source C1 depends on is behind a ToS that forbids automated access"). Committing to these upfront is the single most effective guard against post-hoc rationalization — it is much harder to explain away a criterion you wrote down before you knew the answer.

---

## D1 — Exhaustive Competitor Census

Discovery mode deliberately stops at the 2 closest prior-art products. That's the right call there and the wrong one here: the products that kill a launch are frequently the ones a first pass missed, because the first pass searched in the founder's vocabulary and the market uses a different one.

### The five tiers (tiers 1-4 always get searched — a census with only tier 1 is not a census; tier 5 is conditional)

1. **Direct** — solves the same job for the same user.
2. **Adjacent / partial** — solves part of the job, or the same job for a different user; the ones most likely to expand into your space. Explicitly include **big-platform features** here: an idea that is one roadmap item away from being absorbed by an incumbent's existing product has a different risk profile than one that isn't.
3. **DIY / status quo** — the spreadsheet, the Notion template, the n8n/Zapier/Make recipe, the open-source repo, the ChatGPT prompt people pass around. This tier is what Proof 6 is really competing against, and it is usually free.
4. **Dead** — shut down, archived, delisted, acquired-and-gutted. These feed D4 and are the highest-signal tier in the whole census.
5. **Instrumented / scientific baseline** *(mandatory when the idea infers a physical property from a sensor — microphone, camera, accelerometer, IMU, BLE ranging — or claims an accuracy threshold; skip it and say why for ordinary CRUD ideas)* — not a competitor at all, but the answer to a question no competitor will answer honestly: **what accuracy does the published literature actually achieve, and with what hardware?** Search the peer-reviewed and thesis literature for the same measurement (`[property] detection accuracy [method] site:pmc.ncbi.nlm.nih.gov OR site:arxiv.org OR site:doaj.org`), then compare instrument to instrument. A 95% figure obtained with a laser vibrometer, a NIR spectrometer, or a lab microphone array tells you nothing reassuring about a phone microphone in a supermarket — and Proof 4's ">95% reliability" is otherwise easy to wave through on the strength of a number that belongs to different hardware. If the literature's accuracy depends on instrumentation the user's product won't have, that is a structural finding on the level of a D4 death, and it belongs in the verdict rather than in a footnote.

### Vocabulary sweep (this is what catches the missed competitors)

Run the census in at least **three distinct vocabularies plus one non-English pass**, because each surfaces a different set:

- **User-pain vocabulary**: how a sufferer describes it before knowing a product exists ("I waste hours every week matching X to Y").
- **Category/industry vocabulary**: what a vendor or analyst calls it ("reconciliation automation", "field service quoting").
- **Mechanic vocabulary**: the mechanics-first abstraction from `deep_search_playbook.md` §1, stripped of theme.
- **Non-English pass**: at minimum the language of the target market plus one large software market (IT/DE/ES/FR for EU-targeted tools; JP/CN/KR for consumer and games). Whole product categories are routinely mature in one language and invisible in another.

High-yield surfaces for the second sweep, in rough order of yield:

- **"Alternatives to" aggregators**: `alternativeto.net`, `g2.com/compare`, `capterra`, `producthunt.com/alternatives`, `saashub` — these exist precisely to enumerate competitor sets.
- **Competitors' own comparison pages**: `"[known competitor] vs"` and `site:[competitor.com] /compare OR /vs` — vendors name rivals you haven't heard of, and reveal which ones they consider threatening.
- **Store "similar apps" rails and category top-100s** for mobile; Steam "More like this" and tag pages for games; Chrome Web Store related extensions for web tools.
- **Community "what do you use for X" threads**: `site:reddit.com "what do you use for" [job]`, plus the equivalent in a niche Discord/Slack/forum if one exists. These list the DIY tier better than any directory.
- **YouTube / newsletter reviews**: `[category] tools 2025 review` — roundups enumerate 8-12 products at once and often include the ones that never SEO'd well.
- **GitHub topics & awesome-lists**: `site:github.com/topics [mechanic]`, `"awesome [category]"` — the open-source tier is a real competitor for developer-adjacent ideas and is often free.
- **Funding/launch trails**: `site:producthunt.com/posts [mechanic]` sorted across years, plus `site:techcrunch.com OR site:eu-startups.com "[category]" funding` — a funded entrant changes the competitive math even if the product is early.

**The census lands in `docs/<idea-slug>/competitors.md`, not only in this report** — see [competitor_ledger_template.md](competitor_ledger_template.md). If that file already exists from an earlier discovery session, *append and update it*; the rows already there tell you what the first pass found, and what it missed is the point of this step. The deep-dive report cites the ledger rather than duplicating the whole table; if the two ever disagree, the ledger is the one that gets corrected.

Record every find, even the dismissed ones, in the census table. A competitor that was found and correctly ruled out ("adjacent, targets enterprise only, €900/mo floor") is valuable evidence; a competitor that was never found looks identical to one that doesn't exist, and that's the exact failure this step is designed to prevent.

```markdown
### Competitor Census
| # | Product | Tier | Positioning | Pricing | Traction signal | Last activity | Overlap with our components |
|---|---|---|---|---|---|---|---|
| K1 | [Name](url) | Direct | | €X/mo | 4.2★ / 1.2k reviews | 2026-05 | C1, C2 |
```

If the census turns up a **direct competitor that already ships the exact component stack** the user planned, that is a Kill Criteria hit — say so at the point of discovery, not buried in the final verdict.

### Early-exit check (run at the end of D1, before starting D2)

Walk the D0 Kill Criteria against what the census alone produced. If **the census by itself hits a Kill Criterion decisively** — the component stack already ships at or below the planned price, the category has a free credible tier, several funded entrants shipped the differentiator this year — then D2 through D6 will not change the verdict, and running them anyway costs hours to produce a more thoroughly documented version of a conclusion already reached. In that case:

- Jump to **D7** and write the verdict, stating explicitly that it rests on D1 alone and which criterion closed it.
- Run only the steps that could still *change* the outcome, not the ones that would merely decorate it. Usually that's D4 (is the category's death structural, which determines whether a pivot inside it is viable?) and, if a pivot is on the table, D5.
- Say what was skipped and why in the report header, the same way an unreached depth bar is declared.

This is not licence to stop early when the census is merely discouraging — "lots of competitors" is the normal state of every viable market and is not a Kill Criterion. The exit applies when a criterion the user themselves wrote down before researching has been unambiguously met. Everything short of that runs the full sequence: the whole point of D2-D6 is to catch what a competitor list can't show you.

---

## D2 — Voice-of-Customer: Pain & Praise Ledger

The purpose is not "read some reviews". It is to convert scattered opinion into a ranked, sourced ledger of (a) what existing products get wrong that you could exploit, and (b) what they get right that you must match to be taken seriously at all. Both halves matter — a deep-dive that only collects complaints produces an idea that's differentiated and unusable.

**Where the real signal lives**: 1★-3★ reviews (5★ reviews are content-free; 1★ alone over-weights billing rage), review *replies* from the vendor (tells you what they refuse to fix), public feature-request boards with vote counts and dates, GitHub issues labeled `wontfix`/`stale`, churn threads (`"switched from [X] to"`, `"why I left [X]"`, `"[X] alternative because"`), support forums, and app-store review sections filtered to the most recent 6 months.

**Independent third-party tests are a separate and higher-grade source — search for them explicitly.** Journalist hands-on tests, consumer-association comparisons, university or research-institute explainers, and technical teardowns are qualitatively different from user reviews: they usually test a controlled sample, compare products side by side, and state *why* something fails rather than that it annoyed someone. One such source can settle a question that fifty reviews leave ambiguous. Search `"[category]" test OR "we tried" OR review site:[press/consumer/institute domains]` and the same in the non-English pass — this kind of coverage is frequently local. When one exists, weight it above the review ledger and cite it in the verdict.

**Weighting rules — this is where most competitor analysis goes wrong:**

- A complaint counts as **corroborated** only at **3+ independent sources**. One vivid review is an anecdote; three unrelated people describing the same friction is a pattern.
- Separate **frequency** from **severity**. A rare complaint about data loss outranks a frequent complaint about theme colors.
- **Recency-gate everything**: a complaint from 2021 about a feature shipped in 2023 is noise, and treating it as an opportunity is how you build something that already exists.
- **Price complaints are usually not an opportunity.** "Too expensive" is the single most common review sentiment about every paid product ever made; it signals an opportunity only when it recurs alongside a specific structural mismatch (per-seat pricing for a solo user, an enterprise floor that excludes the whole SMB segment).
- Tag each entry as **table stakes** (must match) or **wedge** (can exploit). Table stakes quietly determine the true MVP scope, and they're the reason "simpler and cheaper" so often loses.
- **Then tag it again — product-specific or category-inherent — because this is the distinction that decides verdicts.** A *product-specific* complaint is about how one team built or priced their thing: a broken sync, a missing integration, a per-seat model. Those are real wedges. A *category-inherent* complaint is about the interaction itself or the physics underneath it, and survives any rebuild: the task takes 15 seconds per item in a shop, the input the method needs can't be captured on the target hardware, the user has to do something socially awkward, the underlying data simply isn't available at that moment. **Category-inherent complaints are never wedges — they are evidence against the whole category**, and mistaking one for an opportunity is the single most expensive error available in this mode, because it turns a reason to stop into a reason to build.
  The test is concrete: *would this complaint disappear if a perfectly-funded, perfectly-competent team rebuilt the product from scratch tomorrow?* If no, it's category-inherent. And if the **majority** of corroborated pains in the ledger come out category-inherent, stop and say so at that point — the deep-dive has already found its answer, and continuing to D3 absorption on a category whose complaints nobody can fix just dresses a KILL in five more sections.

```markdown
### Pain & Praise Ledger
| Competitor | Type | Finding (paraphrased) | Sources | Freq | Severity | Recency | Classification | Scope |
|---|---|---|---|---|---|---|---|---|
| [K1](url) | 🔴 Pain | Sync breaks silently after token expiry | [r1](url), [r2](url), [r3](url) | High | High | 2026-03 | Wedge | Product-specific |
| [K1](url) | 🟢 Praise | Import handles 40+ bank formats | [r4](url), [r5](url) | High | — | 2026-01 | Table stakes | — |
| [K2](url) | 🔴 Pain | Task takes 15s per item, in public, every time | [r6](url), [r7](url), [test](url) | High | High | 2026-05 | **Not a wedge** | **Category-inherent** |
```

**This ledger is written into `docs/<idea-slug>/competitors.md` §3**, alongside the census rows, so the voice-of-customer work survives past this report. Paraphrase every finding — a one-line restatement plus the link, never pasted review or vendor text.

**AI-assisted synthesis is appropriate here, with one constraint**: summarizing 200 reviews into themes is exactly the kind of work worth delegating to a model pass, but every theme in the ledger must still point back to specific, real, linked sources. A theme with no traceable sources is a hallucination risk wearing a table row, and it will be indistinguishable from evidence three weeks later.

---

## D3 — Feature Absorption & Re-modulation

Competitors' good ideas are free R&D — someone already paid to discover that this feature matters. Absorbing them is legitimate and expected. Two guardrails keep it from wrecking the idea:

**The anti-bloat gate.** Every absorbed feature must pass all three:
1. It maps to a **table-stakes entry or a corroborated pain** in D2 (not to your admiration of a competitor's UI).
2. It survives the solo-build budget — absorption is the most common way a 2-week MVP silently becomes a 4-month one. Re-check Proof 7 after absorbing.
3. It doesn't dilute the wedge. Five absorbed features plus your differentiator is a worse product than your differentiator plus two, because the pitch stops being legible.

**Re-modulation, not replication.** Absorb the *job the feature does*, then re-express it in your architecture — a feature copied wholesale also imports the assumptions and constraints that made competitors' users complain about it in the first place. And the IP line from `legal_risk_playbook.md`'s Flanking addendum applies identically here: functionality is fair game; name, logo, copy, visual identity, and source/proprietary content are not.

```markdown
### Absorption Decisions
| Source | Feature | Job it does | Verdict | Re-modulated as | Build cost |
|---|---|---|---|---|---|
| [K3](url) | Bulk CSV mapping UI | Removes onboarding cliff | ABSORB | Auto-detect + confirm, no mapping screen | ~1 day |
| [K5](url) | Team permissions matrix | Enterprise procurement | REJECT | — (out of segment) | — |
```

---

## D4 — Graveyard Analysis (the honest-rejection engine)

This is the step the user explicitly asked not to be soft about, and the one most likely to change the verdict. Dead products are the cheapest possible source of truth about a category, because someone already ran the experiment.

For every dead or dying competitor from census tier 4, establish a **cause of death** with evidence — a shutdown post, a final blog entry, an archived repo with a README note, a "we're winding down" email screenshotted on Reddit, an acquisition announcement followed by product sunset, or (weaker, but usable when it's all there is) a review timeline showing collapse. Classify it:

| Cause | Typical evidence | What it implies for your idea |
|---|---|---|
| **Demand never existed** | Low reviews/installs from the start, founder post-mortem citing no traction | Structural — Proof 1 is probably wrong |
| **CAC exceeded LTV** | Post-mortem citing ad costs, pivot to enterprise | Structural unless your channel is genuinely different |
| **Churn / one-shot use** | Reviews praising the tool, revenue flat | Structural — attacks Proof 3 |
| **Platform / API dependency** | API pricing change, policy change, store delisting | Structural if you depend on the same surface |
| **Regulatory** | Legal notice, geo-restriction, forced feature removal | Structural, and feeds D6 directly |
| **Incumbent absorbed the feature** | The feature now ships free inside a bigger product | Structural — attacks Proof 5 |
| **Monetization mismatch** | Free tier cannibalized paid, priced below COGS | Fixable, sometimes |
| **Founder abandonment / burnout** | Personal post, repo archived, other projects started | Executional — the most encouraging cause to find |

**The structural-vs-executional test, and the rule that follows from it:**

> If **2+ independent dead competitors share the same structural cause of death**, that cause is a property of the category, not of their execution. The idea must either eliminate the component that exposes it to that cause, or be downgraded. "We'll just execute better" is not a rebuttal to a structural cause — it is the specific sentence every one of those founders also wrote.

Each corpse gets a row in `docs/<idea-slug>/competitors.md` §4 with its cause of death and the evidence link, so the next session in this category inherits it.

State the implication per component in the Component Ledger, not globally: often exactly one component carries the structural exposure and cutting it saves the idea. That's the outcome to look for, and it's why the ledger exists.

Note that a category with **no dead competitors at all** is not automatically good news: it usually means either the category is genuinely new (great — say so and check "why now?") or that nobody ever tried, which is a demand signal worth examining rather than celebrating.

---

## D5 — Revenue Feasibility (bottom-up only)

Top-down sizing ("the market is €4B, 0.1% is €4M") is banned in this playbook — it has never once predicted a solo product's revenue and it exists mainly to make decks feel good. Build from the bottom:

1. **Reachable audience, measured, not estimated.** Count what you can actually count and link it: subreddit member counts, Discord/forum sizes, directory listings of the target profession, LinkedIn filter counts, monthly search volume for the top 5 intent keywords, store category install ranges for the census products. This is the number that constrains everything downstream.
2. **Funnel with stated benchmarks.** Reach → visit → signup → paid, each with an assumption you *name and source* (a comparable's public numbers, an indie-hacker report, a published SaaS benchmark). Unsourced conversion assumptions are the single largest error term in the whole model, so mark them as assumptions rather than dressing them as findings.
3. **Price anchored to observed reality.** Use the census pricing column: what does this market *demonstrably* pay, and what does the free tier of the nearest competitor anchor expectations to? A free incumbent tier that covers the job for 80% of users caps your price far below what the "value" argument suggests.
4. **COGS per user — non-negotiable for AI ideas.** Estimate inference/API/storage cost per active user per month at realistic usage, not at the happy path. An AI feature whose heavy users cost more than the subscription is a business that gets worse as it grows, and this is currently the most common silent killer of AI micro-SaaS. If gross margin lands under ~70%, say so explicitly and treat it as a finding, not a footnote.
5. **Churn from evidence.** Use what D2 revealed about how long people stay with tools in this category — not a default 5%.
6. **Usage window and seasonality.** State how many weeks a year and how many sessions per user the product is genuinely used, and derive it from the job rather than from hope. A tax tool lives in two months, a watermelon tool in one summer, a wedding planner once per user ever, a school-timetable tool in September. This changes the answer more than pricing does and is invisible in a monthly-revenue model: a seasonal product doesn't earn a twelfth of the annual figure each month, it earns nothing for nine months while churn and store ranking decay run anyway. If the window is narrow, say what carries the product through the rest of the year — a second job-to-be-done, a second hemisphere, an adjacent season — or accept that Proof 3 fails here regardless of how good the product is.
7. **Three scenarios and a break-even.** Conservative / base / optimistic, each with the number of paying users needed to reach the user's own target income, and a realistic time-to-get-there. State the assumption that moves the answer most.

```markdown
### Revenue Feasibility
- **Reachable audience**: [figure] — [what was counted + links]
- **Funnel**: [reach] → [visit %] → [signup %] → [paid %] — each with source
- **Price point**: €X/mo — anchored to [K1](url) €Y, [K2](url) €Z, free tier at [K4](url)
- **COGS/user/month**: €X (inference €a + infra €b) → gross margin Z%
- **Churn assumption**: X%/mo — from [evidence]
- **Usage window**: [weeks/year active, sessions per user per year] — [what carries it through the off-season, or the admission that nothing does]
- **Break-even**: N paying users → €M MRR; conservative timeline: [months]
- **Most fragile assumption**: [the one that changes the verdict if wrong]
```

---

## D6 — Legal & Regulatory Deep Pass (per component)

`legal_risk_playbook.md` classifies the *idea* into a risk tier. That's the right granularity for discovery and the wrong one here, because legal exposure almost always attaches to a specific component — and cutting one row is usually cheaper than abandoning the idea. Run the tier classification first (it still applies in full), then go per row.

Surfaces to check beyond the base playbook's tiers, in EU/Italy-first order when the user or target market is European:

- **GDPR specifics, not "we'll be GDPR compliant"**: what personal data does each component actually process, on what lawful basis, where is it stored, is a DPA needed with each sub-processor (including the LLM vendor), and does any component involve profiling or automated decision-making.
- **EU AI Act**: transparency obligations for AI-generated content and chatbot disclosure; whether any component lands in a higher-risk use (employment, education, credit, biometric categorization). Most micro-SaaS ideas are limited-risk with disclosure duties — but that's a conclusion to reach, not to assume.
- **Data source terms of service**: if a component scrapes, ingests, or automates against a third-party site or API, read that ToS. A component that depends on prohibited automated access is a structural risk (and often exactly what killed a D4 corpse), not a paperwork detail.
- **Platform policy dependency**: App Store / Play / Chrome Web Store / marketplace rules relevant to the specific component — subscription and external-payment rules, data-safety declarations, review policies for the content type.
- **Consumer & subscription law** (EU/IT): right of withdrawal, auto-renewal disclosure, price-change notice, cancellation flow requirements.
- **Copyright & content provenance**: what the product ingests and what it outputs; whose content trains or feeds the AI component; whether output could reproduce protected material.
- **Accessibility**: the European Accessibility Act's requirements apply to a broad set of consumer-facing digital services in the EU — worth a line for consumer web/mobile products rather than a discovery afterwards.
- **Professional-liability framing**: if any component produces output someone might rely on for a regulated decision, the mitigation shape is the same one real competitors use — decision-support for a competent professional, never a substitute for their judgment.

The per-component ledger is written into `docs/<idea-slug>/legal.md` §3 (template: [legal_dossier_template.md](legal_dossier_template.md)), which also carries the two axes that apply regardless of mode — litigation exposure, and the gatekeeper sweep (regulators, legislation and political instability, closed orders and registries, municipal permits, trade lobbies, citizen committees and NIMBY opposition, boycott risk). At deep-dive depth the gatekeeper rows get the same per-component treatment: which component depends on which gate, and whether clearing it once shuts the door behind us.

```markdown
### Legal Ledger
| Component | Surface | Jurisdiction | Risk | Mitigation | Source |
|---|---|---|---|---|---|
| C1 | Third-party ToS on automated access | EU/global | 🔴 High | Official API only; drop scraping path | [ToS §4](url) |
| C4 | AI Act transparency (generated text) | EU | 🟡 Medium | Label AI output; human review before send | [source](url) |
```

Findings here feed component verdicts directly: a 🔴 High row with no viable mitigation is a CUT, and if it sits on a core component, it's a KILL. That is a legitimate deep-dive outcome and should not be softened into an "area to monitor."

---

## D7 — Adversarial Verdict

**Order matters.** Write the case against the idea *before* the verdict, not after — a written steelman produced after a conclusion is advocacy with extra steps.

1. **Strongest case against building this** (mandatory, minimum a full paragraph): the most credible reason a well-informed skeptic would tell the user not to build it, assembled from what D1-D6 actually found. If this paragraph is easy to write and hard to answer, that is the finding.
2. **Kill Criteria check**: walk the D0 list explicitly, one line each — HIT / NOT HIT / PARTIAL, with the evidence. This is the accountability step; skipping it is how a deep-dive quietly forgets the standards it set for itself.
3. **7-Proof re-scoring**: re-run `evaluation_framework.md`'s protocol against deep-dive evidence, and **state which proofs changed verdict versus the original report and why**. A re-score where nothing moved usually means the new evidence wasn't allowed to matter.
4. **Component Ledger — final**: every row gets KEEP / MODIFY / CUT / ADD, each with a one-line sourced reason. This table is the actual deliverable of the whole mode.
5. **Overall verdict**:
   - **GO** — build as specified (rare; if most deep-dives end here, re-read the Calibration note below).
   - **GO WITH CUTS** — build the reduced component set (the most common healthy outcome).
   - **PIVOT** — the job-to-be-done survives, the current shape doesn't; state the specific pivot.
   - **KILL** — structural cause of death, unmitigable legal exposure, or unviable economics. State which, plainly, and if a salvageable fragment exists (a component with real demand of its own), name it as a candidate for a future discovery session rather than padding the kill with consolation.

---

## D8 — Outputs & Write-Back

1. **`docs/<idea-slug>/deepdive.md`**, at the location resolved by `SKILL.md`'s Output Location & Environment rule (and delivered in-conversation, with the log entry printed for the user to append, if there's no persistent filesystem) — the full report (structure above: D0 ledger → census → pain/praise → absorption → graveyard → revenue → legal → verdict), with a header stating the date, the mode, and the research depth actually achieved against the Depth Contract.
2. **Update the existing `ideas_log.md` entry in place** — a deep-dive does *not* append a new entry, since it's the same idea; that's the distinction from a new evaluation. Add to the existing entry: `Deep-Dive: <date> — <verdict> — [report](docs/<slug>/deepdive.md)`, and refresh the entry's `Artifacts:` line, and if the verdict overturns the original status, change the status line and keep the original visible (`APPROVED → KILLED (deep-dive: 3 structural deaths in category)`). Update the Log Summary counts accordingly.
3. **Write back to the shared knowledge, so discovery mode benefits** — this is the cross-mode payoff and the reason the deep-dive isn't a dead end:
   - The census, the pain/praise ledger and the causes of death live in `docs/<slug>/competitors.md` (Step 6 of `SKILL.md`) — updated in place, not restarted. Link that file from the log entry so a future Original-mode Step 0 doesn't rediscover any of it from zero, and keep only the 2-3 most decisive competitor names in the entry itself.
   - If D4 found a category-level structural cause of death, record it under a **`## Category Red Flags`** section at the top of `ideas_log.md` (create it if absent) — one line, with the evidence link. Step 0 of every future session reads this, which turns one expensive deep-dive into a permanent filter on all future discovery.
4. **Update `docs/<slug>/legal.md`** with the per-component ledger from D6 and any gatekeeper finding the deep-dive turned up, rather than leaving the discovery-grade dossier in place next to a deeper report that contradicts it.
5. **If the verdict is GO or GO WITH CUTS**, regenerate or amend the functional blueprint (`blueprint_template.md` → `docs/<slug>/blueprint.md`) against the *final* Component Ledger — not the original idea. It stays at the functional level: scope, functional spec, UI/UX concept, roadmap — no schemas, endpoints or architecture. A blueprint that still contains cut components is worse than no blueprint, because it silently reinstates exactly what the deep-dive removed.

---

## Calibration for this mode

Discovery mode's calibration rule is "approval should be the exception." The deep-dive equivalent is:

> **A deep-dive that changes nothing is a failed deep-dive.** If a session ends with every component KEEP, the original verdict unchanged, and no serious case against the idea, the most likely explanation is not that the idea was exceptionally well-founded — it's that the research was run to confirm rather than to test. Before finalizing, check: did the census add competitors the original report missed? Did any Kill Criterion come close? Was the "strongest case against" genuinely hard to answer? If all three are no, the depth bar wasn't met, regardless of how many links the report contains.

The healthy distribution over many deep-dives skews toward **GO WITH CUTS** and **PIVOT**, with **KILL** a regular occurrence and **clean GO** the rarest outcome — because an idea that survives this process untouched should be surprising.
