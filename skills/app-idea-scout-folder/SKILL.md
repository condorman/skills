---
name: app-idea-scout
description: Guida un ciclo di ricerca continuo per trovare, aggregare e validare nuove idee di app o giochi da pubblicare su App Store e Google Play. Usa questa skill ogni volta che l'utente cerca idee per una nuova app/gioco, vuole scovare bisogni non soddisfatti degli utenti da forum/community/recensioni, chiede un'analisi della concorrenza per capire se un'idea regge, o vuole valutare la fattibilità di un progetto in base a complessità, rischio legale e tempo disponibile. Attivala anche per richieste come "trovami qualcosa da sviluppare", "che app/gioco potrei fare", "valida questa idea", "cerca nicchie poco sfruttate per app mobile", o quando l'utente ricarica un file di idee generato in precedenza per proseguire il ciclo di ricerca.
---

# App Idea Scout

Una skill per fare da "esploratore" continuo di idee per app e giochi mobile: raccoglie bisogni reali espressi dagli utenti online, li organizza in un file di riferimento persistente, e li filtra per fattibilità confrontandoli con la concorrenza esistente e con i vincoli dichiarati dall'utente (rischio legale accettabile, tempo disponibile).

Il processo è pensato per essere ciclico: ogni volta che viene richiamato produce un nuovo giro di scouting (uno generico + uno di nicchia) e aggiorna lo stesso file, invece di ripartire da zero o disperdere il lavoro in output scollegati tra loro.

## Il ciclo in breve

1. **Contesto** — chi è l'utente, cosa vuole costruire, quali vincoli ha (una tantum, si aggiorna solo se cambia).
2. **Scouting** — raccolta di idee grezze da fonti dove gli utenti reali chiedono/propongono app.
3. **Aggregazione** — le idee finiscono in un unico file Markdown organizzato, senza duplicati.
4. **Validazione** — le idee nuove vengono confrontate con la concorrenza reale e classificate per fattibilità.
5. **Output** — il file aggiornato viene consegnato, con un riepilogo delle idee più promettenti di questo giro.

Le sezioni seguenti descrivono ogni fase. I criteri dettagliati (fonti da interrogare, soglie di rischio legale, come stimare complessità/concorrenza) sono nei file in `references/` — leggili quando arrivi alla fase corrispondente, non serve caricarli tutti subito.

---

## Fase 0 — Recupera il contesto del progetto

Prima di cercare qualsiasi cosa, serve sapere per cosa si sta cercando. Questo contesto va chiesto una sola volta e poi riusato nei cicli successivi, quindi va salvato dentro al file stesso (vedi template in Fase 2), non richiesto ogni volta da capo.

**Controlla prima se esiste già un file precedente.** L'utente lavora ricaricando il file delle idee generato nel ciclo precedente: se in questa conversazione è presente un file tipo `idee-app*.md` (allegato o nella cartella upload), leggilo — contiene già la sezione "Profilo progetto" e l'elenco delle nicchie già esplorate. Usa quei dati e non chiedere di nuovo le stesse cose, a meno che l'utente non dica esplicitamente di volerli cambiare.

Se non c'è nessun file precedente (primo ciclo), chiedi con poche domande dirette (va benissimo usare bottoni/opzioni se il canale lo supporta):

- **Target**: sta cercando idee per un Gioco, un'Applicazione, o è aperto a entrambi?
- **Tolleranza al rischio legale**: Nullo / Medio / Ampio — vedi `references/criteri-fattibilita.md` per cosa distingue queste tre fasce (dati sanitari, pagamenti, contenuti per minori, settori regolamentati, ecc.), così la domanda è concreta e non astratta.
- **Tempo disponibile**: poco tempo (side project nei ritagli) o tanto tempo (progetto principale)?
- **Monetizzazione**: il progetto deve necessariamente prevedere un modello di monetizzazione (abbonamento, pubblicità, acquisti in-app...), oppure va bene anche un'app senza obiettivo di guadagno (portfolio, uso personale, open source)? Cambia sia cosa cercare sia come giudicare la fattibilità: se la monetizzazione è richiesta, un'idea senza un modello di business chiaro pesa meno anche se il bisogno dietro è reale.

Queste risposte sono i filtri che useremo in Fase 3 per separare le idee davvero fattibili per questo utente da quelle solo teoricamente buone.

---

## Fase 1 — Scouting: raccogli bisogni reali

L'obiettivo non è inventare idee, ma **intercettare richieste già espresse da persone reali** — post in cui qualcuno dice esplicitamente "vorrei un'app che...", "non esiste niente che faccia X", recensioni negative che lamentano una funzione mancante, thread pieni di persone con lo stesso problema irrisolto. Questo tipo di segnale vale molto di più di un'idea generata a tavolino, perché c'è già domanda dimostrata.

Consulta `references/canali-ricerca.md` per l'elenco di fonti concrete (forum, subreddit, board di community, dove cercare recensioni utili) distinte per app vs giochi. Ogni ciclo, combina due tipi di scansione:

- **Scansione generica** (2-3 ricerche ampie): batti le fonti generaliste per intercettare richieste recenti e trend del momento. Serve a non perdere segnali "caldi" che emergono di continuo.
- **Affondo di nicchia** (una nicchia per ciclo): guarda la sezione "Nicchie già esplorate" nel file esistente e scegline una **non ancora coperta** (es. fitness per anziani, gestione condomini, hobby specifici, verticali B2B di piccole dimensioni...). Scandagliala a fondo: community dedicate, recensioni delle app leader di quella nicchia specifica, forum di settore. Le nicchie strette sono spesso dove si trovano le idee con meno concorrenza.

Per ogni segnale trovato annota: descrizione del bisogno, tipo (gioco/app), nicchia, fonte (URL), e perché qualcuno lo chiede — questo contesto serve dopo per giudicare quanto è reale il bisogno. Scarta i duplicati evidenti rispetto a quanto già presente nel file.

Usa ricerca web reale (non inventare fonti) e rispetta sempre il copyright: riassumi con parole tue quello che trovi nei post/recensioni, non riportarli per intero.

---

## Fase 2 — Aggregazione nel file di riferimento

Tutto confluisce in un unico file Markdown, che è anche lo strumento con cui l'utente ricarica lo stato tra un ciclo e l'altro. Se stai continuando un file esistente, aggiungi righe senza toccare quelle già presenti (a parte lo stato, che si aggiorna in Fase 4). Se è il primo ciclo, crea il file con questa struttura:

```markdown
# Idee App/Gioco — Ricerca continua
*Ultimo aggiornamento: [data]*

## Profilo progetto
- Target: Gioco / Applicazione / Entrambi
- Tolleranza rischio legale: Nullo / Medio / Ampio
- Tempo disponibile: Poco / Tanto
- Monetizzazione richiesta: Sì / No

## Nicchie già esplorate
- [nicchia 1] (ciclo del [data])
- [nicchia 2] (ciclo del [data])

## Idee raccolte

| ID | Idea | Tipo | Nicchia | Fonte | Data | Perché qualcuno la chiede |
|----|------|------|---------|-------|------|---------------------------|
| 001 | ... | App | ... | [link] | ... | ... |

## Analisi di fattibilità

| ID | Complessità | Concorrenza | Rischio legale | Tempo richiesto | Fattibilità | Note |
|----|-------------|-------------|-----------------|------------------|-------------|------|
| 001 | Media | Bassa | Nullo | Poco | ✅ Fattibile | ... |

## ✅ Fattibili — priorità
- **[Idea]** (ID 001): [una riga sul perché]

## 🟡 Da monitorare
- [idee con un asse borderline, da rivalutare al prossimo ciclo]

## ❌ Scartate
- [idee non fattibili, con motivo breve — tenerle evita di riscoprirle da capo]
```

Ogni nuova idea entra prima nella tabella "Idee raccolte" con stato implicito "da validare"; passa alla tabella "Analisi di fattibilità" solo dopo la Fase 3.

---

## Fase 3 — Validazione: concorrenza e fattibilità

Per ogni idea nuova (o segnata "da rivalutare"), fai una ricerca mirata sulla concorrenza reale: cerca su App Store, Google Play e sul web app simili già esistenti, quante sono, quanto sono valutate/popolari, cosa fanno bene e cosa manca loro — è proprio in quel "cosa manca" che si nasconde lo spazio per una nuova idea, anche in mercati affollati.

Poi valuta due assi e assegnali con un giudizio semplice (Bassa/Media/Alta), seguendo i criteri in `references/criteri-fattibilita.md`:

- **Complessità**: quanto lavoro/competenze richiede costruirla.
- **Concorrenza**: quanto è già occupato/saturo quel mercato.

**Caso particolare: concorrenti già esistenti ma deboli.** Se durante la ricerca trovi app concorrenti con poche installazioni, valutazioni basse o sviluppo abbandonato, non trattarle come "mercato già coperto": sono anzi un segnale doppio, perché confermano che il bisogno è reale (qualcuno ci ha già provato) e mostrano esattamente dove ha fallito. In questi casi leggi le loro recensioni negative e annota gli aspetti concreti da migliorare (bug ricorrenti, funzioni mancanti, UX scomoda, prezzo sbagliato, supporto assente, app non più aggiornata...). Questi spunti sono ciò che rende la nuova idea più solida, interessante o innovativa rispetto a chi ci ha già provato — non una nota a margine, ma parte della definizione del progetto. Riportali nella colonna Note della tabella di fattibilità, così restano collegati all'idea anche nei cicli successivi.

Infine confronta l'idea con i vincoli dichiarati dall'utente in Fase 0:

- **Rischio legale**: l'idea tocca categorie che alzano il rischio (dati sanitari, pagamenti, contenuti rivolti a minori, settori regolamentati...)? Se il rischio stimato supera la tolleranza dichiarata, l'idea non è fattibile per questo utente, indipendentemente da quanto sia buona in astratto.
- **Tempo richiesto**: il tempo di sviluppo stimato è compatibile con la disponibilità dichiarata?
- **Monetizzazione** (solo se l'utente l'ha dichiarata come richiesta in Fase 0): l'idea ha un modello di guadagno plausibile (abbonamento, pubblicità, acquisti in-app, versione premium...)? Se sì, tienine conto anche nella complessità e nel rischio legale: integrare pagamenti o abbonamenti aggiunge lavoro tecnico e sposta il rischio legale almeno a Medio (gestione dati di pagamento, termini di servizio, eventuali rimborsi). Se la monetizzazione non è richiesta, ignora questo aspetto: un'idea senza modello di business chiaro resta valida allo stesso modo delle altre. Questo vincolo è anche una lente utile quando analizzi concorrenti deboli (Fase 3): se le loro recensioni negative lamentano proprio il modo in cui monetizzano (paywall aggressivo, feature base bloccate), e l'utente ha bisogno di monetizzare, quello è uno spunto diretto su come impostare un modello di guadagno migliore, non solo su una feature da aggiungere.

Usa questa logica semplice per la fattibilità finale (dettagli e casi limite in `references/criteri-fattibilita.md`):

- **✅ Fattibile**: complessità e concorrenza Bassa/Media, rischio legale entro la soglia dichiarata, tempo richiesto entro la disponibilità dichiarata.
- **🟡 Da monitorare**: un solo asse è borderline (es. concorrenza Alta ma in una nicchia molto specifica, o tempo leggermente sopra soglia) — vale la pena tenerla d'occhio, magari in un ciclo futuro cambia qualcosa (nuova nicchia scoperta, meno concorrenza).
- **❌ Non fattibile**: rischio legale sopra soglia, oppure complessità e concorrenza entrambe Alte, oppure tempo richiesto chiaramente incompatibile.

---

## Fase 4 — Output del ciclo

Aggiorna il file con le nuove righe e i nuovi verdetti, poi riordina le sezioni finali (✅/🟡/❌) mettendo in cima le new entry. Salva il file (nome consigliato: `idee-app-store.md`, o mantieni il nome del file che l'utente ha ricaricato) e condividilo come allegato.

In chat, non limitarti a dire "fatto": presenta un riepilogo breve delle 2-4 idee più promettenti emerse in *questo* ciclo, con una riga sul perché e la fonte del segnale — è quello il valore concreto del giro di ricerca. Ricorda all'utente che per il prossimo ciclo basta ricaricare lo stesso file per continuare da dove ci si è fermati, senza ripetere nicchie già esplorate.
