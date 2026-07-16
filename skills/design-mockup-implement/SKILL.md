---
name: design-mockup-implement
description: Use when the user asks to implement, build, or align a specific screen/component from the Talkive Claude Design mockup project into the Flutter app, or asks to compare/audit all mockup screens against what's already built. Triggers on phrases like "implementa la schermata X dal design", "porta questo componente dal mockup", "confronta tutti gli screen col design".
---

# Design Mockup → Implementazione Flutter

## Overview

Legge uno o più componenti/schermate dal progetto Claude Design di Talkive
(via tool `DesignSync`, sola lettura) e li implementa nell'app Flutter
locale, oppure confronta tutti gli screen del mockup con quanto già
realizzato e riporta le differenze. Non scrive mai sul progetto Design
(mai `finalize_plan`/`write_files`/`delete_files`/`register_assets`).

Spec di riferimento (contesto, non da rileggere ogni volta):
`docs/superpowers/specs/2026-07-10-design-mockup-implement-skill-design.md`.

## Quando NON usarla

- L'utente vuole pubblicare/sincronizzare componenti locali *verso*
  Claude Design (push) → non è questa skill, e non è nemmeno la skill
  bundled `/design-sync` (quella sincronizza librerie di componenti JS/TS
  verso un progetto design-system, non mockup HTML verso un'app Flutter).
- Nessun riferimento a un mockup/progetto Design nella richiesta → non
  serve questa skill.

## 1. Project ID

1. Controlla la memoria per un projectId Claude Design già salvato
   (oggi: `design_project_id.md`).
2. Se trovato, mostralo all'utente (nome progetto + projectId) e chiedi
   **conferma esplicita** prima di usarlo — non usarlo senza chiederlo,
   anche se sembra ovvio dal contesto.
3. Se assente, o l'utente vuole cambiarlo: usa `DesignSync(list_projects)`
   come aiuto se utile, altrimenti chiedi direttamente il projectId
   all'utente. Una volta ottenuto, salvalo in memoria (tipo `reference`)
   per le richieste successive.

## 2. Lettura mockup

`DesignSync(list_files, projectId)` per ottenere l'elenco dei path
disponibili. Fai fuzzy-match tra il riferimento dell'utente (es.
"Schermata inviti", "Dettaglio invito") e i path/nomi trovati.

## 3. Anteprima + conferma — SEMPRE, senza eccezioni

Per ogni file/frame candidato — **anche con un solo match ad alta
confidenza** — recupera un estratto rilevante via `DesignSync(get_file)`
(titolo/heading/prime righe significative) e mostralo all'utente insieme
al path esatto. **Se possibile, genera e mostra all'utente anche l'immagine/screenshot**
di quanto identificato, oltre al dettaglio testuale. Se ci sono più candidati plausibili (nome ambiguo, più
frame simili, presente sia nel bundle redesign sia nello stato attuale),
mostra tutti gli estratti (e relative immagini, se disponibili) fianco a fianco con `AskUserQuestion` e fai
scegliere quello corretto.

**Non passare mai al punto 4 senza una conferma esplicita dell'utente**
sul riferimento esatto — un match a confidenza singola non è una licenza
per procedere in automatico.

Questo step vale anche in modalità audit (§6), limitatamente ai casi in
cui il matching schermata-mockup ↔ schermata-app sia ambiguo.

## 4. Piano

- **1-2 componenti/schermate**: proponi un piano a fasi direttamente in
  chat, attendi conferma dell'utente, poi implementa. Nessun file spec.
- **Ristrutturazione ampia** (più gruppi di schermate, un intero flusso):
  invoca `superpowers:brainstorming` per validare la direzione, poi
  `superpowers:writing-plans` per il piano dettagliato — spec scritto in
  `docs/superpowers/specs/YYYY-MM-DD-<topic>-design.md`.

In entrambi i casi, il piano deve esplicitamente:

- **Astrarre pattern ripetuti**: se lo stesso componente visivo compare
  su più frame del mockup, proponi di isolarlo come widget condiviso in
  `lib/ui/core/widgets/` invece di duplicarlo per-schermata.
- **Sollevare deviazioni di Design System**: se emergono regole fisse
  (colore/radius/font/spacing ricorrenti) che divergono da
  `docs/DESIGN.md`, chiedi esplicitamente all'utente come procedere —
  non decidere in autonomia (obbligo da `CLAUDE.md`, non derogabile).

## 5. Implementazione

Nell'app Flutter (`app-flutter/`), rispettando l'architettura MVVM a tre
layer (`data/`, `domain/`, `ui/`) — vedi `CLAUDE.md`. Nuovi widget
condivisi in `lib/ui/core/widgets/`; nuovi token/regole di Design System
confermati dall'utente vanno in `docs/DESIGN.md` nello stesso commit.

## 6. Audit comparato (solo su richiesta esplicita)

Itera su tutti gli screen del progetto Design, confrontandoli con le
schermate già implementate nell'app. Applica lo step §3 solo per i
matching ambigui. Riporta le differenze **solo in chat**, schermata per
schermata — nessun file scritto salvo richiesta esplicita dell'utente in
quel momento.

## Quick reference

| Situazione | Azione |
|---|---|
| ProjectId in memoria | Mostra + chiedi conferma esplicita, mai assunto |
| Nessun projectId | Chiedi, poi salva in memoria |
| Riferimento trovato (anche 1 solo match) | Mostra anteprima (path + estratto), attendi conferma |
| Riferimento ambiguo | `AskUserQuestion` con estratti fianco a fianco |
| 1-2 componenti | Piano in chat |
| Ristrutturazione ampia | brainstorming → writing-plans → spec file |
| Pattern ripetuto nel mockup | Proponi widget condiviso in `lib/ui/core/widgets/` |
| Regola DS diverge da `docs/DESIGN.md` | Chiedi esplicitamente, non decidere da solo |
| Audit richiesto | Confronta tutti gli screen, riporta solo in chat |

## Common mistakes

- Procedere all'implementazione senza la conferma esplicita
  dell'anteprima, anche quando il match sembra ovvio.
- Usare `DesignSync` in scrittura (questa skill è sola lettura).
- Decidere da solo un nuovo token/regola di Design System invece di
  chiederlo esplicitamente.
- Scrivere un file di audit quando l'utente non l'ha richiesto.
