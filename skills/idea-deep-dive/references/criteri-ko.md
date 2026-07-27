# Criteri eliminatori — soglie per il GO / NO-GO

Questi criteri rendono concreto il cancello della Fase 2. Ognuno distingue tre stati:

- **Via libera** — nessun problema rilevante.
- **Attenzione** — un ostacolo reale, che va scritto nello SPEC come rischio ma non ferma il progetto.
- **Bloccante** — NO-GO.

**Un solo criterio bloccante basta per fermarsi.** Non si compensa: un progetto illegale non diventa legale perché ha zero concorrenti.

**Due o più criteri in "Attenzione" contemporaneamente valgono come bloccante.** Non perché ciascuno sia fatale, ma perché sommati descrivono un progetto che parte in salita su troppi fronti insieme: mercato presidiato *e* monetizzazione incerta significa competere contro chi è già lì senza sapere come ripagarsi il tempo. In questo caso spiega chiaramente all'utente che è la combinazione a fermare, non il singolo punto — è il caso in cui i pivot funzionano meglio, perché basta togliere uno dei due ostacoli.

---

## 1. Concorrenti già affermati

Il giudizio dipende dal canale scelto, perché "essere presidiato" significa cose diverse sul web e sugli store.

**Web (sito o portale)** — guarda chi occupa la prima pagina di Google per le query che userebbe un utente reale:

- *Via libera*: la prima pagina risponde male o solo di lato all'intento; i risultati sono generalisti, datati, o coprono solo una parte del problema.
- *Attenzione*: esistono due o tre siti dedicati e ben fatti, ma nessuno domina l'intera nicchia e restano intenti di ricerca scoperti.
- *Bloccante*: la prima pagina è occupata stabilmente da attori con dominio forte e contenuto ricco e aggiornato, per tutte le query principali. Superarli richiederebbe anni di SEO o un budget pubblicitario che l'utente non ha.

**Mobile** — guarda App Store e Google Play:

- *Via libera*: nessuna app dedicata, oppure solo app con pochi download, voti bassi o abbandonate (ultimo aggiornamento molto vecchio).
- *Attenzione*: esistono competitor validi ma nessuno domina, oppure il mercato generale è affollato mentre la nicchia specifica individuata è scoperta.
- *Bloccante*: una o due app dominano la categoria con centinaia di migliaia di download, valutazioni alte, aggiornamenti frequenti e brand riconosciuto, e non riesci a indicare una lacuna concreta e sfruttabile.

**Combinazione** — vale il canale messo peggio, ma con un'eccezione utile: se un canale è bloccato e l'altro no, non è un NO-GO, è un pivot già pronto. Proponi di partire dal canale libero.

**Nota che vale su tutti i canali** (ed è la stessa logica di `app-idea-scout`): concorrenti *esistenti ma deboli* non sono un blocco, sono la migliore notizia possibile. Confermano che il bisogno esiste e mostrano dove si è rotto. Quando li trovi, leggi le loro recensioni negative e i commenti degli utenti ed estrai gli aspetti concreti mancanti — diventano il differenziale del nuovo progetto e vanno raccolti già qui, non improvvisati in Fase 3.

---

## 2. Blocchi legali e regolatori

Riferimento normativo: Italia e Unione Europea, salvo che l'utente indichi un altro mercato.

- *Via libera*: nessuna attività riservata, nessun dato particolare, nessun settore vigilato. Restano gli adempimenti ordinari (privacy policy, cookie, condizioni d'uso, obblighi fiscali se si vende) — vanno annotati nello SPEC ma non fermano niente.
- *Attenzione*: adempimenti pesanti ma affrontabili da soli — trattamento di dati personali su larga scala, contenuti generati dagli utenti da moderare (con i relativi obblighi europei sui servizi digitali), pagamenti gestiti tramite operatori terzi, requisiti di accessibilità per portali pubblici o di grandi operatori.
- *Bloccante*: l'attività centrale del prodotto richiede un titolo, una licenza o un'autorizzazione che l'utente non ha e non può ottenere in tempi ragionevoli. I casi tipici: professioni protette da albo (consulenza medica, legale, ingegneristica, psicologica erogata direttamente); servizi finanziari, di pagamento o assicurativi; intermediazione creditizia; gioco d'azzardo e scommesse; intermediazione di dati sanitari o dispositivi medici (anche software, quando fornisce diagnosi o terapia); vendita di sostanze o beni soggetti a regime autorizzatorio; trattamento di dati di minori come fulcro del servizio; raccolta di dati da terzi in violazione dei loro termini di servizio o di diritti d'autore.

Distinzione decisiva, da applicare sempre prima di dichiarare un blocco: **fornire il servizio regolamentato è bloccante, dare uno strumento a chi è già autorizzato a fornirlo non lo è.** Un'app che diagnostica è un dispositivo medico; un'app che aiuta un medico ad annotare le visite non lo è. È anche il pivot più efficace su questo criterio.

Ricorda all'utente che non stai dando un parere legale: stai segnalando che quel terreno richiede una verifica con un professionista prima di investirci.

---

## 3. Tentativi passati falliti

Sapere che qualcuno ci ha già provato non è mai di per sé una bocciatura — dipende interamente dal *perché* si è fermato.

- *Via libera*: nessun tentativo trovato, oppure tentativi chiusi per motivi che non riguardano il mercato (il fondatore ha cambiato lavoro, l'azienda è stata acquisita, il prodotto è stato assorbito in un altro).
- *Attenzione*: tentativi falliti per esecuzione — prodotto lento, brutto, mal posizionato, lanciato troppo presto o troppo tardi. Sono un avvertimento e una mappa: si può rifare meglio, ma va spiegato nello SPEC cosa si farà diversamente.
- *Bloccante*: più tentativi indipendenti chiusi per la **stessa causa strutturale**, e quella causa è ancora lì. I due schemi da riconoscere: "il bisogno c'era ma nessuno era disposto a pagare per risolverlo", e "l'unico modo di far funzionare il prodotto dipendeva da un attore terzo che non ha interesse a collaborare" (accesso a dati altrui, integrazioni negate, piattaforme che hanno chiuso le loro API). Se non sai come rimuovere quella causa, non sei nella posizione di riuscire dove hanno fallito.

Un fallimento singolo, anche rumoroso, non basta a bloccare: quello che pesa è la ripetizione dello stesso muro.

---

## 4. Monetizzabilità

**Questo criterio si applica solo se l'utente ha dichiarato che la monetizzazione è richiesta.** Se il progetto è per portfolio, uso personale o open source, l'analisi si fa comunque ma resta informativa: non può generare un NO-GO.

- *Via libera*: esiste un modello di guadagno plausibile e qualcuno nel mercato lo sta già usando con successo, oppure c'è una spesa già esistente che il prodotto intercetta (il target oggi paga qualcuno o qualcosa per risolvere lo stesso problema in modo peggiore).
- *Attenzione*: il modello esiste ma è fragile — dipende solo dalla pubblicità con volumi incerti, o richiede una massa critica di utenti prima di produrre un euro (tipico dei marketplace e dei prodotti sociali), o il pubblico è notoriamente restio a pagare per questa categoria.
- *Bloccante*: nessuna forma di monetizzazione è applicabile. I casi concreti: il valore per l'utente esiste solo se il servizio è gratuito e senza pubblicità; le regole della piattaforma o il quadro normativo vietano di monetizzare quel tipo di contenuto o dato; il costo variabile per utente (chiamate ad API a pagamento, calcolo, spedizioni, moderazione umana) supera in modo strutturale quello che il target è disposto a pagare; l'unico modello possibile sarebbe la rivendita di dati personali degli utenti, che oltre a essere fragile ricade nel criterio 2.

Attenzione al costo variabile: è la causa più frequente e più sottovalutata di non-monetizzabilità nei progetti che usano modelli di intelligenza artificiale a consumo. Se ogni utente gratuito costa e il tasso di conversione realistico è basso, fai il conto esplicito prima di dichiarare via libera.

---

## 5. Volumi attesi rispetto al tempo di realizzazione

Questo criterio è un rapporto, non un numero assoluto: la stessa dimensione di pubblico può essere ottima per un tool costruito in un weekend e disastrosa per una piattaforma da otto mesi.

Stima prima i due lati, con dati osservabili (le fonti sono in `ricerca-mercato.md`): la **dimensione del pubblico raggiungibile** — volumi di ricerca mensili sulle query dell'intento, download stimati dei concorrenti, iscritti alle community di riferimento, numero di soggetti nel target se è un verticale B2B — e il **tempo di sviluppo dell'MVP**.

Poi giudica:

- *Via libera*: il pubblico raggiungibile è ampiamente sufficiente a ripagare il tempo previsto, anche assumendo di intercettarne solo una piccola frazione. Ragiona sempre su una frazione, mai sul totale: la quota realistica di un nuovo entrante è una fetta piccola, non il mercato intero.
- *Attenzione*: il pubblico è piccolo ma il valore per utente è alto (tipico dei verticali professionali: poche centinaia di clienti possibili, ma ognuno paga un abbonamento serio), oppure il pubblico è grande ma diluito su un intento generico dove è difficile farsi trovare.
- *Bloccante*: il pubblico raggiungibile è minuscolo *e* il tempo richiesto è consistente. In pratica: un progetto da molti mesi per un pubblico da poche centinaia di persone a bassa disponibilità di spesa, o un'idea per cui non trovi nessun segnale di domanda — nessuno la cerca, nessuna community ne parla, nessun concorrente ha traction — pur avendola cercata in più modi.

Prima di bloccare su questo criterio, verifica di non aver cercato con il vocabolario sbagliato: molte nicchie esistono ma si chiamano con parole che l'utente del settore usa e tu no. Chiedi all'utente come chiamerebbe la cosa chi ne ha bisogno, e ricerca con quelle parole. L'assenza di volumi va dichiarata solo dopo aver provato più vocabolari.

Nota utile per non essere troppo severi: se il tempo di sviluppo è breve (giorni o poche settimane), questo criterio difficilmente blocca. Un piccolo tool per un piccolo pubblico è un investimento proporzionato — il problema nasce quando lo sforzo è grande e il pubblico no.
