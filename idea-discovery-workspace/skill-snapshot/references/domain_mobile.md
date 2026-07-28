# Mobile Apps Domain Directives & Category Framework (v5.0)

This reference document contains expanded directives and category frameworks for **Mobile Apps (iOS & Android)** analyzed by the `idea-discovery` skill.

---

## 1. Broad Mobile App Category Spectrum

Mobile apps DO NOT need to rely on hardware sensors (camera, microphone, AR). Discovery MUST actively explore candidate concepts across **7 broad functional categories**:

### A. Strumenti di Calcolo & Simulazione (Niche Calculators & Estimators)
- **Use Cases**: Fast technical calculation tools, contractor job estimate/quote generators, unit economics simulators, solar/HVAC sizing calculators, custom formula tools for micro-professions.
- **Value Prop**: Eliminates complex Excel formulas on mobile; outputs instant client-ready quotes or engineering metrics.

### B. Gestionali & Micro-Productivity (Niche Management Tools & Micro-CRMs)
- **Use Cases**: Solopreneur inventory/stock trackers, client booking & approval portals, field task dispatchers, offline-first job loggers, asset maintenance trackers.
- **Value Prop**: Simple, lightweight alternative to $99/mo enterprise CRMs (HubSpot, Salesforce) tailored for 1-person field businesses.

### C. Tools per Professionisti & B2B Mobile (Professional Field & Office Utilities)
- **Use Cases**: Field audit & safety compliance inspectors, instant contract/proposal builders, micro-invoicing, site report generators, client proof-of-work signers.
- **Value Prop**: Saves 2+ hours per day of evening paperwork for plumbers, electricians, adjusters, and freelancers.

### D. Social, Community & Private Circles (Niche Micro-Communities)
- **Use Cases**: Local hobby/sport matchmaking, accountability circles, private family memory vaults, local micro-event boards, niche challenge groups.
- **Value Prop**: High organic network effects; zero ad spend required when targeting passionate niche subcultures.

### E. Divertimento, Entertainment & Creative Tools
- **Use Cases**: Party & group icebreaker games, interactive fiction, creative audio/visual generators, pass-and-play party arcade games, hobby companion apps.
- **Value Prop**: High viral social media reach and multi-session replayability.

### F. Editoriali, Educational & Content Curation
- **Use Cases**: Daily bite-sized industry digests, interactive decision-tree guides, AI-synthesized micro-learning flashcards, niche exam prep utilities.
- **Value Prop**: Strong daily active habit (DAU) retention.

### G. Hardware & Sensor-Based Apps (Optional)
- **Use Cases**: Camera vision, LiDAR mesh, BLE/UWB proximity, motion tracking, spatial audio processing.

---

## 2. Category Rotation & Anti-Fissazione Gate

- **CHECK `ideas_log.md`**: Inspect the last 3 mobile app entries.
- **STRICT ROTATION RULE**: If 2 recent entries belong to the same category (e.g., Sensor/Audio apps), **DO NOT propose another sensor app**. You MUST choose a concept from Categories A (Calcolo), B (Gestionali), C (Tools Professionisti), D (Social/Community), E (Divertimento), or F (Editoriali).

---

## 3. Mobile App Store Search Dorks

- `site:apps.apple.com "[category_or_job_to_be_done_keywords]"`
- `site:play.google.com/store/apps "[category_keywords]"`
- `site:producthunt.com/posts "[mobile_app_concept]"`
- `site:reddit.com/r/AppIdeas OR site:reddit.com/r/SomebodyMakeThis "[problem_statement]"`
