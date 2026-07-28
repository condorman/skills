# Deep Search & Prior-Art Audit Playbook (v3.0)

This playbook provides targeted Google Dorks, automated search helpers, patent registries, demand velocity checks, and non-software status quo tests for the `idea-discovery` skill.

---

## 0. Automated Search Miner Execution

To generate a complete multi-platform search payload before writing the report, execute:
```bash
python scripts/deep_search_miner.py "<core_mechanic_terms>"
```

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
For deep-tech algorithms, hardware integrations, or novel game mechanics/shaders:
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

Innovative micro-apps or indie game mechanics frequently launch first in non-English tech hubs. Translate core mechanics into target languages:

- **Japanese (BOOTH / DLsite / Twitter)**: 
  - `"物理演算" AND "ゲーム"` (Physics simulation game)
  - `"自動化" AND "ツール"` (Automation tool)
- **Chinese (Bilibili / Xiaohongshu / WeChat Mini Programs)**:
  - `"小程序" AND "[feature description]"` (Mini Program + feature)
  - `"独立游戏" AND "[mechanic description]"` (Indie game + mechanic)

---

## 6. Feature Delta Matrix Template

For every candidate concept evaluated against prior art, construct this exact matrix:

| Feature / Dimension | Candidate Concept | Closest Prior Art #1 | Closest Prior Art #2 | Innovation Delta / Verdict |
|---|---|---|---|---|
| **Core Mechanics** | [Description] | [Description] | [Description] | 🟢 Novel / 🟡 Reskin |
| **Distribution Channel** | [Zero-CAC Channel] | [Paid Ads / Organic] | [None / Saturated] | 🟢 Advantage / 🔴 Saturated |
| **Tech Enabler ("Why Now?")** | [Recent AI/API] | [Legacy Tech] | [Manual Script] | 🟢 Breakthrough / 🔴 Stale |
| **Monetization & UX** | [Pricing Model] | [Pricing Model] | [Pricing Model] | 🟢 Unique / 🔴 Commodity |

---

## 7. Mandatory Verification Evidence Log

Every prior-art report MUST include a list of verified URLs examined during deep search:

```markdown
#### 3.2 Evidence & Verification Log
- **Searched Dorks/Queries**:
  - `site:store.steampowered.com/app "magnetic whip"`
  - `https://patents.google.com/?q=magnetic+whip+physics`
- **Examined Prior-Art Links**:
  - [Title/App Name](file:///https://example.com/app1) - *Result: Different genre.*
  - [Title/App Name](file:///https://example.com/app2) - *Result: Identical core mechanics (Prior Art Exists).*
```
