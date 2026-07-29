# 📐 Functional Blueprint: FreshKeeper AI

**Status**: APPROVED (7/7) — Original Discovery 2026-07-29
**One-line pitch**: Zero-friction household food expiration tracker that converts supermarket receipts into an auto-expiring pantry inventory with 1-tap anti-waste recipes.
**Companion artifacts**: [evaluation](evaluation.md) · [competitors](competitors.md) · [legal](legal.md)

---

## 1. Product Definition & Scope

- **Job-to-be-done**: Prevent household grocery items from rotting unremembered in the fridge or pantry, saving money and eliminating food waste without requiring tedious manual typing.
- **Primary user**: Household shoppers, meal preppers, and budget-conscious individuals who buy groceries 1-3 times a week.
- **The moment of use**: Opened immediately after unpacking groceries (2-second receipt scan), or at 6:00 PM when deciding what to cook for dinner based on what is expiring soonest.
- **Success for the user**: Throwing away zero expired food items at the end of the month and saving $40–$70 on the monthly grocery budget.
- **Explicitly out of scope for v1**:
  1. Multi-user shared cloud sync across non-family members (kept local/iCloud for MVP).
  2. Complex dietary macro/calorie tracking (handled by fitness apps like MyFitnessPal).
  3. Direct supermarket online delivery cart integration (kept strictly as an inventory & recipe companion).

---

## 2. Functional Specification

### 2.1 Capabilities

| # | Capability | What the user can do | Rules & constraints | Priority |
|---|---|---|---|---|
| F1 | Receipt OCR Ingestion | Snap a photo of a printed paper receipt from major supermarkets | Parses store line items into individual pantry records in <3 seconds | MVP |
| F2 | Smart Shelf-Life Assignment | Auto-assign estimated expiration date based on item storage zone (Fridge, Freezer, Pantry) | Pre-populated from local default database; editable in 1 tap | MVP |
| F3 | Visual Expiration Timeline | View color-coded inventory sorted by urgency (Red = <48h, Yellow = <5 days, Green = Fresh) | High-contrast visual cards with swipe-to-consume or swipe-to-trash actions | MVP |
| F4 | 1-Tap Zero-Waste Recipe Matcher | Generate 3 instant dinner recipes using items in the Red/Yellow expiration zone | AI prompt prioritizes soonest expiring ingredients first | MVP |
| F5 | Smart Expiration Alerts | Receive localized push notifications when items enter <48h expiration window | Daily notification at customizable user time (e.g. 5:30 PM) | MVP |

### 2.2 Core user stories

- **Story 1 (Grocery Logging)**: As a user unpacking groceries, I want to take a quick photo of my receipt so that all 15 purchased items are added to my pantry with estimated expiration dates in under 5 seconds.
  - *Done when*: Receipt photo is processed and all items appear in the visual pantry list categorized by Fridge/Pantry/Freezer with assigned dates.
- **Story 2 (Dinner Decision)**: As a user wondering what to cook, I want to tap "Use Expiring Items" so that I get 3 recipe ideas combining my milk, mushrooms, and spinach expiring tomorrow.
  - *Done when*: App displays 3 step-by-step recipe cards utilizing at least 2 items expiring within 48 hours.

### 2.3 States, transitions & edge cases

- **Empty state**: Clean graphic illustration of a fresh refrigerator with a prominent "Scan First Receipt" primary button and a "Quick Add Single Item" secondary button.
- **Error & failure states**: If OCR fails due to dark lighting or a crumpled receipt, the app displays a clear prompt: "Receipt unclear. Retake photo or tap to type items manually."
- **Edge cases**: Unrecognized receipt item code (e.g., store internal SKU code) defaults to "General Grocery Item - Pantry (14 days)" with an inline edit prompt.

### 2.4 Functional constraints

- **On-device privacy**: Image OCR processing must execute on-device or via secure API without storing receipt images permanently on public servers.
- **Speed ceiling**: Receipt scan to populated inventory list must complete in <3.0 seconds total on mid-tier smartphone devices.

### 2.5 Non-goals & explicit trade-offs

- **No calorie counting**: Deliberately omits nutrition macro tracking to keep the interface 100% focused on food shelf life and zero-waste savings.

---

## 3. UI/UX Concept

### 3.1 Screen hierarchy

- **Home (Pantry Dashboard)** — Top summary card ("3 items expiring soon - Save $14"), search bar, storage tabs (Fridge | Freezer | Pantry), color-coded item cards.
  - **Scan Receipt Sheet** — Camera viewport with bounding box guide and instant snap trigger.
  - **Item Detail Modal** — Adjust expiration date, change storage zone, or mark as consumed.
- **Zero-Waste Kitchen (Recipes)** — Top banner ("Cooking with 4 items expiring this week"), 3 generated recipe cards with step-by-step instructions.
- **Settings & Analytics** — Monthly savings count ($ saved from zero waste), notification time preference.

### 3.2 Primary flow (end to end)

1. User opens FreshKeeper after returning from the grocery store (Tap 1).
2. Taps floating camera icon "Scan Receipt" (Tap 2).
3. Snaps receipt photo (Tap 3).
4. System processes receipt in 2 seconds; previews 12 auto-parsed items with green/yellow dates.
5. User taps "Confirm & Save to Pantry" (Tap 4). Total time: 6 seconds.

### 3.3 The signature interaction

**The "Save-the-Food" Swipe**: Swiping an expiring item card right plays a satisfying green checkmark haptic sound effect and adds the estimated monetary value of that item to the user's "Monthly Waste Saved" counter ($4.50 saved!).

### 3.4 Visual direction

- **Tone**: Crisp, fresh, eco-friendly, modern, and effortless.
- **Reference points**: Apple Fitness rings, Lifesum, Too Good To Go.
- **Colour tokens**:
  - Primary (Fresh Green): `#10B981`
  - Warning/Expiring Soon (Yellow-Orange): `#F59E0B`
  - Critical/Expire <24h (Coral Red): `#EF4444`
  - Background/Surface (Clean Slate): `#F8FAFC`
- **Typography & density**: Inter font, bold quantitative numbers, spacious card padding readable at arm's length in the kitchen.

---

## 4. Implementation Roadmap

| Phase | Goal | Delivers | Riskiest assumption tested |
|---|---|---|---|
| **0 — De-risk** | Test OCR parsing speed & accuracy | Python/Flutter test script parsing 20 real supermarket receipts | Can Apple Vision / ML Kit parse store receipt lines accurately? |
| **1 — Walking Skeleton** | Basic inventory DB & OCR scan flow | Receipt scanning -> SQLite local pantry list | Local DB persistence & date calculation |
| **2 — MVP** | Full shippable product | Push notifications + AI recipe matcher + freemium subscription | User retention past week 1 |
| **3 — First Iteration** | Community & Family sharing | Family iCloud pantry sync + barcode scanner fallback | Multi-device sync stability |

- **Realistic solo build estimate**: 3 weeks total (2 weeks core app UI + ML Kit OCR pipeline, 1 week AI prompt tuning & notification engine).
- **First-users plan**: Launch on Reddit (`/r/MealPrepSunday`, `/r/ZeroWaste`, `/r/AppIdeas`) with a video showing a 3-second receipt scan saving $40 of food.
- **What would make me stop**: If OCR parsing accuracy on standard European receipts falls below 85% despite prompt tuning.
