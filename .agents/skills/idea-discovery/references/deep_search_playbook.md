# Deep Search & Prior-Art Audit Playbook (v5.1)

This playbook provides targeted Google Dorks, automated search helpers, patent registries, demand velocity checks, and non-software status quo tests for the `idea-discovery` skill.

---

## 0. Automated Search Miner Execution

To generate a search payload scoped to the right domain before writing the report, execute:
```bash
python scripts/deep_search_miner.py "<core_mechanic_terms>" <mobile|games|saas|web|ai_tools|all> [--deep-tech]
```
For **Vertical Deep-Dive Mode**, pass `--deepdive` instead — it emits a different matrix entirely (competitor census across 4 tiers, voice-of-customer/churn mining, shutdown & post-mortem signals, pricing reality, EU-first legal surfaces) because a deep-dive is enumerating a whole competitive field rather than checking whether prior art exists:
```bash
python scripts/deep_search_miner.py "<topic>" <domain> --deepdive
```
See `vertical_deepdive_playbook.md` for how each group maps onto the D1-D6 report sections.

Only pass `--deep-tech` when the mechanism is genuinely novel from an engineering standpoint (custom signal processing, novel physics/rendering, an uncalibrated on-device model — see Proof 7 in `evaluation_framework.md`). It adds the Google Patents / arXiv pass, which is disproportionate research overhead for an ordinary CRUD or utility idea.

---

## 1. Mechanics-First Search Protocol

Before searching by topic or branding, **abstract the candidate concept into its core underlying mechanism**:

- **Wrong Search**: `"cat medieval physics game"`
- **Correct Mechanics-First Search**: `"magnetic whip physics game" OR "rotating chain arcade mechanics"`

- **Wrong Search**: `"daily history timeline trivia game"`
- **Correct Mechanics-First Search**: `"chronological event card ordering game" OR "timeline ordering puzzle"`

- **Wrong Search**: `"AI invoicing app for freelancers"`
- **Correct Mechanics-First Search**: `"automated invoice data extraction script" OR "unpaid invoice reminder webhook"`

---

## 2. Vertical-Specific Search Dorks & Registries

### A. Mobile Apps & Store Dorks (Apple App Store & Google Play)
- `site:apps.apple.com "[core mechanics keywords]"`
- `site:play.google.com/store/apps "[core mechanics keywords]"`
- Search App Store review sites: `site:toucharcade.com "[mechanic]"` or `site:pocketgamer.com "[mechanic]"`

### B. Indie Games & PC/Console (Steam & itch.io)
- `site:store.steampowered.com/app "[gameplay loop keywords]"`
- `site:steamdb.info "[game mechanics tags]"`
- `site:itch.io "[physics / arcade loop keywords]"`

### C. Developer & Open-Source Prior Art (GitHub)
- `site:github.com/topics "[core feature keyword]"`
- `site:github.com "is there a tool to" OR "script that automates"`

### D. Micro-SaaS, Extensions & Web Tools
- `site:chromewebstore.google.com "[extension capability]"`
- `site:producthunt.com/posts "[problem statement or workflow tool]"`
- `site:canny.io "in progress" OR "planned" OR "under review" "[requested feature]"`

### E. Patent & Academic Prior Art Audit (Google Patents & arXiv)
*Run this only when the mechanism is genuinely novel from an engineering standpoint (same bar as `--deep-tech` in the miner script and Proof 7's red-flag checklist) — for an ordinary CRUD/utility idea, skip it and say so rather than running it as a formality.* For deep-tech algorithms, hardware integrations, or novel game mechanics/shaders:
- `https://patents.google.com/?q=[core_mechanic_keywords]`
- `site:arxiv.org "[core_algorithm_or_mechanic]"`
- `site:dl.acm.org "SIGGRAPH" "[game_physics_or_rendering_technique]"`

---

## 3. Demand Velocity & Trend Momentum Check

Verify whether search interest and market demand for the problem space is **Exploding**, **Stable**, or **Dead**:
- Search Google Trends / Exploding Topics: `"is search volume for [problem] growing 3-6x year-over-year?"`
- **Pass Threshold**: Must have active growing search queries or active monthly job postings. If search volume is zero and flat for 3+ years, flag as **Dead Market Risk**.

---

## 4. Status Quo Bias & Non-Software Substitute Test

Evaluates whether the candidate app's primary competitor is actually **free human inertia**:
- **Test Query**: *"Can the target user solve this pain point adequately using a free spreadsheet, a pinned WhatsApp message, a paper checklist, or basic email folders?"*
- **Status Quo Verdict**: If the free non-software workaround takes <60 seconds/week and users prefer inertia over paying $15/mo, **REJECT (Status Quo Inertia Failure)**.

---

## 5. Cross-Language & Asian Market Search Queries

Run by default for **Games** — innovative indie mechanics frequently launch first in non-English tech hubs (BOOTH, DLsite). For other domains, only run this pass if the mechanic is the kind that plausibly ships first in an Asian indie/consumer market; for a niche English-language B2B tool, note in the Evidence Log that this pass was skipped as low-yield rather than running it as a formality. Translate core mechanics into target languages:

- **Japanese (BOOTH / DLsite / Twitter)**: 
  - `"物理演算" AND "ゲーム"` (Physics simulation game)
  - `"自動化" AND "ツール"` (Automation tool)
- **Chinese (Bilibili / Xiaohongshu / WeChat Mini Programs)**:
  - `"小程序" AND "[feature description]"` (Mini Program + feature)
  - `"独立游戏" AND "[mechanic description]"` (Indie game + mechanic)

---

## 6. Feature Delta Matrix Template

For every candidate concept evaluated against prior art, construct this exact matrix. Every "Closest Prior Art" cell MUST name the product as a link — `[App/Tool Name](url)` — not a bare description; product names collide often enough (three unrelated apps can all be called some variant of "Job Estimator") that the link is what actually disambiguates them for whoever reads this later:

| Feature / Dimension | Candidate Concept | Closest Prior Art #1 | Closest Prior Art #2 | Innovation Delta / Verdict |
|---|---|---|---|---|
| **Core Mechanics** | [Description] | [App/Tool Name](url) — [Description] | [App/Tool Name](url) — [Description] | 🟢 Novel / 🟡 Reskin |
| **Distribution Channel** | [Zero-CAC Channel] | [App/Tool Name](url) — [Paid Ads / Organic] | [App/Tool Name](url) — [None / Saturated] | 🟢 Advantage / 🔴 Saturated |
| **Tech Enabler ("Why Now?")** | [Recent AI/API] | [App/Tool Name](url) — [Legacy Tech] | [App/Tool Name](url) — [Manual Script] | 🟢 Breakthrough / 🔴 Stale |
| **Monetization & UX** | [Pricing Model] | [App/Tool Name](url) — [Pricing Model] | [App/Tool Name](url) — [Pricing Model] | 🟢 Unique / 🔴 Commodity |

---

## 7. Mandatory Verification Evidence Log

Every prior-art report MUST include a list of verified URLs examined during deep search:

```markdown
#### 3.2 Evidence & Verification Log
- **Searched Dorks/Queries**:
  - `site:store.steampowered.com/app "magnetic whip"`
  - `https://patents.google.com/?q=magnetic+whip+physics`
- **Examined Prior-Art Links**:
  - [Title/App Name](https://example.com/app1) - *Result: Different genre.*
  - [Title/App Name](https://example.com/app2) - *Result: Identical core mechanics (Prior Art Exists).*
```
