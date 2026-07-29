# 📐 Functional Blueprint: TabSnap AI

**Status**: APPROVED (7/7) — Original Discovery (2026-07-29)
**One-line pitch**: Instant on-device receipt scanner that splits restaurant bills, tax, and tips among friends in 8 seconds with zero logins or app downloads required for the table.
**Companion artifacts**: [evaluation](evaluation.md) · [competitors](competitors.md) · [legal](legal.md)

---

## 1. Product Definition & Scope

- **Job-to-be-done**: Split a long paper restaurant receipt among a group of 2–12 friends instantly at the end of a meal, calculating exact line items plus proportional tax and tip, and generating instant settlement payment links.
- **Primary user**: The "table host" (the person holding the paper bill or making the primary credit card payment), plus fellow diners who claim their items.
- **The moment of use**: Sitting at a restaurant or bar table when the paper check arrives. The environment is dim, noisy, and fast-paced; speed and zero friction are paramount.
- **Success for the user**: Receipt scanned, items claimed by everyone at the table, tax/tip added proportionally, and payment request QR/links generated in under 15 seconds without any awkward math or arguments.
- **Explicitly out of scope for v1**:
  - Multi-month trip IOU balances (use [Tricount](https://www.tricount.com) or [Spliit](https://spliit.app) for long trips).
  - In-app bank wallet payment processing (payments are deferred to native Venmo/Revolut/PayPal deep links).
  - Web backend cloud storage (all receipt data lives locally on-device).

---

## 2. Functional Specification

### 2.1 Capabilities

| # | Capability | What the user can do | Rules & constraints | Priority |
|---|---|---|---|---|
| F1 | On-Device Receipt Camera Scan | Point camera at receipt; auto-detect text bounding boxes for items and prices | Must execute on-device via VisionKit/MLKit in <300ms offline | MVP |
| F2 | Interactive Item Assignment | Tap parsed items to assign to specific friends (or split 1 item among N people) | Quantities and sub-items must be editable with 1 tap | MVP |
| F3 | Proportional Tax & Tip Splitter | Enter overall tip % or dollar amount; automatically distribute tax/tip based on individual subtotal | Proportional distribution must equal total receipt amount down to the exact cent | MVP |
| F4 | Instant Table QR & Web Bridge | Display a local QR code; friends scan it to view their individual bill summary on their phone browser | Must work zero-login via local QR/WebRTC web bridge without requiring friends to install the app | MVP |
| F5 | Direct Payment Deep Links | Tap "Request Payment" to open Venmo/Revolut/PayPal populated with exact amount and note | Uses standard system URI schemes (`venmo://`, `revolut.me/`) | MVP |

### 2.2 Core user stories

- As a diner at a group dinner, I want to snap a photo of the paper receipt, so that all item names and prices are recognized instantly. **Done when**: Bounding boxes highlight all receipt items and total matches within 2 seconds.
- As the table host, I want to assign items to friends or tag shared starters, so that everyone pays only for what they consumed. **Done when**: Each friend's avatar/color is attached to their items, with tax and tip added proportionally.
- As a friend at the table, I want to scan a QR code on the host's phone, so that I can see what I owe and pay via Revolut/Venmo immediately. **Done when**: Scanning QR opens a clean mobile web summary page with a 1-tap "Pay Host" button.

### 2.3 States, transitions & edge cases

- **Empty state**: Camera view overlay with a receipt outline target guide and "Snap Receipt" button.
- **Error & failure states**: Dim lighting or blurry receipt -> prompt "Turn on Flashlight" or "Tap to enter total manually".
- **Edge cases**: Wrinkled receipts, handwritten receipts, 2 people sharing 1 burger -> allow splitting a single line item 50/50 across 2 or more assignees.

### 2.4 Functional constraints

- **Performance**: OCR scan to interactive line item list must take <500ms on iPhone 12 / Android mid-range devices.
- **Offline operation**: Must function 100% offline in restaurant basements without mobile signal.

---

## 3. UI/UX Concept

### 3.1 Screen hierarchy

- **Receipt Camera Screen** — Live viewfinder, flash toggle, camera shutter button.
  - **OCR Item Review Sheet** — Bounding box list of parsed items & prices; 1-tap edit mode.
- **Table Breakdown Screen** — Visual list of diners (Color avatars); tap items to assign; tip % slider (15%, 18%, 20%, Custom).
- **Settlement Summary Sheet** — Per-person breakdown card; "Show Table QR" and "Send Venmo Link" buttons.

### 3.2 Primary flow (end to end)

1. Open app -> Camera opens immediately (Tap 1: Shutter snap).
2. OCR parses items -> Item breakdown screen appears (Tap 2: Confirm items).
3. Tap items to assign to Diner A, Diner B, Diner C (Taps 3–6: Assign items).
4. Slide tip selector to 18% (Tap 7: Confirm tip).
5. Tap "Show Table QR" -> Friends scan QR to pay (Tap 8: Settle).
**Total taps to settlement: 8 taps in ~10 seconds.**

### 3.3 The signature interaction

**The "Item Flick"**: Tapping an OCR item row smooth-animates a colored avatar pill onto that item line with a subtle tactile haptic vibration, instantly updating that person's total pill at the top of the screen in real-time.

### 3.4 Visual direction

- **Tone**: Fast, sleek, ultra-clean, tactile.
- **Reference points**: Apple Wallet, Flighty, Revolut UI.
- **Colour tokens**: Primary `#10B981` (Emerald Green), Surface `#0F172A` (Dark Slate), Accent `#6366F1` (Indigo), Danger `#EF4444` (Coral Red).
- **Typography & density**: Inter / SF Pro Display; high contrast, large touch targets (minimum 48dp) for easy use in dim restaurant environments.

---

## 4. Implementation Roadmap

| Phase | Goal | Delivers | Riskiest assumption tested |
|---|---|---|---|
| **0 — De-risk** | VisionKit/MLKit local receipt parser | On-device text recognition prototype | Receipt line-item price extraction accuracy in dim lighting |
| **1 — Walking skeleton** | Core scanner + item assigner | F1, F2, F3 | 10-second end-to-end flow with manual tax/tip adjustment |
| **2 — MVP** | Full app + QR web bridge + payment links | +F4, F5 | Zero-install friend QR web view rendering |
| **3 — First iteration** | History log & receipt PDF export | Local SQLite history, receipt export | Multi-currency auto-conversion for international travel |

- **Realistic solo build estimate**: 7 days total (4 days Flutter UI + VisionKit OCR, 2 days QR web-sync bridge, 1 day payment deep links).
- **First-users plan**: Launch on Product Hunt, post demo videos on Reddit (r/Splitwise, r/androidapps, r/AppIdeas), and TikTok/Reels table-scan demos.
- **What would make me stop**: If native VisionKit/MLKit line-item parsing accuracy drops below 90% on standard printed restaurant receipts.
