# Legal & Regulatory Risk Playbook

This playbook governs Step 4's Legal & Regulatory Safety Check, Step 7's Legal & Gatekeeper Dossier (`docs/<idea-slug>/legal.md`, template in [legal_dossier_template.md](legal_dossier_template.md)), and Section 6 of the Standardized Evaluation Report. Its purpose is to stop "Legal Risk: Very Low / Zero" from being a default sentence that gets copy-pasted regardless of what the idea actually does.

---

## Why this matters

A calculation/ledger tool that never touches money and never gives advice (like a tip-pool splitter) genuinely does carry very low legal risk — that conclusion is fine when it's earned. The failure mode is applying the same "Very Low, fully compliant" verdict to ideas that touch **health, money movement, minors, biometric data, or professional advice**, where real regulatory exposure exists and a one-line disclaimer does not make it go away. The check MUST be proportionate to the domain, not uniformly optimistic.

---

## Step 1: Classify the idea into a risk tier

Before writing anything, identify which of these the idea touches. An idea can land in multiple tiers.

### 🔴 Elevated-scrutiny domains (require actual research, not boilerplate)

- **Health, mental health, or medical content**: symptom triage, therapy/CBT/exposure exercises, diagnosis-adjacent claims, fitness/injury guidance, pet health triage. Risk surface: FDA/EU "Software as a Medical Device" (SaMD) classification boundaries, health-claim substantiation, App Store / Play Store health-content review policies, liability if the app's guidance contributes to harm (e.g. an exposure-therapy app used without clinical oversight).
- **Money movement or financial advice**: anything that moves, holds, or advises on funds (not just *calculates* a number someone else already decided to pay). Risk surface: money-transmitter licensing, PCI scope, investment-advice regulation.
- **Minors**: any app whose plausible user base includes children. Risk surface: COPPA (US), UK Age Appropriate Design Code, App Store Kids Category requirements.
- **Biometric or sensitive personal data**: voice prints, gait, face, health metrics captured and stored (not just processed transiently on-device). Risk surface: BIPA (Illinois) and similar state biometric privacy laws, GDPR special-category data rules.
- **Professional advice substitutes**: legal, tax, or safety-critical engineering output presented as authoritative (e.g. auto-generated compliance narratives, structural safety assessments). Risk surface: unauthorized practice of law/accounting, professional liability.
- **Insurance/claims-adjacent workflows**: anything that produces documentation used in a legal or insurance dispute.
- **High-consequence physical/industrial safety compliance**: apps that log, certify, or guide inspections/decisions where a wrong call risks physical injury or equipment failure — rigging/lifting hardware, electrical work, structural/load-bearing assessments, food-safety logs, fall protection, confined-space or lockout-tagout checklists. Risk surface: OSHA/ASME/NFPA/local building-code standards, and liability if the app's output (a "pass" on an inspection, a calculated safe-load figure) turns out wrong. This is distinct from Proof 4's accuracy question — it's about who bears responsibility when a *correct-looking but wrong* output leads to a real injury. Mitigation almost always follows the same shape real competitors use: the app is decision-support for a certified/competent person, not a replacement for their judgment or signature.

### 🟢 Standard-scrutiny domains (a concise, evidence-light check is fine)

- Pure calculation/utility tools that don't move money and don't give advice (the app computes a number from inputs the user already controls and configures).
- Productivity/organizational tools operating on data the user already owns.
- Games and entertainment with no data-collection beyond basic analytics.
- Developer tools operating on the user's own code/infrastructure.

---

## Step 2: For 🔴 elevated-scrutiny ideas, do the actual research

Do not write "Very Low / Zero" for an elevated-scrutiny idea without having searched for and cited at least one real, relevant source. Useful starting points:

- `site:fda.gov "software as a medical device" [category]` — check whether the specific function (triage, diagnosis-adjacent scoring, treatment guidance) crosses into regulated SaMD territory, and whether comparable existing apps market themselves as "not intended to diagnose or treat" to stay outside it.
- `"App Store Review Guidelines" health OR medical` and `"Google Play" "medical" policy` — platform-level content policies that can get an app rejected or pulled even if no law is technically broken.
- `[state] biometric privacy law OR BIPA` for anything storing voice/gait/face data.
- Search for how the closest real competitor positions its legal disclaimers (many health-adjacent apps publicly state "not a substitute for professional care" — read how they scope their claims, not just that they have a disclaimer).

Cite what you find the same way prior-art evidence is cited — a real URL and a one-line takeaway, not a generic assertion.

## Step 3: Write the report section proportionate to the tier

- **🟢 Standard tier**: A short paragraph is fine — state plainly why the idea doesn't touch money movement, advice, minors, or sensitive data, and confirm there's no payment/PCI scope.
- **🔴 Elevated tier**: Must include: (a) which specific regulatory/policy surface applies, (b) what the closest real competitors do to stay compliant (scope of their claims, disclaimers, whether they explicitly avoid diagnosis language), (c) a concrete mitigation the *candidate idea* would need to adopt (not a generic "consult a lawyer" line), and (d) an honest risk level — "Low" or "Moderate" are legitimate outcomes here; forcing everything to "Very Low" defeats the purpose of this check. If the research surfaces a real blocker (e.g. the function as described would likely require FDA clearance), that should push the idea toward **PIVOT REQUIRED** or **DISCARDED**, not get papered over in Section 6 while the rest of the report says APPROVED.

---

## Step 4: Second axis — gatekeepers and non-regulatory blockers

The tiers above answer "is this lawful, and who regulates it". They do not answer the question that actually stops locally-anchored and profession-gated products: **who can block this without a court being involved?** Both axes go into `docs/<idea-slug>/legal.md` — see [legal_dossier_template.md](legal_dossier_template.md) for the table and the rules; the short version of the actor list is:

regulators and authorities · government law and current legislation · pending legislation and political instability in the target market · closed associations, professional orders and registries · local bureaucracy, municipal permits and building concessions · trade associations and lobbies · citizen committees and NIMBY opposition · ethical or cultural boycott risk.

Two things about this axis are worth internalizing rather than looking up:

- **Each actor gets read twice** — does it block us, and does it protect an incumbent? The same gate is a wall from outside and a moat from inside, and a gate that can be cleared once at a known cost while staying shut behind us is a Proof 5 finding, not just a risk row.
- **A gate everyone in the category already passed is not a moat**, it's the cost of entry. The strongest gates are the ones attached to a *person* — a licensed professional, a registered member — because they can't be bought quickly, which is why "partner with one insider" is so often the only real go-to-market for a gated segment.

Proportionality applies here too: an idea with no local footprint, no professional gate and no physical presence gets one honest paragraph explaining why the axis is empty. What isn't acceptable is a table of blank cells, which reads as checked when nothing was.

---

## Deep-Dive-Mode Addendum: go per component, and go EU-first

In **Vertical Deep-Dive Mode** this playbook still runs in full — the tier classification above is the entry point — but the granularity changes. Classify the *idea* into a tier here, then run D6 of `vertical_deepdive_playbook.md`, which produces one legal-ledger row **per component** of the Component Ledger.

The reason is practical rather than pedantic: at deep-dive stage the useful output is almost never "this idea is legally risky." It's "component C3 depends on a data source whose ToS forbids automated access, and cutting C3 costs one feature and removes the entire exposure." A whole-idea verdict cannot express that, and so it tends to produce either an over-broad scare or a shrug — neither of which changes what gets built.

D6 also widens the surface list beyond the tiers above (third-party ToS and platform-policy dependency, GDPR specifics per component including LLM sub-processors, EU AI Act transparency duties, EU consumer/subscription rules, content provenance, accessibility). Those additions matter most for EU-based builders and EU-targeted products, so run the jurisdiction order EU/Italy first, then US, unless the target market says otherwise.

---

## Quick self-check before finalizing Section 6

Ask: *if a journalist or a platform reviewer read this idea's one-line pitch, would "health app," "handles money," "for kids," or "records biometric data" be a fair description?* If yes, the elevated-tier research above is mandatory — a confident "Very Low" without it is not a real answer, it's an assumption.

---

## Flanking-Mode Addendum: IP, Trademark & Passing-Off Risk

This is a separate risk axis from the domain tiers above, specific to Flanking Discovery Mode (see `flanking_playbook.md`) — it's about *how* the candidate was built, not what activity it performs.

- **What to check**: does the rebuild reuse the target product's name, a confusingly similar name, its logo or visual identity, its marketing copy, or its source code/proprietary content? Any of these raises real trademark, passing-off, or copyright exposure independent of how different the underlying functionality is.
- **What's fine**: building a functionally superior alternative with its own name and identity, inspired by proven demand for the category the target product serves. "A better X" as a positioning statement in your own head is fine; "X 2.0" or a lookalike name/logo in the actual product is not.
- **Section 6 for Flanking-Mode ideas** must state explicitly that the candidate's name/branding/assets were checked against the target product and found distinct — not just silence on the topic. If the candidate's current working name is derivative of the target's, flag it and recommend a genuinely distinct one before this goes further, the same way an elevated legal-risk finding elsewhere pushes toward PIVOT REQUIRED rather than getting silently absorbed into an APPROVED verdict.
