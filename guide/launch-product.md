# Guida Legale per il Lancio di Prodotti (Siti Web e App Mobile)

Questa guida ha lo scopo di fornire una panoramica chiara e semplificata delle normative e dei documenti legali necessari quando si lancia un nuovo sito web o un'app mobile.

## 1. Documenti Base: Termini d'Uso, Privacy Policy e Cookie Policy

Spesso li vediamo in tutti i siti (es. PsyEventi, LinkedIn). Sono sempre obbligatori?

* **Privacy Policy (Informativa sulla Privacy):** **Sì, è obbligatoria per legge** (es. GDPR in Europa) se raccogli qualsiasi tipo di dato personale (nome, email, indirizzo IP, o anche solo tracciamento per statistiche). Spiega agli utenti quali dati raccogli, perché, come li usi e quali sono i loro diritti.
* **Cookie Policy:** **Sì, è obbligatoria** se utilizzi cookie non strettamente necessari per il funzionamento tecnico del sito (es. cookie di profilazione, marketing, o analytics di terze parti). Devi anche ottenere il consenso esplicito (il classico "banner dei cookie") prima di installarli.
* **Termini d'Uso (o Condizioni Generali):** **Non sono strettamente obbligatori per legge per un sito vetrina**, ma sono **fortemente raccomandati**. Diventano di fatto **obbligatori** se vendi prodotti/servizi (e-commerce, in questo caso si chiamano Condizioni di Vendita) o se gli utenti possono registrarsi e generare contenuti. Regolano il contratto tra te e l'utente, proteggendoti da abusi e limitando la tua responsabilità.

## 2. Documenti Specifici: EECC, Proprietà Intellettuale e Report di Trasparenza

Alcuni siti, come WhatsApp, presentano documenti molto più complessi. Vanno inseriti sempre? **No, dipendono dal tipo di business.**

* **Codice Europeo delle Comunicazioni Elettroniche (EECC):** Si applica solo ai fornitori di servizi di comunicazione elettronica (come app di messaggistica, VoIP, servizi telefonici). Se la tua app non è un sistema di telecomunicazione, non ti serve.
* **Disciplina sulla Proprietà Intellettuale (IP Policy):** È necessaria se la tua piattaforma ospita contenuti creati dagli utenti (User Generated Content) come foto, articoli, recensioni. Serve a stabilire di chi sono i diritti e come gestisci le segnalazioni di violazione del copyright (es. DMCA).
* **Report Normativi e sulla Trasparenza:** Sono richiesti a grandi piattaforme (es. motori di ricerca, grandi social network) ai sensi di normative specifiche come il Digital Services Act (DSA) in Europa, per spiegare come moderano i contenuti e quante richieste governative ricevono. Non servono per app e siti standard appena lanciati.

## 3. Differenze tra Sito Web e App Mobile

C'è differenza tra i testi legali di un SITO e quelli di un'APP? Posso rimandare i testi dell'APP verso il sito?

* **Differenze:** Sì, ci sono. Un'app mobile solitamente ha accesso a funzioni del dispositivo (fotocamera, microfono, GPS, rubrica) che un sito web non ha. La Privacy Policy dell'app deve spiegare chiaramente perché richiede questi permessi. Inoltre, l'app è soggetta ai termini e alle linee guida degli App Store (Apple App Store, Google Play), che hanno requisiti specifici sulla privacy (es. Apple richiede le *Privacy Nutrition Labels*).
* **Rimando al sito web:** **Sì, è una pratica comune e corretta.** Puoi (e spesso devi) inserire nell'app un link che rimanda alla Privacy Policy e ai Termini d'Uso ospitati sul tuo sito web. L'importante è che il testo ospitato sul sito includa esplicitamente le clausole relative al funzionamento dell'app mobile.

## 4. Glossario dei Termini Tecnici

Ecco il significato dei termini che si incontrano spesso:

* **DPA (Data Processing Agreement):** Accordo sul Trattamento dei Dati. È un contratto che firmi con i tuoi fornitori (es. il servizio di hosting, o il software di newsletter) che trattano dati personali per tuo conto, stabilendo come devono proteggerli.
* **DSAR (Data Subject Access Request):** Richiesta di Accesso dell'Interessato. È quando un utente ti scrive per esercitare i suoi diritti previsti dal GDPR (es. "Voglio sapere quali miei dati avete", "Cancellate il mio account e i miei dati").
* **PIA (Privacy Impact Assessment):** Valutazione d'Impatto sulla Privacy. Un'analisi preventiva dei rischi generali per la privacy che si fa prima di lanciare una nuova funzionalità.
* **DPIA (Data Protection Impact Assessment):** Valutazione d'Impatto sulla Protezione dei Dati. È il termine specifico del GDPR (Art. 35). È una procedura *obbligatoria* in Europa quando si progetta un trattamento dati che presenta un "rischio elevato" per le persone (es. tracciamento su larga scala, dati sanitari). È, in pratica, una versione molto più formale e rigorosa della PIA.
* **Privacy Triage:** Un processo iniziale di "smistamento" e valutazione rapida. Quando un team di prodotto vuole lanciare una nuova feature, il team legale fa un *triage* veloce per capire se serve un'analisi approfondita (PIA/DPIA) o se è sicura così com'è.
* **Policy Monitor:** Uno strumento o processo aziendale utilizzato per monitorare costantemente le modifiche alle normative legali esterne o l'applicazione delle policy interne (es. assicurarsi che il codice prodotto rispetti le linee guida sulla privacy).

## 5. Utilizzo dei plugin Claude-for-Legal per il lancio dell'App

Il repository *claude-for-legal* di Anthropics offre strumenti eccellenti per automatizzare e scalare i processi legali del prodotto:

* **Plugin `privacy-legal`:** È estremamente utile per automatizzare il **Privacy Triage** e le **PIA**. Puoi usarlo per analizzare i requisiti della tua app (es. "L'app chiede l'accesso al GPS") e il plugin può suggerirti le clausole necessarie da aggiungere alla tua Privacy Policy o segnalare potenziali rischi di conformità (es. GDPR).
* **Plugin `product-legal`:** Ti aiuta nella revisione generale del prodotto. Può analizzare il flusso della User Experience (UX) dell'app per assicurarsi che, ad esempio, le caselle di spunta (checkbox) per i consensi non siano preselezionate, e aiutarti a redigere la prima bozza dei Termini d'Uso o a rivedere testi per l'interfaccia utente in modo che siano "legalmente solidi".

**Conclusione:** L'utilizzo di questi plugin è **altamente raccomandato** in fase di pianificazione e lancio. Permettono di risparmiare tempo e intercettare problemi macroscopici, aiutandoti a scrivere bozze solide. *Ricorda sempre, però, che l'output di un'IA non sostituisce il parere finale di un consulente legale qualificato.*

## 6. Approccio Guidato: I Prompt per il Lancio dell'App "Talkive"

Invece di eseguire numerosi passaggi manuali, puoi usare l'approccio guidato (orchestrato) di *claude-for-legal*. Copia e incolla questi prompt in sequenza nella chat: l'IA ti farà domande e ti guiderà automaticamente attraverso l'analisi fino alla creazione dei documenti.

### Fase 1: Avvio e Intervista (Cold Start)

**Obiettivo:** Far capire all'IA il contesto della tua app prima di analizzare il codice.

* **Prompt 1 (Intervista iniziale):** *"/product-legal:cold-start-interview Ciao, sto per lanciare la mia app mobile Fammi le domande necessarie per calibrare i rischi legali e di prodotto prima del lancio. vorrie salvare le analisi in docs/privacy/analisi ed i file da pubblicare sul sito in docs/privacy/publish"*

### Fase 2: Revisione del Lancio (Launch Review)

**Obiettivo:** Eseguire la vera e propria revisione legale del codice e del progetto.

* **Prompt 2 (Launch Review):** *"/product-legal:launch-review Ora che hai il contesto, avvia una Full Launch Review del progetto. Analizza i file di configurazione Android/IOS `app-flutter`,  ed i backend`app-firebase` e `app-cloudflare`per dirmi quali permessi chiediamo, quali dati salviamo e quali documenti legali mi mancano."*

### Fase 3: Approfondimento Rischi Specifici (Opzionale)

**Obiettivo:** Se la *Launch Review* trova funzionalità critiche, sarà lei stessa a suggerirti di approfondire.

* **Prompt 3 (Risk Assessment):** *"/product-legal:feature-risk-assessment Come suggerito dalla revisione precedente, facciamo un deep-dive sui rischi della specifica funzionalità che hai segnalato."*

### Fase 4: Stesura Documenti

**Obiettivo:** Generare Privacy Policy e Termini d'Uso basati sull'analisi appena completata.

* **Prompt 4 (Privacy e T&C):** *"/privacy-legal:matter-workspace Basandoti sui rischi e sui dati emersi dalla Launch Review, redigi la Privacy Policy (GDPR compliant) e i Termini d'Uso (inclusi i vincoli per l'Apple App Store sugli User Generated Content) per Talkive."*
