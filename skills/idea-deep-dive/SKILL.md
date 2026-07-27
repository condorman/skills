---
name: idea-deep-dive
description: Approfondisce una singola idea di prodotto digitale prima di scrivere codice. Chiede il canale (sito web, portale web, app mobile o combinazione), poi fa un'analisi di mercato approfondita con ricerca web reale su concorrenti affermati, vincoli legali, tentativi falliti in passato, monetizzabilità e volumi attesi. Solo se l'idea supera tutti i criteri eliminatori conduce un brainstorming con l'utente e produce un file SPEC.md con la definizione completa del progetto, altrimenti si ferma e propone dei pivot. Usala quando l'utente vuole andare in profondità su una singola idea, validarla seriamente, capire se conviene realizzarla, se esistono già concorrenti o vincoli di legge, se il traffico o le installazioni giustificano il lavoro, o quando chiede uno SPEC o un documento di progetto. Attivala dopo la skill app-idea-scout, quando l'utente ricarica il file delle idee e vuole approfondirne una, o dice "questa idea mi piace, analizzala a fondo", "vale la pena farla?", "fammi lo SPEC di questo progetto".
---

# Idea Deep Dive

Questa skill prende **una sola idea** e la porta da "sembra interessante" a "progetto definito e documentato" — oppure la ferma prima che l'utente ci investa tempo.

È il passo successivo di `app-idea-scout`: lo scout produce e filtra molte idee in modo veloce e superficiale, qui invece si scava a fondo su una sola. La differenza di profondità è il punto: lì si fanno stime rapide, qui si cercano prove.

## Principio guida

Il valore di questa skill non è dire di sì. È **evitare che l'utente costruisca qualcosa che non poteva funzionare** — perché il mercato è già presidiato, perché una legge lo impedisce, perché altri ci hanno già sbattuto la testa, perché non ci sarà mai modo di monetizzarlo, o perché il pubblico è troppo piccolo per ripagare i mesi di lavoro.

Quindi: sii onesto e verifica davvero, non compiacente. Un NO-GO documentato dopo un'ora di ricerca vale molto più di uno SPEC entusiasta di un progetto morto. Allo stesso tempo, non bocciare per pigrizia: ogni verdetto negativo deve poggiare su fonti trovate realmente, non su una sensazione.

## Il percorso in cinque fasi

1. **Fase 0 — Idea e canale**: si sceglie l'idea da approfondire e su quale canale si realizza.
2. **Fase 1 — Analisi di mercato approfondita**: ricerca web reale sui cinque criteri eliminatori.
3. **Fase 2 — Cancello GO / NO-GO**: se anche un solo criterio è bloccante ci si ferma e si propongono pivot.
4. **Fase 3 — Brainstorming** (solo se GO): si definisce il progetto insieme all'utente.
5. **Fase 4 — SPEC.md**: si scrive il documento di progetto e lo si consegna.

Le fasi 3 e 4 non si fanno mai prima della 2. Definire funzionalità e stack di un progetto che poi si scopre bloccato è lavoro buttato, e per l'utente è peggio che inutile: crea attaccamento a un'idea che andava lasciata andare.

I dettagli operativi stanno nei file in `references/` — leggi quello della fase in cui ti trovi, non serve caricarli tutti insieme.

---

## Fase 0 — Quale idea, e su quale canale

### Recupera l'idea

Due strade, entrambe valide:

- **Dal file dello scout**: se nella conversazione c'è un file tipo `idee-app-store.md` / `idee-app*.md`, leggilo, mostra all'utente le idee marcate ✅ Fattibile e 🟡 Da monitorare (ID, nome, una riga di sintesi) e chiedi quale vuole approfondire. Riusa quello che il file dice già — profilo progetto (tolleranza legale, tempo disponibile, monetizzazione richiesta), fonti del bisogno, concorrenti deboli già individuati e le loro carenze. Sono materiale prezioso: non ripartire da zero.
- **Da descrizione libera**: se l'utente descrive l'idea a voce, riformulala in due o tre righe e fattela confermare prima di partire. Un fraintendimento qui si propaga su tutta la ricerca. Se mancano il tempo disponibile e la necessità di monetizzare, chiedili ora: servono in Fase 1 e in Fase 2.

### Chiedi il canale — sempre, prima di cercare

Questa domanda va fatta **prima** di qualsiasi ricerca, perché cambia chi sono i concorrenti, dove si cercano, come si stimano i volumi e quanto costa costruire. Usa bottoni/opzioni se il canale di conversazione lo supporta:

- **Sito web** — presenza contenuta: vetrina, landing, tool singolo, blog, portfolio. Poche pagine, poca o nessuna gestione di utenti.
- **Portale web** — piattaforma articolata: articoli, eventi, formazione, registrazione e area riservata per gli utenti finali, promozione di servizi e prodotti, ricerca e filtri, back office redazionale.
- **Applicazione mobile** — app nativa o cross-platform su App Store / Google Play.
- **Combinazione** — più tecnologie insieme (es. portale web + app mobile, o app mobile + backend con pannello web). Chiedi quale combinazione ha in mente e quale pezzo viene per primo: quasi sempre conviene partire da uno solo e aggiungere il resto dopo, e questo va scritto nello SPEC.

Se l'utente non sa scegliere, aiutalo con una domanda concreta: dove sta il momento d'uso? Qualcosa che si consulta seduti al computer o si trova da Google vive sul web; qualcosa che serve in mobilità, con notifiche o sensori, vive su mobile. Non proporre "facciamo tutto" come default: allarga la superficie da validare e da costruire senza aggiungere certezze.

Annota la scelta: da qui in poi ogni verifica si fa **sul canale scelto**.

---

## Fase 1 — Analisi di mercato approfondita

Qui si usa ricerca web reale, con più query e più fonti per ogni punto. Non accontentarti della prima pagina di risultati e non inventare mai fonti: ogni affermazione dello SPEC dovrà poggiare su un link che hai davvero aperto.

Leggi `references/ricerca-mercato.md` per le fonti e le query concrete per ciascun canale, e `references/criteri-ko.md` per le soglie con cui giudicare.

I cinque punti da verificare, tutti obbligatori:

1. **Concorrenti già affermati sul canale scelto.** Chi occupa oggi questo spazio? Se il canale è web, guarda chi domina i risultati di ricerca per le query che userebbe un utente reale; se è mobile, guarda gli store; se è una combinazione, entrambi. Per ognuno raccogli: nome, cosa fa, quanto è forte (posizionamento, download, recensioni, ultimo aggiornamento), e soprattutto **cosa gli manca**.
2. **Blocchi legali e regolatori.** Esiste una legge, un albo professionale, un ente regolatore, un requisito di licenza o autorizzazione, un vincolo su dati o contenuti che rende il lancio difficile o impossibile? Verifica sul contesto normativo che riguarda l'utente (Italia/UE salvo indicazione diversa), non in astratto.
3. **Tentativi passati falliti.** Qualcuno ci ha già provato e ha chiuso? Cerca prodotti dismessi, startup fallite, progetti abbandonati nella stessa nicchia, e soprattutto *perché* si sono fermati: causa legale, mercato inesistente, complessità sottovalutata, target sbagliato, costi di acquisizione insostenibili. È l'informazione più sottovalutata di tutta l'analisi e spesso la più utile.
4. **Monetizzabilità.** Esiste un modo plausibile di guadagnare, e qualcuno in questo mercato lo sta già facendo? Guarda come monetizzano i concorrenti: se nessuno ci riesce, è un segnale. Se l'utente ha dichiarato che la monetizzazione non è richiesta, questo punto resta informativo e non può da solo generare un NO-GO.
5. **Volumi attesi.** Quante persone cercano davvero questa cosa? Stima la dimensione del pubblico raggiungibile con dati osservabili — volumi di ricerca, download dei concorrenti, dimensione delle community di riferimento, numero di soggetti nel target se è un verticale B2B — e confrontala con il tempo di sviluppo stimato. Un progetto da sei mesi per un pubblico da poche centinaia di persone non si ripaga, né in soldi né in soddisfazione.

Per ciascun punto tieni traccia di: cosa hai cercato, cosa hai trovato, i link, e il giudizio che ne ricavi. Servirà tutto nello SPEC, e servirà all'utente per fidarsi (o per contestarti, il che va benissimo).

Rispetta il copyright: riassumi con parole tue quello che leggi in recensioni, articoli e post, non riportarli integralmente.

---

## Fase 2 — Il cancello: GO o NO-GO

Metti insieme i cinque esiti e applica i criteri di `references/criteri-ko.md`. Ogni criterio ha una soglia esplicita che distingue il "difficile ma affrontabile" dal "bloccante".

### Se anche un solo criterio è bloccante → **fermati**

Non proseguire con il brainstorming e non scrivere lo SPEC. Presenta all'utente:

- **Il verdetto e il motivo**, in una frase chiara: quale criterio ha fallito e su quale evidenza.
- **Le prove**: i link e i dati che ti hanno portato lì. L'utente deve poter verificare da sé, anche perché potrebbe sapere qualcosa che tu non hai trovato.
- **Due o tre pivot concreti**: varianti dell'idea che aggirano davvero il blocco. Un pivot buono cambia ciò che *ha causato* il NO-GO, non il nome del prodotto. Esempi del tipo di mossa: restringere il target a una nicchia dove i grandi non arrivano; togliere la funzione che fa scattare l'obbligo di licenza e diventare strumento di supporto anziché fornitore del servizio regolamentato; spostare il canale (un'app in un mercato mobile saturo può essere un tool web che intercetta ricerche scoperte); cambiare chi paga (da consumatore finale a professionista che ci lavora); attaccare esattamente il punto in cui il tentativo passato è fallito, se sai come evitarlo.
- **La domanda finale**: vuole approfondirne uno? In caso affermativo si riparte dalla Fase 0 con l'idea riformulata — il canale può essere cambiato dal pivot, quindi va richiesto.

Chiedi all'utente se vuole comunque un file di sintesi del NO-GO: se sì, salvalo come `ANALISI-<nome-idea>.md` con l'analisi e i pivot, non come `SPEC.md` — quel nome è riservato a un progetto che si fa davvero.

### Se nessun criterio è bloccante → **GO**, e si prosegue

Prima di passare oltre, riassumi in chat in modo compatto: cosa hai verificato, cosa hai trovato di rilevante, dove sta lo spazio libero e quali sono i rischi che restano (perché GO non significa "nessun rischio", significa "nessun blocco"). Poi chiedi conferma esplicita all'utente prima di iniziare il brainstorming. È un momento di decisione, non un passaggio automatico.

---

## Fase 3 — Brainstorming del progetto

Solo dopo un GO confermato. Qui si passa dall'analisi alla costruzione: l'obiettivo è arrivare a un progetto definito con l'utente, non presentargli un progetto già deciso.

Conduci la conversazione a domande brevi, poche per volta, proponendo sempre una tua ipotesi da confermare o correggere — è molto più facile reagire a una proposta concreta che rispondere a "cosa vorresti?". Porta nel brainstorming quello che hai imparato in Fase 1: le lacune dei concorrenti sono la materia prima del differenziale, e gli errori di chi ha fallito sono i vincoli da rispettare.

I temi da coprire:

- **Utente e problema**: chi è precisamente la persona che lo usa e in quale momento della sua giornata.
- **Differenziale**: perché sceglierebbe questo invece del concorrente principale. Se non riesci a scrivere questa frase in modo convincente, il progetto ha un problema che nessuna funzionalità risolverà.
- **Funzionalità dell'MVP**: la lista corta di cosa serve per essere utile alla prima versione, e la lista di cosa si rimanda esplicitamente. Il "non facciamo" vale quanto il "facciamo".
- **Modello di monetizzazione** (se richiesto): come si guadagna, quanto costa, e perché qualcuno pagherebbe.
- **Aspetti tecnici**: stack e architettura coerenti con il canale scelto e con le competenze dell'utente, dati da gestire, integrazioni esterne necessarie, dove gira.
- **Vincoli emersi dall'analisi**: adempimenti privacy/legali da rispettare, requisiti degli store se c'è mobile, accessibilità se c'è un portale pubblico.
- **Tempi**: una stima onesta per l'MVP, da confrontare con il tempo che l'utente ha davvero.

Quando i temi sono coperti, ricapitola il progetto in dieci righe e fattelo confermare. Poi si scrive.

---

## Fase 4 — SPEC.md

Scrivi il file seguendo la struttura in `references/template-spec.md`. Lo SPEC contiene sia l'analisi (che è la giustificazione delle scelte, e va conservata: fra tre mesi l'utente non ricorderà perché aveva escluso una strada) sia la definizione tecnica del progetto.

Due qualità contano più di tutte:

- **Verificabilità**: ogni affermazione di mercato ha la sua fonte con link. Niente numeri senza provenienza.
- **Azionabilità**: il documento deve bastare a chi comincia a costruire — sia esso l'utente o un agente di coding a cui lo passerà. Se una sezione non aiuta a decidere o a implementare qualcosa, non serve.

Salva il file come `SPEC.md` (se ce n'è già uno di un altro progetto, usa `SPEC-<nome-progetto>.md` per non sovrascriverlo) e consegnalo come allegato. In chat non ripetere il contenuto: scrivi due o tre righe su cosa si è deciso e qual è il primo passo concreto per iniziare.

Se l'idea veniva dal file dello scout, ricorda all'utente di annotare lì che l'idea è passata al deep dive, così ai giri successivi non la rivaluta da capo.
