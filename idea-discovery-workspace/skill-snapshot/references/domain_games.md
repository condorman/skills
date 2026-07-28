# Gaming Domain Directives & Verification Rules

This reference document contains specialized directives and evaluation criteria for **Game Concepts (Web, Mobile, PC/Console)** analyzed by the `idea-discovery` skill.

---

## 1. Mandatory Game Ideas Directive

- **DO NOT** propose "daily-only" micro-games by default (where the user plays once a day for 2 minutes and cannot play again).
- **ALWAYS PRIORITIZE** games with:
  1. **High Organic Virality**: Mechanics that generate clip-worthy TikTok/Reels/Shorts visuals, satisfying chain reactions, screen-shake combos, or social challenges.
  2. **Multi-Session Replayability**: Endless arcade modes, roguelite progression, physics merge loops, or instant retry mechanics that encourage playing multiple times per day.

---

## 2. Mechanics-First Game Search Dorks

Always abstract the game into its raw physics or logic loop before searching:

- `site:store.steampowered.com/app "[gameplay_loop_keywords]"`
- `site:steamdb.info "[physics_or_mechanic_tag]"`
- `site:itch.io "[arcade_physics_keywords]"`
- `site:toucharcade.com "[mobile_mechanic]"`
- `site:pocketgamer.com "[mobile_mechanic]"`
- `site:booth.pm "物理演算" AND "[mechanic_jp]"` (Japanese indie prototypes)

---

## 3. Gaming Anti-Churn & Retention Checklist

| Game Category | Churn Risk Level | Mitigation Required |
|---|---|---|
| **Daily Wordle Clones** | 🔴 High (Abandonment after week 2) | Must add Endless Mode + Ranked Duels |
| **Physics Arcade / Merge** | 🟢 Low (High daily replayability) | Add Roguelite Upgrade Tree |
| **Puzzle / Card Ordering** | 🟡 Medium (High content depletion) | Add AI Procedural Level/Deck Generation |
