# 📐 Functional Blueprint: RentShield AI

**Status**: APPROVED (7/7)  
**One-line pitch**: Room-by-room tenant move-in/out inspection vault with on-device AI defect tagging, SHA-256 cryptographic timestamps, and instant landlord PDF report generation.  
**Companion artifacts**: [evaluation](evaluation.md) · [competitors](competitors.md) · [legal](legal.md)

---

## 1. Product Definition & Scope

- **Job-to-be-done**: Lock in proof of a rental unit's exact physical condition on move-in day so the tenant gets 100% of their security deposit returned at move-out.
- **Primary user**: Apartment renters, university students, roommates, and relocators moving into a new leased home.
- **The moment of use**: Move-in day (first 48 hours after receiving keys) while the apartment is still empty, and move-out day before turning in keys.
- **Success for the user**: Having an unalterable, room-by-room, timestamped PDF report emailed to their landlord on day 1, establishing legal baseline proof of all pre-existing flaws.
- **Explicitly out of scope for v1**:
  - Landlord account login / landlord portal dashboard (app is 100% tenant-controlled).
  - Online rent payment processing or bank linking.
  - Multi-tenant lease dispute litigation management.

---

## 2. Functional Specification

### 2.1 Capabilities

| # | Capability | What the user can do | Rules & constraints | Priority |
|---|---|---|---|---|
| F1 | Room Walkthrough Wizard | Select room template (Kitchen, Bedroom 1, Bathroom, Living Room, Exterior) and capture structured photos | Minimum 2 photos per room required; auto-labels room tags | MVP |
| F2 | On-Device AI Defect Auto-Tagging | Camera auto-detects scratches, stains, wall cracks, and places visual bounding box tags | Tap box to edit description or mark severity (Minor / Major) | MVP |
| F3 | SHA-256 Cryptographic Stamp | Automatically generates SHA-256 cryptographic hash of image data + EXIF timestamp + GPS coordinates | Embedded immutably in image metadata & PDF report footer | MVP |
| F4 | PDF Move-In Report Generator | Generates a clean, professional PDF report with room galleries, damage callouts, tenant signature, and SHA-256 proof block | Compresses PDF for easy email attachment (<5MB) | MVP |
| F5 | Landlord Delivery Verification | Sends PDF copy directly to landlord's email with read receipt tracking | Generates proof-of-delivery certificate for tenant records | MVP |
| F6 | Mid-Lease Damage & Repair Log | Add timestamped entries for mid-lease issues (water leaks, HVAC failures, landlord notices) | Appends to existing property folder | v1.1 |
| F7 | Move-In vs Move-Out Comparative Visual Diff | Side-by-side photo comparison of move-in condition vs move-out condition | Highlights matching camera angles | v1.1 |

### 2.2 Core user stories

- **Story 1 (Move-In Walkthrough)**: As a new tenant, I want to follow a guided 10-minute room-by-room photo checklist, so that I don't miss photographing any hidden appliance or wall defect. **Done when**: All selected rooms have completed photo series and defect notes logged.
- **Story 2 (PDF Generation & Proof)**: As a tenant, I want to export a signed PDF report containing timestamped photos and SHA-256 hashes, so that I can send it to my landlord as undeniable proof. **Done when**: PDF compiles locally and opens in iOS/Android native share sheet.

### 2.3 States, transitions & edge cases

- **Empty state**: Clean dashboard displaying a prominent "Start New Move-In Audit" button with an estimated completion timer ("10 min").
- **Low light / blurry photo edge case**: On-device Vision detector flags low light or blurry capture and prompts user to turn on flash or hold steady.
- **Offline mode**: 100% functional offline. Photos, SHA-256 hashes, and PDF exports generate locally without an active internet connection.

### 2.4 Functional constraints

- **Local-first offline capability**: Must allow full inspection capture and PDF generation in basements or apartments without cellular service.
- **Cryptographic integrity**: Image EXIF timestamp and SHA-256 hash must be generated at moment of capture before local saving.
- **Export size ceiling**: PDF report containing up to 30 photos must stay under 5MB for email attachment compatibility.

---

## 3. UI/UX Concept

### 3.1 Screen hierarchy

- **Home Dashboard** — Active rental property card, move-in status, quick action: "Continue Walkthrough" or "Export PDF".
  - **Room Selector Sheet** — Select room (Kitchen, Living Room, Bathroom, Bedroom, Balcony, Storage).
  - **Camera Inspection View** — Custom camera interface with overlay guides, AI defect auto-detection bounding boxes, and instant note drawer.
  - **PDF Preview & Signature Sheet** — Review compiled room report, sign on screen, and trigger native share sheet / email delivery.

### 3.2 Primary flow (end to end)

1. Open app -> Tap **"Start New Inspection"** (1 tap)
2. Enter property address & lease start date (Form input)
3. Select rooms -> Tap **"Begin Walkthrough"** (2 taps)
4. Snap photos in Kitchen -> AI auto-flags cabinet scratch -> Tap **"Add Note: Pre-existing scratch on cabinet door"** (3 taps)
5. Repeat for Bathroom & Bedroom -> Tap **"Complete Walkthrough"** (1 tap)
6. Sign digital signature pad -> Tap **"Generate Legal PDF"** (2 taps)  
*Total: 9 taps to courtroom-ready PDF report!*

### 3.3 The signature interaction

**The AI Defect Lens**: As the user points the camera at a wall or appliance, subtle real-time yellow bounding boxes appear over surface scuffs, cracks, or discoloration. Tapping a box instantly anchors a defect tag on the photo with auto-generated neutral text (*"Pre-existing scuff mark on lower drywall - 3cm"*), saving typing time while holding the phone.

### 3.4 Visual direction

- **Tone**: Professional, trustworthy, protective, crisp. (Deep navy blue & shield emerald accents).
- **Reference points**: Apple Measure, iOS Files app, TurboTax document scanner.
- **Colour tokens**: Primary `#1E3A8A` (Deep Navy), Surface `#F8FAFC` (Slate White), Accent `#059669` (Shield Emerald), Danger `#DC2626` (Alert Red).
- **Typography & density**: Inter / SF Pro; bold high-contrast text readable in bright apartment sunlight or dim hallways.

---

## 4. Implementation Roadmap

| Phase | Goal | Delivers | Riskiest assumption tested |
|---|---|---|---|
| **0 — De-risk** | Validate on-device SHA-256 hashing + local PDF generation | Standalone React Native proof of concept | Fast local PDF compilation with 20+ images under 5MB |
| **1 — Walking skeleton** | Guided room checklist + custom camera + note logging | F1, F2, F3 | Smooth camera UX & fast AI defect bounding box overlay |
| **2 — MVP** | Digital signature + PDF generator + share sheet | F4, F5 | User completes full 10-min move-in audit & exports PDF |
| **3 — First iteration** | Mid-lease repair log + side-by-side move-out diff | F6, F7 | User retains app for mid-lease issue logging |

- **Realistic solo build estimate**: 5 days total (3 days core app & camera walkthrough flow + 2 days PDF generation & SHA-256 cryptographic hashing).
- **First-users plan**: Launch free move-in checklist PDF landing page targeted at university student Reddit communities (r/college, r/renting) and TikTok move-in tips.
- **What would make me stop**: If user feedback shows renters prefer taking standard unorganized camera roll photos even after losing deposit funds.
