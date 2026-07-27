# VitalsPatch AI ⚡

> **Automated Real-Time INP & Core Web Vitals Remediation Agent**  
> *Chrome Extension + Micro-SaaS for Web Agencies, E-Commerce Merchants & Developers*

---

## 🎯 Overview

**VitalsPatch AI** solves one of the biggest web performance headaches introduced by Google: **Interaction to Next Paint (INP)** penalties and **Cumulative Layout Shift (CLS)** flags in Google Search Console.

Instead of requiring developers to spend hours analyzing complex Chrome DevTools performance traces, VitalsPatch AI intercepts long tasks and layout shifts in real-time, identifies the blocking JavaScript execution or missing CSS dimensions, and generates clean, drop-in remediation patches (utilizing modern web standards like `scheduler.yield()`, `requestAnimationFrame`, and `content-visibility`).

---

## 📁 Repository Structure

```
idea1/
├── evaluation_report.md  # Standardized 5-Proof Anti-False-Positive Evaluation Report
├── README.md             # Project Master Blueprint & Architecture
└── ideas_log.md          # Local Memory Log of evaluated ideas
```

---

## 🚀 Key Features

1. **Real-Time INP Interceptor**: Captures user interactions (clicks, keypresses, taps) taking longer than 50ms and maps them to the exact invoker script and DOM node.
2. **Automated `scheduler.yield()` AST Patching**: Generates non-destructive JavaScript wrapper functions to break heavy main-thread work into yieldable micro-tasks.
3. **Visual CLS Layout Shield**: Detects dynamic layout shifts and outputs CSS `contain-intrinsic-size` or explicit `aspect-ratio` rules.
4. **Drop-in `vitalspatch.js` Shim**: Hostable script snippet that applies patches dynamically on live sites without requiring deep source code refactoring.
5. **Agency Audit Export**: Generates white-label PDF/HTML performance audit reports for clients.

---

## 🛠️ Architecture & Tech Stack

- **Extension**: Chrome Extension Manifest V3 (TypeScript, PerformanceObserver API)
- **Web App / Dashboard**: Vite + React + Tailwind CSS
- **Backend / Database**: Supabase (Auth, Postgres, Edge Functions)
- **AI Core**: Gemini 2.0 Flash / Pro API (Structured JSON & AST Patch Generator)
- **CDN Shim**: Cloudflare Workers / Fastly (serving lightweight `vitalspatch.js` bundles)

---

## 📋 MVP Development Roadmap (14-Day Sprint)

- [x] **Day 1-2**: Market discovery, 5-Proof verification, and concept approval.
- [ ] **Day 3-5**: Chrome Extension Manifest V3 prototype with `PerformanceObserver` INP listener.
- [ ] **Day 6-8**: Gemini API integration for generating `scheduler.yield()` & CSS CLS patches.
- [ ] **Day 9-11**: Web App dashboard (Vite + Tailwind) & `vitalspatch.js` CDN generator.
- [ ] **Day 12-14**: Chrome Web Store submission & pSEO landing page launch.

---

## 📄 License & Status

**Status**: APPROVED (5/5 Verification Protocol)  
**Target Market**: Web Agencies, WordPress / Shopify Store Managers, SEO Consultants.
