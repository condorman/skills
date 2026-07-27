# Criteri per complessità, concorrenza e rischio legale

Questi criteri servono a rendere concreti i giudizi Bassa/Media/Alta richiesti in Fase 3 della skill, evitando stime a sensazione.

## Complessità (Bassa / Media / Alta)

Pensa in termini di cosa serve costruire, non di quanto è "figa" l'idea:

- **Bassa**: funzionalità singola e ben definita, nessuna integrazione con servizi terzi complessi, UI semplice, nessun backend articolato (o nessun backend). Realizzabile in poche settimane da una persona sola.
- **Media**: più funzionalità collegate tra loro, un backend con account utente/sincronizzazione, magari un'integrazione con un'API esterna (pagamenti semplici, mappe, notifiche). Richiede alcuni mesi.
- **Alta**: componenti che richiedono competenze specialistiche (machine learning, hardware/sensori, real-time multiplayer, compliance pesante), molte integrazioni, o un backend complesso da mantenere nel tempo.

## Concorrenza (Bassa / Media / Alta)

Non guardare solo "quante app simili esistono", ma quanto è difficile inserirsi:

- **Bassa**: poche o nessuna app dedicata a quel bisogno specifico; quelle che esistono sono datate, mal recensite, o coprono solo una parte del problema.
- **Media**: esistono alcuni competitor validi ma nessuno domina chiaramente, oppure il mercato è ampio ma la nicchia specifica individuata è scoperta.
- **Alta**: pochi player dominano saldamente la categoria con recensioni alte e base utenti consolidata; entrare richiederebbe un differenziale enorme o budget marketing importante.

**Nota importante**: la concorrenza va giudicata sulla qualità dell'esecuzione, non solo sul numero di competitor. Un'app concorrente con poche installazioni, recensioni negative o sviluppo abbandonato conta come concorrenza più bassa nella pratica — il bisogno resta scoperto anche se qualcuno ci ha già provato. In questi casi non fermarti al giudizio Bassa/Media/Alta: leggi le recensioni negative del concorrente debole ed estrai gli aspetti concreti che non hanno funzionato, da usare come base per differenziare la nuova idea (più affidabile, più semplice, con la feature che a loro manca...). Questo passaggio trasforma la validazione della concorrenza in un vero brief per un prodotto migliore, non solo in un punteggio.

## Rischio legale (Nullo / Medio / Ampio)

Usa queste categorie per capire a quale fascia appartiene un'idea, e per spiegare la domanda all'utente in Fase 0 in modo concreto invece che astratto:

- **Nullo**: l'app non tratta dati sensibili, non gestisce pagamenti diretti tra utenti, non è rivolta a minori, non opera in settori regolamentati. Es: utility, produttività personale, giochi single-player senza dati condivisi.
- **Medio**: l'app gestisce dati personali "normali" (account, preferenze), oppure pagamenti tramite piattaforme terze standard (in-app purchase, Stripe), oppure ha una componente social/community da moderare. Richiede attenzione a privacy policy e termini di servizio ma senza normative settoriali specifiche.
- **Ampio**: l'app tratta dati sanitari o finanziari sensibili, gestisce transazioni dirette tra utenti (marketplace, scommesse), è rivolta esplicitamente a minori, opera in settori regolamentati (farmaci, integratori, armi, contenuti per adulti, criptovalute/investimenti), o comporta responsabilità legale diretta verso terzi (es. app che dà consigli medici/legali/finanziari personalizzati).

Quando valuti un'idea, confronta il rischio stimato con la tolleranza dichiarata dall'utente: se l'idea è "Ampio" ma l'utente ha detto "Nullo", il progetto va marcato non fattibile per questo utente anche se altrimenti valida — non è una bocciatura dell'idea in sé, ma un disallineamento con chi la dovrebbe costruire.

## Monetizzazione (nota trasversale)

Se l'utente ha dichiarato in Fase 0 che la monetizzazione è richiesta, questo non è un asse a sé ma influenza gli altri due: integrare pagamenti, abbonamenti o acquisti in-app di solito sposta la complessità almeno a Media (serve un backend per gestirli, non solo l'interfaccia) e il rischio legale almeno a Medio (gestione dati di pagamento, termini di servizio, politiche di rimborso), anche se il resto dell'idea sarebbe altrimenti più semplice. Se invece la monetizzazione non è richiesta, non applicare questo aggiustamento: un'idea senza modello di guadagno non va penalizzata su nessuno dei due assi.

## Tabella di decisione per la fattibilità finale

| Complessità | Concorrenza | Rischio legale vs soglia utente | Tempo vs disponibilità | Verdetto |
|---|---|---|---|---|
| Bassa/Media | Bassa/Media | entro soglia | entro soglia | ✅ Fattibile |
| Bassa/Media | Bassa/Media | entro soglia | leggermente sopra | 🟡 Da monitorare |
| Alta | Bassa | entro soglia | entro soglia | 🟡 Da monitorare |
| qualsiasi | Alta | entro soglia | entro soglia | 🟡 Da monitorare (solo se la nicchia specifica è comunque scoperta) altrimenti ❌ |
| qualsiasi | qualsiasi | **sopra** soglia | qualsiasi | ❌ Non fattibile |
| Alta | Alta | qualsiasi | qualsiasi | ❌ Non fattibile |
| qualsiasi | qualsiasi | qualsiasi | chiaramente incompatibile | ❌ Non fattibile |

Il rischio legale sopra soglia è l'unico criterio "eliminatorio" da solo: tutti gli altri assi si bilanciano tra loro, ma se il rischio supera quello dichiarato dall'utente il progetto va scartato indipendentemente dal resto.
