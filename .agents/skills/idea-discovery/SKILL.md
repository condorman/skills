---
name: idea-discovery
description: Discover, research, evaluate and stress-test product ideas for Web, Mobile, B2B Micro-SaaS, Games, and AI Tools. Auto-routes between three modes - Original Discovery (a brand-new unserved idea), Flanking Discovery (an abandoned or stagnant product worth displacing), and Vertical Deep-Dive (adversarial validation of one chosen idea - competitor census, forum and review pain mining, failed-predecessor autopsies, bottom-up revenue modelling). Applies a strict 7-Proof anti-false-positive protocol and files one folder per idea under docs/ - evaluation report, competitor ledger, legal and gatekeeper dossier, functional blueprint - indexed by docs/ideas_log.md. Use for project ideas, micro-SaaS concepts, app or game ideas, product validation, competitor research, "what should I build next?", "find me a new app idea", "evaluate this idea", and for an idea already on the table - "is this feasible?", "who are the competitors?", "will this make money?", "what would kill this?", "legal risks?", or /idea-discovery.
---

# Idea Discovery, Flanking & Vertical Deep-Dive Skill (v7.0)

This skill provides an advanced methodology to discover, research, evaluate, architect, and stress-test **product ideas** (Web, Mobile Apps, B2B Micro-SaaS, AI Tools, Games). It eliminates **false positives** by subjecting every candidate concept to a rigorous **7-Proof Verification Protocol** (Willingness to Pay & Demand Velocity, Zero-CAC Distribution, Anti-Churn Frequency, AI Technical Reliability, Micro-Moat Defensibility, Status Quo Resistance, and True Solopreneur Buildability).

It runs in **three modes**, routed automatically in Step 0:

| Mode | The question it answers | Playbook |
|---|---|---|
| **Original Discovery** | "What unserved thing could I build?" | this file (default) |
| **Flanking Discovery** | "Which existing product is vulnerable enough to displace?" | `references/flanking_playbook.md` |
| **Vertical Deep-Dive** | "This specific idea — what would kill it?" | `references/vertical_deepdive_playbook.md` |

The first two are **selection** modes: they scan many candidates on deliberately thin evidence, because most candidates die and deep research on all of them is wasted. The third is a **commitment** mode: one idea, exhaustive evidence, and an explicitly adversarial posture. They share the same spine (evidence integrity, the 7 Proofs, the legal check, `ideas_log.md`), but their failure modes are opposite — discovery fails by approving too much, deep-dive fails by confirming what the user already believes.

**A note on rigor**: this protocol only does its job if most candidates fail it. If a batch of candidates comes back nearly all approved, that's not evidence the ideas were unusually good — it's a sign the proofs were applied as a rubric to justify a conclusion already reached. See the Calibration section in `references/evaluation_framework.md` and apply it throughout, not just at the end. The Deep-Dive equivalent of that rule is in `vertical_deepdive_playbook.md`: a deep-dive that changes nothing is a failed deep-dive.

---

## Workflow Overview

```
 0. Intent Routing (Original / Flanking / Deep-Dive)
    + Category Red Flags check + semantic duplicate scan (FULL log)
        │
        ├─► DEEP-DIVE TRACK ──► references/vertical_deepdive_playbook.md (D0-D8)
        │      Step 4's domain + legal gates still apply (D6 extends them);
        │      rejoins at Steps 6-9 for the ledger, dossier, log and blueprint.
        │
        └─► DISCOVERY TRACK (Original / Flanking)
             1. Candidate Mining        — friction/workaround vs abandoned/stagnant
             2. Verification Audit      — 5-pass prior art vs target-product status
                                          (every source from a real tool call)
             3. 7-Proof Protocol        — Flanking: Eligibility Gate first
             4. Qualification Gates     — "Why Now?", legal tier, domain file
             5. Evaluation Report       — docs/<slug>/evaluation.md
             6. Competitor Ledger       — docs/<slug>/competitors.md   (always)
             7. Legal Dossier           — docs/<slug>/legal.md         (always)
             8. Log Update              — docs/ideas_log.md
             9. Functional Blueprint    — mandatory for APPROVED 7/7
```

Steps 6 and 7 run for **every** idea that reaches an evaluation, including DISCARDED ones. That's deliberate: the competitor list and the legal picture are the two findings most likely to be needed again — by a future idea in the same category, or by this same idea if it gets revisited — and they're the two that cost the most to rebuild from scratch. The blueprint, by contrast, is only worth writing for an idea someone might actually build.

---

## Output Location & Environment

### One directory per idea

`docs/` holds **one shared spine file and one sub-directory per idea**. Flat artifacts in `docs/` were the previous layout and they stop being readable after ~5 ideas, because five ideas produce twenty files whose only ordering is alphabetical.

```
docs/
├── ideas_log.md              ← the only shared file: cross-idea ledger, never moves
├── <idea-slug>/
│   ├── evaluation.md         ← Step 5 report (Original / Flanking)
│   ├── competitors.md        ← Step 6 competitor ledger — persistent, appended across sessions
│   ├── legal.md              ← Step 7 legal & gatekeeper dossier
│   ├── blueprint.md          ← Step 9 functional blueprint (approved ideas only)
│   └── deepdive.md           ← Deep-Dive report (D8), when that mode runs
└── <other-idea-slug>/
```

The **slug** is kebab-case, derived from the idea name, stable for the life of the idea: `sagra-finder`, `chargeback-autopilot`. Once created it does not get renamed, because `ideas_log.md` links point at it. If the idea's *name* changes later, keep the directory and note the new name in the log entry rather than moving files and breaking every link.

Inside a per-idea directory the file names are short and fixed (`evaluation.md`, not `<slug>_evaluation.md`) — the directory already carries the slug, and predictable names are what let a later session find an artifact without listing the tree first.

**Migration of a pre-existing flat `docs/`**: if flat artifacts (`<slug>_evaluation.md`, `<slug>_blueprint.md`, …) are found at the top level, don't mix layouts and don't reorganize silently. Say what's there, propose the move (one `docs/<slug>/` per idea, files renamed to the short form, `ideas_log.md` links rewritten), and act on the answer. New ideas in this session always use the new layout regardless.

Resolve where `docs/` itself lives in this order:

1. A **target project path** given in the prompt → `<target_project>/docs/`.
2. Otherwise, a writable workspace → `<workspace_root>/docs/`.
3. **No persistent filesystem at all** (a plain chat session, mobile, or any context where files don't survive the conversation) → this is not a reason to skip the pipeline, but it changes two things and both must be said out loud:
   - **Deliver the artifacts in the conversation**, and additionally as downloadable files if the interface supports them — each one under its own clear heading, in the same order it would have had on disk (evaluation → competitors → legal → blueprint). Don't silently drop an artifact because there's nowhere to save it: the competitor ledger and the legal dossier are the two most expensive to reconstruct later, so they're the last things to cut, not the first.
   - **Handle the log explicitly instead of failing Step 0 quietly.** Open the session by stating that no `ideas_log.md` was reachable, and ask the user to paste theirs if they keep one — the duplicate scan is the check that stops the same idea coming back three sessions in a row, so it's worth one question. Close the session by printing the log entry as a copy-pasteable markdown block for them to append themselves. A skipped duplicate scan that nobody announced is the single most expensive silent failure in this skill, because the waste only shows up sessions later.

**First run**: if the log doesn't exist yet in a writable environment, create it before Step 0's checks rather than treating "no log" as "no history to worry about":

```markdown
# Ideas Log

## Log Summary
- Total evaluated: 0 | Approved: 0 | Pivot Required: 0 | Discarded: 0
- Approval rate: n/a

## Category Red Flags
_(structural causes of death found by deep-dives — read this before committing to any candidate)_

## Evaluated Ideas
```

---

## Multi-Idea Sessions

If the user asks for more than one idea in a single request (e.g. "give me 5 app ideas"), run Steps 0–4 fully and independently for each candidate. Two failure modes are specific to this case and worth naming, because they don't show up when evaluating one idea at a time:

- **The rotation gate applies within the batch, not just across sessions.** Two candidates generated back-to-back in the same reply can share the same underlying mechanic or template just as easily as two candidates from different weeks — check each new candidate against the others already produced *in this same batch*, not only against `ideas_log.md`.
- **Evidence gets reused instead of re-gathered.** It's easy to let Proof 1 (WTP) or Proof 6 (Status Quo) evidence from candidate #1 quietly justify a similar-sounding candidate #3 without a fresh search. Each candidate needs its own retrieved evidence.

**A count is a target, not a contract.** If the user asks for 5 ideas and only 2 survive mining and prior-art, deliver 2 and say why — padding the batch with candidates already known to be dead produces reports nobody can act on and quietly teaches the reader that the verdicts are decorative. Concretely: when a candidate is killed by the *first* prior-art pass (an established competitor already ships it, or the category is commodity at a free price point), **replace it before writing its report**, and only write up a rejection in full when the rejection is itself informative — a near-miss, or a candidate the user is likely to think of themselves. Two well-evidenced candidates plus a one-line note on what was screened out beats five reports of which three were foregone conclusions.

**Only candidates that reach an evaluation get a directory.** A niche screened out during Step 1/2 doesn't need `docs/<slug>/` — it needs one line in the batch's note about what was screened out and why, and, if a real product was the reason it died, a row in the surviving idea's `competitors.md`. Creating four directories for four candidates that never got past mining recreates exactly the clutter this layout was meant to remove.

Before presenting a batch of 3+ candidates, do one batch-level pass: state the approval rate across the batch, and if most of them passed, re-audit those approvals *before* presenting them rather than after. (For single- or two-idea sessions, see the calibration rule below — a batch that small carries no rate signal.)

---

## Approval-Rate Calibration: Read It Cumulatively

The ~1/3 guideline in `evaluation_framework.md` is a property of the **log over time**, not of a single session, and the difference matters because the arithmetic is degenerate at small N: a one-idea session that ends APPROVED is a 100% approval rate and means nothing at all. Treating that as a red flag manufactures a re-audit on every successful short session, and a warning that fires constantly is one that gets ignored exactly when it's real.

So: track the rate from the `Approval rate` line in `ideas_log.md`'s Log Summary (Step 8 keeps it current), and trigger a re-audit when **either**

- the cumulative rate across ~6+ evaluated ideas sits meaningfully above ~1/3, **or**
- a single batch of 3+ candidates approves most of them.

When it fires, re-audit the most recent approvals — Proofs 1 and 6 first, since those are the two easiest to pass on vibes — against the Calibration section in `evaluation_framework.md`.

---

## What All Three Modes Share

The modes are three depths of the same pipeline, not three skills bolted together:

- **Evidence integrity** (Step 2): every competitor, URL, review quote, and price comes from a real tool call in this session. Most load-bearing in Deep-Dive, where the volume of citations makes a single fabricated one hard to spot later.
- **Name-as-link everywhere**: `[Product](url)` at first mention in every section, log entry included.
- **The 7 Proofs** and **the legal check**: the same protocol throughout. What changes is evidence quality — discovery scores them on thin evidence, Flanking reads them against a real incumbent, Deep-Dive re-scores them on exhaustive evidence and must state which verdicts moved and why.
- **One directory per idea, and two cumulative files inside it**: `competitors.md` and `legal.md` are written by whichever mode reaches the idea first and *updated* by every mode that touches it afterwards — never restarted. This is what makes research compound instead of being re-run: a deep-dive three months later starts from the first pass's competitor list and adds to it.
- **`ideas_log.md` as the single spine**: discovery modes *append* entries, Deep-Dive *updates* the existing one in place. One idea, one entry, whatever depth it has reached. This is also what makes deep-dives compound: a deep-dive writes its competitor census and any category-level cause of death back into the log, so the next Original-mode Step 0 inherits research it never had to run.

What is deliberately *not* shared: the **calibration target**. Discovery is calibrated so that approval is rare. Deep-Dive is calibrated so that *change* is common — an unchanged idea is the suspicious outcome, not the good one. Applying discovery's "approve rarely" instinct to a deep-dive produces theatrical pessimism; applying deep-dive's "it survived, ship it" instinct to discovery produces exactly the false-positive flood this skill was built to stop.

---

## Step 0: Intent Routing, Memory Log Check, Semantic Duplicate Scan & Category Diversity Gate

### 0.A — Route the request to a mode (infer it; only ask when genuinely ambiguous)

**Infer the mode from what the user actually said rather than opening with a menu.** The three modes answer visibly different questions, and the request almost always reveals which one is wanted. Asking anyway is a small tax on every session and reads as not having listened — so ask only when the signals genuinely conflict.

The decisive signal is **the object of the request**: a *set* of possible ideas (discovery) versus **one specific idea already on the table** (deep-dive).

| Route here | When the request looks like | Examples |
|---|---|---|
| **Vertical Deep-Dive** (`vertical_deepdive_playbook.md`) | One named/known idea is the object, and the ask is validation, competitors, money, risk, or "should I actually build it" | "approfondisci l'idea X", "is this feasible?", "find me every competitor for X", "will this make money?", "what would kill this?", "legal risks for X?", "deep dive on the idea from last time", "I'm about to start building X" |
| **Flanking Discovery** (`flanking_playbook.md`) | The object is *existing products* to displace | "find an abandoned app worth reviving", "which competitor has stopped innovating?", "something I could clone and do better" |
| **Original Discovery** (default) | The object is an unserved gap; often plural or open-ended | "what should I build next?", "give me 5 app ideas", "find me a new micro-SaaS idea" |

Three routing rules that resolve most of the remaining ambiguity:

- **"Evaluate this idea" for an idea the user brings in from outside** is a Deep-Dive, not Original Discovery. The idea already exists; nothing is being discovered. Run the deep-dive and let it produce the 7-Proof scoring as part of D7.
- **A follow-up turn inside a discovery session** ("ok, the second one — go deeper", "tell me more about that one") is a Deep-Dive on that specific candidate. This is the most common way the mode is reached, and it doesn't need a mode question: the user already picked, which is exactly the signal.
- **A deep-dive that ends in KILL or PIVOT can hand back to discovery** in the same session, if the user wants a replacement. Say which mode you're switching to and why, rather than silently changing the kind of work being done.

State the routed mode in one short line before starting (`Deep-Dive on <idea> — 8+ competitors, VoC mining, graveyard, revenue, legal.`) so a misroute is cheap to correct. If two routes are genuinely plausible — and only then — ask once, with buttons if the interface supports them.

### 0.B — Memory & duplicate checks (all modes)

**In Deep-Dive Mode the duplicate scan inverts**: finding the idea already in `ideas_log.md` is expected and required, not disqualifying. Read that entry *and* its linked evaluation report before searching — the deep-dive's job is to go past what the original report claimed, which is impossible without knowing what it claimed. Steps 5 and the Step 8 log-append below are then replaced by the D0-D8 sequence in `vertical_deepdive_playbook.md`; Step 4's domain and legal gates still apply (D6 extends them rather than replacing them). If the idea isn't in the log (the user brought it from outside), create the entry first, then deep-dive it.

**Check `## Category Red Flags` at the top of `ideas_log.md`** (if present) before committing to any candidate in any mode. That section is written by past deep-dives and records category-level structural causes of death found the expensive way. A new candidate that walks straight into a recorded red flag must either address it explicitly with new evidence or be dropped — re-proposing into a known graveyard is the most wasteful failure this skill can produce.

The remaining checks apply identically to all three modes:

1. Read `docs/ideas_log.md` at the location resolved by the Output Location & Environment rule above. If it isn't reachable, say so before proceeding — don't let a missing file turn into a silently unchecked session.
2. Check all previously recorded **APPROVED**, **PIVOT REQUIRED**, and **DISCARDED** ideas.
3. **DO NOT** re-propose or re-analyze concepts already recorded unless specifically instructed.
4. **Semantic duplicate scan (not just literal name matching)**: Before committing to a candidate concept, compare it against **every** entry already in the log, at two levels — not only whether the two ideas do the same *thing*, but whether they're built from the same *template*:
   - **Core mechanic/job-to-be-done**: Two ideas with different names and taglines can still be the same product. "A magnetic-whip physics arcade game" and "a magnetic-chain physics arcade game" are the same underlying mechanic even with different names.
   - **Underlying architecture/business-model template reused across a different vertical name**: this is the subtler and more common trap for Web App / SaaS / marketplace concepts. "A verified professional directory + credential OCR + event ticketing + content hub + embeddable badge" is the same software product whether it's aimed at machinery-safety consultants, holistic-health practitioners, acoustics technicians, or art restorers — a different professional noun does not make it a different idea. If a candidate shares 3+ structural components with something already in the log, treat it as the same template even if every domain-specific detail (the vertical, the regulatory body, the price) differs.

   Either skip the new concept or explicitly frame it as a deliberate variant and say why it's different enough to coexist (different platform, meaningfully different core loop or architecture, etc.). If you're unsure whether two concepts are "the same idea," err toward treating them as duplicates and picking something else — the log is only useful as a competitive/novelty ledger if near-duplicates get caught here instead of after a full research cycle.

   **In Flanking Mode**, this scan has a third, simpler check: if the log already contains an entry that flanked the same target product, don't re-attempt it without genuinely new evidence — a repeat flanking attempt on the same target is a duplicate exactly the way a repeated mechanic is in Original Discovery Mode.
5. **Enforce Category Diversity Gate**: Inspect the last 3 entries in `ideas_log.md` *within the same domain* (mobile app / B2B SaaS / game). If 2+ recent entries in that domain cluster on the same underlying vertical (e.g. Audio FFT / Spectrogram sensor apps, or physics-merge arcade games, or Stripe-reconciliation SaaS tools), **DO NOT propose another one in that same cluster**. For mobile apps, rotate across the categories in `domain_mobile.md`. For SaaS and Games, see the rotation rules in `domain_saas.md` and `domain_games.md`.
6. **Rejection-reason consistency check**: This is different from the duplicate scan above — it's not about whether the *idea* repeats, it's about whether a *reason for rejection* repeats without being addressed. Look at the most recent DISCARDED or PIVOT REQUIRED entries and read their stated rejection reason. If the new candidate shares the same broad category, genre, or distribution channel as one of those recent rejections (e.g. the last entry was a cozy mobile/Steam simulation game discarded for "category saturation / high UA cost," and the new candidate is also a cozy simulation game), the new evaluation must explicitly engage with that same concern — cite what's actually different about the demand, distribution, or moat this time — rather than silently writing a fresh Proof 1/Proof 2 assessment that never mentions the sibling that just failed on the same axis. Silence on a directly-relevant recent rejection is itself a red flag that the new evaluation isn't being applied with real rigor.

---

## Step 1: Candidate Mining (mode-dependent)

### Original Discovery Mode — Anchored Friction Mining

**Mine anchors, not adjectives.** This is the single highest-leverage rule in the step, and it exists because the obvious approach fails in a specific, repeatable way: queries built from adjectives — "wastes hours every week", "manual workaround", "hacky process" — are the exact phrases software vendors and infoproduct sellers optimise for, so they return content marketing, listicles and Gumroad funnels rather than people with a problem. An **anchor** is a dated, checkable document that created or proves the friction: a regulation with a compliance date, a platform policy with a cutoff, a feature request with a vote count and an age, a published rate card or price increase, a tender specification. Anchors can be verified in one click and can't be manufactured by a marketing team.

Run the miner first, passing the sector being mined (not a product idea) and the market's language — for a market-specific niche, the local language goes first, since an English-only sweep of an Italian or German B2B niche misses both the incumbents and the rule that created the demand:

```bash
python scripts/deep_search_miner.py "<sector or audience>" <domain> --mining [--locale=it]
```

The five anchor families it emits are a menu, not a checklist — run the ones that plausibly apply and state which you skipped and why. Then work the three pillars, each anchored:

1. **Obligation & policy anchors** *(strongest)*: a rule, standard, or platform requirement with a date attached. The affected population is defined by the rule itself, the deadline supplies the "Why Now?", and the friction is documented before anyone builds anything.
2. **Money-already-moving anchors**: recurring freelance job posts ($300–$2,000 automation requests), consultant rate cards, tender specs, published price increases people are complaining about. This is Proof 1 evidence gathered before the candidate exists.
3. **Counted-demand anchors**: feature requests with votes and dates sitting unaddressed on public boards, and practitioner *enumeration* threads ("what do you use for X") — which list real tools, where complaint threads list blog posts.

**"Why Now?" still has to be answered**, but as a property of the candidate rather than a mining channel: name the recent capability (multimodal vision, cheap inference, browser agents, a new platform API) that makes the anchored friction solvable by one person now and not 12 months ago.

If a sweep produces no anchored candidate, say so and propose mining a different sector rather than falling back on adjective queries — the fallback is what produces plausible-sounding candidates with no evidence behind them.

### Flanking Discovery Mode — Abandoned, Stagnant & Improvable Candidate Mining

Consult `references/flanking_playbook.md` for the full methodology. In brief: mine for candidates matching one of three patterns — **Abandoned-but-Proven** (had real traction, now genuinely unmaintained), **Stagnant-but-Validated** (still alive, real usage, but stopped innovating), or **Good-Foundation-Needs-Innovation** (healthy today, but a specific sourced gap could displace it). Every candidate needs the full evidence bar for its pattern, not just "looks old" — see the playbook for the exact search signals (store listing update dates, `alternativeto.net`, low-star recent reviews, archived GitHub repos, stale feature-request boards).

---

## Step 2: Verification Audit (mode-dependent)

### Original Discovery Mode — Prior-Art & Novelty Verification Protocol

Consult `references/deep_search_playbook.md` for vertical Dorks, mechanics-first isolation, patent registries, and Asian market queries.

Before starting search execution, run the search payload miner helper script, passing the domain (`mobile` / `games` / `saas` / `web` / `ai_tools`) so it only returns dorks relevant to that channel. Add `--deep-tech` only when the mechanism is genuinely novel from an engineering standpoint (see Proof 7) — it adds the Patent/arXiv pass, which is disproportionate for an ordinary CRUD/utility idea:
```bash
python scripts/deep_search_miner.py "<core_mechanics_terms>" <domain> [--deep-tech]
```

Run a **5-pass verification search**. Passes 1, 2, and 5 always run. Passes 3 and 4 are conditional — running them unconditionally on every idea (a patent search for a tip-splitter calculator, an Asian-market search for a niche English-language B2B tool) burns research time without adding signal, and a thin-but-honest scoped search beats a padded one that technically checked every box:

- **Pass 1: Mechanics-First Isolation Search**: Abstract the concept into its raw game/UX loop (ignoring graphics/theme) and search across vertical platforms (App Store, SteamDB, GitHub, Chrome Web Store).
- **Pass 2: Direct Keyword & Ecosystem Search**: Google Dorks on Product Hunt, GitHub topics, BetaList, Hacker News, and Canny boards.
- **Pass 3: Cross-Language & Regional Verification** *(run by default for Games; for other domains, only run it if the mechanic is the kind that plausibly ships first in an Asian indie/consumer market — otherwise note in the Evidence Log that it was skipped and why)*: Search Asian markets (BOOTH/DLsite for JP, WeChat/Xiaohongshu for CN) using translated core mechanics keywords.
- **Pass 4: Patent & Academic IP Audit** *(only run when the mechanism is genuinely novel from an engineering standpoint — the same bar as Proof 7's red-flag checklist in `evaluation_framework.md`: custom signal processing, novel physics/rendering, an uncalibrated on-device model. For an ordinary CRUD/utility idea, state explicitly that this pass was skipped as disproportionate rather than running it as a formality)*: Search Google Patents (`patents.google.com`) and arXiv/SIGGRAPH for deep-tech algorithms, novel game physics/rendering shaders, or patented workflow methods.
- **Pass 5: Failed Predecessor & Feature Delta Audit**:
  - Analyze why dead predecessors failed (e.g. pre-LLM technology bottleneck vs low demand).
  - Construct a **Feature Delta Matrix** comparing the candidate idea against the 2 closest prior-art solutions.
  - Require an **Evidence Audit Log** listing verified query strings and real URLs examined.

### Flanking Discovery Mode — Target Product Status & Displacement-Gap Audit

Consult `references/flanking_playbook.md`. Instead of proving the idea is novel (it isn't — that's not the point), this audit proves the target product genuinely matches its claimed pattern and that a displacement path exists: pull the store listing's last-update date, recent review sentiment, changelog/feature-request history, and residual-demand signals, all with real links. This is where the Feature Delta Matrix's "Closest Prior Art" columns become the target product itself rather than a coincidental competitor.

**Evidence integrity rule**: every entry in the Evidence Audit Log — every competitor name, URL, review quote, or pricing figure — must come from an actual search/fetch tool call made during this session, not from general knowledge or a plausible-sounding guess. If a search tool isn't available or a claim can't be verified, say so explicitly in the report ("prior-art search for X could not be completed") rather than filling the gap with an invented-but-plausible URL or app name. A thin but honest evidence log is far more useful than a complete-looking one that's partly fabricated, since the whole point of this step is to catch prior art that would otherwise sink the idea later.

**Name every real competitor as a link, everywhere it appears — not only in the Evidence Audit Log.** This includes the Feature Delta Matrix cells, the `ideas_log.md` entry, and any narrative mention in the report ("similar to X" or "unlike Y"). A bare name is close to useless downstream: app-store and product names collide constantly (a search for a job-quoting app can turn up "Job Pricing," "Job Price Estimator," and "Job Estimator and Invoices" as three distinct, unrelated products), and the person reading the report later has no fast way to tell which specific one was meant or verify it without redoing the search themselves — which defeats the purpose of having done the research. Write it as `[App/Tool Name](url)` at first mention in each section, not just once in a log at the bottom.

---

## Step 3: Anti-False-Positive 7-Proof Verification Protocol

**If Flanking Mode is active**, first run the **Flanking Eligibility Gate** in `references/flanking_playbook.md` (Genuine Pattern Match + Displacement Feasibility) before scoring anything below. A candidate that doesn't clear the gate isn't a Flanking candidate at all — it's a regular competitor analysis with extra steps, and doesn't get scored against the 7 Proofs until it either clears the gate or is re-routed through Original Discovery Mode. If the gate is cleared, `flanking_playbook.md` also explains how to read each of the 7 Proofs below against a real incumbent rather than a hypothetical one.

Consult `references/evaluation_framework.md` for complete guidelines, the Calibration section, and scoring matrices.

Every candidate idea MUST be evaluated against all 7 Proofs. For each one, apply the steelman-rejection habit from the Calibration section before marking it PASS:

1. **Proof 1: Willingness to Pay & Demand Velocity (WTP & Trends)**: Prove that users or companies are currently spending real money (on freelancers, competitor software, or manual workarounds) AND search volume momentum is rising/active.
2. **Proof 2: Zero-CAC Organic Distribution**: Identify a specific, unpaid organic channel (Chrome Web Store SEO, pSEO, template marketplace, active niche community, viral short-form video) to acquire users without paid ads.
3. **Proof 3: High Frequency & Retention (Anti-Churn)**: Ensure the tool solves a daily or weekly recurring task—not a one-time utility.
4. **Proof 4: AI Technical Reliability**: Verify that the AI pipeline achieves >95% accuracy without requiring human-in-the-loop debugging or overwhelming 1 person with support tickets.
5. **Proof 5: Micro-Moat Defensibility**: Define a unique advantage (niche prompt workflow, complex API integrations, SEO lock-in, spatial audio calibration) that prevents instant 1-day cloning by generic AI wrappers.
6. **Proof 6: Status Quo Resistance (Non-Software Substitute Test)**: Prove that the app saves >2 hours/week or $200+/month compared to free human inertia (paper, spreadsheet, pinned WhatsApp message).
7. **Proof 7: True Solopreneur Buildability**: Verify the core mechanism can be built almost entirely by composing existing SDKs/APIs rather than inventing and empirically calibrating novel signal-processing or ML techniques — and that the stated MVP timeline honestly separates ordinary CRUD/UI work from any novel-component R&D and real-device calibration time. Treat "unprecedented" mechanisms as carrying build risk by default; see the Proof 7 red-flag checklist in `evaluation_framework.md`.

**Scoring**:
- **7/7 Proofs Passed**: **APPROVED**
- **6/7 Proofs Passed**: **PIVOT REQUIRED** (Identify and fix the missing proof)
- **≤5/7 Proofs Passed**: **DISCARDED** (Eliminated as a False Positive)

---

## Step 4: Qualification & Domain-Specific Directives

Load the relevant domain reference file based on the concept type:
- For **Game Concepts**: Consult [domain_games.md](references/domain_games.md) (Multi-session replayability, virality loops, endless modes, mechanic rotation gate).
- For **B2B SaaS / Web Apps** (including verified directories, reference portals, and other two-sided marketplaces — they belong here even though they don't look like a typical API-integration tool): Consult [domain_saas.md](references/domain_saas.md) (API integrations, compliance churn <2%, freelancer WTP, workflow-vertical rotation gate, and — for marketplace/directory ideas specifically — Section 5's template-reskin detection and Bootstrap Proof requirement).
- For **Mobile Apps**: Consult [domain_mobile.md](references/domain_mobile.md) (7 broad functional categories and the Category Rotation Gate).

Then run the **Legal & Regulatory Risk Check**: consult [legal_risk_playbook.md](references/legal_risk_playbook.md) and classify the idea into a risk tier. Ideas touching health/mental health, money movement, minors, biometric data, or professional-advice substitutes require actual cited regulatory research before Section 6 of the report can be written — a "Very Low / Zero" verdict without that research is not acceptable for those categories.

---

## Step 5: Standardized Original Idea Evaluation Report

Save it as `docs/<idea-slug>/evaluation.md`.

**Deep-Dive Mode uses its own report format instead** — the D0-D8 structure in `vertical_deepdive_playbook.md`, saved as `docs/<idea-slug>/deepdive.md`. Don't produce both: a deep-dive report that opens with a fresh discovery-style evaluation is duplicating the original report it was supposed to supersede. The 7-Proof matrix still appears inside the deep-dive report, at D7, as a *re-scoring* against the new evidence.

For every validated idea in Original / Flanking modes, use the report template in [report_template.md](references/report_template.md) exactly as written — sections 1-8, the Feature Delta Matrix, the Evidence Audit Log, and the 7-Proof matrix. Two things about it are worth keeping in mind while filling it in rather than discovering afterwards:

- **The Feature Delta Matrix and the 7-Proof matrix are the parts people actually read.** Everything else is supporting material; those two are where a vague answer does the most damage.
- **Omit inapplicable subsections rather than leaving them blank** (3.0 outside Flanking Mode, 3.3 outside marketplace/directory ideas).

---

## Step 6: Competitor Ledger (ALWAYS — `docs/<idea-slug>/competitors.md`)

Every mode of this skill spends most of its research budget looking at other people's products, and until now that work survived only as scattered cells inside a report — a Feature Delta Matrix here, a census table there, a Pain & Praise Ledger in a deep-dive. Consult [competitor_ledger_template.md](references/competitor_ledger_template.md) and write it to a file of its own instead. It is a **cumulative** file: a deep-dive months later appends to it and updates rows, it never starts over.

Per competitor, the ledger records: **name as a link**, a **classification** (Formidable incumbent / Adjacent / Abandoned / Stagnant / Dead / DIY-status-quo / Open-source), the **user critiques and compliments** with sources, and — for anything dead or dying — the **cause of death**, or for anything winning, **why it wins**. The template has the exact columns and the rules for filling them.

Two rules matter more than the format:

- **Screened-out candidates go in too.** A product that was found and correctly dismissed ("enterprise-only, €900/mo floor") is evidence; a product that was never found looks identical to one that doesn't exist. In discovery modes this is what turns Step 1's discarded niches into something a future session can reuse instead of rediscovering.
- **Evidence integrity applies unchanged**: every row comes from a real tool call in this session. An unsourced competitor row is worse here than in a report, because a ledger is read months later by someone who will assume it was verified.

---

## Step 7: Legal & Gatekeeper Dossier (ALWAYS — `docs/<idea-slug>/legal.md`)

Step 4's risk-tier classification produces a *verdict*; this step produces the **file that shows the work**, and it widens the question. Consult [legal_dossier_template.md](references/legal_dossier_template.md), which covers two distinct axes:

1. **Litigation & regulatory exposure** — is there a realistic risk of a legal dispute, and with whom: regulators and authorities, current legislation, IP/trademark holders, platform operators, data subjects, users harmed by a wrong output. Per `legal_risk_playbook.md`, elevated-tier domains need cited research here, not assertions.
2. **Gatekeepers and non-regulatory blockers** — the actors who can stop a product without any court being involved. Regulators and authorities; government law and pending legislation; political instability in the target market; closed associations, orders and registries that control access to the professional segment; local bureaucracy, municipal permits and building concessions; trade associations and lobbies with an interest in the status quo; citizen committees and NIMBY opposition; ethical or cultural boycott risk.

The second axis is the one that gets skipped, and it's the one that kills locally-anchored ideas: a product whose demand depends on a permit office, a professional register, or a municipality's goodwill has a real dependency even when it is perfectly legal. Each row asks the same two questions: **does this actor block us**, and **does it protect an incumbent** — because a gatekeeper that keeps everyone out is a barrier to entry when you're outside it and a moat once you're inside, and which of the two applies changes the strategy rather than just the risk score.

**Proportionality still governs the depth.** A single-player utility with no local footprint gets a short dossier that says, per axis, why it doesn't apply — that's a legitimate result and takes a paragraph. Marking every axis "not applicable" without saying why is not; it's the same failure as a copy-pasted "Legal Risk: Very Low." Where the dossier finds something material, Section 6 of the evaluation report summarizes it and links here rather than duplicating it.

---

## Step 8: Memory Logging

Update `ideas_log.md` with every analyzed idea (both Approved and Discarded) including the **Novelty Factor**, **7-Proof Score**, and **Rejection Reason**, to prevent redundant research in future sessions. **For Flanking Mode entries**, also record the specific target product as a name+link in the Summary line — this is what Step 0's duplicate scan checks against to catch a repeat flanking attempt on the same product later.

**Deep-Dive Mode updates the existing entry in place rather than appending** — same idea, same entry; appending would inflate the log's counts and break the approval-rate tracking Step 0 relies on. The exact write-back (verdict line, status overturn, census competitors, `## Category Red Flags`) is specified in D8 of `vertical_deepdive_playbook.md`.

**Every entry links its own directory.** Add an `Artifacts:` line listing what exists for that idea — `[evaluation](docs/<slug>/evaluation.md) · [competitors](docs/<slug>/competitors.md) · [legal](docs/<slug>/legal.md) · [blueprint](docs/<slug>/blueprint.md)` — omitting the ones not produced. The log stays the index; the directory holds the depth. This is also what keeps the log summary short: detail that used to bloat an entry now has a file to live in.

**Link named competitors here too, not just in the session's report**: if the Rejection Reason names a specific product (e.g. "2+ existing chargeback-management SaaS tools already cover this workflow"), name and link it — `[Product Name](url)` — in the log entry itself. The log is what future sessions read to avoid redoing this research; a bare name recreates the exact disambiguation problem this is meant to solve, just deferred to whoever reads the log next.

**Avoid the numbering-collision bug**: entries must NOT be numbered with a per-session counter that restarts or gets guessed (this log has previously ended up with several entries all titled `### 1.`). Instead:
1. Before adding an entry, count the existing `###` idea headings already in the file.
2. Always **append at the very end of the "Evaluated Ideas" section** (never insert above older entries) and number it `<existing count> + 1`.
3. Update the **Log Summary** counts (Total / Approved / Pivot Required / Discarded) and the **Approval rate** line to match reality after the append. This is what makes the calibration rule checkable at a glance in the next session instead of re-derived from memory.
4. If the count looks unreliable (e.g. the log was hand-edited), drop the numeric prefix for that entry rather than guessing — a heading without a number is harmless; two headings with the same number breaks anything referencing "entry #N" later.

**Keep the Summary bullet scannable**: the log's whole purpose is to be quickly skimmable in a future Step 0 — that only works if each entry's summary stays a few sentences. If Step 1/2 screening ruled out many candidate niches before landing on this one (a good sign of rigor, not a problem), name the 2-3 closest alternatives seriously considered and why they lost out, and leave the rest to the evaluation report's Section 3.

---

## Step 9: Functional Blueprint (MANDATORY for APPROVED 7/7 Ideas)

For every concept that achieves an **APPROVED (7/7)** rating — and, in Deep-Dive Mode, for every **GO** or **GO WITH CUTS** verdict — consult [blueprint_template.md](references/blueprint_template.md) and generate `docs/<idea-slug>/blueprint.md`.

**This blueprint stops at the functional level on purpose.** At this stage the idea has been validated, not committed to; database schemas, API contracts and architecture diagrams written now are guesses that get thrown away the moment real building starts, and worse, they make an unbuilt idea *feel* decided. The things genuinely worth fixing early are what the product does, what it feels like to use, and in what order it gets built:

1. Product definition & scope — the job-to-be-done, the user, what is explicitly out of scope.
2. Functional specification — features as capabilities and behaviours (user stories, rules, states, edge cases), never as implementation.
3. UI/UX concept — screen hierarchy, the primary flow end to end, the key interaction that carries the product, visual direction and tokens.
4. Implementation roadmap — the ordered path to a shippable MVP, with the riskiest thing first.

**Stay out of**: DDL and table schemas, API endpoint tables and payload contracts, architecture diagrams, infrastructure and vendor choices, library selection. If a technical constraint genuinely shapes the product ("must work offline in a basement with no signal", "the export has to be a PDF a client can sign"), state it as a **functional constraint** in the spec — that's product information — and leave how it gets satisfied to whoever builds it.

**After a Deep-Dive, build the blueprint from the final Component Ledger, not from the original idea** — and if a blueprint already existed, amend it rather than leaving the old one alongside. A blueprint that still contains cut components silently reinstates exactly what the deep-dive removed, which is worse than having no blueprint at all.

---

## References

- [sources.md](references/sources.md): Portals, marketplaces and dorks — including the anchors-beat-adjectives rule and the anchor dork families that Step 1's mining depends on.
- [deep_search_playbook.md](references/deep_search_playbook.md): Vertical search Dorks, Mechanics-First isolation, Asian market queries, Patent search, Status Quo inertia test, Feature Delta Matrix, and Evidence Audit Log rules.
- [evaluation_framework.md](references/evaluation_framework.md): Detailed 7-Proof verification protocol against false positives, plus the Calibration section on keeping approval the exception.
- [legal_risk_playbook.md](references/legal_risk_playbook.md): Risk-tier classification and required research depth for health/financial/minor/biometric-data ideas, plus the Flanking-Mode IP/trademark/passing-off addendum.
- [vertical_deepdive_playbook.md](references/vertical_deepdive_playbook.md): Methodology for Vertical Deep-Dive Mode — the Depth Contract, Component Ledger and upfront Kill Criteria, the 5-tier competitor census and vocabulary sweep, the Pain & Praise Ledger, feature absorption rules, graveyard analysis, bottom-up revenue and COGS modelling, the per-component legal ledger, and the adversarial verdict.
- [flanking_playbook.md](references/flanking_playbook.md): Methodology for Flanking Discovery Mode — the three existing-product patterns, candidate-mining search signals, the Flanking Eligibility Gate, and how to read the 7 Proofs against a real incumbent.
- [domain_games.md](references/domain_games.md): Directives for gaming concepts, including the mechanic rotation gate.
- [domain_saas.md](references/domain_saas.md): Directives for B2B SaaS and developer tools, including the workflow-vertical rotation gate.
- [domain_mobile.md](references/domain_mobile.md): Directives for iOS/Android native app capabilities.
- [report_template.md](references/report_template.md): The Step 5 evaluation report format for Original & Flanking modes.
- [blueprint_template.md](references/blueprint_template.md): Functional blueprint template for approved ideas — scope, functional spec, UI/UX concept and implementation roadmap, deliberately stopping short of technical architecture.
- [competitor_ledger_template.md](references/competitor_ledger_template.md): The Step 6 persistent competitor ledger — classification, critiques and compliments, causes of death and reasons for success.
- [legal_dossier_template.md](references/legal_dossier_template.md): The Step 7 legal & gatekeeper dossier — litigation exposure plus regulators, legislation, closed associations, local bureaucracy, lobbies, NIMBY committees and boycott risk.
