# 🔍 Competitor Ledger: TabSnap AI

**Idea**: Instant On-Device OCR Receipt Splitter & Group Expense Auditor · **Category**: Mobile Utility (iOS & Android)
**Last updated**: 2026-07-29 — Original Discovery
**Coverage**: 5 competitors across Formidable, Beatable Direct, Stagnant, and Open Source · vocabularies searched: `split bill OCR`, `restaurant receipt splitter`, `splitwise alternative`, `group expense ledger` · non-English pass: skipped (English & global App Store focus)

---

## 1. Summary — the shape of the field

The group expense and bill splitting market is currently experiencing high user churn and dissatisfaction due to aggressive monetization shifts by market leader [Splitwise](https://www.splitwise.com) (which introduced a 3-entry daily free limit and a $39.99/year subscription). Most alternatives ([Tricount](https://www.tricount.com), [Spliit](https://spliit.app), [PayBuddies](https://paybuddies.app)) focus on multi-day trip expense logging with manual entry, ignoring the immediate at-the-table restaurant receipt scanning problem. Dedicated receipt splitters like [Tab App](https://tabapp.co) suffer from outdated UI, legacy cloud backend dropouts, and forced account creation. The clear market opening is a zero-login, on-device instant receipt scanner with web/QR sharing and direct payment deep links.

**Price floor observed**: Free open-source web ledger at [Spliit](https://spliit.app) / Free manual logging on [Tricount](https://www.tricount.com) / Paid $39.99/yr floor on [Splitwise Pro](https://www.splitwise.com).

---

## 2. The ledger

| # | Competitor | Class | What it does / positioning | Pricing | Traction & last activity | Overlap | First seen |
|---|---|---|---|---|---|---|---|
| K1 | [Splitwise](https://www.splitwise.com) | 🏰 Formidable | Market leader in group expense tracking & trip IOUs | Free (3 entries/day limit) / $39.99/yr Pro | 4.4★ / 10M+ installs · updated 2026-07 | General expense ledger | 2026-07 Original |
| K2 | [Tab App](https://tabapp.co) | ⚔️ Beatable direct | Line-item receipt splitter for restaurant dining | Free with ads / $2.99 in-app | 3.8★ / 500k+ installs · updated 2024-11 | Direct line-item OCR split | 2026-07 Original |
| K3 | [Tricount](https://www.tricount.com) | 🏰 Formidable | Vacation & roommate expense balance calculator | Free with ads / $4.99/yr Premium | 4.6★ / 5M+ installs · updated 2026-06 | Multi-person balance calculator | 2026-07 Original |
| K4 | [Spliit](https://spliit.app) | 🐙 Open source | Open-source, web-first, account-free trip expense tracker | Free / Self-hostable | Active open-source community · updated 2026-07 | Zero-login balance settlement | 2026-07 Original |
| K5 | [Plates by Splitwise](https://apps.apple.com/app/id1112404094) | 🪦 Abandoned | Standalone restaurant bill splitter created by Splitwise | Free (Deprecated) | Delisted / Abandoned · last updated 2019 | Standalone receipt splitter | 2026-07 Original |

---

## 3. Critiques & compliments (voice of customer)

| Competitor | 🔴 / 🟢 | Finding (paraphrased) | Sources | Freq | Severity | Recency | Table stakes / Wedge | Product-specific / Category-inherent |
|---|---|---|---|---|---|---|---|---|
| [K1 Splitwise](https://www.splitwise.com) | 🔴 Pain | 3-expense daily limit on free tier renders app unusable during travel or weekend dining out | [Reddit r/Splitwise](https://www.reddit.com/r/Splitwise/) | High | High | 2026-06 | Wedge | Product-specific |
| [K1 Splitwise](https://www.splitwise.com) | 🟢 Praise | Automatic multi-person debt simplification across months of shared expenses | [App Store](https://apps.apple.com) | High | — | 2026-05 | Table stakes | — |
| [K2 Tab App](https://tabapp.co) | 🔴 Pain | Cloud server fails to process receipt photo in noisy/low-coverage restaurants; slow OCR scanning | [App Store](https://apps.apple.com) | Med | High | 2025-02 | Wedge | Product-specific |
| [K2 Tab App](https://tabapp.co) | 🟢 Praise | Ability for friends at the table to claim individual items from a shared receipt photo | [Play Store](https://play.google.com) | High | — | 2024-10 | Table stakes | — |
| [K3 Tricount](https://www.tricount.com) | 🔴 Pain | Requires manual typing of every single item cost; no receipt camera scan capability | [Reddit r/androidapps](https://www.reddit.com/r/androidapps/) | High | Med | 2026-04 | Wedge | Product-specific |

---

## 4. Causes of death & reasons for success

### 🪦 Why the dead ones died

| Competitor | Died / went quiet | Cause of death | Evidence | Structural or executional? | What it implies for us |
|---|---|---|---|---|---|
| [Plates by Splitwise](https://apps.apple.com/app/id1112404094) | 2019 | Incumbent absorbed standalone app into main subscription app; neglected maintenance | [App Store history](https://apps.apple.com) | Executional | Dedicated single-purpose micro-utilities thrive when main incumbents bloat their core products |

### 🏆 Why the winners win

| Competitor | What it actually wins on | Evidence | Can we match it, absorb it, or avoid competing on it? |
|---|---|---|---|
| [Splitwise](https://www.splitwise.com) | Brand network effect & historical group trip lock-in | [Product Hunt](https://www.producthunt.com) | Avoid competing on multi-month group trip ledgers; attack the instant 10-second restaurant receipt split use case |

---

## 5. Coverage gaps & what to search next

- **Vocabularies searched**: `split bill OCR`, `restaurant receipt scanner app`, `splitwise alternatives`
- **Surfaces not reachable**: Android Play Store private crash analytics
- **Open question for the next session**: Testing local WebRTC vs QR code web-bridge performance for zero-install friend item selection at dinner tables.
