# Legal & Gatekeeper Dossier Template

Written at Step 7 of `SKILL.md`, for **every** idea that reaches an evaluation, as `docs/<idea-slug>/legal.md`. `legal_risk_playbook.md` supplies the risk tiers and the research bar; this file is where the work is written down.

## The two axes, and why the second one exists

**Axis 1 — litigation & regulatory exposure**: could this end up in a dispute, and with whom? Regulators, authorities, IP owners, platform operators, data subjects, users harmed by a wrong output, competitors.

**Axis 2 — gatekeepers and non-regulatory blockers**: who can stop this product without any court being involved? A perfectly legal idea dies just as thoroughly when a professional register won't let non-members near its data, when the municipality that has to grant a permit is uninterested, when a trade association tells its members not to adopt it, or when a neighbourhood committee turns a launch into a local controversy.

Axis 2 is the one routinely skipped, and it is the one that kills locally-anchored, physical-world-adjacent, and profession-gated ideas. A digital product's dependency on a permit office or a closed order is real even when nothing about it is unlawful.

**Every gatekeeper row answers the same two questions**, and this is the part that changes strategy rather than just risk scoring:

- **Does it block us?** — the barrier we have to pass, buy, wait for, or route around.
- **Does it protect an incumbent?** — the same gate, seen from inside. A barrier that keeps everyone out is a wall while you're outside it and a moat once you're through. If a gate can be passed *once*, at a known cost, and it keeps the next ten entrants out, that's a defensibility finding and belongs in Proof 5, not only in a risk list.

## Proportionality

A single-player utility with no local footprint gets a short dossier: a paragraph per axis saying concretely why it doesn't apply, and done. Marking every row "N/A" with no reasoning is not the same thing — that's a copy-pasted "Legal Risk: Very Low" wearing a table. The depth follows the idea: elevated-tier domains (health, money movement, minors, biometric data, professional-advice substitutes, physical-safety compliance) require cited research per `legal_risk_playbook.md`, and any idea touching a place, a profession, or a public process requires Axis 2 to be worked seriously rather than dismissed.

**Jurisdiction order**: EU/Italy first, then US, unless the target market says otherwise.

**This is not legal advice**, and the dossier should say so once, plainly, at the end — it's structured research to decide what to build and what to ask a real lawyer about, and a specialist review is what an elevated-tier finding warrants before launch.

---

```markdown
# ⚖️ Legal & Gatekeeper Dossier: [Idea Name]

**Idea**: [one-line pitch] · **Target market / jurisdictions**: [e.g. Italy → EU]
**Risk tier** (per `legal_risk_playbook.md`): [🟢 Standard / 🔴 Elevated — which domains triggered it]
**Overall exposure**: [Very Low / Low / Moderate / High] · **Blocking findings**: [none / list]
**Last updated**: [YYYY-MM-DD]

---

## 1. Litigation exposure — is there a realistic risk of a dispute?

**Short answer**: [one paragraph — with whom, over what, how likely, and whether it's avoidable by design]

| # | Counterparty | What triggers it | Likelihood | Severity | Avoidable by design? | Source |
|---|---|---|---|---|---|---|
| L1 | [Regulator / platform / IP owner / user / data subject / competitor] | [the specific act: scraping under a ToS, an output relied on for a regulated decision, a name too close to an existing mark] | Low/Med/High | Low/Med/High | [the design change that removes it, or "no"] | [link](url) |

Surfaces worth checking before declaring this section empty — each one is a real dispute someone has already had:

- **Third-party ToS**: does any part of the product ingest, scrape, or automate against someone else's site or API? Read the actual terms. A component depending on prohibited automated access is a structural risk, and frequently what killed a dead competitor.
- **IP & trademark**: name, logo and visual identity checked against existing marks in the target market; content ingested and content generated; whether output could reproduce protected material. In Flanking Mode this check is mandatory against the target product (see `legal_risk_playbook.md`'s Flanking addendum).
- **Liability for output**: if someone relies on what this produces and it's wrong, what's the consequence, and what does the disclaimer actually have to say to be meaningful? Decision-support for a competent professional is the standard shape; "not a substitute for professional judgment" is the standard framing, and it only holds if the product genuinely behaves that way.
- **Data & privacy**: GDPR specifics, not "we'll be compliant" — what personal data each part processes, lawful basis, where it's stored, DPAs needed with sub-processors including the LLM vendor, profiling or automated decision-making, special-category data.
- **Consumer & subscription law (EU/IT)**: right of withdrawal, auto-renewal disclosure, price-change notice, cancellation flow.
- **Platform policy**: App Store / Play / Chrome Web Store / marketplace rules for this specific content type and payment model. A policy breach doesn't need a court to end the product.
- **EU AI Act**: transparency duties for generated content and chatbots; whether any function lands in a higher-risk use (employment, education, credit, biometric categorization).
- **Sector rules**: whatever the tier classification surfaced — SaMD boundaries, money-transmitter licensing, COPPA/age-appropriate design, BIPA and biometric privacy, unauthorized practice of law/accounting, OSHA/ASME/NFPA-style safety standards.

---

## 2. Gatekeepers & non-regulatory blockers

One row per actor that plausibly exists for this idea. Where an actor genuinely doesn't apply, write one line saying why — a reasoned "not applicable" is a finding; a blank cell is a gap.

| Actor | Present here? | Does it block us? | Does it protect an incumbent? | Cost / time to clear | Evidence |
|---|---|---|---|---|---|
| **Regulators & authorities** (sector authority, data protection, consumer, competition) | | | | | [link](url) |
| **Government law & current legislation** (existing rules that define what's permitted) | | | | | |
| **Pending legislation & political instability** (bills in progress, an election that could reverse a rule, a market whose rules move) | | | | | |
| **Closed associations, professional orders & registries** (membership required to practise, to be listed, or to access the data) | | | | | |
| **Local bureaucracy, municipal permits & building concessions** (anything requiring a comune, a licence, an occupancy or works permit) | | | | | |
| **Trade associations & lobbies** (organized incumbents with a stake in the status quo) | | | | | |
| **Citizen committees & NIMBY opposition** (organized local resistance to the physical or social footprint) | | | | | |
| **Ethical or cultural boycott risk** (a use that a community, a press cycle, or a customer base would reject on principle) | | | | | |

For every row marked as blocking, add underneath:

- **The specific dependency**: what exactly must be obtained, from whom, and in what order.
- **The workaround**: the version of the product that doesn't need this gate — usually a narrower scope, a different user on the same job, or a partnership with someone already inside.
- **The moat reading**: if we clear it, does it stay shut behind us? Say so explicitly, and reflect it in Proof 5 rather than leaving it buried here.

### Reading the gates honestly

- **A gate that everyone in the category already passed is not a moat** — it's the cost of entry, and the incumbents have amortized it.
- **A gate that requires a person, not a company** (a licensed professional, a registered member) is the strongest kind: it can't be bought quickly, and it's the reason "partner with one insider" is so often the real go-to-market.
- **Political instability cuts both ways**: a rule about to change can destroy a product built on it *or* create the whole opportunity. Say which, with the date and the source, rather than noting that things are uncertain.
- **Boycott and cultural risk is a launch risk, not a legal one**, and it's the one most likely to be dismissed as unserious. The test is concrete: is there a plausible headline about this product that a reasonable person would find damning? If yes, name it now.

---

## 3. Per-component ledger *(Deep-Dive Mode — see `vertical_deepdive_playbook.md` D6)*

In Deep-Dive Mode the useful output is almost never "this idea is legally risky"; it's "component C3 carries the exposure, and cutting it costs one feature." One row per Component Ledger row.

| Component | Surface | Jurisdiction | Risk | Mitigation | Verdict | Source |
|---|---|---|---|---|---|---|
| C1 | Third-party ToS on automated access | EU/global | 🔴 High | Official API only; drop the scraping path | CUT / MODIFY | [ToS §4](url) |

A 🔴 High row with no viable mitigation is a CUT. On a core component it's a KILL — a legitimate outcome, not something to soften into "an area to monitor".

*(Omit this section entirely outside Deep-Dive Mode rather than leaving an empty table.)*

---

## 4. Verdict & what to do about it

- **Blocking findings**: [what must be resolved before building, or "none"]
- **Design changes adopted as a result**: [the concrete ones — scope cut, data not stored, output reframed as decision-support, a jurisdiction excluded at launch]
- **Defensibility gained** (if any gate protects us once cleared): [what, and how durably — feeds Proof 5]
- **Open questions for a specialist**: [the specific ones worth paying for, phrased as questions]
- **Effect on the idea's status**: [none / PIVOT REQUIRED / DISCARDED — an unmitigable finding changes the verdict, it doesn't get absorbed into an APPROVED report]

*This dossier is structured research, not legal advice. Elevated-tier findings warrant review by a qualified professional in the target jurisdiction before launch.*
```
