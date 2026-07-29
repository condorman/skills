# Competitor Ledger Template

Written at Step 6 of `SKILL.md`, for **every** idea that reaches an evaluation — approved or discarded — as `docs/<idea-slug>/competitors.md`.

## Why it's a file and not a table inside a report

Competitor research is the most expensive thing this skill does and, until now, the least reusable: it survived as cells scattered across a Feature Delta Matrix, a census table and a Pain & Praise Ledger, inside documents written for a different purpose. Three months later the useful question is never "what did the report conclude" but "who else is in this space, which of them are dangerous, and what do their users complain about" — and answering it meant redoing the searches.

Two properties make this file work:

- **It is cumulative.** A deep-dive months later *appends and updates rows*; it never starts a fresh list. A row that turns out to be wrong gets corrected in place with the date; a row that dies gets its status changed, not deleted.
- **It records the dismissals.** A competitor found and correctly ruled out is evidence. A competitor never found is indistinguishable from one that doesn't exist — which is exactly the failure the census exists to prevent.

**Evidence integrity, unchanged**: every row comes from a real tool call made in the session that wrote it. A ledger is read later by someone who will assume it was verified, so an unsourced row here does more damage than an unsourced line in a report.

## Classification — pick one per competitor

The classification is the field the reader acts on, so it has to mean something specific:

| Class | What it means | What it implies |
|---|---|---|
| 🏰 **Formidable incumbent** | Healthy, funded or well-established, actively shipping, owns the category vocabulary | Don't fight head-on; find the segment it doesn't serve, or drop the idea |
| ⚔️ **Beatable direct** | Direct competitor with a real, corroborated weakness (pricing model, missing platform, a pain nobody fixes) | The flanking target — the weakness must be named, not assumed |
| 🧩 **Adjacent / partial** | Solves part of the job, or the same job for a different user | Watch: one roadmap item from absorbing the idea |
| 💤 **Stagnant** | Alive and used, but no meaningful update in a long time | Displaceable — record the last-activity evidence |
| 🪦 **Abandoned / dead** | Delisted, archived, sunset, acquired-and-gutted | Highest-signal row in the file — the cause of death is the point |
| 🛠️ **DIY / status quo** | Spreadsheet, Notion template, Zapier recipe, a prompt people pass around | Usually free and usually the real competitor — this is what Proof 6 fights |
| 🐙 **Open source** | Free, self-hostable, community-maintained | Caps the price ceiling; check whether it's actually maintained |

## The file

```markdown
# 🔍 Competitor Ledger: [Idea Name]

**Idea**: [one-line pitch] · **Category**: [category]
**Last updated**: [YYYY-MM-DD] — [session type: Original / Flanking / Deep-Dive]
**Coverage**: [N competitors] across [tiers/classes covered] · vocabularies searched: [list] · non-English pass: [language, or why skipped]

---

## 1. Summary — the shape of the field

[3-6 sentences: how crowded it is, who dominates and on what, whether there is a free credible tier (the single most important fact in the file), what the category's recurring complaint is, and where the opening is — or that there isn't one.]

**Price floor observed**: [free tier at [X](url) / lowest paid €Y at [Z](url)] — this is what any pricing model has to argue against.

---

## 2. The ledger

| # | Competitor | Class | What it does / positioning | Pricing | Traction & last activity | Overlap | First seen |
|---|---|---|---|---|---|---|---|
| K1 | [Name](url) | 🏰 Formidable | [positioning in one line] | €X/mo | 4.2★ / 1.2k reviews · updated 2026-05 | [components/features] | 2026-07 Original |

*One row per competitor, including the dismissed ones. `First seen` records which session found it, so a later deep-dive can tell what it added.*

---

## 3. Critiques & compliments (voice of customer)

What users actually say, per competitor. This section is the reason the file is worth keeping: it's the raw material for both the wedge and the table stakes.

| Competitor | 🔴 / 🟢 | Finding (paraphrased) | Sources | Freq | Severity | Recency | Table stakes / Wedge | Product-specific / Category-inherent |
|---|---|---|---|---|---|---|---|---|
| [K1](url) | 🔴 Pain | [what breaks, in your words] | [r1](url), [r2](url), [r3](url) | High | High | 2026-03 | Wedge | Product-specific |
| [K1](url) | 🟢 Praise | [what users would refuse to give up] | [r4](url), [r5](url) | High | — | 2026-01 | Table stakes | — |

Rules that make this section trustworthy rather than decorative — the full versions live in `vertical_deepdive_playbook.md` D2, and they apply here even when a discovery-mode session fills only a few rows:

- **Paraphrase, never paste review text.** A one-line restatement plus the link is what the file needs; reproducing users' or vendors' wording is both a copyright problem and dead weight.
- **3+ independent sources before a complaint counts as corroborated.** One vivid review is an anecdote.
- **Separate frequency from severity.** A rare data-loss complaint outranks a frequent complaint about colours.
- **Recency-gate everything.** A 2021 complaint about a feature shipped in 2023 is noise.
- **"Too expensive" is almost never a wedge** on its own — only alongside a structural mismatch (per-seat pricing for solo users, an enterprise floor that excludes the whole segment).
- **Product-specific vs category-inherent is the field that decides verdicts.** Would the complaint disappear if a perfectly-funded team rebuilt the product tomorrow? If no, it's category-inherent and it is evidence against the category, not an opportunity.
- **Praise is not filler.** It's what the MVP has to match to be taken seriously; skipping it produces a differentiated product nobody can actually use.

---

## 4. Causes of death & reasons for success

The two questions worth answering explicitly, because they're what a future session reads this file for.

### 🪦 Why the dead ones died

| Competitor | Died / went quiet | Cause of death | Evidence | Structural or executional? | What it implies for us |
|---|---|---|---|---|---|
| [K7](url) | 2024 | [Demand never existed / CAC > LTV / one-shot use / platform dependency / regulatory / incumbent absorbed it / monetization mismatch / founder abandonment] | [post-mortem](url) | Structural | [which component it threatens] |

**The rule that carries the most weight in the whole file**: if 2+ independent dead competitors share the same *structural* cause of death, that cause belongs to the category, not to their execution. "We'll execute better" is the sentence every one of those founders also wrote. Record it here **and** as a `## Category Red Flags` line in `ideas_log.md`, so future discovery sessions inherit it.

### 🏆 Why the winners win

| Competitor | What it actually wins on | Evidence | Can we match it, absorb it, or avoid competing on it? |
|---|---|---|---|
| [K1](url) | [distribution / integration depth / brand / data moat / price / timing] | [source](url) | [honest answer] |

Winning on distribution rather than product is the common case and the one most often missed — a better product losing to a worse one with a channel is the default outcome, not the exception.

---

## 5. Coverage gaps & what to search next

- **Vocabularies searched**: [list] — **not yet searched**: [list]
- **Surfaces not reachable**: [e.g. G2 reviews behind login] — [what was substituted]
- **Open question for the next session**: [the specific thing that would change the picture]

*Written honestly, this section is what lets a later deep-dive start where this one stopped instead of re-running the same three queries.*
```

## Filling it per mode

- **Original Discovery**: expect a short ledger — the 2 closest prior-art products, plus every niche or product screened out during mining, plus the DIY/status-quo row (which almost always exists and is almost always free). Sections 3 and 4 may be thin; say so in §5 rather than padding them.
- **Flanking Discovery**: the target product is row K1 and gets the fullest treatment — its critiques *are* the displacement thesis, and its praise is the table-stakes list the rebuild has to match.
- **Vertical Deep-Dive**: this file is where D1's census and D2's Pain & Praise Ledger land permanently. The deep-dive report cites it rather than duplicating it; if the two ever disagree, this file is the one that gets corrected.
