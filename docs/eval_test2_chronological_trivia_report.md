# Evaluation Report: Chronological Event Card Ordering Trivia Game

**Date**: 2026-07-27  
**Skill Version**: `idea-discovery` (v2.0 - Deep Search & Prior-Art Audit Protocol)  
**Target Evaluation**: Test Case 2 (Daily Chronological Trivia / Event Card Ordering Game)

---

### 💡 ChronoCards: Historical & Pop-Culture Timeline Ordering Trivia

**Context Category**: Web & Mobile Game (iOS / Android / WebGL)  
**Novelty Level**: Prior Art Exists / Commodity Mechanics (Identical to *Timeline* board game & *Chronophoto*)

---

#### 1. Core Problem & Latent Friction
- **Discovered Friction**: Trivia enthusiasts love quick brain-teasers, but existing trivia apps (e.g. *Trivia Crack*) are bloatware filled with ads, timer pressures, and multiple-choice questions. Users enjoy ordering events visually, but static web implementations lack rank progression or social multiplayer.
- **Target Audience**: Casual trivia players, history/pop-culture buffs, students, and daily puzzle fans.

---

#### 2. The "Why Now?" Factor (Tech Enabler)
- **Recent Tech Breakthrough**: LLM-augmented historical factual validation pipelines allow real-time generation of custom niche decks (e.g., *"90s Hip-Hop Milestones"*, *"Tech Startup Launches"*, *"Sci-Fi Movie Releases"*) with zero manual card creation costs.
- **Why It Couldn't Be Built Earlier**: Creating thousands of verified event cards with accurate dates and licensed images historically required massive editorial teams.

---

#### 3. Novelty & Prior-Art Verification (4-Pass Search Results)

- **Pass 1 (Mechanics-First Isolation Search)**:
  - *Core Mechanic*: Dragging and inserting a card (event, invention, pop-culture milestone) into a growing chronological timeline of historical cards.
  - *Prior-Art Identified*:
    1. **Timeline (Board Game & App by Asmodee)**: The definitive physical and digital card game where players place event cards in chronological order.
    2. **Chronophoto**: Viral web game where players guess the decade/year of historical photos and arrange them.
    3. **HistoryTimeline / Wikigame**: Numerous web-based trivia apps featuring event sorting.
- **Pass 2 (Direct Keyword & Ecosystem Search)**:
  - App Store / Google Play search for `"timeline trivia"` returns dozens of existing card-sorting trivia apps.
- **Pass 3 (Cross-Language Search)**:
  - Japanese Quiz Sites (`"年表" AND "クイズ"`): Chronological ordering is a staple mechanic on Japanese web quiz portals.
- **Pass 4 (Game Directive & Anti-Churn Audit)**:
  - **FAIL on Pure Daily-Only Concept**: A strict "1 play per day" limit (Wordle format) without infinite replay modes fails the Game Ideas Directive.
- **Originality Verdict**: **Prior Art Exists (High Market Saturation)**. Concept cannot be approved as "Original" in its raw state.

---

##### 3.1 Feature Delta Matrix

| Feature / Dimension | Proposed Daily Chrono Trivia | Timeline (Asmodee) | Chronophoto (Web) | Innovation Delta / Verdict |
|---|---|---|---|---|
| **Core Mechanics** | 5-Card Chronological Sorting | Card Placement in Line | Photo Year Placement | 🔴 **Identical Core Mechanics** |
| **Game Modes** | Daily-Only (2 mins/day) | Full Game Sessions | Web Endless Rounds | 🔴 **High Churn Risk (Daily-Only)** |
| **Deck Generation** | Static Event Database | Physical/Digital Decks | Fixed Photo Database | 🟡 **Minor Tech Delta (AI Decks)** |
| **Social / PvP** | Asynchronous Share | Pass & Play / Multiplayer | Leaderboard | 🟡 **Commodity Social Share** |

---

##### 3.2 Evidence & Verification Audit Log

- **Dorks / Queries Run**:
  - `site:apps.apple.com "timeline trivia" OR "chronological order"`
  - `site:play.google.com "order events history game"`
  - `site:producthunt.com "timeline game"`
- **Verified URLs Examined**:
  - [Timeline Official Game](file:///https://www.asmodee.com/) - *Findings: Established board game IP with identical card-sorting rules.*
  - [Chronophoto Web Game](file:///https://www.chronophoto.app/) - *Findings: Viral web game based on chronological photo ordering.*
  - [WikiTimeline Quiz Apps](file:///https://github.com/topics/timeline-quiz) - *Findings: Open-source repositories implementing identical timeline sorting.*

---

#### 4. Anti-False-Positive 5-Proof Verification Matrix

- **Proof 1 (Willingness to Pay - WTP)**: **PASS**
  - Trivia games monetize well via Ad-Free IAP ($2.99) and Custom Deck Packs ($0.99).
- **Proof 2 (Zero-CAC Organic Distribution)**: **PASS**
  - High organic sharing of score grids (Wordle-style emoji grids: 🟩🟩🟨🟩) on X/Twitter and WhatsApp.
- **Proof 3 (High Frequency & Retention - Anti-Churn)**: **FAIL (if Daily-Only)**
  - **Pitfall**: A "daily-only" 2-minute trivia game causes massive user dropoff after week 2 when users get a question wrong and cannot retry.
  - **Required Fix**: Must add **Multi-Session Replayability** (Infinite Practice, Ranked 1v1 Blitz Duels, Unlimited Category Decks).
- **Proof 4 (AI Technical Reliability >95%)**: **PASS**
  - AI generated dates/events can be programmatically verified against Wikidata/Wikipedia APIs to guarantee 100% historical accuracy.
- **Proof 5 (Micro-Moat Defensibility)**: **FAIL**
  - Low defensibility against generic clones; any developer can build a card-sorting UI in 2 days.
- **Protocol Score**: **3/5 -> PIVOT REQUIRED**

---

#### 5. Solopreneur + AI Feasibility Stack

- **Recommended Tech Stack**: Next.js / Vite + Tailwind + Supabase (Realtime PvP) + Wikidata API
- **AI Automation Scope**: Auto-generation and fact-checking of niche card decks (e.g. Cinema history, Gaming history).
- **Solo Execution Time**: 1 week for Web MVP.

---

#### 6. Legal & Regulatory Safety

- **Legal Risk Level**: Zero (Public domain historical facts; avoid trademarked brand logo usage on cards).

---

#### 7. Monetization Strategy

- **Pricing Model**: Free Daily Puzzle + $3.99/mo Unlimited Deck Pass (Unlocks Custom Niche Decks & Ranked Duels).

---

#### 8. Summary Recommendation & Required Pivot

- **Status**: **PIVOT REQUIRED**
- **Pivot Prescription**:
  1. **Abandon "Daily-Only" Restriction**: Introduce an **Endless Arcade Mode** and **1v1 Real-Time Speed Duels** to pass Proof 3 (Anti-Churn Retention).
  2. **Introduce Micro-Moat (Niche AI Decks)**: Allow users to type *any* topic (e.g. *"History of Nintendo Consoles"*) and auto-generate custom playable timeline decks using AI + Wikipedia.
