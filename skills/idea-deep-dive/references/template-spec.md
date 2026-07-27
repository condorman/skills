# Struttura di SPEC.md

Usa questa struttura come base. Adattala al progetto — se una sezione non ha contenuto vero, meglio toglierla che riempirla di frasi generiche — ma non saltare l'analisi di mercato e le fonti: sono ciò che distingue questo documento da un elenco di desideri.

Scrivi in modo diretto e verificabile. Numeri con la loro fonte, scelte con la loro motivazione, e una distinzione netta tra ciò che è dimostrato ("i tre concorrenti principali hanno tutti recensioni negative sulla sincronizzazione") e ciò che è ipotesi ("presumiamo che il target preferisca un abbonamento mensile").

Le sezioni sono divise in due blocchi: **A. Analisi** — perché questo progetto ha senso; **B. Progetto** — cosa si costruisce.

---

```markdown
# SPEC — [Nome del progetto]

*Documento generato il [data] · Canale: [Sito web / Portale web / App mobile / Combinazione: ...]*
*Verdetto: ✅ GO*

## In una frase

[Cosa fa il prodotto, per chi, e perché è meglio di come si risolve oggi il problema. Una frase sola: se non ci sta in una frase, il progetto non è ancora a fuoco.]

---

# A. Analisi di mercato

## A1. Idea e origine

- **Idea**: [descrizione in 3-5 righe]
- **Origine del segnale**: [file dello scout con ID, oppure "proposta dall'utente"]
- **Problema che risolve**: [qual è il bisogno reale e chi lo esprime]
- **Come si risolve oggi**: [cosa fanno le persone adesso, in assenza di questo prodotto]

## A2. Canale scelto

[Quale canale e perché. Se è una combinazione: quali componenti, e da quale si parte.]

## A3. Concorrenti

| Concorrente | Canale | Forza | Modello di guadagno | Cosa gli manca | Fonte |
|---|---|---|---|---|---|
| [nome] | Web/Mobile | [download, recensioni, posizionamento, ultimo aggiornamento] | [abbonamento/ads/...] | [lacuna concreta] | [link] |

**Lettura del panorama**: [chi domina davvero, dove resta spazio libero, e su quale lacuna si inserisce questo progetto. Se ci sono concorrenti deboli, cosa insegnano le loro recensioni negative.]

**Esito**: Via libera / Attenzione — [motivo in una riga]

## A4. Vincoli legali e regolatori

- **Attività centrale del prodotto**: [la frase che è stata verificata]
- **Cosa si applica**: [normative, autorizzazioni, obblighi rilevanti, policy delle piattaforme]
- **Cosa non si applica e perché**: [in particolare, se il prodotto è uno strumento per professionisti autorizzati anziché il fornitore del servizio regolamentato, dirlo esplicitamente]
- **Adempimenti da mettere in conto**: [privacy policy, informative, termini d'uso, moderazione, accessibilità, requisiti degli store...]

**Esito**: Via libera / Attenzione — [motivo]

> Nota: questa non è una consulenza legale. Prima del lancio, i punti sopra vanno verificati con un professionista.

## A5. Tentativi precedenti

| Progetto | Cosa faceva | Quando ha chiuso | Perché | La causa esiste ancora? | Fonte |
|---|---|---|---|---|---|
| [nome] | ... | ... | ... | Sì / No / Superabile | [link] |

**Cosa non ripetere**: [gli errori concreti da evitare, che diventano vincoli di progetto]

**Esito**: Via libera / Attenzione — [motivo]

## A6. Monetizzazione

- **Modello proposto**: [abbonamento / acquisto singolo / freemium / pubblicità / commissione / B2B / nessuno, se non richiesta]
- **Come monetizzano i concorrenti**: [cosa mettono dietro il paywall e a che prezzo]
- **Disponibilità a pagare**: [prove trovate: spesa già esistente da spostare, prezzi accettati nel mercato, oppure segnali contrari]
- **Costi variabili per utente**: [servizi esterni a consumo, elaborazione, archiviazione, moderazione — con il conto, se rilevante]

**Esito**: Via libera / Attenzione / Non applicabile — [motivo]

## A7. Volumi attesi

| Segnale | Dato | Fonte |
|---|---|---|
| Volumi di ricerca | ... | [link] |
| Download dei concorrenti | ... | [link] |
| Dimensione delle community | ... | [link] |
| Soggetti nel target (se B2B) | ... | [link] |

- **Pubblico raggiungibile stimato**: [ordine di grandezza, con la frazione realisticamente intercettabile — non il totale del mercato]
- **Tempo di sviluppo dell'MVP**: [stima]
- **Rapporto**: [il pubblico giustifica il tempo? con quale margine?]

**Esito**: Via libera / Attenzione — [motivo]

## A8. Verdetto e rischi residui

**✅ GO** — [sintesi in due righe del perché il progetto passa]

Rischi che restano aperti, da tenere sotto controllo durante lo sviluppo:

- [rischio 1 e come si può mitigare]
- [rischio 2 e come si può mitigare]

---

# B. Definizione del progetto

## B1. Utente e momento d'uso

- **Utente tipo**: [chi è, cosa fa, quale livello di dimestichezza ha]
- **Momento d'uso**: [quando e dove apre il prodotto]
- **Attività principale**: [la cosa che viene a fare, in una frase]

## B2. Proposta di valore e differenziale

[Perché sceglie questo invece del concorrente principale. Deve collegarsi direttamente a una lacuna documentata in A3 — se il differenziale non ha un aggancio nell'analisi, è un'ipotesi e va dichiarata come tale.]

## B3. Funzionalità dell'MVP

| # | Funzionalità | Perché serve alla prima versione |
|---|---|---|
| 1 | ... | ... |

**Esplicitamente fuori dall'MVP** (da valutare dopo): [lista breve. Serve a proteggere la prima versione: ogni voce qui è tempo che non si spende ora.]

## B4. Modello di monetizzazione

[Come si guadagna in pratica: piani, prezzi, cosa è gratuito e cosa no, e perché questa divisione. Se la monetizzazione non è richiesta, scrivere "Non prevista" e il motivo.]

## B5. Architettura e stack

- **Componenti**: [frontend, backend, database, servizi esterni, pannelli di amministrazione]
- **Stack proposto**: [tecnologie, con una riga sul perché — adeguatezza al canale, competenze di chi costruisce, costi di gestione]
- **Dati principali**: [le entità che il sistema gestisce e le relazioni tra loro]
- **Integrazioni esterne**: [servizi terzi necessari, con eventuali costi e limiti]
- **Dove gira**: [hosting, distribuzione sugli store, dominio]

## B6. Requisiti non funzionali

[Solo quelli che contano davvero per questo progetto: prestazioni attese, funzionamento offline, accessibilità, lingue supportate, protezione dei dati, backup, indicizzazione sui motori di ricerca se è un progetto web.]

## B7. Roadmap

| Fase | Cosa si costruisce | Tempo stimato | Risultato osservabile |
|---|---|---|---|
| 1 | ... | ... | ... |

## B8. Criteri di successo

[Come si capirà, dopo il lancio, se sta funzionando: numeri concreti e verificabili, non "avere successo". Es. utenti attivi al mese, tasso di conversione al piano a pagamento, iscritti dopo tre mesi.]

## B9. Prossimo passo

[La prima cosa concreta da fare domani mattina per iniziare.]

---

## Fonti

Elenco completo delle fonti consultate durante l'analisi.

1. [Titolo o descrizione] — [link] — consultato il [data]
```

---

## Note per chi compila

- **La sezione A non è un preambolo.** È la parte che l'utente rileggerà fra tre mesi quando si chiederà perché aveva escluso una strada. Scrivila per quel momento.
- **Il differenziale (B2) deve poggiare su A3.** Se la ragione per cui qualcuno dovrebbe scegliere questo prodotto non compare da nessuna parte nell'analisi dei concorrenti, è un desiderio, non un vantaggio — dichiaralo come ipotesi da verificare.
- **Le stime vanno dichiarate come stime.** Scrivi "stimato" o "ordine di grandezza" quando lo sono. Un documento onesto sulle sue incertezze è più utile di uno che sembra sicuro di tutto.
- **Se una sezione della parte B non è stata discussa nel brainstorming, non inventarla.** Meglio lasciarla con una nota "da definire con l'utente" che riempirla di default plausibili che nessuno ha scelto.
