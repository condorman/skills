# Functional Blueprint Template

For every idea that receives an **APPROVED (7/7)** rating — or a **GO / GO WITH CUTS** deep-dive verdict — generate `docs/<idea-slug>/blueprint.md` using this structure.

## What this document is, and what it deliberately isn't

This is the **product** definition, not the technical one. The idea has been validated; it hasn't been committed to. Database schemas, endpoint contracts and architecture diagrams written at this point are guesses made before a single real constraint has been met — they get discarded the moment building starts, and in the meantime they make an unbuilt idea feel more decided than it is. The technical layer is worth writing when the idea earns it: when someone starts building.

So this blueprint answers three questions and stops:

- **What does it do?** — functional specification: capabilities, rules, states, edge cases.
- **What does it feel like to use?** — the UI/UX concept: screens, the primary flow, the one interaction that carries the product.
- **In what order does it get built?** — the roadmap, riskiest thing first.

**Do not include**: SQL/DDL, table or collection schemas, API endpoint tables, request/response payloads, architecture or sequence diagrams, infrastructure, hosting, vendor or library choices, auth implementation.

**The one legitimate exception** is a technical fact that changes what the product *is*: it must work offline, the output must be a signable PDF, the capture has to happen in under three seconds or nobody uses it. Those are functional constraints and belong in §2.4 — stated as the constraint, never as the solution to it.

---

```markdown
# 📐 Functional Blueprint: [Idea Name]

**Status**: [APPROVED (7/7) | GO | GO WITH CUTS — deep-dive <date>]
**One-line pitch**: [What it does, for whom, in one sentence someone else could repeat]
**Companion artifacts**: [evaluation](evaluation.md) · [competitors](competitors.md) · [legal](legal.md)

---

## 1. Product Definition & Scope

- **Job-to-be-done**: [The job the user hires this for — a job, not a feature]
- **Primary user**: [Who specifically; if there are two sides, both, and which one is served first]
- **The moment of use**: [When and where it gets opened — the physical/temporal context, because it constrains the whole UX]
- **Success for the user**: [What has to be true after using it for them to come back]
- **Explicitly out of scope for v1**: [3-6 things a reasonable person would expect and won't get, with a one-line why each. If the idea came through a deep-dive, every CUT component belongs here by name]

---

## 2. Functional Specification

### 2.1 Capabilities

One row per capability. Describe behaviour and rules, not implementation.

| # | Capability | What the user can do | Rules & constraints | Priority |
|---|---|---|---|---|
| F1 | [Name] | [Observable behaviour] | [Limits, validations, permissions, what's forbidden] | MVP / v1.1 / Later |

### 2.2 Core user stories

- As a [user], I want to [action], so that [outcome]. **Done when**: [observable acceptance condition]

Cover the primary flow end to end. A story whose "done when" can't be checked by looking at the screen is still a wish, not a spec.

### 2.3 States, transitions & edge cases

- **Empty state**: [what the user sees before any data exists — the most under-specified and most-seen screen in any product]
- **Error & failure states**: [what happens when the input is unusable, the network is gone, the operation half-succeeded]
- **Edge cases that change behaviour**: [the awkward inputs — duplicates, very large or very small values, the offline case, the two-users-at-once case]

### 2.4 Functional constraints

Technical realities that shape what the product is, stated as constraints rather than as solutions: offline capability, response-time ceilings, output formats someone else's process depends on, device/permission requirements, data-retention rules inherited from `legal.md`.

### 2.5 Non-goals & explicit trade-offs

What this product deliberately does worse than a competitor, and why that's the right call. Named here so it doesn't get quietly "fixed" later — this is the wedge from the evaluation, expressed as a design decision.

---

## 3. UI/UX Concept

### 3.1 Screen hierarchy

- **[Screen name]** — purpose in one line; what's on it; the single primary action.
  - [Sub-screen / modal / sheet] — when it appears.

### 3.2 Primary flow (end to end)

Number the steps a first-time user takes from opening the product to their first real outcome, with the screen at each step. Count the taps/clicks to that first outcome and state the number — it's the most honest single measure of whether the concept works, and it's cheap to fix on paper.

### 3.3 The signature interaction

The one moment that makes the product itself rather than a form over a database. Describe it concretely enough to be prototyped: what the user does, what the interface does in response, and what makes it feel fast or satisfying.

### 3.4 Visual direction

- **Tone**: [3-4 adjectives, and what it should *not* look like]
- **Reference points**: [products whose feel is close — as a shorthand for the direction, not to copy]
- **Colour tokens**: Primary `#______`, Surface `#______`, Accent `#______`, Danger `#______`
- **Typography & density**: [display vs. dense-data; whether it's read at arm's length, in a hurry, in the field, in gloves, in sunlight]
- **Accessibility floor**: [contrast, touch target size, text scaling, screen-reader-relevant labelling — cheaper as a constraint now than a retrofit later]

---

## 4. Implementation Roadmap

Ordered by risk, not by convenience: whatever could still kill the product goes first, because building the easy shell first only delays finding out.

| Phase | Goal | Delivers | Riskiest assumption tested |
|---|---|---|---|
| **0 — De-risk** | [The one thing that must work] | [Throwaway prototype / manual test] | [What you find out] |
| **1 — Walking skeleton** | [Primary flow, one path, ugly] | [F1, F2] | |
| **2 — MVP** | [Shippable to the first real users] | [+F3, F4] | |
| **3 — First iteration** | [Post-feedback] | [Deferred capabilities] | |

- **Realistic solo build estimate**: [split honestly — ordinary UI/CRUD work vs. anything novel that needs calibration or research time, per Proof 7]
- **First-users plan**: [how the first 10-20 real users are reached — from the evaluation's Proof 2 channel, named specifically]
- **What would make me stop**: [the observable signal from phase 0-2 that means this doesn't work — decided now, while it's still cheap to believe]
```
