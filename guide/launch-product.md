# Guida Legale per il Lancio di Prodotti (Siti Web e App Mobile)

Questa guida ha lo scopo di fornire una panoramica chiara e semplificata delle normative e dei documenti legali necessari quando si lancia un nuovo sito web o un'app mobile.

## 1. Documenti Base: Termini d'Uso, Privacy Policy e Cookie Policy

Spesso li vediamo in tutti i siti (es. PsyEventi, LinkedIn). Sono sempre obbligatori?

*   **Privacy Policy (Informativa sulla Privacy):** **Sì, è obbligatoria per legge** (es. GDPR in Europa) se raccogli qualsiasi tipo di dato personale (nome, email, indirizzo IP, o anche solo tracciamento per statistiche). Spiega agli utenti quali dati raccogli, perché, come li usi e quali sono i loro diritti.
*   **Cookie Policy:** **Sì, è obbligatoria** se utilizzi cookie non strettamente necessari per il funzionamento tecnico del sito (es. cookie di profilazione, marketing, o analytics di terze parti). Devi anche ottenere il consenso esplicito (il classico "banner dei cookie") prima di installarli.
*   **Termini d'Uso (o Condizioni Generali):** **Non sono strettamente obbligatori per legge per un sito vetrina**, ma sono **fortemente raccomandati**. Diventano di fatto **obbligatori** se vendi prodotti/servizi (e-commerce, in questo caso si chiamano Condizioni di Vendita) o se gli utenti possono registrarsi e generare contenuti. Regolano il contratto tra te e l'utente, proteggendoti da abusi e limitando la tua responsabilità.

## 2. Documenti Specifici: EECC, Proprietà Intellettuale e Report di Trasparenza

Alcuni siti, come WhatsApp, presentano documenti molto più complessi. Vanno inseriti sempre? **No, dipendono dal tipo di business.**

*   **Codice Europeo delle Comunicazioni Elettroniche (EECC):** Si applica solo ai fornitori di servizi di comunicazione elettronica (come app di messaggistica, VoIP, servizi telefonici). Se la tua app non è un sistema di telecomunicazione, non ti serve.
*   **Disciplina sulla Proprietà Intellettuale (IP Policy):** È necessaria se la tua piattaforma ospita contenuti creati dagli utenti (User Generated Content) come foto, articoli, recensioni. Serve a stabilire di chi sono i diritti e come gestisci le segnalazioni di violazione del copyright (es. DMCA).
*   **Report Normativi e sulla Trasparenza:** Sono richiesti a grandi piattaforme (es. motori di ricerca, grandi social network) ai sensi di normative specifiche come il Digital Services Act (DSA) in Europa, per spiegare come moderano i contenuti e quante richieste governative ricevono. Non servono per app e siti standard appena lanciati.

## 3. Differenze tra Sito Web e App Mobile

C'è differenza tra i testi legali di un SITO e quelli di un'APP? Posso rimandare i testi dell'APP verso il sito?

*   **Differenze:** Sì, ci sono. Un'app mobile solitamente ha accesso a funzioni del dispositivo (fotocamera, microfono, GPS, rubrica) che un sito web non ha. La Privacy Policy dell'app deve spiegare chiaramente perché richiede questi permessi. Inoltre, l'app è soggetta ai termini e alle linee guida degli App Store (Apple App Store, Google Play), che hanno requisiti specifici sulla privacy (es. Apple richiede le *Privacy Nutrition Labels*).
*   **Rimando al sito web:** **Sì, è una pratica comune e corretta.** Puoi (e spesso devi) inserire nell'app un link che rimanda alla Privacy Policy e ai Termini d'Uso ospitati sul tuo sito web. L'importante è che il testo ospitato sul sito includa esplicitamente le clausole relative al funzionamento dell'app mobile.

## 4. Glossario dei Termini Tecnici

Ecco il significato dei termini che si incontrano spesso:

*   **DPA (Data Processing Agreement):** Accordo sul Trattamento dei Dati. È un contratto che firmi con i tuoi fornitori (es. il servizio di hosting, o il software di newsletter) che trattano dati personali per tuo conto, stabilendo come devono proteggerli.
*   **DSAR (Data Subject Access Request):** Richiesta di Accesso dell'Interessato. È quando un utente ti scrive per esercitare i suoi diritti previsti dal GDPR (es. "Voglio sapere quali miei dati avete", "Cancellate il mio account e i miei dati").
*   **PIA (Privacy Impact Assessment) / DPIA:** Valutazione d'Impatto sulla Privacy. Un'analisi preventiva dei rischi per la privacy che fai prima di lanciare una funzionalità particolarmente "invasiva" o che tratta dati sensibili.
*   **Privacy Triage:** Un processo iniziale di "smistamento" e valutazione rapida. Quando un team di prodotto vuole lanciare una nuova feature, il team legale fa un *triage* veloce per capire se serve un'analisi approfondita (PIA) o se è sicura così com'è.
*   **Policy Monitor:** Uno strumento o processo aziendale utilizzato per monitorare costantemente le modifiche alle normative legali esterne o l'applicazione delle policy interne (es. assicurarsi che il codice prodotto rispetti le linee guida sulla privacy).

## 5. Utilizzo dei plugin Claude-for-Legal per il lancio dell'App

Il repository *claude-for-legal* di Anthropics offre strumenti eccellenti per automatizzare e scalare i processi legali del prodotto:

*   **Plugin `privacy-legal`:** È estremamente utile per automatizzare il **Privacy Triage** e le **PIA**. Puoi usarlo per analizzare i requisiti della tua app (es. "L'app chiede l'accesso al GPS") e il plugin può suggerirti le clausole necessarie da aggiungere alla tua Privacy Policy o segnalare potenziali rischi di conformità (es. GDPR).
*   **Plugin `product-legal`:** Ti aiuta nella revisione generale del prodotto. Può analizzare il flusso della User Experience (UX) dell'app per assicurarsi che, ad esempio, le caselle di spunta (checkbox) per i consensi non siano preselezionate, e aiutarti a redigere la prima bozza dei Termini d'Uso o a rivedere testi per l'interfaccia utente in modo che siano "legalmente solidi".

**Conclusione:** L'utilizzo di questi plugin è **altamente raccomandato** in fase di pianificazione e lancio. Permettono di risparmiare tempo e intercettare problemi macroscopici, aiutandoti a scrivere bozze solide. *Ricorda sempre, però, che l'output di un'IA non sostituisce il parere finale di un consulente legale qualificato.*

## 6. Esempio Pratico: I Prompt da copiare e incollare per l'App "Talkive"

Di seguito i passi da lanciare in sequenza al tuo assistente AI per un progetto monorepo reale come *Talkive*. Copia e incolla queste frasi (prompt) direttamente nella chat. Ogni prompt inizia con il richiamo esplicito alla skill (es. `/privacy-legal:nome-skill`) per assicurarti che venga interpellato il framework corretto:

### Fase 1: Mappatura dei Dati (Privacy Triage)
**Obiettivo:** Estrarre permessi e modelli dati.
*   **Prompt 1 (Permessi):** *"/privacy-legal:use-case-triage Scansiona i file `app-flutter/ios/Runner/Info.plist` e `app-flutter/android/app/src/main/AndroidManifest.xml` del progetto Talkive ed elencami tutti i permessi richiesti dal dispositivo (es. fotocamera, posizione) per fare un Privacy Triage."*
*   **Prompt 2 (Dati salvati):** *"/product-legal:feature-risk-assessment Analizza la cartella `app-firebase` (schemi e regole di sicurezza) e `app-cloudflare`. Dimmi esattamente quali dati degli utenti vengono salvati nel database o nei log, così posso capire i rischi per la privacy."*

### Fase 2: Analisi d'Impatto e Conformità (PIA)
**Obiettivo:** Valutare i rischi dei dati mappati.
*   **Prompt 3 (PIA):** *"/privacy-legal:pia-generation Basandoti sui dati e permessi appena trovati, esegui una Privacy Impact Assessment (PIA). Verifica se la gestione dei dati su Firebase e Cloudflare rispetta il GDPR, indicando se i server sono sicuri e se ci servono consensi espliciti."*

### Fase 3: Redazione dei Documenti Legali
**Obiettivo:** Creare le bozze di Privacy Policy e Termini.
*   **Prompt 4 (Privacy Policy):** *"/privacy-legal:matter-workspace Scrivi l'informativa sulla privacy per l'app Talkive. Assicurati di menzionare esplicitamente tutti i dati che abbiamo trovato, l'uso di Firebase e Cloudflare, e i pacchetti di tracciamento presenti nel `pubspec.yaml`."*
*   **Prompt 5 (Termini d'Uso):** *"/product-legal:cold-start-interview Redigi le Condizioni d'Uso per Talkive. Essendo un'app di messaggistica, inserisci clausole rigide sugli User Generated Content (UGC) per scaricare le responsabilità da noi e definire le regole di ban, come richiesto dall'Apple App Store."*

### Fase 4: Revisione dell'Interfaccia Utente (UX/UI Legal Check)
**Obiettivo:** Controllare che l'interfaccia sia a norma.
*   **Prompt 6 (Controllo UX):** *"/product-legal:launch-review Analizza il codice sorgente nella cartella `app-flutter/lib/features/auth/`. Verifica che le checkbox per accettare la Privacy Policy e i Termini d'Uso non siano pre-selezionate (per rispettare il GDPR) e che ci siano i banner corretti."*

### Fase 5: Preparazione per gli App Store
**Obiettivo:** Compilare i moduli sulla privacy degli store.
*   **Prompt 7 (Nutrition Labels):** *"/product-legal:launch-review Usa i dati che abbiamo mappato per fornirmi le risposte esatte da spuntare nel modulo 'Data Privacy' di App Store Connect (Apple) e Google Play Console, indicando per ogni dato se è legato all'identità dell'utente."*
