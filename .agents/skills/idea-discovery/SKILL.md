---
name: idea-discovery
description: Guide the user in discovering, evaluating, and filtering original and unprecedented product or business ideas across Web, Mobile, Services, AI, and Social contexts. Performs deep research using organic search dorks, manual workaround mining, social networks, freelance job boards, and specialized portals; verifies absolute novelty via prior-art checks; evaluates competitor strength and user complaints; verifies single-person + AI feasibility ("Why Now" tech enablers) and zero legal/regulatory barriers; defines monetization strategies; and maintains a memory log of evaluated ideas. Use whenever the user asks for new project ideas, startup concepts, micro-SaaS opportunities, side project validation, or market research for new products, even if they just ask "what should I build next?".
---

# Original Idea Discovery & Evaluation Skill

This skill provides an advanced methodology to discover, research, and evaluate **original, highly innovative, and unprecedented product ideas** (Web, Mobile, Micro-Services, AI Tools, Social/Community Apps). It focuses on uncovering unserved market friction, leveraging fresh "Why Now?" technology enablers, and guaranteeing that every idea can be executed by a **single person using AI** with **zero legal risks**.

---

## Workflow Overview

```
 ┌─────────────────────────────────────────────────────────┐
 │ 0. Memory Check (Verify past logged/discarded ideas)    │
 └────────────────────────────┬────────────────────────────┘
                              │
 ┌────────────────────────────▼────────────────────────────┐
 │ 1. Deep Friction & Workaround Mining                    │
 │    - Search manual workarounds, hacky scripts, complaints│
 │    - Identify "Why Now?" Tech Enablers (New AI/APIs)    │
 └────────────────────────────┬────────────────────────────┘
                              │
 ┌────────────────────────────▼────────────────────────────┐
 │ 2. Prior-Art & Novelty Audit (3-Pass Search)            │
 │    - Prove idea is unprecedented or solve why past failed│
 └────────────────────────────┬────────────────────────────┘
                              │
 ┌────────────────────────────▼────────────────────────────┐
 │ 3. Strict Qualification Filters                         │
 │    - Novelty & Originality Gate                         │
 │    - Solopreneur + AI Feasibility Gate                  │
 │    - Legal & Regulatory Safety Check                    │
 │    - Competitor & Flanking Matrix                       │
 │    - Monetization Formula Validation                    │
 └────────────────────────────┬────────────────────────────┘
                              │
 ┌────────────────────────────▼────────────────────────────┐
 │ 4. Idea Pitch & Detailed Evaluation Report              │
 └────────────────────────────┬────────────────────────────┘
                              │
 ┌────────────────────────────▼────────────────────────────┐
 │ 5. Memory Log Update (Update memory/ideas_log.md)       │
 └─────────────────────────────────────────────────────────┘
```

---

## Step 0: Check Memory Log

1. Read `memory/ideas_log.md` (or the workspace memory file).
2. Check all previously recorded **APPROVED** and **DISCARDED** ideas.
3. **DO NOT** re-propose or re-analyze concepts already marked as DISCARDED unless specifically instructed.

---

## Step 1: Deep Friction & Workaround Mining

Consult `references/sources.md` for specific Google Dorks, queries, and investigation platforms.

Focus discovery on **three pillars**:
1. **Unserved Friction & Hacky Workarounds**: Search for people combining 3+ tools, writing custom scripts, or complaining about spending hours on manual Excel/browser tasks.
2. **Freelance Job Board Pain Points**: Search Upwork/Fiverr job posts for recurring custom automation requests that companies pay $500–$2,000 to solve.
3. **"Why Now?" Technological Enablers**: Identify recent AI model releases (multimodal vision, open-source LLMs, browser agents, real-time voice APIs) that enable a 1-person micro-SaaS to solve a problem that was technically impossible or economically infeasible 6 months ago.

---

## Step 2: Prior-Art & Novelty Verification Protocol

Before declaring an idea "unprecedented", run a **3-pass verification search**:

- **Pass 1: Direct Keyword Search**: Google `"[Core Mechanism] app OR tool OR software"`.
- **Pass 2: Ecosystem & Repo Search**: Search Product Hunt, GitHub, BetaList, and Hacker News Show HN.
- **Pass 3: Failed Predecessor Analysis**:
  - If a similar product existed and died, analyze *why* it failed.
  - If it failed because the tech wasn't ready (e.g., pre-LLM era), but modern AI solves the core bottleneck effortlessly, classify as **Greenlit under "Why Now" Flank Strategy**.
  - If an active identical product already exists with high adoption, classify as **Prior Art Exists** and evaluate under Filter 3 (Competitor Matrix).

---

## Step 3: Strict Qualification Filters

Every proposed idea MUST pass all five qualification gates:

### Filter 1: Novelty & Originality Gate
- **Requirement**: The concept MUST introduce an original solution angle, a novel combination of emerging tech, or target an underserved niche that has no direct, purpose-built software equivalent.
- **Reject if**: It's a generic clone of existing popular software (e.g., "yet another Notion clone" or "yet another basic PDF reader").

### Filter 2: Solopreneur + AI Feasibility Gate ("Why Now?")
- **Requirement**: The entire product lifecycle (MVP development, content generation, maintenance, user support, and ops) MUST be buildable and maintainable by **1 single person using AI tools**.
- **Reject if**: Requires a dedicated sales team, 24/7 human ops, hardware manufacturing, or complex multi-disciplinary teams.

### Filter 3: Zero / Ultra-Low Legal Risk Gate
- **Requirement**: Absolute independence from regulatory boards, licenses, or legal consultations.
- **Reject instantly if**:
  - Medical/health advice or diagnostics (FDA/EMA/HIPAA).
  - Financial trading, banking, investment advice, or crypto custody (SEC/FINRA/MiCA).
  - Gambling, betting, adult content.
  - Aggressive platform scraping with known litigation risks.
  - Professional guild, union, or institutional authorization requirements.

### Filter 4: Competitor Matrix & Flank Strategy
- **Unbeatable Goliath**: Massive network effects or enterprise lock-in -> **DISCARD IMMEDIATELY**.
- **Defeatable / Flankable**: Bloated, expensive, outdated UX, missing AI automation -> **KEEP** & define the **Flank Strategy** using 1–3 star review complaint mining from G2/Capterra/App Stores.

### Filter 5: Clear Monetization Formula
- Must have a direct B2B or B2C payment trigger from day 1 (SaaS subscription, pay-per-use, lifetime deal).
- **Reject if**: Dependent solely on ad impressions or requiring massive viral scale before earning revenue.

---

## Step 4: Standardized Original Idea Evaluation Report

For every validated original idea, present the report in this exact format:

```markdown
### 💡 [Idea Name]: [Short Catchy Tagline]

**Context Category**: [Web | Mobile | Micro-Service | AI Tool | Social/Community]
**Novelty Level**: [Unprecedented / Novel Combination / Unserved Niche Flank]

#### 1. Core Problem & Latent Friction
- **Discovered Friction**: [Manual process, hacky workaround, or recurring job posting found]
- **Target Audience**: [Specific audience willing to pay for automation]

#### 2. The "Why Now?" Factor (Tech Enabler)
- **Recent Tech Breakthrough**: [What AI capability/API makes this possible today]
- **Why It Couldn't Be Built Earlier**: [What bottleneck was eliminated]

#### 3. Novelty & Prior-Art Verification
- **Prior-Art Search Results**: [Findings from 3-pass search]
- **Originality Verdict**: [Confirmed Original / Flanking Existing Competitor]

#### 4. Competitor Analysis & Flank Strategy (If applicable)
- **Existing Alternatives**: [Current clunky/manual alternatives]
- **User Complaint Mining**: [Insights from 1-3 star reviews]
- **Our Flank Angle**: [Why our tool wins]

#### 5. Solopreneur + AI Feasibility Stack
- **Recommended Tech Stack**: [e.g. Next.js / Vite + Tailwind + LLM/Vision API + Supabase]
- **AI Automation Scope**: [What AI handles automatically]
- **Solo Execution Time**: [Estimated time for MVP, e.g. 1-2 weeks]

#### 6. Legal & Regulatory Safety
- **Legal Risk Level**: Very Low / Zero
- **Notes**: Fully compliant, zero licenses required.

#### 7. Monetization Strategy
- **Pricing Model**: [e.g. $19/month or $49 one-time]
- **Value Proposition**: [Clear ROI for buyer]

#### 8. Summary Recommendation
- **Status**: [APPROVED]
```

---

## Step 5: Memory Logging

Update `memory/ideas_log.md` with every analyzed idea (both Approved and Discarded) including the **Novelty Factor** and **Rejection Reason** to prevent redundant research in future sessions.

---

## References

For deep research operators, Google Dorks, and investigation channels:
- [sources.md](file:///Users/alessandromizzoni/Documents/Progetti/skills/.agents/skills/idea-discovery/references/sources.md)
