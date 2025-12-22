# Document: APPUNTI LEZIONE_mining copia.pdf

DATA MINING E TEXT 
ANALYTICS 
2 elevato a k—> dove k è numero di bit 
Computer a 2 bit potrà avere 4 lettere, rappresen -
tazione 
LLM, cioè reti neurali 
INTRODUZIONE 
• Rumore (noise) —> qualcosa che non ci fa leg -
gere bene i dati, disturba la lettura del dato e 
quindi anche l'interpretazione. 
• Bias (altro tipo di rumore) —> pregiudizi, per 
esempio di genere. Preconcetti che possono es -
sere riprodotti sia nei dati sia in chi legge.  
Differenza—> noise in generale è qualcosa che 
disturba il segnale, bias preconcetto che viene ri -
flesso all'interno dei dati 
Rumore sale e pepe (pixel bianchi e neri sull'im -
magine), attraverso il ﬁltro mediano  è possibile 
cancellare il rumore. Rumore è un qualcosa che 
viene aggiunto. 
Perchè utilizzare il data mining? 
Il data mining è un processo utilizzato per scoprire 
informazioni preziose all'interno di grandi quantità 
di dati. Per comprendere meglio questo concetto, 
immagina di scavare un buco mentre cerchi qual -
cosa di prezioso. (Scoprire conoscenza) 
Il Processo di Ricerca dell'Informazione 
Durante il processo di scavo, dovrai attraversare 
diversi strati di materiale: terra di scavo, rocce, re -
sidui di pietra e altri elementi che potrebbero non 
essere esattamente ciò che stai cercando. Allo 
stesso modo, nel data mining lavori con grandi 
volumi di dati grezzi per trovare le informazioni che 
ti servono. 
Strumenti e Tecniche Necessari 
Per raggiungere il tuo obiettivo - l'INFORMAZIO -
NE  - hai bisogno di alcuni strumenti e tecniche 
specifici che ti guidino nel processo di ricerca e 
analisi. 
I Pattern: I Mattoni dell'Informazione 
Prima di estrarre l'informazione finale, è necessario 
mettere insieme alcuni piccoli pezzi o componenti 
che, una volta combinati, favoriscono la composi -
zione dell'informazione stessa. Questi piccoli pezzi 
sono chiamati PATTERN (modelli). 
Deﬁnizione di Pattern 
I pattern sono un insieme di elementi presenti nei 
dati che esprimono: 
• Sequenze: ordini specifici di eventi o dati 
• Motivi: ricorrenze o schemi ripetitivi 
• Codici: rappresentazioni strutturate di infor -
mazioni 
• E molti altri tipi di strutture informative 
Pattern in stock price 
Analisi del Prezzo delle Azioni 
L’analisi del prezzo delle azioni è un argomento 
cruciale. Le fluttuazioni nei prezzi possono rivelare  
eventi di interesse per il mercato. 
Esempio di Serie Storica: 
Dove: 
- Pt è il tempo dell'azione al 
tempo 
- Et è un fattore additivo (rumore o variabilità ca -
suale) 
Trends and hidden patterns 
Punto medio è una linea (rossa) 
Trend cercando di eliminare la diminuzione e au -
mento del prezzo 
1

Esempi di Data Mining 
• Identificare correlazioni nei dati finanziari e di 
business intelligence 
• Consentire agli ospedali di rilevare trend e ano -
malie nelle cartelle cliniche dei pazienti 
• Migliorare il posizionamento e il ranking negli 
engine di ricerca e negli spazi pubblicitari 
• Permettere ad agenzie ambientali e di sanità 
pubblica di individuare schemi e irregolarità nei 
loro dataset 
• Monitorare i consumi energetici degli elettrodo -
mestici di casa 
• Analizzare pattern in bioinformatica e in dati far -
maceutici 
• Scoprire trend in blog, Twitter e altre piattaforme 
social 
Deﬁnizione formale di Data Mining 
Il data mining, comunemente noto anche come 
Knowledge Discovery from Data (KDD), è l’estra -
zione automatizzata o facilitata di pattern che rap -
presentano conoscenza implicitamente memorizza-
ta o catturata in grandi database, data warehouse, 
sul Web, in altri vasti repository di informazioni o in 
flussi di dati. 
Deﬁnizione informale di Data Mining 
Il  Data Mining  è il processo mediante il quale un 
programma informatico esplora grandi quantità di 
dati alla ricerca di pattern o relazioni nascoste. 
• Individuazione di combinazioni di sintomi che 
fungono da indicatori affidabili per una determi -
nata malattia 
• Scoperta di quali prodotti i clienti tendono a 
comprare insieme (analisi del “market basket”) 
• Raggruppamento di dati che mostrano particolari 
correlazioni tra variabili 
• Qualsiasi scenario in cui serva estrarre insight da 
enormi moli di informazioni in modo automatiz -
zato 
Che cosa rivelano i pattern? 
I pattern consentono di individuare regolarità, ten -
denze e correlazioni nei dati, mettendo in luce re -
lazioni non ovvie tra variabili. 
1. Definizione di pattern 
Un  pattern  è qualsiasi elemento o sequenza 
che si ripete con una forma o organizzazione 
costante all’interno del dataset. 
2. Correlazioni mostrate dai pattern 
1. Una sequenza di segnali che si manifesta 
periodicamente 
2. Elementi che seguono una progressione 
lineare 
4. Tipologia di dati 
I pattern possono emergere sia da dati struttu -
rati  (tabelle, database relazionali) sia da 
dati  non strutturati  (testi, immagini, flussi di 
log). 
Dati strutturati 
Dati con un elevato grado di organizzazione (in 
modo simile a un foglio di calcolo), dove ogni 
elemento è descritto da campi e schemi ben defi -
niti. 
Dati semistrutturati 
Dati con un certo livello di organizzazione (per 
esempio moduli XML o JSON), che includono tag 
o marcatori ma non rispettano uno schema relazio -
nale rigido. 
Dati non strutturati 
Dati privi di un’organizzazione predefinita (come un 
file di testo libero), senza uno schema o campi sta -
biliti a priori. 
2

Databases 
Una  database  è una raccolta organizzata di dati 
strutturati, tipicamente memorizzati elettronica -
mente in un sistema informatico. Ogni elemento di 
informazione è archiviato secondo uno schema 
definito che ne facilita l’accesso, la gestione e la 
modifica. 
Il database è normalmente gestito da un Database 
Management System (DBMS), un software che of -
fre strumenti per: 
• Definire e modificare la struttura dei dati 
• Inserire, aggiornare ed eliminare record 
• Eseguire query per recuperare informazioni 
• Garantire integrità, sicurezza e concorrenza nel -
l’accesso ai dati 
Data Warehouse: Deﬁnizione e caratteristiche 
Un  data warehouse  è un sistema di gestione dei 
dati progettato per supportare attività di Business 
Intelligence (BI) e soprattutto analisi. 
• È pensato per eseguire query e analisi, spesso 
su grandi volumi di dati storici. 
• I dati contenuti in un data warehouse provengo -
no da una  molteplicità di fonti  (log applicativi, 
database transazionali, CRM, ecc.). 
• Col tempo costruisce un  archivio storico  che di -
venta prezioso per data scientist e analisti azien -
dali, fungendo da  “single source of truth ”  (uni-
ca fonte di verità).  
• Grazie alla centralizzazione e alla consolidazione 
dei dati, un data warehouse permette di ottenere 
viste integrate e coerenti dell’intera organizza -
zione, facilitando decisioni basate su informazioni 
complete e affidabili. 
Enterprise Data Warehouse 
Raccoglie tutte le informazioni relative ai soggetti 
di interesse dell’intera organizzazione. 
È progettato per supportare l’integrazione dei dati 
a livello aziendale (cross-funzionale) e può conte -
nere da centinaia di gigabyte a terabyte (o oltre) di 
dati storici. 
Data Mart 
Contiene un sottoinsieme di dati aziendali di valore 
per un gruppo specifico di utenti (ad esempio un 
dipartimento). 
Il suo ambito è limitato a determinati soggetti. Per 
esempio: 
• Un marketing data mart potrebbe concentrarsi su 
cliente, prodotto, canali di marketing e vendite. 
• Un risk control data mart  potrebbe focalizzarsi su 
credito cliente, rischi e frodi. 
Data Lake 
In alcune aziende esistono enormi quantità di fonti 
dati complesse  con una  grande varietà  di tipolo -
gie, formati e qualità dei dati, come: 
• Dati aziendali 
• Comunicazioni tra clienti e organizzazione 
• Normative e regolamentazioni 
• Analisi di mercato 
Può essere  difficile progettare un Data 
Warehouse dove i dati vengono integrati, struttura-
ti e caricati secondo criteri specifici, specialmente 
quando si ha a che fare con questa varietà di fonti 
eterogenee. 
Un  data lake  è un  repository unico  che contiene 
tutti i dati aziendali nel loro  formato naturale, in -
cludendo, utile per i disaster recovery: 
• Dati relazionali (database strutturati) 
• Dati semistrutturati (file XML, JSON) 
• Dati non strutturati (documenti, testi) 
• Dati binari (audio, immagini, video) 
Un data lake spesso conserva sia: (key:backup) 
• Copie raw (dati grezzi originali) 
• Dati trasformati  (elaborati attraverso processi di 
analisi) 
Questi vengono archiviati in  repository cloud  o  di-
stribuiti, permettendo una gestione scalabile e 
flessibile delle informazioni aziendali. 
Database, Data Warehouse e Data Lake 
Database (DB) 
I database sono progettati per l’elaborazione rapi-
da e transazionale di dati strutturati. 
3
Data Warehouse (DW) 
I data warehouse sono ottimizzati per le query ana -
litiche  su dati strutturati, con un approccio  top-
down e orientato agli obiettivi. 
Data Lake (DL) 
I data lake memorizzano dati grezzi, non strutturati 
o semistrutturati per analisi su larga scala. 
Scenari reali con Database, Data Warehouse e 
Data Lake 
Elaborazione transazionale con Database 
Un sito di e-commerce utilizza un database relazio -
nale (ad esempio MySQL) per memorizzare e gesti-
re ordini cliente, giacenze di magazzino e account 
utente. Quando un cliente effettua un ordine, il 
database elabora la transazione in tempo reale, 
aggiornando le quantità di prodotto e registrando i 
dettagli dell’ordine. 
Query analitiche con Data Warehouse 
Un’azienda retail impiega Amazon Redshift come 
data warehouse per analizzare le tendenze di ven -
dita degli ultimi cinque anni. Il data warehouse ag -
grega i dati di vendita provenienti da diversi nego -
zi, consentendo all’azienda di eseguire query com-
plesse per comprendere il comportamento dei 
clienti, i trend stagionali e la redditività. 
Gestione di dati grezzi e non strutturati con 
Data Lake 
Un servizio di video streaming sfrutta Amazon S3 
come data lake per immagazzinare grandi volumi 
di file video grezzi, log di interazione degli utenti e 
metadati. I data scientist accedono a questi dati 
“raw” per eseguire algoritmi di machine learning 
che raccomandano contenuti agli utenti in base  
alla loro cronologia di visione e alle loro preferen -
ze. 
Data and information technology evolution 
• “La necessità, che è la madre dell’invenzione.” 
– Platone 
• Enorme crescita del volume di dati disponibili 
• Informatizzazione della società  
• Rapido sviluppo di potenti strumenti di raccolta e 
di archiviazione dei dati 
• Alcuni dati sulla crescita dei dati 
Ogni giorno vengono caricati su YouTube 720.000 
ore di video . Ogni giorno vengono condivise su 
Instagram 1,3 miliardi di immagini. 
Esempi di dati prodotti dalle aziende 
Transazioni di vendita, record di scambi azionari, 
descrizioni di prodotti, promozioni commerciali, 
profili e performance aziendali, e feedback dei 
clienti sono solo alcuni esempi dei dati generati 
dalle imprese. 
I dati delle vendite al dettaglio vengono attual -
mente analizzati su più variabili per identificare pat-
tern e tendenze. 
Wal-Mart gestisce ogni settimana centinaia di mi -
lioni di transazioni in migliaia di filiali sparse nel 
mondo. 
Studi scientifici dimostrano che il meteo può in -
fluenzare le vendite al dettaglio. 
Le cinque categorie di prodotti più sensibili alle 
condizioni atmosferiche coprono un’ampia gamma 
di tipologie, con gli alimenti salutistici in prima li -
nea per variabilità legata al clima. 
Statistiche e Tendenze 
• Statistiche e trend possono aiutare a scoprire 
alcune correlazioni tra i dati. 
• Se alcuni pattern sono facili da individuare, altri 
non sono altrettanto semplici da estrarre. 
• Il data mining entra in gioco per scoprire cono -
scenza a partire dai dati disponibili. 
• Il processo di Knowledge Discovery Process è 
composto da diversi passi. (Passo 0 —> raw data)  
4

KDP: Passi principali ed esempi 
1. Data Cleaning (Pulizia dei dati) 
• Rimozione di rumore e dati inconsistenti. 
• Obiettivo: rendere i dati più affidabili eliminando 
errori, duplicati e valori anomali. 
2. Data Integration (Integrazione dei dati) 
• Unione di più fonti di dati, integrazione sorgenti. 
• Obiettivo: combinare informazioni provenienti da 
database diversi per avere un dataset completo 
e coerente. 
3. Data Transformation (Trasformazione dei dati) 
• Trasformazione e consolidamento dei dati in 
forme adatte all'analisi. 
• Include operazioni di sintesi e aggregazione (ad 
esempio: calcolo delle medie, somma di valori, 
raggruppamenti). 
4. Data Mining (Estrazione dei dati) 
• Applicazione di  metodi intelligenti  per estrarre 
pattern significativi o costruire modelli dai dati. 
• Esempi: algoritmi di classificazione, clustering, 
regole di associazione. 
5.  Pattern/Model Evaluation (Valutazione dei 
Pattern o Modelli) 
• Processo di  identificazione dei pattern o modelli 
davvero utili  e interessanti, sulla base di misure 
specifiche. 
• Serve a selezionare la conoscenza realmente rile -
vante da quella meno significativa. 
6.  Knowledge Presentation (Presentazione della 
Conoscenza) 
• Visualizzazione e rappresentazione della cono -
scenza trovata, per facilitarne l'interpretazione da 
parte degli utenti. 
• Si usano grafici, report, cruscotti o altre forme di 
presentazione chiara ed efficace. 
Data Mining Descrittivo e Predittivo 
Il data mining descrittivo si occupa di analizzare e 
descrivere le proprietà e le caratteristiche dei dati 
presenti nel dataset. L'obiettivo principale è indivi -
duare pattern, relazioni e riassunti che aiutano a 
comprendere la struttura dei dati, senza necessa -
riamente fare previsioni. Alcuni esempi di tecniche 
descrittive sono il clustering, la ricerca di regole di 
associazione e l'analisi delle correlazioni. 
Il  data mining predittivo , invece, mira a costruire 
un modello (attraverso un processo di induzione) 
che sia in grado di prevedere valori futuri o scono -
sciuti di una variabile target, utilizzando le altre 
variabili disponibili nel dataset. Le tecniche predit -
tive più comuni includono la classificazione, la re -
gressione e il forecasting. 
Tipi di dati che possono essere analizzati con il 
data mining 
È possibile applicare tecniche di data mining su 
diverse tipologie di dati: 
• Dati di database:   informazioni organizzate in 
tabelle relazionali tradizionali (ad esempio, data -
base gestionali). 
• Data warehouse:   insiemi di grandi quantità di 
dati, spesso provenienti da fonti eterogenee e 
integrati in un'unica struttura per l'analisi. 
• Dati transazionali: dati relativi a transazioni effet-
tuate, ad esempio registrazioni di acquisti, vendi -
te, movimenti bancari. 
• Altri tipi di dati :  possono includere dati non 
strutturati, dati testuali, dati multimediali, dati 
web, serie temporali e dati spaziali. 
Queste categorie coprono quasi tutte le fonti di 
dati che possono essere oggetto di estrazione di 
conoscenza mediante tecniche di data mining. 
Database Data 
Un sistema di database, chiamato anche  Database 
Management System (DBMS) , è formato da una 
collezione di dati correlati (database) e da un in -
sieme di programmi software che permettono di 
gestire e accedere a questi dati. 
Per capire meglio, si può immaginare una struttura 
molto simile a un foglio di calcolo, con colonne e 
righe che rappresentano come vengono organizza-
ti e trattati i dati all'interno di un database. 
5

Quando viene richiesto di trovare l' attributo che 
identifica  in modo univoco  i dati di un'azienda in 
un database, bisogna individuare la  colonna  (o at-
tributo) che contiene valori diversi per ciascuna 
azienda e che quindi permette di distinguerle sen -
za ambiguità. 
Questa colonna prende il nome di  chiave prima -
ria  (primary key): è un attributo, o un insieme di 
attributi, che permette di identificare  univocamen -
te ogni record  (ogni azienda, in questo caso) nella 
tabella del database. 
Se si parte dal presupposto che nessuna azienda 
abbia lo stesso nome, l'attributo "Company 
Name" permette di identificarla in modo univoco 
nel database ed assume il ruolo di chiave primaria. 
Nel caso specifico, quindi, il  Company Name  rap -
presenta la chiave primaria della tabella, cioè l' at-
tributo che distingue in maniera unica ogni 
azienda. 
Al contrario, attributi come il fatturato di febbraio 
(o quello di altri mesi) non identificano univoca -
mente l’azienda, poiché valori identici possono 
essere condivisi da aziende diverse. 
Un database relazionale è formato da una raccol -
ta di tabelle, ognuna identificata da un nome uni -
co. 
Ogni tabella contiene un insieme di attributi (co -
lonne, chiamate anche campi) e memorizza un ele -
vato numero di tuple (record o righe), dove cia -
scuna tupla rappresenta un oggetto. 
Ogni oggetto (tupla) è identificato in modo univo -
co da una chiave primaria  (unique key/primary 
key) ed è descritto da diversi valori di attributo. 
Le relazioni tra le varie tabelle vengono stabilite 
tramite le chiavi esterne  (external keys), che per -
mettono di collegare dati tra tabelle diverse all’in -
terno del database. 
Consideriamo AllElectronics, un’azienda fittizia. 
L’azienda viene rappresentata tramite un database 
relazionale composto da diverse tabelle di relazio -
ne, ciascuna dedicata ad aspetti diversi dell’orga -
nizzazione. In particolare, le tabelle principali sono: 
• customer (clienti) 
• item (prodotti/articoli) 
• employee (dipendenti) 
• branch (filiali/sedi) 
Queste tabelle consentono di modellare i dati fon -
damentali dell’azienda e di descrivere le sue rela -
zioni interne. 
Quando si lavora con i database, è utile considera -
re gli  schemi logici. Questi rappresentano la strut -
tura logica del database attraverso diversi elementi 
chiave: 
• Tabelle (Entità):  punti di raccolta dati nel siste -
ma. 
• Attributi (Campi): proprietà o caratteristiche del -
le entità.  
• Relazioni:  indicano come le diverse entità sono 
collegate tra loro (ad esempio, relazioni uno-a-
uno, uno-a-molti). 
• Vincoli:  regole che governano come i dati pos -
sono essere inseriti o collegati, tra cui chiavi pri -
marie, chiavi esterne, vincoli di unicità.  
Gli schemi logici aiutano a progettare il database 
in modo chiaro e sicuro, garantendo che i dati sia -
no ben strutturati e che le relazioni tra le parti sia -
no esplicite. 
Gli schemi logici del database di AllElectronics 
sono rappresentati dalle seguenti tabelle di rela -
zione, ognuna con i propri attributi: 
• customer:  contiene dati come ID cliente, nome, 
indirizzo, età, occupazione, reddito annuo, in -
formazioni di credito, categoria, ecc. 
• item: include ID prodotto, marca, categoria, tipo, 
prezzo, luogo di produzione, fornitore, costo, 
ecc. 
• employee:  gestisce ID dipendente, nome, cate -
goria, gruppo, salario, commissione, ecc. 
6
• branch:  dati relativi a ciascuna sede (ID sede, 
nome, indirizzo, ecc.). 
• purchases:  registra le transazioni d’acquisto (ID 
transazione, ID cliente, ID dipendente, data, ora, 
metodo di pagamento, importo). 
• items sold: elenca per ogni transazione i prodotti 
venduti (ID transazione, ID articolo, quantità).  
• works_at:  tiene traccia di dove lavorano i dipen -
denti (ID dipendente, ID sede). 
In sintesi, ogni riga di queste tabelle rappresenta 
un record, mentre gli attributi tra parentesi identifi -
cano le proprietà di ciascuna entità nel database. 
L’accesso ai database relazionali  avviene tramite i 
linguaggi di interrogazione basati su query, 
come SQL. Questi consentono di eseguire interro -
gazioni per recuperare informazioni dai database. 
Le istruzioni più comuni sono join, selezione e pro -
iezione, che permettono di: 
• unire dati da più tabelle, 
• selezionare solo i record di interesse, 
• visualizzare specifici attributi. 
Un esempio di query potrebbe essere “Mostrami 
la lista di tutti gli articoli venduti da gennaio 2022”. 
Inoltre, i linguaggi relazionali permettono di usare 
le funzioni di aggregazione (come somma, media, 
conteggio, massimo, minimo) per svolgere analisi 
più complesse. 
Ad esempio: “Mostrami il totale delle vendite del -
l’ultimo mese raggruppato per filiale”. 
Nel contesto dei database relazionali, il data mi-
ning viene utilizzato principalmente per 
cercare pattern (schemi ricorrenti) nei dati. 
Ad esempio, analizzando i dati dei clienti si posso -
no prevedere rischi di credito per i nuovi clienti, 
basandosi su variabili come reddito, età e prece -
denti informazioni creditizie. 
Un altro compito fondamentale è l’ analisi 
delle deviazioni (deviation): il data mining aiuta a 
individuare prodotti che registrano vendite molto 
diverse rispetto alle aspettative, ad esempio con -
frontando le vendite con gli anni precedenti. Que -
ste deviazioni possono essere indagate ulterior -
mente per scoprirne le cause. 
Il data mining può anche rilevare c ambiamenti 
nascosti, come modifiche nel packaging di un 
prodotto, che potrebbero influenzare l’andamento 
delle vendite o altri indicatori aziendali. 
Data Warehouse 
Immagina che AllElectronics diventi una grande 
azienda internazionale con diverse ﬁliali sparse nel 
mondo, e che ogni filiale gestisca i propri database 
separati. 
Se volessi confrontare, ad esempio, l’andamento 
dei diversi tipi di articoli venduti in ogni filiale, sa -
rebbe molto complicato lavorando solo con data -
base relazionali separati: dovresti raccogliere dati 
da più fonti e integrarli manualmente. 
In questi casi entra in gioco il  Data Warehouse. Un 
Data Warehouse permette di uniﬁcare e integrare 
i dati provenienti da tutte le filiali, rendendo pos -
sibile analisi avanzate e centralizzate sull’intera or -
ganizzazione, superando i limiti dei semplici data -
base relazionali distribuiti. 
Un  data warehouse  è un archivio di informazioni 
raccolte da diverse fonti, integrate tramite uno 
schema unificato. 
La costruzione di un data warehouse richiede fasi 
come: Data cleaning, Integration, Transformation, 
Loading e Refreshing. 
I dati sono generalmente organizzati per tematiche 
rilevanti all’analisi decisionale: clienti, prodotti, for-
nitori, attività, ecc. 
 
Nel data warehouse, i dati vengono salvati anche 
per ﬁnalità storiche (ad esempio, sintesi degli ul -
timi 6-12 mesi). 
Struttura multidimensionale: 
Il data warehouse possiede una struttura multidi -
mensionale, detta Data Cube: 
7
• Ogni  dimensione  rappresenta un attributo o un 
insieme di attributi (es.: periodo, prodotto, 
filiale). 
• Ogni cella del cubo contiene un valore aggrega -
to, come la somma delle vendite di un prodotto 
in una certa filiale in uno specifico mese. 
Questo modello permette analisi complesse e fles -
sibili sui dati aziendali, favorendo la visione d’in -
sieme, la comparazione storica, la scoperta di pat -
tern e trend. 
Data Warehouse | Drill-down, Roll-up 
Un data warehouse consente di effettuare analisi 
dettagliate e flessibili sui dati grazie alle funzioni 
di  drill-down  e  roll-up, che corrispondono a vi -
sualizzazioni differenti delle informazioni. 
• Drill-down: consiste nel “scendere” nel detta -
glio dei dati, focalizzandosi su attributi specifici 
(ad esempio, visualizzare le vendite per singolo 
prodotto piuttosto che per categoria). 
• Roll-up: è l’operazione inversa, che permette di 
“raggruppare” i dati in maniera più compatta, 
aggregando gli attributi per ottenere una visione 
d’insieme (esempio: vendite totali trimestrali). 
I data warehouse  mettono a disposizione stru -
menti di OLAP (Online Analytical Processing), che 
permettono analisi interattive sui dati multidimen -
sionali a diversi livelli di granularità. 
Esempio: le vendite di AllElectronics sono archivia -
te e analizzabili per tipologia di prodotto, periodo 
(trimestri) e località (città). Questo consente con -
fronti rapidi e approfondimenti tra diverse dimen -
sioni dei dati aziendali. 
Drill-down on Time for Q1 
Roll-up on address 
Transactional Data 
Ogni record in un database transazionale rappre-
senta una transazione, come un acquisto effettua-
to da un cliente, una prenotazione di volo o i click 
di un utente su una pagina web. 
Di solito contiene un  transaction ID  (identificativo 
univoco della transazione) e una lista degli articoli 
coinvolti (prodotti acquistati). 
Le  Transactional Databases  possono avere anche 
altre tabelle correlate, per descrivere meglio gli 
articoli acquistati (ad esempio: descrizione, infor-
mazioni sul negozio o sul venditore). 
AllElectronics Transactional DB 
Un esempio concreto di database transazionale 
per AllElectronics mostra una tabella con due co -
lonne: 
• trans_ID: identificativo della transazione (es. 
T100, T200) 
• list_of_item_IDs: lista degli identificativi degli 
articoli acquistati in quella transazione (es. 11, 13, 
18, 116) 
Queste informazioni consentono di capire quali 
prodotti vengono spesso acquistati insieme (mar -
8

ket basket analysis), strategia utilizzata per ottimiz -
zare promozioni e aumentare le vendite. 
Altri tipi di Dati 
Oltre ai dati tabellari e transazionali, il data mining 
può essere applicato a molti altri tipi di dati: 
• Dati temporali o sequenziali: serie storiche, dati 
di borsa, record biologici, sequenze temporali. 
• Dati multimediali e ipertestuali : testi, immagini, 
dati audio/video. 
• Dati a grafo e di rete : dati provenienti da reti 
sociali o reti di informazione. 
Esempi di applicazioni: 
• Sulle borse valori si possono individuare trend 
utili per strategie di investimento. 
• I flussi di dati delle reti informatiche vengono 
analizzati per rilevare anomalie (sistemi di rileva -
mento intrusioni). 
• Le immagini possono essere utilizzate per adde -
strare modelli di machine learning che classifica -
no oggetti e assegnano etichette semantiche, 
suddividendo dataset complessi in categorie 
precise. 
 
Quali pattern si possono estrarre? 
Nel data mining è possibile estrarre diversi tipi di 
pattern dai dati: 
• Classi o concetti: rappresentano categorie o 
tipologie di dati (ad esempio, il segmento di 
clientela). 
• Associazioni e correlazioni:  relazioni che indica -
no quali elementi compaiono frequentemente 
insieme (regole di associazione). 
• Classiﬁcazione e regressione:  tecniche per pre -
vedere valori (regressione) o assegnare una clas -
se a ciascun dato (classificazione). 
• Cluster analysis:  identificazione di gruppi omo -
genei di dati all’interno del dataset senza cono -
scere le categorie a priori. 
• Outlier analysis: individuazione di dati anomali 
che si discostano significativamente dal resto del 
dataset (outlier). 
Classi e concetti 
I dati possono essere associati a classi o concetti, 
che rappresentano categorie specifiche o rag -
gruppamenti coerenti all'interno del dataset. 
Ad esempio, AllElectronics vende diversi articoli 
che possono essere raggruppati per categorie di 
costo (come “Big Spender” oppure “budget 
Spenders”). 
Le classi e i concetti sono descritte in termini det -
tagliati e queste descrizioni sono chiamate concet -
ti o classi.  
Si possono costruire tramite 2 approcci: 
• La caratterizzazione (Data Characterisan)  consi-
ste nel sintetizzare le caratteristiche generali di 
una classe di dati (es. “strumenti software con 
vendite aumentate del 10% nell’ultimo anno”). 
• La  discriminazione (Data Discrimination)  invece 
mette a confronto le caratteristiche tra classi di 
dati diverse, evidenziandone le differenze princi -
pali. 
Characterisation & Discrimination 
Output examples: pie charts, bar charts, curves, 
multidimensional data cubes and multidimensional 
tables 
Esempi pratici: Data Characterisation e Data Di -
scrimination 
Data Characterisation Task: 
Si tratta di riassumere le caratteristiche dei clienti 
che spendono più di $5000 all’anno da AllElectro -
nics. 
Risultato: si ottiene un profilo generale di questi 
clienti (per esempio: hanno tra i 40 e i 40 anni di 
età, sono occupati e possiedono ottimi rating di 
credito). 
9

Data Discrimination Task: 
In questo caso, il manager della customer relation -
ship di AllElectronics vuole confrontare due gruppi 
di clienti secondo gli articoli acquistati. Più nello 
specifico, si vogliono confrontare i clienti che ac -
quistano regolarmente gli stessi prodotti con quelli 
che lo fanno raramente. 
Risultato: si ottiene un profilo comparativo dei 
gruppi di clienti. Ad esempio, l’80% di chi acquista 
spesso prodotti informatici ha tra i 20 e i 40 anni 
ed è laureato, mentre il 60% di chi fa acquisti rari 
degli stessi articoli non ha una laurea ed è più an -
ziano o più giovane rispetto al primo gruppo. 
Pattern frequenti 
Nel data mining, è possibile individuare pattern 
analizzando la presenza ricorrente di alcuni ele -
menti nei database. 
Spesso, insiemi di oggetti appaiono con regolarità 
nello stesso dataset transazionale. Ad esempio, 
latte e pane vengono spesso comprati insieme. 
L’analisi dei pattern frequenti permette di estrarre 
associazioni e correlazioni tra gli elementi presenti 
nei dati, rivelando legami utili per strategie di mar -
keting, ottimizzazione delle vendite e comprensio -
ne dei comportamenti dei clienti. 
Esempio: Association Analysis 
Se vuoi sapere quali articoli vengono acquistati 
frequentemente insieme da AllElectronics, puoi 
utilizzare l’Association Analysis. 
Un esempio di regola prodotta dall’Association 
Analysis è: 
Buys(X, "computer") ˰ buys(X, "software") 
[support = 1%, conﬁdence = 50%] 
Questo significa che ogni volta che X (un cliente) 
acquista un computer, con una certa frequenza 
(support) e probabilità (confidence), acquista anche 
un software. 
La regola individua quindi un’associazione concre -
ta tra i prodotti acquistati dai clienti, mostrando 
come computer e software siano spesso acquistati 
nello stesso ordine. 
Spiegazione dettagliata: Support, Con ﬁdence e 
soglia nelle associazioni 
• La regola di Association Analysis nel caso AllElec-
tronics (Buys(X, "computer") 㱺 buys(X, "soft -
ware") [support = 1%, confidence = 50%]) indica 
che il 1% di tutte le transazioni analizzate contie -
ne sia computer che software (support). 
• Il valore di confidence del 50% significa che, se 
un cliente acquista un computer, c’è il 50% di 
probabilità che acquisti anche un software.  
• Le associazioni vengono tipicamente considerate 
utili solo se superano una certa soglia (threshold) 
di confidence stabilita dai data analyst. 
Questi parametri sono fondamentali per selezio -
nare solo quelle regole che risultano statistica -
mente significative e davvero rilevanti per le stra -
tegie aziendali. 
Classiﬁcazione per Analisi Predittiva 
La classiﬁcazione è un processo che consente di 
trovare un modello o una funzione capace di di -
stinguere tra diverse classi o concetti di dati. 
Per addestrare un modello di classificazione, si 
utilizza un training set, cioè un insieme di dati eti -
chettati (con etichette già note). 
Quando si esegue una classificazione, il modello 
viene poi utilizzato per fare previsioni su nuovi 
dati, sfruttando la conoscenza inferita durante 
l’addestramento. 
Esistono diversi approcci per realizzare la classifica-
zione: 
• IF THEN ELSE (classificazione basata su regole) 
• Decision Tree (rete di nodi che rappresentano 
diversi test) 
• Neural Network (è necessario un training set per 
inferire la conoscenza dai dati etichettati) 
Regressione 
La regressione, a differenza della classificazione 
che restituisce valori discreti (etichette), produce 
previsioni su una scala continua. 
10
Viene usata per stimare valori numerici mancanti o 
non disponibili, invece di assegnare semplici eti -
chette di classe. 
L’analisi di regressione è una metodologia statisti-
ca particolarmente adatta per le previsioni numeri -
che e per individuare i trend di distribuzione nei 
dati. 
Mentre la classificazione necessita di dati etichetta-
ti, la regressione si basa su numeri per produrre 
stime statistiche (ad esempio, previsioni su trend 
futuri partendo da serie storiche di dati). 
Esempio: Classiﬁcazione vs Regressione 
Un sales manager di AllElectronics vuole classiﬁca-
re un insieme di articoli dello store in base a 3 tipi 
di risposta a una campagna di vendita: 
• good response 
• mild response 
• no response 
In questo caso, il sistema di classificazione assegna 
a ogni articolo una delle 3 possibili etichette 
(label), scegliendola tra quelle indicate. 
La classificazione restituisce quindi un valore di -
screto (buona risposta, risposta moderata, nessuna 
risposta) per ogni elemento analizzato. 
Se ti viene chiesto di stimare il possibile ricavo di 
una vendita futura di uno specifico articolo, dovrai 
fornire delle previsioni mese per mese. 
In questi casi la classificazione non è adatta, perché 
serve una previsione numerica e non un'etichetta 
discreta. 
La regressione, invece, fornisce una curva su un 
diagramma: permette di stimare in modo continua-
tivo il valore previsto (ad esempio, ricavi mensili), 
visualizzando così chiaramente la tendenza dei 
dati. 
Nell’esempio mostrato, la regressione lineare sem-
plificata genera una retta che meglio approssima i 
punti osservati, rendendo possibile la previsione 
dei valori futuri. 
Analisi dei cluster 
A differenza della classificazione e della regressio -
ne, la cluster analysis raggruppa i campioni di 
dati senza utilizzare etichette predefinite. 
Nei casi in cui i dati etichettati non siano disponibi -
li, la cluster analysis consente di suddividere i cam -
pioni in gruppi omogenei sulla base delle caratteri-
stiche osservate. 
Questa tecnica può anche essere utilizzata per ge -
nerare nuovi dati etichettati (labels) e facilitare suc -
cessive fasi di analisi. 
Esempio: se ti viene chiesto di identificare dei sot -
togruppi tra i clienti di un’azienda, la cluster analy -
sis ti permette di suddividere la clientela in gruppi 
distinti, ad esempio in base all’area geografica di 
provenienza. 
Quali tecnologie sono utilizzate nel Data  Mi -
ning? 
 
Statistica 
Il data mining è strettamente collegato alla statisti -
ca, che si occupa della raccolta, analisi e interpre -
tazione dei dati. 
Un modello statistico è costituito da un set of ma -
thematical functions  che descrivono come si com -
portano le variabili di un dataset. 
Il comportamento di queste variabili viene descrit -
to attraverso variabili casuali e le loro distribuzioni 
di probabilità.  
La statistica permette sia di rappresentare il “ ru-
more” presente nei dati, sia di sintetizzare e rias -
sumere l’informazione contenuta nei dati raccolti. 
11

Statistica: test, inferenza e signiﬁcatività 
La statistica inferenziale modella i dati per trarre 
conclusioni sulla popolazione oggetto di studio. 
Il  Statistical Hypothesis Test   è essenziale per 
prendere decisioni statistiche sulla base di pattern 
osservati negli esperimenti. Un risultato è 
definito Statistically Signiﬁcant quando non è do -
vuto al caso.  Esistono diversi test che permettono 
di verificare se un risultato è davvero Statistically 
Significant oppure se potrebbe essere semplice -
mente frutto di casualità nei dati. 
"Se si etichettano i dati per addestrare un modello 
allora si utilizzano un modello di ML supervisiona -
to.  
Informazioni raw (grezzo), dato atomico —> inter -
rogo datawarehouse 
Alla base del data management ci sono i singoli 
database, data warehouse, Enterprise DW e poi 
data mart per dipartimento" 
Dalla slide si vede che le 3 tabelle hanno una rela -
zione : 
Customer id sia chiave primaria sei esterna (nella 
prima tabella che si collega con cutomer id della 
seconda tabella ma che ha solo una chiave prima -
ria che è order id e poi nella terza con customer 
come chiave esterna e come shipping id come 
chiave solamente primaria)" 
Fondamenti di Structured Query Language 
(SQL): 
 
Deﬁnizione e Manipolazione di Base dei 
Dati: La Tabella Customers 
Per dimostrare le capacità di SQL, il processo 
inizia con la definizione di una tabella fonda-
mentale denominata Customers (Clienti). La 
creazione di questa struttura dati avviene tra-
mite il comando CREATE TABLE. 
(VARCHAR(50) —> stringa variabile con una 
lunghezza massima di 50 caratteri  
Successivamente alla definizione della struttu-
ra, sono stati inseriti dati campione utilizzando 
il comando INSERT INTO al fine di popolare la 
tabella per le successive operazioni di query.  
L'Operazione di Selezione (SELECT) e Ordi-
namento 
L'operazione SELECT è il comando cardine 
per interrogare il database e recuperare in-
formazioni. Essa permette non solo di filtrare 
le righe (la vera selezione in termini di algebra 
relazionale), ma anche di definire quali colon-
ne (attributi) devono essere visualizzate (la 
Projection). 
Un esempio pratico dell'uso combinato di se-
lezione e ordinamento si manifesta nella query 
che recupera i nomi e i cognomi dei clienti 
residenti negli Stati Uniti (USA), ordinandoli 
per età in ordine decrescente. La sintassi di 
tale operazione è:  
Questa istruzione dimostra come l'utente pos-
sa applicare un filtro (WHERE country = 
"USA") per isolare un sottoinsieme di righe e 
allo stesso tempo applicare un ordinamento 
(ORDER BY age DESC) per presentare i risulta-
12

ti in base a criteri specifici, evidenziando pri-
ma i clienti più anziani tra quelli statunitensi. 
L'Arte della Congiunzione (JOIN): Tipi e 
Semantica Operativa 
L'operazione di JOIN (Congiunzione) è crucia -
le nell'SQL per combinare logicamente righe 
provenienti da due o più tabelle, basandosi su 
un attributo comune. Gli esempi forniti pre-
suppongono l'esistenza di una seconda tabel-
la, Orders (Ordini), che viene collegata alla 
tabella Customers attraverso la corrisponden-
za dei rispettivi customer_id. 
Congiunzione Interna (INNER JOIN) 
Il tipo di JOIN più restrittivo e spesso utilizzato 
è l'INNER JOIN (Congiunzione Interna), che è 
anche il tipo predefinito se si specifica sempli-
cemente JOIN. L'obiettivo semantico di que-
sta operazione è chiaro: restituire solo le righe 
dove esiste una corrispondenza tra l'attributo 
di congiunzione (customer_id) in entrambe le 
tabelle. 
La query di esempio per la Congiunzione In-
terna seleziona il nome del cliente, l'articolo 
ordinato (item) e l'importo (amount) combi-
nando i dati dei clienti e degli ordini:  
La clausola ON c.customer_id = o.custome-
r_id definisce la condizione di unione. 
Congiunzione Sinistra (LEFT JOIN) 
A differenza della Congiunzione Interna, il 
LEFT JOIN (Congiunzione Sinistra) opera ga-
rantendo l'inclusione di tutte le righe della ta-
bella di sinistra, anche se non esiste una corri-
spondenza nella tabella di destra. 
La semantica operativa implica che vengano 
restituiti tutti i clienti, inclusi quelli che non 
hanno effettuato alcun ordine. Nel caso in cui 
un cliente non abbia ordini corrispondenti, i 
campi relativi all'articolo (item) e all'importo 
(amount) provenienti dalla tabella Orders risul-
teranno con valore NULL (che indica l'assenza 
di dati validi). 
Congiunzione Destra (RIGHT JOIN) 
Il RIGHT JOIN (Congiunzione Destra) è l'ope -
razione speculare al LEFT JOIN. In questo 
caso, vengono restituite tutte le righe della 
tabella di destra (gli ordini nell'esempio), indi-
pendentemente dal fatto che esista un cliente 
corrispondente nella tabella di sinistra. 
Il significato è quello di visualizzare tutti gli 
ordini registrati. Se un ordine dovesse esistere 
senza un cliente associato (ad esempio, a cau-
sa di un'anomalia nei dati o un cliente non re-
gistrato), i campi relativi al cliente (first_name, 
last_name, ecc.) provenienti dalla tabella Cu-
stomers risulteranno NULL.  
13

L'istruzione che implementa questo compor-
tamento è:  
Congiunzione Completa (FULL JOIN) 
Il FULL JOIN (Congiunzione Completa) rap-
presenta l'operazione di unione più inclusiva, 
poiché restituisce tutte le righe da entrambe 
le tabelle, abbinando i record dove possibile. 
L'interpretazione operativa è che vengono re -
stituiti sia tutti i clienti che tutti gli ordini. Le 
regole per la gestione dei dati non corrispon-
denti sono simmetriche: se un cliente non ha 
ordini, le informazioni sull'ordine saranno 
NULL. Analogamente, se un ordine non ha un 
cliente corrispondente, le informazioni sul 
cliente saranno NULL. La query che esegue 
questa congiunzione è:  
La Proiezione (PROJECTION): Isolamento 
degli Attributi 
La Projection (Proiezione) è un concetto fon -
damentale nell'algebra relazionale che, nel-
l'ambito SQL, si realizza attraverso la specifi-
cazione delle colonne nel comando SELECT. Il 
suo scopo è selezionare solamente determina -
te colonne (attributi) da una tabella, riducendo 
così la dimensionalità del set di risultati. 
Ad esempio, se l'obiettivo è visualizzare uni -
camente i nomi dei clienti e i paesi di prove-
nienza, si utilizza una query che isola precisa-
mente questi tre attributi, escludendo età, ID 
o altri dettagli. La query di esempio fornita 
dimostra questa pura operazione di proiezio-
ne:  
Il risultato di tale operazione, come indicato 
nel materiale, mostra solo le colonne specifi-
cate. 
In sintesi, mentre l'operazione SELECT nel suo 
complesso si riferisce all'atto di interrogare e 
recuperare dati, la Projection si focalizza sulla 
scelta verticale degli attributi, risultando es-
senziale per focalizzare l'analisi su dati specifi-
ci. 
L'Apprendimento Non Supervisionato e le Tecni-
che di Clustering: Struttura nel Dato Non Eti -
chettato 
Dall'Ignoto all'Apprendimento Non Supervisio -
nato (Unsupervised Learning) 
Il termine "Ignoto" ( Unknown), in questo contesto, 
fa riferimento specifico alla mancanza di dati eti -
chettati. Poiché mancano le etichette ( labels), è 
necessario esplorare l'"Ignoto" senza alcuna forma 
di supervisione. Questo percorso introduce l'Ap -
prendimento Non Supervisionato ( Unsupervised 
Learning), una branca del machine learning  dove 
gli algoritmi mirano a scoprire pattern (schemi o 
modelli) intrinseci nei dati senza l'ausilio di esempi 
etichettati o di una guida diretta. A differenza del -
l'Apprendimento Supervisionato ( Supervised 
Learning), che opera con dati etichettati (coppie 
input-output), l'Apprendimento Non Supervisiona -
to lavora con dati non etichettati, scoprendo auto -
nomamente la struttura inerente. 
Le caratteristiche fondamentali che definiscono 
l'Apprendimento Non Supervisionato sono distin -
te e cruciali:  
• non vengono fornite etichette o output target  
(risultati attesi) durante la fase di training (adde-
stramento), il che obbliga l'algoritmo a identifica-
re autonomamente schemi, relazioni e strutture.  
14

Di conseguenza, spesso non esiste una singola 
risposta considerata "corretta" ( single 'correct' 
answer), e algoritmi differenti possono identificare 
strutture valide, ma diverse. Questo comporta una 
sfida nella fase di valutazione, poiché manca una 
Verità di Base ( Ground Truth) con cui confrontare i 
risultati. 
La Verità di Base e il Valore dell'Apprendimento 
Non Supervisionato 
La Verità di Base ( Ground Truth), nel campo della 
scienza dei dati, rappresenta i valori o le etichette 
veri e verificati utilizzati come riferimento ( bench-
mark) per addestrare e valutare i modelli. Essa in -
carna l'esito o la classificazione attuale che un mo -
dello dovrebbe idealmente prevedere.  
La Ground Truth  è indispensabile nell'apprendi -
mento supervisionato, dove i modelli imparano 
dai dati etichettati; esempi tipici includono imma -
gini etichettate come "cat" o "dog" o recensioni 
di clienti classificate come "positive" o "negative". 
Durante la valutazione, le previsioni del modello 
vengono confrontate con la Ground Truth per cal -
colare metriche prestazionali come accuratezza, 
precisione e recall (sensibilità). 
L'Apprendimento Non Supervisionato risulta par-
ticolarmente prezioso in diverse situazioni applica -
tive: quando si dispone di grandi quantità di dati 
non etichettati, quando l'obiettivo è scoprire pat-
tern nascosti senza nozioni preconcette, quando 
l'etichettatura dei dati risulterebbe proibitivamente 
costosa o richiederebbe troppo tempo, oppure 
quando è necessario comprendere la struttura na -
turale dei dati prima di applicare altre tecniche. 
A titolo di esempio, un sito di e-commerce po -
trebbe analizzare i dati di acquisto dei clienti e, 
grazie all'Apprendimento Non Supervisionato, po -
trebbe scoprire inaspettatamente che i clienti che 
acquistano attrezzi da giardinaggio comprano an -
che frequentemente mangiatoie per uccelli.  
Questa è una connessione non prevista dai marke-
ter (esperti di marketing) che apre nuove oppor-
tunità di cross-selling (vendita incrociata).  
Nel caso di grandi quantità di dati non etichettati, 
una piattaforma di social media che traccia milioni 
di interazioni giornaliere può usare il clustering per 
identificare automaticamente diversi segmenti di 
utenti basati sui loro schemi comportamentali, rive-
lando gruppi distinti come "creatori di contenuti", 
"scorridori passivi" (passive scrollers) e "connettori 
sociali". 
Un esempio in ambito medico dimostra come 
l'Apprendimento Non Supervisionato possa ridurre 
costi e tempi: in un progetto con 10.000 scansioni 
cerebrali, l'etichettatura manuale da parte di spe -
cialisti richiederebbe mesi e costi elevati.  
L'Apprendimento Non Supervisionato può rag -
gruppare scansioni simili, permettendo agli esperti 
di esaminare solo pochi esempi rappresentativi per 
ogni cluster (gruppo). Infine, comprendere la strut -
tura naturale dei dati è utile prima di applicare 
modelli supervisionati: un'azienda che analizza le 
chiamate del servizio clienti potrebbe scoprire, 
tramite l'Apprendimento Non Supervisionato, che 
esistono sette tipi distinti di problemi, rispetto alle 
sole tre categorie utilizzate nel loro sistema manua-
le, aiutando a progettare un modello supervisiona -
to più appropriato. 
Fondamenti e Scopi del Clustering 
Il Clustering è una tecnica fondamentale nell'am -
bito del machine learning e dell'analisi dei dati che 
ha come obiettivo il raggruppamento di punti dati 
simili tra loro, basandosi sulle loro caratteristiche o 
features (attributi). Essendo un metodo di Appren -
dimento Non Supervisionato, non necessita di dati 
etichettati per identificare gli schemi. 
L'obiettivo principale del clustering è organizzare 
i dati in gruppi significativi dove si verificano 2 
condizioni essenziali:  
15
• in primo luogo, gli elementi all 'interno dello 
stesso cluster (gruppo) devono essere simili tra 
loro; 
• in secondo luogo, gli elementi in cluster diversi 
devono essere dissimili l'uno dall'altro. 
La versione più semplice e basilare di analisi dei 
cluster è il partizionamento (partitioning).  
Nel clustering a partizionamento , gli oggetti di 
un dato dataset (insieme di dati) vengono organiz -
zati in diversi gruppi o cluster esclusivi. Un requisi -
to fondamentale di questo approccio è che il nu-
mero di cluster ($k$) deve essere fornito in anti -
cipo; esso costituisce il punto di partenza per i me -
todi di clustering a partizionamento.  
Formalmente, dato un dataset D di n oggetti, e un 
numero k di cluster da formare, un algoritmo di 
partizionamento organizza gli oggetti in k partizio -
ni, con la condizione che k sia minore o uguale a n. 
Esistono diverse metodologie di clustering nella 
letteratura scientifica, le più popolari includono: 
• K-means (Metodo a Partizionamento) 
• Hierarchical clustering (Clustering Gerarchi -
co) 
• DBSCAN (Density-Based Spatial Clustering 
of Applications with Noise - Clustering Spa -
ziale Basato sulla Densità di Applicazioni 
con Rumore) 
Il Clustering a Partizionamento: L'Algoritmo K-
means 
Il K-means è uno degli algoritmi di clustering più 
rappresentativi, noto per essere relativamente 
semplice e ampiamente utilizzato in settori quali la 
segmentazione dei clienti, l'analisi di immagini e il 
document clustering  (raggruppamento di docu -
menti). In questo algoritmo, la lettera " K" rappre-
senta il numero di cluster desiderati, che deve es -
sere predeterminato dall'utente. 
Il K-means opera attraverso un processo iterativo, 
affinando progressivamente i cluster fino al rag -
giungimento di una stabilità. L'obiettivo principale 
è raggruppare punti dati simili. 
Pseudo-codice e Funzionamento di K-means 
Il processo di K-means si svolge in fasi successive: 
1. Selezione di K:  Si definisce in anticipo il 
numero K di gruppi che si desidera trovare 
(ad esempio, K=3). 
2. Inizializzazione dei Centroidi:  Vengono 
posizionati casualmente K "centri" (detti 
Centroidi), che fungono da stime iniziali per 
il centro di ciascun gruppo. 
3. Assegnazione dei Punti:  Ogni punto dati 
nel dataset viene analizzato in base alla sua 
distanza dai K centroidi. Il punto viene 
quindi assegnato al gruppo il cui centroide 
è il più vicino. I punti più vicini al primo cen -
troide formano il Gruppo 1, quelli più vicini 
al secondo formano il Gruppo 2, e così via. 
4. Ricalcolo dei Centroidi:  Per ogni gruppo 
appena formato, si calcola la posizione me -
dia di tutti i punti che ne fanno parte. Que -
sta media definisce il nuovo centroide, che 
si spera sia una rappresentazione migliore 
della posizione effettiva del gruppo. 
5. Iterazione: I passi di assegnazione (3) e ri -
calcolo dei centri (4) vengono ripetuti. I 
punti vengono riassegnati al nuovo centroi -
de più vicino e i centri vengono nuovamen -
te ricalcolati. 
6. Convergenza: Il processo continua fino a 
quando i centri non si muovono più in 
modo significativo, o quando le assegna -
zioni dei gruppi non cambiano sostanzial -
mente. A quel punto, l'algoritmo ha trovato 
un insieme stabile di cluster. 
Un esempio visivo tipico è dato da un diagramma 
a dispersione ( scatter plot) che mostra una distri -
buzione di punti raggruppati con K=3, dove sono 
chiaramente identificabili i tre centroidi (C1, C2, 
C3) all'interno dei rispettivi cluster. 
16
Vantaggi e Svantaggi di K-means 
K-means presenta diversi punti di forza (Pros):  
• è concettualmente diretto e facile da implemen -
tare (Simplicity);  
• è efficiente e veloce, con una complessità tem -
porale lineare O(n \cdot k \cdot d \cdot i), dove 
n è il numero di punti dati, k è il numero di clu-
ster, d è la dimensionalità e i è il numero di itera -
zioni (Efficiency);  
• funziona bene su dataset di grandi dimensioni e 
con molte dimensioni (Scalability);  
• è garantita la convergenza verso un ottimo locale 
(Guaranteed convergence);  
• è adattabile e può essere modificato (come in k-
means++ o mini-batch k-means) per migliorarne 
le prestazioni; e i suoi risultati sono semplici da 
comprendere e spiegare (Interpretability). 
Tuttavia, K-means ha anche limitazioni ( Cons) si -
gnificative:  
• richiede obbligatoriamente la specifica del nu -
mero k di cluster in anticipo;  
• è sensibile all' inizializzazione, poiché i cluster 
finali possono variare a seconda del posiziona -
mento iniziale dei centroidi;  
• è limitato a cluster sferici (spherical clusters ) e 
funziona male quando i cluster hanno forme 
complesse;  
• è sensibile agli outliers (valori anomali) che pos -
sono distorcere significativamente il calcolo della 
media (del centroide); la sua implementazione 
standard utilizza la distanza Euclidea, che po -
trebbe non essere appropriata per tutti i tipi di 
dati;   
• a causa dell' inizializzazione casuale , non è de -
terministico, il che significa che diverse esecuzio -
ni possono produrre risultati diversi. 
È possibile trovare soluzioni di clustering K-means 
applicate a dataset di acquisti di clienti in reposito-
ry GitHub specifici. 
Il Clustering Gerarchico: Strutture Nidi ﬁcate e 
Dendrogrammi 
Il Clustering Gerarchico (Hierarchical Clustering) è 
generalmente considerato l'opposto dei metodi di 
clustering a partizionamento come K-means. A 
differenza del partizionamento, che crea una parti -
zione piatta a livello singolo, il clustering gerarchi-
co costruisce una gerarchia a più livelli di cluster 
nidiﬁcati. 
Una differenza cruciale è che il clustering gerarchi-
co non richiede la speciﬁca preventiva del nume-
ro di cluster. Mentre il clustering a partizionamen-
to ottimizza una funzione obiettivo globale, il ge -
rarchico prende decisioni locali a ogni passo (quale 
cluster unire o dividere).  
Inoltre, nel gerarchico, una volta che un punto è 
assegnato a un cluster, non può essere riassegna -
to, al contrario del K-means dove i punti possono 
muoversi durante l'ottimizzazione.  
Il risultato principale di questa tecnica è un den-
drogramma completo che mostra le relazioni tra i 
cluster a diversi livelli. 
Esistono 2 approcci principali nel clustering gerar-
chico: 
1. Agglomerativo ( bottom-up - dal basso 
verso l'alto):  Inizia trattando ogni punto 
dati come un cluster separato. Procede 
progressivamente unendo i cluster più vicini 
tra loro, continuando fino a quando tutti i 
punti non appartengono a un unico cluster. 
2. Divisivo (top-down - dall'alto verso il bas -
so): Inizia con tutti i punti in un unico clu-
ster. Divide ricorsivamente i cluster fino a 
quando ogni punto si trova nel proprio clu-
ster individuale. 
Procedura Agglomerativa e Metriche di Distanza 
17

La procedura per il Clustering Agglomerativo si 
articola in 5 passaggi: 
1. Assegnare ogni punto al proprio cluster 
individuale. 
2. Calcolare le distanze tra tutte le coppie di 
cluster. 
3. Unire i due cluster più vicini. 
4. Aggiornare le distanze tra il nuovo cluster 
risultante e tutti gli altri cluster. 
5. Ripetere i passi 3 e 4 fino a quando rimane 
un solo cluster. 
La distanza tra i cluster stessi può essere misurata 
utilizzando diversi approcci, noti come linkage: 
• Single linkage  (Collegamento Singolo): La 
distanza è misurata tra i punti più vicini nei 
due cluster. 
• Complete linkage (Collegamento Comple -
to): La distanza è misurata tra i punti più 
lontani nei due cluster. 
• Average linkage (Collegamento Medio): La 
distanza media tra tutte le coppie di punti 
tra i cluster. 
• Ward's method (Metodo di Ward): Mira a 
minimizzare l'aumento della varianza all'in -
terno del cluster (within-cluster variance) 
quando i cluster vengono uniti. 
Il Dendrogramma 
Il Dendrogramma è la rappresentazione visiva ge -
nerata (spesso utilizzando il Metodo di Ward) per il 
clustering gerarchico agglomerativo. Ogni linea 
verticale nel diagramma rappresenta l'unione di 
due cluster. L'altezza a cui due cluster vengono 
uniti riflette la distanza (o dissimiliarità) tra essi.  
Un vantaggio significativo di questo strumento è 
la possibilità di " tagliare" il dendrogramma a  
qualsiasi altezza per determinare il numero di clu-
ster desiderato; ad esempio, un taglio a una certa 
altezza specifica potrebbe produrre tre cluster. 
Applicazioni, Vantaggi e Svantaggi 
I vantaggi (Pros) del Clustering Gerarchico inclu-
dono:  
• la possibilità di una gerarchia visiva (il dendro -
gramma);  
• non richiede la specifica preliminare del conteg -
gio dei cluster;  
• è versatile grazie alla possibilità di utilizzare di -
verse metriche di distanza;  
• può scoprire cluster di varie forme;  
• è molto utile per l'esplorazione della struttura dei 
dati. 
I principali svantaggi (Cons) sono:  
• è computazionalmente costoso, con una com -
plessità temporale O(n^3) (dove n è il numero di 
punti dati); es. 10 punti da clusterizzare, 
10*10*10=1000 
• non è possibile annullare le decisioni di fusione o 
divisione (merge/split);  
• è sensibile al noise (rumore) e agli outliers; e può 
risultare difficile da interpretare con dataset mol-
to grandi. 
Un esempio pratico di applicazione è l' ottimizza-
zione della Catena di Fornitura  ( Supply Chain 
Optimization) nel settore retail (vendita al detta -
glio). Una catena nazionale con oltre 500 negozi 
affrontava sfide nella gestione dell'inventario, tra 
cui frequenti esaurimenti delle scorte (stockouts) in 
alcune sedi, inventario in eccesso in altre, aumento 
dei costi logistici e declino della soddisfazione del 
cliente.  
Gli approcci tradizionali basati su zone geografiche 
o dimensioni dei negozi non riuscivano a catturare 
efficacemente i complessi pattern di domanda. Il 
team di analisi ha implementato il clustering gerar -
chico agglomerativo con Ward's linkage per identi-
ficare raggruppamenti naturali di negozi con pat -
tern operativi simili. Hanno raccolto 18 mesi di 
18

dati, includendo la velocità di vendita per catego -
ria di prodotto, le fluttuazioni della domanda sta -
gionale, i tassi di reso, i tempi di consegna e le 
caratteristiche del mercato locale. Analizzando il 
dendrogramma, sono stati identificati sette cluster 
distinti, che rappresentavano punti di rottura natu -
rali nei pattern operativi, permettendo una gestio -
ne dell'inventario più mirata. 
DBSCAN: Raggruppamento Basato sulla Densità 
e Rilevamento del Rumore 
Il DBSCAN ( Density-Based Spatial Clustering of 
Applications with Noise), letteralmente Clustering 
Spaziale Basato sulla Densità di Applicazioni con 
Rumore, è un approccio di clustering basato sulla 
densità. Esso si distingue significativamente da K-
means e dal Clustering Gerarchico per le sue ca -
pacità specifiche. 
DBSCAN è progettato per trovare cluster di forme 
arbitrarie nei dati, identificando e isolando effica -
cemente i punti di rumore  (noise points). A diffe -
renza di K-means, che tende a trovare cluster circo-
lari o sferici, DBSCAN può identificare cluster di 
qualsiasi forma. Inoltre, come il clustering gerarchi-
co, non richiede di speci ﬁcare in anticipo il nu -
mero di cluster . DBSCAN classifica automatica -
mente gli outliers come punti di " rumore" che 
non appartengono a nessun cluster. 
Parametri e Classiﬁcazione dei Punti in DBSCAN 
Il funzionamento di DBSCAN si basa su 2 parame-
tri fondamentali: 
1. Epsilon (\epsilon): La distanza massima tra 
due punti affinché siano considerati vicini 
(neighbors). 
2. MinPts: Il numero minimo di punti richiesto 
per formare una regione densa. 
L'algoritmo classifica i punti in 3 tipologie specifi-
che: 
• Core points (Punti Centrali): Punti che han -
no almeno MinPts vicini entro la distanza 
\epsilon. 
• Border points (Punti di Bordo): Punti che si 
trovano entro la distanza \epsilon da un 
punto centrale, ma che hanno meno di 
MinPts vicini. 
• Noise points  (Punti di Rumore): Punti che 
non sono né punti centrali né punti di bor -
do. 
DBSCAN è particolarmente utile quando la quanti-
tà di cluster esistenti nei dati non è nota e quando 
i cluster possono avere forme complesse e non 
convesse, condizioni in cui algoritmi come K-
means avrebbero difficoltà. 
È possibile osservare la differenza operativa con-
frontando DBSCAN e K-means sulla stessa distri -
buzione spaziale di dati. Mentre la distribuzione 
spaziale dei cluster di K-means dipende stretta -
mente dalle coordinate dei centroidi, DBSCAN è in 
grado di raggruppare forme complesse e isolare 
punti anomali, rappresentati visivamente da punti 
bianchi che DBSCAN raggruppa o identifica come 
rumore. 
Dal Neurode al Perceptron Multistrato: Fonda -
menti Storici e Computazionali dell'Intelligenza 
Artiﬁciale Ispirata al Cervello 
L'Ispirazione Biologica e la Ricerca di Pattern nei 
Dati 
L'evoluzione dei modelli di calcolo neurale trae 
origine dall'osservazione di processi cognitivi ele -
mentari presenti nel mondo animale, in particolare 
la capacità di discernere pattern (schemi o modelli) 
nell'ambiente circostante. Già negli anni '50, gli 
etologi avevano identificato schemi comportamen -
tali significativi negli animali. Un esempio lampante 
è fornito dagli anatroccoli, i quali dimostrano la 
capacità di distinguere le proprietà degli oggetti 
che vedono muoversi subito dopo la schiusa, un 
fenomeno noto come imprinting. È stato notato 
19
che gli anatroccoli di Mullard non solo possono 
eseguire l'imprinting sulla prima creatura vivente in 
movimento, ma anche su oggetti inanimati e, signi-
ficativamente, su concetti relazionali  che gli og -
getti incorporano. 
Se gli anatroccoli vedono inizialmente due oggetti 
rossi in movimento, in seguito seguiranno due og -
getti che presentano la stessa relazione numerica 
(due oggetti), anche se il colore è differente (ad 
esempio, blu e non rosso). Questa osservazione 
rivela la capacità di individuare la similarità. Allo 
stesso modo, gli anatroccoli mostrano l'abilità di 
riconoscere la dissimilarità. Se i primi oggetti che 
vedono sono, ad esempio, un cubo e un prisma 
rettangolare, riconosceranno la differenza di forma; 
di conseguenza, seguiranno in seguito due oggetti 
diversi nella forma (come una piramide e un cono), 
ignorando due oggetti aventi la stessa forma. Tali 
capacità—rilevare somiglianze e dissomiglianze 
con una brevissima esposizione a stimoli sensoriali 
e agire in base a essi—rappresentano la base del -
l'intelligenza. Sebbene l'Intelligenza Artificiale con -
temporanea sia ancora lontana dall'implementare 
esattamente tali compiti, condivide con gli ana -
troccoli la capacità fondamentale di selezionare e 
apprendere pattern nei dati. Fu in questo contesto 
che Frank Rosenblatt inventò il Perceptron alla 
fine degli anni '50, un algoritmo innovativo e ispi -
rato al cervello che poteva apprendere modelli nei 
dati semplicemente esaminandoli. 
Le Radici Storiche del Neurode: McCulloch e 
Pitts 
Le fondamenta teoriche del Perceptron risiedono 
in un articolo pubblicato nel 1943, frutto della  col-
laborazione tra il neurofisiologo americano Warren 
McCulloch e l'adolescente prodigio Walter Pitts. 
McCulloch, con una formazione in filosofia, psico -
logia e medicina, si era precedentemente concen -
trato sulla neuroanatomia e sulla mappatura delle 
connessioni cerebrali delle scimmie, spostando 
successivamente la sua attenzione sulla "logica del 
cervello". La ricerca di McCulloch era influenzata 
dalle suggestioni dei matematici e filosofi come 
Alan Turing, Alfred North Whitehead e Bertrand 
Russell, che avevano evidenziato i legami tra logica 
e computazione. 
Il quesito centrale che guidava la ricerca di McCul -
loch era: se il cervello è un dispositivo computa -
zionale, come implementa la logica, ad esempio 
una proposizione logica come "Se P è vera E Q è 
vera, allora S è vera"?. Nel 1943, McCulloch e Pitts 
pubblicarono il saggio intitolato "A Logical Calcu -
lus of the Ideas Immanent in Nervous Activity", in 
cui proposero un modello semplice del neurone 
biologico. 
Un neurone biologico è composto da un Cell Body 
(corpo cellulare) che riceve gli input tramite le sue 
proiezioni ramificate, i Dendrites (dendriti). Il cor -
po cellulare esegue un calcolo sugli input e, in 
base ai risultati, può inviare segnali spiking (a pic -
co) lungo una proiezione più lunga denominata 
Axon (assone). Questo segnale viaggia attraverso i 
Axon Terminals (terminali assonici) per comunicare 
con i neuroni vicini. 
McCulloch e Pitts tradussero questo meccanismo 
biologico in un modello computazionale, l' artiﬁcial 
neuron (neurone artificiale), chiamato anche Neu-
rode (un neologismo che unisce "neurone" e 
"nodo"). Il Neurode è in grado di implementare 
operazioni logiche BOOLEAN (booleane) di base 
come AND, OR, NOT, che costituiscono i mattoni 
fondamentali della computazione digitale. Il fun -
zionamento di un Neurode (graficamente rappre -
sentato come un cerchio che riceve input x_1 e x_2 
e produce un output y) si basa su un calcolo sem -
20

plice: dati gli input x_1, x_2 \in {0, 1}, il Neurode ne 
somma i valori e confronta la somma con una thre-
shold (soglia), indicata con \theta. L'output y è pari 
a 1 se la somma di x_1 e x_2 è maggiore o uguale 
alla soglia (\theta), ed è 0 altrimenti. Formalmente: 
y = 1 se (x_1 + x_2) \geq \theta, altrimenti y = 0. 
L'Architettura del Perceptron di Rosenblatt e 
l'Introduzione dell'Apprendimento 
Frank Rosenblatt partì dal contributo del Neurode 
e lo estese in un nuovo modello computazionale 
caratterizzato da "neuroni artiﬁciali che si ricon ﬁ-
gurano mentre imparano, incorporando infor -
mazioni nella forza delle loro connessioni" . Ro -
senblatt, uno psicologo, non disponeva di risorse 
hardware sufficienti per testare la sua teoria e per -
tanto utilizzò un IBM 704, un gigantesco computer 
di cinque tonnellate delle dimensioni di una stanza, 
presso il Cornell Aeronautical Laboratory. L'articolo 
del 1958 che presentava il Perceptron era intitolato 
"The Design of an Intelligent Automation: Introdu -
cing the Perceptron – a Machine that Senses, Re -
cognises, Remembers, and Responds like the Hu -
man Mind". Sebbene Rosenblatt in seguito si 
rammaricò del nome Perceptron perché suonava 
troppo "macchina", intendeva con esso descrivere 
una classe di modelli del sistema nervoso. 
L'architettura del Perceptron introduce due ele -
menti fondamentali che lo distinguono dal Neuro -
de: i weights (w_i, pesi) e il bias (b, distorsione o 
termine di polarizzazione). Nel Perceptron, ogni 
input (x_i) è moltiplicato per il suo peso corrispon -
dente (w_i). 
Il calcolo eseguito dal Perceptron è una somma 
pesata e una funzione di attivazione : somma = 
w_1x_1 + w_2x_2 + \ldots + w_nx_n + b Dove b è 
il termine di Bias. 
La funzione di attivazione (di soglia) determina 
l'output y: 
• Se $somma > 0, allora y = 1 
• Altrimenti, y = -1 
Si noti che l'output del Perceptron utilizza i valori 1 
e -1, a differenza del Neurode che usava 0 e 1. La 
funzione di attivazione e la somma pesata sono 
rappresentate graficamente all'interno del nodo 
centrale del Perceptron. 
Crucialmente, a differenza del Neurode, il Percep -
tron ha la capacità di apprendere il valore corretto 
per i pesi (w_i) e per il Bias (b) per risolvere un de -
terminato problema. 
Il Processo di Apprendimento del Perceptron 
(Learning Process) 
Il processo di apprendimento del Perceptron si 
basa sull'aggiustamento iterativo dei pesi e del 
Bias in risposta agli errori di previsione, con l'obiet-
tivo di trovare un confine decisionale ottimale. 
Per illustrare il processo, si consideri un semplice 
Perceptron addestrato a prevedere se un individuo 
21

gradirà una pizza, basandosi sul livello di piccan -
tezza (x_1) e la quantità di formaggio (x_2). 
Conﬁgurazione Iniziale: 
• Pesi iniziali: w_1 = 0.5 (piccantezza), w_2 = 
0.5 (formaggio). 
• Bias iniziale: b = -1 (scelto arbitrariamente). 
• Funzione di attivazione: Se (somma pesata 
+ bias) > 0, l'output è +1 (gradisce); altri -
menti l'output è -1 (non gradisce). 
Esempio di Addestramento (a): Classi ﬁcazione 
Corretta 
• Input: Poco piccante (x_1 = 2), molto for -
maggio (x_2 = 3). Target (etichetta di ad -
destramento): +1 (gradisce la pizza). 
• Calcolo della somma pesata: y = (0.5 \ti -
mes 2) + (0.5 \times 3) - 1 = 1 + 1.5 - 1 = 
1.5. 
• Previsione: Poiché 1.5 > 0, l'output è $+1. 
La previsione è corretta, in quanto corri -
sponde al target. 
Esempio di Addestramento (b): Misclassi ﬁcazio-
ne e Aggiornamento dei Pesi 
• Input: Molto piccante (x_1 = 5), poco for -
maggio (x_2 = 1). Target: -1 (non gradisce 
la pizza). 
• Calcolo della somma pesata: y = (0.5 \ti -
mes 5) + (0.5 \times 1) - 1 = 2.5 + 0.5 - 1 = 
2. 
• Previsione: Poiché 2 > 0, l'output è +1 
(gradisce la pizza). 
• Errore: Vi è una misclassiﬁcation (errore di 
classificazione), poiché il target è -1 ma la 
previsione è +1. 
Aggiornamento dei Pesi (Weight Update) L'algo-
ritmo di apprendimento aggiusta i pesi in base a 
questo errore di previsione, muovendo il confine 
decisionale. Supponendo un Learning Rate  (tasso 
di apprendimento) \alpha = 0.1. 
La regola di aggiornamento del peso è: \Delta w_i 
= \alpha \times (target - prediction) \times x_i. 
1. Aggiornamento del peso w_1: \Delta w_1 
= 0.1 \times (-1 - (+1)) \times 5 = 0.1 \times 
(-2) \times 5 = -1. 
2. Aggiornamento del peso w_2: \Delta w_2 
= 0.1 \times (-1 - (+1)) \times 1 = 0.1 \times 
(-2) \times 1 = -0.2. 
3. Aggiornamento del Bias: \Delta bias = 0.1 
\times (-1 - (+1)) = -0.2. 
I nuovi pesi dopo l'aggiornamento sono: 
• w_1 = 0.5 - 1 = -0.5 
• w_2 = 0.5 - 0.2 = 0.3 
• bias = -1 - 0.2 = -1.2. 
Il processo di addestramento continua finché non 
vengono soddisfatti specifici criteri di arresto. I cri -
teri di convergenza (Convergence Criteria) inclu -
dono la classificazione corretta di tutti gli esempi di 
addestramento o l'assenza di aggiornamenti dei 
pesi in un intero ciclo ( epoch) sui dati di addestra -
mento. I meccanismi pratici di arresto possono in -
cludere un limite massimo di iterazioni o l'assenza 
di misclassificazioni nell'ultimo ciclo completo. 
Vincoli e Limitazioni del Perceptron: Il Concetto 
di Linearmente Separabile 
Il Perceptron ha una limitazione fondamentale le -
gata alla natura dei dati che può classificare: la li-
near separability (separabilità lineare). 
I Dati Linearmente Separabili  (Linearly Separable 
Data) sono un insieme di punti che possono essere 
perfettamente divisi in due classi distinte traccian -
do una singola linea retta (in due dimensioni) o un 
hyperplane (iperpiano) in dimensioni superiori. 
Questo concetto è cruciale perché determina  l'effi-
cacia dell'algoritmo Percep -
tron nel trovare un confine 
decisionale. 
Quando i dati sono linear -
mente separabili, l'algoritmo 
22

di apprendimento del Perceptron è garantito di 
convergere(converge), il che significa che troverà 
un insieme di pesi capace di classificare corretta -
mente tutti gli esempi di addestramento dopo un 
numero finito di iterazioni. 
Al contrario, se i dati non sono linearmente sepa -
rabili, il Perceptron non convergerà e continuerà 
indefinitamente a commettere errori di classifica -
zione. 
Un'immagine (un diagramma cartesiano) illustra 
questo concetto di separabilità lineare, mostrando 
punti dati di due classi diverse (cerchi blu e croci 
rosse) disposti nello spazio definito da due features 
(caratteristiche). L'asse X è la Feature 1 e l'asse Y è 
la Feature 2. Tali punti, che potrebbero rappresen -
tare ad esempio i clienti in base alla localizzazione 
geografica e alla spesa, sono chiaramente separati 
da una singola linea retta, a conferma che sono 
linearmente separabili. L'applicazione pratica del 
Perceptron include la classificazione di spam/non-
spam. 
L'Evoluzione verso il Perceptron Multistrato 
(MLP) 
Per superare le restrizioni del Perceptron, in parti -
colare la sua incapacità di gestire dati non linear -
mente separabili, è stato sviluppato il Multilayer 
Perceptron (MLP), che mantiene i concetti primari 
del Perceptron ma introduce maggiore complessi -
tà. 
Le differenze principali nell'architettura MLP (visibi -
le in un diagramma come una rete di nodi disposti 
in strati) includono: 
1. Molteplici Strati: Un Input Layer (strato di 
ingresso), uno o più Hidden Layers  (strati 
nascosti), e un Output Layer(strato di usci -
ta). 
2. Funzioni di Attivazione Non Lineari:  L'in-
troduzione di funzioni di attivazione non 
lineari (come la sigmoid o la ReLU, Recti-
ﬁed Linear Unit). 
Il Perceptron Multistrato può modellare conﬁni 
decisionali complessi e non lineari  e apprendere 
rappresentazioni gerarchiche delle caratteristi -
che. Le relazioni intricate tra input e output sono 
modellate grazie agli strati nascosti, che imparano 
higher level features (caratteristiche di livello supe -
riore) a partire dai dati grezzi. 
Gli Strati Nascosti (Hidden Layers) 
Gli strati nascosti rappresentano i livelli intermedi 
tra l'input e l'output. Matematicamente, la loro 
funzione è trasformare lo spazio degli input in uno 
spazio di features più separabile, rendendo possi -
bili classificazioni complesse. 
Funzioni e Meccanismi:  Gli strati nascosti trasfor -
mano le caratteristiche di input attraverso combi -
nazioni lineari pesate e applicano successivamente 
le funzioni di attivazione non lineari . Questo pas-
saggio è essenziale per introdurre la complessità 
necessaria per gestire dati non linearmente sepa -
rabili. Essi ricevono gli input pesati dallo strato 
precedente, applicano la funzione di attivazione 
(come ReLU o Sigmoid) e generano transformed 
features (caratteristiche trasformate) che vengono 
trasmesse agli strati successivi. Più si avanza negli 
strati, più le caratteristiche apprese sono di alto 
livello. 
Caratteristiche Chiave:  Gli strati nascosti sono 
spesso considerati una black box  (scatola nera) 
poiché non sono direttamente osservabili dall'e -
sterno della rete. Il numero di neuroni in questi 
strati determina la capacità rappresentativa del 
modello. I pesi all'interno dello strato nascosto 
23

apprendono rappresentazioni di caratteristiche 
intermedie. 
Funzioni di Attivazione Non Lineari:  Le funzioni 
Sigmoid e ReLU sono introdotte per dotare l'archi -
tettura di non linearità, permettendo di trattare 
dati non linearmente separabili. 
• Funzione Sigmoid:  Graficamente, mostra 
una curva a S, con un range di output 
compreso tra 0 e 1, centrato a 0.5. 
• Funzione ReLU (Recti ﬁed Linear Unit):  
Graficamente, la funzione è nulla per tutti i 
valori di input negativi (x < 0) e cresce li -
nearmente per i valori positivi. 
Il meccanismo di apprendimento in un MLP utilizza 
la backpropagation (retropropagazione), un pro -
cesso per aggiornare i pesi attraverso tutti gli stra -
ti, ritornando indietro dall'output agli strati inter -
medi. 
Rilevanza Contemporanea 
Il Perceptron, pur nella sua semplicità, è fonda -
mentale per l'apprendimento di concetti chiave 
nell'IA, inclusi il processo di addestramento, la 
somma pesata degli input, il Bias, il Learning Rate, 
l'Prediction Error  (errore di previsione) e la com -
prensione dei dati linearmente separabili. 
Il MultiLayer Perceptron (MLP) estende il Percep -
tron aggiungendo non linearità tramite le funzioni 
di attivazione e gli strati nascosti. L'MLP è ampia -
mente adottato oggi perché può inferire cono -
scenza da una vasta gamma di scenari reali, dove i 
dati sono ricchi di non linearità. Inoltre, l'MLP è 
spesso preferito per certe applicazioni grazie al suo 
costo computazionale relativamente contenuto 
rispetto ai metodi di deep learning (apprendimen-
to profondo) più complessi. 
In sostanza, se il Perceptron funge da semplice 
classificatore lineare—come un confine netto che 
separa i punti sul piano—il Perceptron Multistrato 
è come un sistema di canali complessi e intercon -
nessi che possono curvarsi e intrecciarsi nello spa -
zio dimensionale, consentendogli di distinguere 
forme e relazioni molto più complesse e sfumate. 
Analisi dei Dati Testuali e Text Mining: Concetti 
Fondamentali, Applicazioni e S ﬁde nell'Era dei 
Modelli Linguistici di Grandi Dimensioni (LLM) 
Contesto Accademico e Fondamenti Deﬁnitori 
Il campo del Text Mining (Estrazione di Informa -
zioni dal Testo) e della Text Analytics (Analisi del 
Testo) costituisce un pilastro fondamentale nei 
programmi avanzati di intelligenza artificiale, come 
dimostrato dalla sua inclusione nel programma 
post-laurea "AI for Business and Society" per 
l'Anno Accademico 2025-2026. Il Text Mining è 
una disciplina complessa e multidisciplinare che 
integra l'Elaborazione del Linguaggio Naturale 
(Natural Language Processing  - NLP), la Classifica -
zione di Pattern (Pattern Classification) e il Machine 
Learning (Apprendimento Automatico). 
A causa della sua natura ibrida, il Text Mining non 
possiede una definizione canonica universalmente 
accettata. Per questo motivo, si ricorre spesso a 
definizioni mutuate dal più ampio campo del Data 
Mining (Estrazione di Dati). Una definizione essen -
ziale per il Text Mining è "l'estrazione non banale 
di fatti impliciti, precedentemente sconosciuti e 
interessanti da una raccolta di testi" . In parallelo, 
il Data Mining è definito come l'estrazione non 
banale di informazioni implicite, precedentemente 
sconosciute e potenzialmente utili dai dati. Dal 
punto di vista aziendale, il glossario Gartner de -
scrive il Text Mining come "il processo di estra -
zione di informazioni da raccolte di dati testuali 
e il loro utilizzo per obiettivi di business" . In tutti 
i casi, il Mining implica compiti quali la scoperta, la 
24

ricerca, l'induzione e il perfezionamento ( refine-
ment), poiché le informazioni cercate sono spesso 
latenti e celate nel testo. 
La Struttura del Contenuto Testuale e la Sua Ri -
levanza per il Text Mining 
Il Text Mining si concentra sull'analisi e la modella -
zione del contenuto in linguaggio naturale. Una 
caratteristica cruciale dei dati testuali è che sono 
quasi sempre non strutturati, a differenza dei dati 
gestiti in ambienti come database o data warehou -
se. È essenziale distinguere tra le diverse tipologie 
di dati basate sul loro livello di organizzazione. 
I Dati Strutturati (Structured Data) presentano un 
alto grado di organizzazione, tipicamente disposti 
in modo tabellare o simile a un foglio di calcolo. 
Esempi di questa tipologia includono file CSV 
(Comma-separated value file ), tabelle di database 
relazionali e fogli di calcolo Excel. Si stima che i 
dati strutturati costituiscano circa il 20% del volu -
me totale dei dati a livello globale. A un livello in -
termedio si collocano i Dati Semi-strutturati  
(Semi-structured Data ), che possiedono un certo 
grado di organizzazione, spesso caratterizzata da 
una struttura gerarchica. Ne sono esempi i file 
HTML, XML e Json. Infine, i Dati Non Strutturati  
(Unstructured Data) sono privi di un'organizzazione 
predefinita. Esempi di dati non strutturati includo -
no documenti PDF, file Word e semplici file di te -
sto. Attualmente, la maggior parte dei dati che 
vengono generati quotidianamente, come i post 
sui social media (ad esempio, Tweets e Facebook 
posts), ricade in questa categoria non strutturata. 
Distinzione Funzionale tra Text Mining e Natural 
Language Processing (NLP) 
Nonostante la stretta integrazione tecnologica, 
Text Mining e NLP perseguono obiettivi diversi. Il 
Natural Language Processing (NLP) , le cui origini 
risalgono agli anni '50, ha l'obiettivo primario di 
comprendere il linguaggio umano, concentrandosi 
sull'analisi della sintassi grammaticale, del parlato 
o del testo. L'obiettivo storico dell'NLP è rendere i 
computer capaci di comprendere il linguaggio 
umano. 
Al contrario, il Text Mining è impiegato per estrar -
re informazioni da contenuti, siano essi strutturati o 
non strutturati. Mentre l'NLP si concentra prima -
riamente sul significato (la semantica) del contenu -
to, il Text Mining pone maggiore enfasi sull'estra -
zione della struttura (le relazioni, i fatti impliciti). 
Storicamente, le prime applicazioni di Text Mining 
(fine anni '90) applicavano algoritmi di Data Mining 
e Machine Learning direttamente sul testo, senza 
ricorrere alle tecniche di NLP . Solo successivamen-
te il Text Mining ha incorporato l'NLP; tuttavia, ne -
gli ultimi dieci anni, i due campi hanno sviluppato 
intersezioni e punti comuni, pur mantenendo scopi 
finali distinti. 
Nel contesto applicativo, le problematiche che il 
Text Mining è chiamato ad affrontare possono es -
sere raggruppate in due scenari principali: utenti 
che hanno domande speciﬁche ma non conosco -
no la risposta , e utenti che hanno chiaro l'ambito 
o l'obiettivo generale ma non hanno formulato 
domande speciﬁche. 
Domini di Applicazione e Dinamiche di Mercato 
della Text Analytics 
Il Text Mining è una tecnologia pervasiva, spesso 
incorporata in diverse applicazioni aziendali e so -
ciali. I suoi domini applicativi sono vasti e includo -
no: Economia, Gestione Sociale, Servizi Informativi, 
Gestione del Rischio di Sicurezza, Servizio di Assi -
25

stenza Clienti ( Customer Care Service ), Rilevamen-
to di Frodi (Fraud Detection), Business Intelligence, 
Analisi dei Social Media, Previsione dell'Abbando -
no del Cliente ( Customer Churn Prediction ), Siste-
mi di Domanda e Risposta ( Q&A Systems) e Mar -
keting. 
Nel Marketing, l'analisi del sentiment ( Sentiment 
Analysis), ad esempio, è uno strumento eccellente, 
utilizzato per categorizzare e valutare i risultati del -
le risposte ai sondaggi, comprendere l'esperienza 
complessiva del cliente ( customer experience ) e 
misurare l'interesse verso nuovi prodotti. Un esem -
pio di integrazione profonda del Text Mining si 
trova nei sistemi Q&A, dove esso supporta compiti 
quali la ricerca nella base di conoscenza, l'inferenza 
e il filtraggio delle risposte potenziali, oltre all'ana -
lisi della domanda (question parsing). 
Dal punto di vista economico, il mercato della Text 
Analytics è caratterizzato da una robusta crescita. I 
dati di mercato per il periodo 2018-2028 indicano 
un Tasso di Crescita Annuale Composto ( Com-
pound Annual Growth Rate - CAGR) del 17,35%. Il 
grafico a barre fornito illustra chiaramente questa 
tendenza, mostrando che il volume di mercato 
previsto per il 2026 è sensibilmente superiore a 
quello registrato nel 2021. L'area geografica con la 
crescita più rapida è l'Asia Pacifico, mentre il mer -
cato più grande in termini assoluti è il Nord Ameri -
ca. Tra gli attori principali (Major Players) del setto-
re figurano SAS, Microsoft, IBM, SAP e Clarabrid -
ge. 
I Compiti Centrali del Text Mining Tradizionale 
L'analisi testuale standard comprende sette compi-
ti principali (tasks), che sono fondamentali per 
l'estrazione di conoscenza dai testi non strutturati. 
Classiﬁcazione e Raggruppamento del Testo 
Il compito di Classiﬁcazione del Testo (Text Classi-
fication) mira a dividere un testo in categorie o tipi 
predefiniti. Essa è considerata una tecnologia di 
classificazione di pattern. Un esempio di questa 
operazione è la Classificazione Bibliotecaria Cine -
se, che raggruppa tutti i libri in cinque categorie e 
ventidue sottocategorie, basando la classificazione 
sul contenuto. 
Diversamente, il Clustering del Testo (Text Cluste-
ring) è un processo che divide il testo in diverse 
categorie senza fare affidamento su categorie pre -
definite. Il numero e la natura delle categorie 
emerse dipendono da specifici indici e criteri di 
valutazione. Questo può portare alla clusterizzazio -
ne del testo in macro-aree tematiche (come sport, 
finanza o intrattenimento) o, basandosi su prospet -
tive soggettive, in categorie come positive (atteg -
giamenti supportivi) o negative (atteggiamenti 
passivi). Il diagramma visivo del Text Clustering  
mostra la separazione di diversi punti colorati in tre 
gruppi distinti, circondati da ellissi, rappresentando 
il principio del raggruppamento dei dati per simila-
rità intrinseca. 
L'Estrazione di Argomenti e Sentimenti 
Il Modello di Argomento  (Topic Model) è un ap -
proccio statistico che assegna un valore di probabi-
lità di argomento a ciascuna parola. Un argomento 
è concettualmente definito da parole che condivi -
dono forti relazioni semantiche e concettuali, e 
ogni argomento è associato a un proprio dizionario 
specifico. La figura che illustra il Topic Model evi-
denzia come un singolo documento sia composto 
da una miscela di argomenti, ciascuno rappresen -
26

tato da una serie di parole chiave e probabilità (ad 
esempio, "gene", "dna", "genetic" con probabili -
tà 0.04 e 0.02). L'immagine mostra come le parole 
nel testo vengano assegnate a specifici argomenti 
e come le proporzioni complessive dei topic all'in -
terno del documento vengano visualizzate tramite 
un istogramma. 
L'Analisi del Sentiment e Opinion Mining  si con -
centra sull'estrazione dell'informazione soggettiva 
veicolata dagli autori, con l'obiettivo di rivelare il 
loro punto di vista e atteggiamento. I compiti prin -
cipali includono la Classificazione del Sentiment e 
l'Estrazione degli Attributi. La Classificazione del 
Sentiment può essere considerata una forma spe -
cializzata di Classificazione del Testo, in cui la clas -
sificazione avviene su basi soggettive. Questa ana -
lisi è cruciale quando, per esempio, un'azienda 
cerca di monitorare tempestivamente le valutazioni 
dei clienti su un nuovo prodotto o quando la rete 
viene inondata da commenti in seguito a un even -
to. 
Il Rilevamento e Tracciamento di Argomenti  (To-
pic Detection and Tracking) si occupa di identifica -
re e monitorare gli argomenti che polarizzano l'at -
tenzione pubblica (hot topics) attraverso l'analisi di 
notiziari e commenti. Tali tecniche sono essenziali 
nell'analisi delle opinioni. 
Estrazione di Informazioni e Riassunto Automa -
tico 
L'Estrazione di Informazioni  ( Information Extrac -
tion - IE) è il processo di estrazione di dati fattuali 
precisi – come entità, attributi di entità, relazioni 
tra entità ed eventi – da contenuti semi-strutturati 
e non strutturati provenienti da fonti come docu -
menti accademici, social media o notizie web.  
L'IE include compiti specifici come il Riconosci -
mento di Entità Nominate ( Named Entity Recogni-
tion), la Disambiguazione di Entità ( Entity Disambi-
guation), l'Estrazione di Relazioni ( Relationship Ex-
traction) e l'Estrazione di Eventi ( Event Extraction). 
Le relazioni in IE si riferiscono a collegamenti se -
mantici tra due o più concetti. L'Estrazione di 
Eventi è particolarmente tecnica: mentre nel lin -
guaggio comune l'evento è una narrazione con 
riferimenti temporali e spaziali, nell'IE l'evento è un 
determinato stato o azione "attivato" da un verbo 
all'interno di una specifica struttura predicativa 
(predicate framework). 
Infine, il Riassunto Automatico del Testo  ( Auto-
matic Text Summarisation ) è una tecnologia che 
utilizza metodi NLP per generare automaticamente 
riassunti. In un contesto di saturazione informativa, 
le aziende utilizzano questo strumento per estrarre 
rapidamente gli estratti più significativi dal testo. 
Tuttavia, un limite importante risiede nella difficoltà 
di creare strumenti "intelligenti" capaci di com -
prendere non solo la grammatica, ma anche la se -
mantica profonda di un testo. 
I Modelli Linguistici di Grandi Dimensioni (LLM) 
I Modelli Linguistici di Grandi Dimensioni (LLM) 
hanno introdotto una nuova era per l'NLP e il Text 
Mining. Sebbene i metodi standard rimangano in 
uso, gli LLM sono oggetto di studio approfondito. 
Questi modelli, ancora in fase di sviluppo, hanno la 
capacità di eseguire una vasta gamma di compiti 
complessi. Tra le loro funzioni figurano la genera -
zione di diversi formati di testo creativo (come co -
27

dice, poesie o email), la capacità di seguire istru -
zioni e completare richieste in modo ponderato e 
di rispondere a domande in modo completo e in -
formativo, anche se aperte o inusuali. 
Un concetto fondamentale è l' LLM Foundation 
Model (Modello Fondamentale LLM), definito 
come un modello linguistico pre-addestrato di 
grandi dimensioni utilizzato per una varietà di 
compiti di NLP . Questi modelli sono addestrati su 
enormi volumi di dati testuali e possono essere 
impiegati per la traduzione linguistica, la genera -
zione di testo e la risposta a domande. Le immagi -
ni fornite indicano la rapida diffusione di questi 
modelli ("It's raining LLMs"), citando esempi noti 
come ChatGPT, Vicuna (un Open-Source LLM ), 
Falcon LLM  (definito "King of Open-Source 
LLMs"), Claude (sviluppato da Anthropic) e Gemi-
ni, oltre a varianti di Llama 3.1 con diversi parame-
tri (8B, 70B, 405B). 
È cruciale distinguere tra un Modello Fondamenta -
le LLM generico e ChatGPT. La differenza risiede 
nella loro specializzazione. Un Modello Fondamen -
tale LLM ha uno scopo di NLP generico ed è adde -
strato su quantità massicce di dati testuali, puntan -
do a versatilità e accuratezza. ChatGPT è invece 
un LLM speci ﬁco che è stato ottimizzato ( fine-
tuned) per il dialogo conversazionale . È stato 
addestrato su un dataset di testo e codice, e il suo 
compito principale è generare conversazioni di 
chat coerenti e realistiche, con punti di forza nella 
fluidità e nel realismo, pur avendo un ambito di 
applicazione più limitato rispetto al modello fon -
damentale non ottimizzato. 
Principali Sﬁde e Limitazioni Tecniche 
Il percorso del Text Mining e dell'NLP è costellato 
di sfide che limitano l'accuratezza e la completezza 
dei risultati. 
Una difficoltà rilevante è rappresentata dal rumore 
e dalle espressioni mal formate . Mentre i testi 
formali (pubblicazioni accademiche, articoli politici) 
seguono regole semantiche standard, il testo onli -
ne presenta una quantità significativa di espres -
sioni non standardizzate o mal formate. Ciò ridu -
ce l'accuratezza dei compiti di NLP e Text Mi -
ning; per esempio, la segmentazione delle paro -
le cinesi ( Chinese Word Segmentation ) vede i 
suoi tassi di accuratezza scendere al di sotto del 
90% nel testo online, rispetto a oltre il 95% sui 
testi più strutturati. 
Un'altra sfida complessa è l' ambiguità e l'occul-
tamento della semantica del testo. Il linguaggio 
naturale è ambiguo: una parola come "Bank" può 
significare sia un istituto finanziario che la riva di un 
fiume, mentre "Apple" può riferirsi al frutto o al 
prodotto tecnologico. L'ambiguità si estende alla 
struttura sintattica delle frasi, come nel caso di "Ho 
visto un ragazzo con un telescopio", dove l'inter -
pretazione (il ragazzo aveva il telescopio o io ho 
usato il telescopio per vedere il ragazzo?) rimane 
indefinita (contesto). Attualmente, i sistemi NLP 
trovano difficile risolvere queste ambiguità, e non 
esistono metodi completamente efficaci per supe -
rare tale ostacolo. 
28

Inoltre, i metodi moderni di Text Mining, basati su 
Machine Learning e Deep Learning , richiedono 
grandi quantità di dati annotati  per l'addestra -
mento. La raccolta di tali dati da fonti online è resa 
difficile dalla presenza di contenuti protetti da co -
pyright. Anche quando il copyright non è un pro -
blema, il contenuto online è spesso formattato 
male, rendendo necessari numerosi passaggi di 
pre-elaborazione. La difficoltà aumenta quando i 
contenuti riguardano aree specialistiche, richie -
dendo l'intervento di esperti per l'annotazione 
manuale, un processo dispendioso. 
La Sﬁda della Rappresentazione Vettoriale 
Una sfida specifica e fondamentale riguarda la 
Rappresentazione Vettoriale delle Parole  (Word-
Vector Representation o Word Embedding). Que -
sta tecnica in NLP converte parole e frasi in vettori 
numerici. L'obiettivo è codificare le relazioni se -
mantiche e sintattiche tra le parole. Un metodo di 
rilievo è word2vec, sviluppato da Google, che uti -
lizza architetture come continuous bag-of-words  
(CBOW) e continuous skip-gram, entrambe basate 
sulla predizione delle parole circostanti data una 
parola centrale. I vettori numerici risultanti (Em -
beddings) rappresentano la parola; ad esempio, in 
una frase come "The King is born", ogni parola è 
associata a una colonna di valori numerici. La rap -
presentazione vettoriale riesce a catturare le di -
mensioni semantiche; ad esempio, associando 
concetti come animal (animale), domesticated(ad-
domesticato) o fluffy (soffice) a vettori numerici di 
parole specifiche (es. dog, cat). 
Nonostante l'efficacia a livello lessicale, il limite 
risiede nel collegamento della semantica delle 
singole parole alla semantica di insiemi più 
grandi di parole , come frasi, proposizioni, para -
grafi e la semantica del discorso ( discourse seman-
tics). Sebbene i metodi di Machine Learning siano 
efficaci nella rappresentazione semantica delle sin -
gole parole, l'elaborazione della semantica di inte -
re frasi e paragrafi non risulta altrettanto immedia -
ta. 
Estrazione e Analisi del Testo: Acquisizione, Pre-
elaborazione e Strumenti di Linguistica Compu -
tazionale Avanzata 
Il presente documento accademico esplora le me -
todologie e le tecniche fondamentali impiegate 
nell'ambito del Data Mining e della Text Analytics 
(Analisi del Testo), concentrandosi in particolare 
sulle fasi cruciali di acquisizione, annotazione e 
pre-elaborazione dei dati testuali, elementi essen -
ziali per i programmi post-laurea in Intelligenza 
Artificiale ( AI for Business and Society ), come illu -
strato nella Lecture 05: Text Mining 2  tenuta dal 
Prof. Alessandro Bruno. L'intero processo di estra -
zione della conoscenza dal testo può essere con -
cettualizzato, come suggerito da un'immagine 
chiave, come un imbuto di ﬁltraggio ( funnel). 
Questo imbuto poligonale, composto da punti 
interconnessi, riceve una vasta quantità di dati di -
spersi e disordinati dall'alto (che rappresentano il 
"rumore" o i dati grezzi), elaborandoli e concen -
trandoli in un flusso ridotto e strutturato in uscita. 
Tale metafora visiva evidenzia l'obiettivo principale 
di queste discipline: trasformare i macro-dati non 
strutturati in informazioni concise e fruibili. 
Acquisizione dei Dati: Fonti e Sﬁde di Dominio 
L'acquisizione dei dati testuali rappresenta il primo 
passo in qualsiasi progetto di Text Mining. Le fonti 
di dati possono essere distinte in due categorie 
principali, ciascuna con le proprie implicazioni per 
il trattamento e la preparazione. 
Dati di Dominio Aperto e Chiuso 
I dati possono provenire da Domini Chiusi (Closed 
Domain Data ) o Domini Aperti  ( Open Domain 
29
Data). I Domini Chiusi sono ambienti specifici e 
altamente specializzati, come il campo finanziario o 
i sistemi sanitari ( Healthcare Systems ). In questi 
contesti, i documenti contengono termini molto 
specifici; ad esempio, nel campo finanziario si in -
contrano termini relativi a investimenti e finanzia -
menti, mentre nei sistemi sanitari le Cartelle Clini -
che Elettroniche ( EHR - Electronic Health Records ) 
sono sature di terminologia medica. 
Affidarsi esclusivamente ai dati di un dominio spe -
cifico potrebbe non essere sufficiente per l'analisi, 
poiché l'interpretazione di tali dati richiede una 
conoscenza professionale di dominio . Di conse -
guenza, le fonti di dati pubblicamente disponibili 
sono spesso utilizzate per compensare le informa -
zioni mancanti o la ristrettezza del contesto nei 
Domini Chiusi. 
I Domini Aperti includono fonti di dati accessibili 
al pubblico come Wikipedia, Baidu (un motore di 
ricerca e enciclopedia cinese), enciclopedie e libri 
di testo. Tuttavia, è fondamentale notare che i Pu-
blic Networks (Reti Pubbliche) tendono a contene -
re espressioni molto più rumorose ( noisy) e mal 
formate. Questa caratteristica richiede un notevole 
overhead processing , ovvero la necessità di ese -
guire complesse routine di pulizia e pre-elabora -
zione per rendere i dati utilizzabili. 
Il Caso di Studio IMDB e l'Estrazione Web ( Web 
Scraping) 
Un esempio pratico di acquisizione di dati da Do -
minio Aperto è il caso di studio di IMDb (Internet 
Movie Database). IMDb è un sito molto popolare 
che fornisce agli utenti commenti e recensioni sui 
film, ed è ricco di collegamenti a contenuti cinema -
tografici. Gli utenti possono visualizzare facilmente 
voti e commenti, con una grande quantità di re -
censioni consultabili cliccando sull'icona della stella 
gialla. 
Il processo di Estrazione Web  ( Web Scraping ) o 
Web Crawling (letteralmente, "scansione web") si 
pone come soluzione per scaricare automatica -
mente l'intero contenuto delle recensioni. Utiliz -
zando il linguaggio di programmazione Python, 
strumenti come la libreria urllib2 possono aiutare a 
scaricare l'intero contenuto della sezione desidera -
ta. La possibilità di effettuare un crawling (scansio-
ne automatica) è essenziale, ad esempio, per scor -
rere tutte le recensioni degli utenti fino in fondo 
alla pagina. 
Il Protocollo Robots.txt e le Considerazioni Eti -
che 
Prima di procedere con l'estrazione automatica dei 
contenuti di una pagina web, è prassi comune e 
necessaria verificare il protocollo robots del sito. 
Questo protocollo è specificato in un file denomi -
nato Robots.txt. Il Robots.txt è un file che contie -
ne tutte le limitazioni imposte dal proprietario del 
sito contro la scansione automatica ( crawling). Ad 
esempio, l'URL specifico https://www.imdb.com/
robots.txt contiene il protocollo con un elenco di 
limitazioni. 
Nel contesto del caso IMDB, si è osservato che, 
non essendoci restrizioni in atto per scaricare il 
contenuto delle recensioni, il proprietario del sito 
consente agli utenti/sviluppatori di effettuare il 
crawling di tali contenuti. Sebbene il file robots.txt, 
introdotto come " Robots Exclusion Protocol ", non 
imponga vincoli legali contro il web scraping, esso 
svolge un ruolo cruciale nello stabilire le aspettati -
ve e le autorizzazioni del proprietario del sito web 
riguardo all'accesso automatizzato. È inoltre rac -
comandato che il crawling dei contenuti avvenga 
durante periodi di bassa attività di rete, tipicamen -
te durante la notte. 
Per l'estrazione vera e propria dei contenuti della 
pagina web e per ottenere i collegamenti alla pa -
gina successiva, un kit di strumenti ( toolkit) basato 
30
su Python chiamato Beautiful Soup è ampiamente 
utilizzato. 
Processi di Pulizia e Annotazione dei Dati 
Una volta acquisito il contenuto testuale, esso 
deve sottoporsi a processi di data cleaning (pulizia 
dei dati) e di pre-elaborazione per eliminare il ru-
more e prepararlo per l'analisi. 
Rimozione del Rumore e dei Simboli Speciali 
I contenuti delle pagine web sono spesso pieni di 
simboli speciali che non hanno significato semanti -
co per l'analisi del testo. Il compito di analizzare e 
depurare il contenuto è chiamato parsing. Esempi 
di questi simboli speciali includono &nbsp; (che 
rappresenta uno spazio non divisibile, non-brea-
king space) e &lt; (che rappresenta il simbolo "mi -
nore di", less than). 
Una tabella chiarisce ulteriormente questi simboli e 
le relative entità HTML ( Entity Name): 
La finalità della rimozione dei simboli speciali è la 
riduzione del rumore  ( Noise Reduction ), che eli -
mina caratteri irrilevanti che possono ostacolare 
l'analisi, e la standardizzazione, garantendo un 
formato di dati coerente. Ciò comporta un miglio-
ramento dell'accuratezza  ( Improved Accuracy ), 
focalizzando l'analisi sugli elementi testuali essen -
ziali. L'impatto sul Text Mining è significativo, con -
sentendo una rilevazione del sentimento più preci -
sa ( Sentiment Analysis ), una più chiara identifica -
zione dei temi sottostanti ( Topic Modeling) e una 
maggiore accuratezza nella categorizzazione del 
testo (Text Classification). 
Oltre ai simboli speciali, la fase di elaborazione del 
rumore ( Noise Processing ) rimuove elementi te -
stuali come il simbolo "@" (spesso seguito da un 
nome utente) o collegamenti pubblicitari, in quan -
to non sono significativi per il Text Mining. L'elimi-
nazione di questi elementi è tipicamente realizzata 
attraverso approcci basati su regole ( Rule-based) o 
modelli (template-based). 
Gestione dei Dati Brevi e Mappatura delle Eti -
chette 
All'interno dell'acquisizione dei dati, si effettua 
anche la rimozione dei commenti ritenuti troppo 
brevi e quindi potenzialmente privi di significato 
(meaningless). Per attuare questa rimozione, è ne -
cessaria la segmentazione delle parole  ( word 
segmentation) per ottenere un conteggio accurato. 
Mentre nel contenuto in lingua inglese il conteggio 
delle parole è relativamente semplice (si basa sul 
conteggio degli spazi), lingue come il cinese ri -
chiedono la combinazione di caratteri separati per 
formare parole. Un sistema basato su regole sem -
plice può eliminare tutte le parole composte da un 
numero di caratteri inferiore a una certa soglia (ad 
esempio, meno di tre caratteri). 
Un altro passaggio cruciale è la Mappatura delle 
Etichette (Mappings of labels ), necessaria quando 
le etichette "nascoste" nel codice HTML del sito 
web differiscono per numero o nome da quelle 
previste da un classificatore. Questo passaggio è 
richiesto per risolvere qualsiasi ambiguità tra i due 
gruppi di categorie-etichette. 
31

Un esempio illustrativo si verifica quando un pun -
teggio di valutazione scaricato utilizza un sistema a 
5 punti, ma il classificatore di sentimenti lavora 
solo con un sistema a 2 punti (ad esempio, Positi -
vo/Negativo). Per evitare discrepanze, si procede 
alla mappatura: i voti 1 e 2 sono mappati come 
Negative Feedback (Feedback Negativo), mentre 4 
e 5 sono mappati come Positive Feedback (Feed-
back Positivo). Il voto 3, che si trova a metà strada, 
potrebbe essere considerato un feedback neutro e 
viene rimosso per concentrare il classificatore sulle 
polarità chiare. 
L'Annotazione dei Dati come Base per l'Ap -
prendimento Supervisionato 
L'Annotazione dei Dati (Data Annotation) costitui-
sce il fondamento per i compiti di Apprendimento 
Automatico Supervisionato ( Supervised Machine 
Learning). Essa trasforma i dati grezzi (come dichia-
razioni estratte da Internet) in dati annotati. Ad 
esempio, le dichiarazioni possono essere etichetta -
te come relative a "Marketing Topics" o "Topics 
different than Marketing" per addestrare un classi -
ficatore. 
L'obiettivo è ottenere volumi maggiori di dati an -
notati e una copertura più ampia per migliorare la 
qualità dei risultati e le prestazioni dei modelli ad -
destrati. 
Tuttavia, il compito di annotazione non è sempre 
semplice e spesso richiede conoscenza professio-
nale di dominio  per applicare correttamente le 
etichette e identificare le parole pertinenti. Un 
esempio complesso tratto dal contesto sanitario 
mostra una descrizione post-operatoria di un pa -
ziente. Il testo grezzo, una volta annotato, identifi -
ca entità specifiche: il paziente (Sig. Shinabery), 
l ' o s p e d a l e ( [ S u r g l u t h e L e o n C a l c n e r 
Healthcare]Hosp), la data ([9/9/02]Time), i sintomi 
([crescendo spontaneous angina]sym), la durata 
([three-and-one-half months]dur), le malattie/dia -
gnosi ([subacute left cyrcumflex thrombosis]dis), i 
trattamenti ([Dilation of the left circumflex]Treat, 
[placement of multiple stents]Treat), e il risultato 
del trattamento ([angiographic and clinical 
result]TR). Le categorie fondamentali identificate in 
questo contesto sono: Ospedale ( Hospital), Tempo 
(Time), Sintomi ( symptoms), Durata ( duration), Ma-
lattia (disease), Trattamento (Treatment) e Risultato 
del Trattamento (Treatment Result). 
L'annotazione dei dati non si limita al solo testo; 
nelle tecniche di Data Mining  può essere estesa 
per includere l' annotazione multimodale di testo, 
video e immagini. 
Per comprendere meglio il contesto dell'annota -
zione, è utile definire due concetti correlati: 
1. Lessico ( Lexicon): Generalmente ha una 
forma altamente strutturata, immagazzi -
nando i significati e gli usi di ciascuna pa -
rola e codificando le relazioni tra parole e 
significati. 
2. Corpus: Una collezione di testi o audio 
autentici (scritti o parlati da madrelingua o 
dialettali) organizzati in dataset. Un corpus 
può includere elementi come giornali, ro -
manzi, ricette, trasmissioni radiofoniche, 
programmi televisivi, film e tweet. Nel con-
testo del Natural Language Processing  
(NLP), un corpus contiene i dati testuali e 
vocali utilizzati per addestrare sistemi di 
intelligenza artificiale e machine learning. 
In senso lato, il Text Mining (Estrazione di Testo) è 
un campo interdisciplinare che coinvolge diverse 
aree come il Data Mining , l'Intelligenza Artificiale 
(AI), il Machine Learning, il Natural Language Pro -
cessing (NLP) e la Computational Linguistics  (Lin -
guistica Computazionale). Le attività principali del 
Text Mining includono la Classificazione di Docu -
menti ( Document Classification ), il Clustering di 
Documenti ( Document Clustering ), l'Estrazione di 
Informazioni ( Information Extraction ), l'Estrazione 
di Concetti (Concept Extraction) e il Web Mining. 
32
Fasi Cruciali di Pre-elaborazione del Testo (NLP) 
Immediatamente dopo l'ac -
quisizione dei dati, entrano 
in gioco i passaggi di pre-
elaborazione ( Preproces -
sing Steps ) fondamentali, 
molti dei quali derivano dal 
Natural Language Proces -
sing (NLP). 
Tokenizzazione: La Segmentazione Lessicale 
La Tokenizzazione ( Tokenization) è un processo 
che segmenta un dato testo in unità lessicali  
chiamate "token". Ad esempio, la frase "That’s" 
viene tokenizzata in due token: "that" e "‘s"; men-
tre "rule-based" viene separato in tre token: 
"rule", "-", e "based". 
Nelle lingue latine e flessive (come l'inglese), gli 
spazi e i segni di punteggiatura sono sufficienti per 
realizzare la lessicalizzazione. Al contrario, le lingue 
prive di marcatori di separazione (come il cinese) e 
alcune lingue agglutinanti (come il giapponese, il 
coreano e il vietnamita) richiedono prima un pas -
saggio di segmentazione delle parole . La toolkit-
NLTK in Python fornisce un pacchetto dedicato alla 
tokenizzazione. 
Rimozione delle Stop Words 
La fase di rimozione delle stop words (parole fun -
zionali o ausiliarie) mira a minimizzare lo spazio di 
archiviazione necessario per il Text Mining. Le stop 
words sono parole ad alta frequenza che appaiono 
comunemente nei documenti ma che veicolano 
poca informazione testuale. Esempi di queste pa -
role funzionali includono articoli, preposizioni, 
congiunzioni e parole modali (come "The", "is", 
"at", "which", "on"). 
Durante la fase di rappresentazione del testo, le 
parole funzionali vengono scartate. Nell'implemen-
tazione di un modulo di Text Mining, viene stabilita 
una lista di stop words, e tutte queste parole ven -
gono rimosse prima di procedere all'estrazione 
delle feature (caratteristiche). 
Normalizzazione della Forma Verbale: Lemma -
tizzazione e Stemming 
La Normalizzazione della Forma della Parola  
(Word Form Normalisation ) è un processo cruciale 
per garantire che parole diverse, ma grammatical -
mente correlate o derivanti dalla stessa radice, sia -
no trattate come equivalenti. Questo concetto si 
articola in due tecniche principali: la Lemmatizza-
zione (Lemmatisation) e lo Stemming. 
1. Lemmatizzazione: Consiste nel ripristino 
delle parole arbitrariamente deformate alle 
loro forme originali (o lemmi). Ad esempio, 
la forma plurale "cats" viene ripristinata a 
"cat", e la forma passata "did" a "do". 
2. Stemming: È il processo di rimozione degli 
affissi (suffissi e prefissi) per ottenere la 
radice (root) della parola. Ad esempio, "fi -
sher" viene ridotto a "fish", e "effective" a 
"effect". 
La normalizzazione è solitamente realizzata tramite 
regole basate su espressioni regolari ( regular ex -
pressions). Uno degli algoritmi di stemming più 
diffusi è l'algoritmo di Porter stemming, che con -
siste in quattro fasi principali: 
1. Divisione delle lettere in vocali e conso -
nanti. 
2. Utilizzo di regole per processare le parole 
che terminano con i suffissi -s, -ing e -ed. 
3. Progettazione di regole speciali per gestire 
suffissi più complessi (ad esempio, 
-ational). 
4. Affinamento dei risultati del processo tra -
mite regole aggiuntive. 
Esistono diversi algoritmi di stemming che posso -
no produrre risultati differenti anche per la stessa 
lingua. A livello applicativo, il toolkit NLTK in 
33

Python fornisce funzioni per richiamare l'algoritmo 
di Porter stemming. Quando si impiegano metodi 
statistici, è fondamentale che le parole che condi -
vidono la stessa radice (stem) vengano considerate 
come la stessa parola; si pensi a forme diverse 
come "Take", "takes", "taken", "took", "taking". 
Strumenti di Analisi Linguistica Avanzata 
Per ottimizzare i compiti di Text Mining, entrano in 
gioco diversi processi avanzati di NLP , inclusi il 
Part-of-Speech(POS) Tagging, il Riconoscimento 
delle Entità Nominate (NER) e i Syntactic Parsers. Il 
POS Tagging, per esempio, elabora tutte le fun -
zioni grammaticali svolte da ogni parola in una fra -
se. 
Riconoscimento delle Entità Nominate (NER) 
Il Riconoscimento delle Entità Nominate  ( NER - 
Named Entity Recognition ) è un componente di 
pre-elaborazione cruciale nei flussi di lavoro di ana-
lisi del testo e NLP , poiché l'integrazione di questo 
strumento migliora la comprensione e la prepara -
zione del testo per le attività a valle. 
Il NER offre molteplici vantaggi operativi: 
• Filtro Intelligente del Contenuto  ( Smart 
Content Filtering ): Isola automaticamente 
le entità significative dal testo, permetten -
do di focalizzare l'analisi sulle informazioni 
chiave (ad esempio, estraendo figure di 
spicco e luoghi dagli articoli di notizie). 
• Pulizia del Testo Migliorata  ( Enhanced 
Text Cleaning): Rimuove in modo strategi -
co il contenuto non essenziale, concen -
trandosi sul mantenimento delle entità 
identificate. 
• Creazione di Caratteristiche Avanzate  
(Advanced Feature Creation ): Trasforma le 
entità riconosciute in featurepronte per il 
modello, aggiungendo contesto (ad 
esempio, tipo di entità: Persona, Luogo, 
Organizzazione) per migliorare le presta -
zioni del modello. 
• Tecniche di Standardizzazione (Standardi-
zation Techniques ): Crea rappresentazioni 
coerenti delle entità e può abilitare l'ano -
nimizzazione tramite placeholder  (ad 
esempio, convertendo "Sarah Johnson" in 
<PERSON>). 
• Connessione alla Conoscenza  ( Knowled-
ge Connection): Identifica le entità da col -
legare a database esterni o basi di cono -
scenza (ad esempio, collegando nomi di 
aziende alle loro voci nel database). 
• Segmentazione Intelligente del Testo  
(Intelligent Text Segmentation): Preserva le 
entità multi-parola come singole unità (ad 
esempio, mantenendo "San Francisco" 
come un'unica entità), migliorando l'accu -
ratezza della tokenizzazione. 
• Elaborazione Specializzata  ( Specialized 
Processing): Si adatta alle esigenze specifi -
che del dominio (come termini medici o 
indicatori finanziari). 
Per esempio, data la frase: "Tim Cook met with 
Microsoft executives in Seattle last Friday to di -
scuss AI developments worth $50 million," (Tim 
Cook ha incontrato i dirigenti di Microsoft a Seattle 
venerdì scorso per discutere sviluppi di intelligenza 
artificiale del valore di 50 milioni di dollari), il NER 
produce le seguenti mappature di entità: 
• "Tim Cook" - PERSONA ( People, inclu -
ding fictional) 
• "Microsoft" - ORG (Organizzazione: Com-
panies, agencies, institutions) 
• "Seattle" - GPE (Geo-political Entity: Paesi, 
città, stati) 
• "Friday" - DATE (Absolute or relative dates 
or periods) 
• "AI" - ORG (Organizzazione) 
• "$50 million" - MONEY (Monetary values, 
including unit) 
34
Analisi Sintattica e Alberi di Dipendenza 
L'analisi sintattica ( Syntactic parsing ) è un altro 
strumento chiave che mira a estrarre la struttura 
delle frasi (phrase structure) e le relazioni di dipen -
denza. L'output di questo processo è un albero 
della struttura sintattica  ( Syntactic structure tree ) 
della frase analizzata. 
Per ottimizzare il Text Mining, si ricorre sia all'Albe-
ro di Dipendenza (Dependency Tree) che all'Albe-
ro Sintattico(Syntax Tree), che fornisce informazio -
ni a livello di frase (phrase-level information). 
Considerando una frase, ad esempio: "I drive a car 
to my college," (Io guido un'auto verso il mio col -
lege), è possibile visualizzare le differenze tra le 
due rappresentazioni strutturali. L' Albero Sintatti-
co mostra una struttura gerarchica della frase. La 
frase viene scomposta in costituenti come Sintag -
ma Nominale ( Noun Phrase ) e Sintagma Verbale 
(Verb Phrase ), e utilizza nodi intermedi  per rag -
gruppare le parole in frasi, illustrando come le frasi 
sono costruite. Si concentra sulla composizione 
strutturale e sull'analisi a livello di frase. 
L'Albero di Dipendenza , invece, mostra le rela-
zioni dirette tra le parole . In questa rappresenta -
zione, ogni parola si collega direttamente alla sua 
parola principale ( head word ). Le relazioni sono 
etichettate da funzioni grammaticali (ad esempio, 
nsubj per soggetto nominale, dobj per oggetto 
diretto, prep per preposizione, pobj per oggetto di 
preposizione), e non sono presenti nodi intermedi. 
L'Albero di Dipendenza è più efficace nel mostrare 
le relazioni grammaticali  ed è particolarmente 
utile per l'estrazione di relazioni. Offre una rappre -
sentazione più compatta e di più facile elaborazio -
ne computazionale, focalizzandosi sull'analisi a li -
vello di parola e sulle connessioni grammaticali 
funzionali. 
In sintesi, mentre l'Albero Sintattico aiuta a com -
prendere la composizione della frase e la struttura 
gerarchica, l'Albero di Dipendenza è migliore per 
identificare le relazioni funzionali dirette tra le paro-
le, essenziale per l'estrazione precisa di informa -
zioni. 
Data Mining, Analisi Testuale e Classi ﬁcazione: 
Paradigmi e Architetture di Apprendimento Au -
tomatico 
I. Introduzione e Contesto: Data Mining, Analisi 
Testuale e Classiﬁcazione del Testo 
Un'applicazione cruciale in questo campo è la 
Classificazione del Testo, conosciuta anche come 
text tagging (etichettatura del testo) o text catego-
rization (categorizzazione del testo). La classifica -
zione del testo è definita come il processo di asse -
gnazione di testo a gruppi organizzati. I classifica -
tori di testo sono strumenti capaci di analizzare 
automaticamente il testo in input e assegnare un 
insieme di etichette o categorie predefinite basate 
sul suo contenuto. Ad esempio, un sistema di clas -
sificazione può prendere un input testuale come 
l'affermazione "You’re the best" (Sei il migliore) e 
classificarla nell'Output (Uscita) come "Positive" 
(Positiva), tipico nei compiti in cui si desidera di -
stinguere affermazioni "buone" da quelle 
"cattive". 
II. Paradigmi di Apprendimento Automatico: 
Tradizionale vs. Moderno (Deep Learning) 
Le numerose metodologie di Machine Learning  
(Apprendimento Automatico) applicate in svariati 
scenari possono essere raggruppate in due fami -
glie principali: gli approcci Tradizionali e gli ap -
procci di Newer Machine Learning(Apprendimento 
Automatico più Recente). La distinzione cruciale tra 
queste famiglie risiede nel passaggio di feature 
extraction (estrazione delle caratteristiche). 
A. Apprendimento Automatico Tradizionale 
35
Negli approcci tradizionali di Machine Learning , 
l'estrazione delle feature (caratteristiche) è un pas -
saggio separato e distinto da tutte le fasi coinvolte 
nell'addestramento (training), nella validazione ( va-
lidation) e nel test ( testing) del modello. Gli svilup -
patori devono ricorrere a metodi di estrazione del -
le feature per configurare array e vettori che si 
adattino meglio all'esperimento o all'applicazione 
specifica. In certi casi, si possono usare descrittori 
statistici come feature rappresentative di un dato 
di input. Queste feature vengono poi fornite all'ar -
chitettura di machine learningtradizionale per l'ad -
destramento. Il concetto fondamentale in questo 
paradigma è che la bontà della classificazione di -
pende in gran parte dalla capacità dell'operatore 
di estrarre feature che aiutino efficacemente il mo -
dello a discriminare tra le categorie di interesse. 
B. Apprendimento Profondo (Deep Learning) 
Gli approcci più nuovi, in gran parte riconducibili al 
Deep Learning  (Apprendimento Profondo), si ba -
sano sulle Reti Neurali Profonde ( Deep Neural 
Networks, DNNs). A differenza dei metodi tradi -
zionali, gli approcci di Deep Learning apprendono 
automaticamente le rappresentazioni gerarchiche, 
eliminando la necessità di un'ingegneria delle fea-
ture(ovvero, l'estrazione manuale delle caratteristi -
che). Questi modelli hanno la capacità di migliora -
re le loro prestazioni con l'aumento dei dati dispo -
nibili e della potenza computazionale (caratteristica 
nota come "scalabilità"). Sono particolarmente 
adatti a gestire enormi volumi di dati non struttura -
ti, come immagini, testo e voce, dai quali sono in 
grado di estrarre schemi complessi. 
III. Il Framework Tradizionale per la Classiﬁcazio-
ne del Testo 
La struttura ( framework) tradizionale per la classifi -
cazione del testo si articola in tre componenti es -
senziali e distinti: la Rappresentazione del Testo 
(Text Representation), la Selezione delle Caratteri -
stiche (Feature Selection) e, infine, la Classificazio -
ne (Classification). 
A. Rappresentazione del Testo e Vettorializza -
zione 
La Rappresentazione del Testo svolge un ruolo 
cruciale, poiché deve riflettere fedelmente il con -
tenuto testuale e disporre di una capacità sufficien -
te per distinguere i diversi tipi di testo. La selezio -
ne del metodo di rappresentazione è strettamente 
correlata all'algoritmo di classificazione scelto. Ad 
esempio, l'algoritmo Support Vector Machine  
(SVM) utilizza spesso il vector space model  (VSM, 
Modello dello Spazio Vettoriale) come metodo di 
rappresentazione. 
Per rendere il testo leggibile dal modello, l'input 
(che consiste in parole, frasi o periodi) deve essere 
trasformato in un formato numerico. Un concetto 
chiave in questo processo è l' word embedding  
(rappresentazione vettoriale di parola), che è defi -
nito come un array numerico utilizzato per rappre -
sentare una parola. L'output di questa fase, insie -
me alla selezione delle feature, viene inviato alle 
fasi successive di Training, Validation e Testing del 
modello. 
B. Selezione delle Caratteristiche e Algoritmi 
Tradizionali 
La Selezione delle Caratteristiche è il processo 
mediante il quale viene scelto un sottoinsieme ot -
timale di feature per la rappresentazione e la classi-
ficazione del testo. Esistono due grandi categorie 
di approcci per la selezione delle feature: supervi-
sionati e non supervisionati. 
Gli approcci non supervisionati vengono applicati 
a un corpus (insieme di testi) che non dispone di 
annotazioni di categoria. Questi metodi si basano 
36

comunemente su misure statistiche come la Fre -
quenza del Termine (Term Frequency, TF) e la Fre -
quenza del Documento ( Document Frequency , 
DF). Al contrario, gli approcci supervisionati sfrut-
tano l'annotazione di categoria, il che permette 
loro di selezionare un sottoinsieme di feature più 
efficace per il compito di classificazione. 
Immediatamente dopo la rappresentazione e la 
selezione delle feature, viene applicato un algorit -
mo di classificazione. I più utilizzati nel Machine 
Learning tradizionale per la classificazione del testo 
sono Naïve Bayes, Maximum Entropy(Massima En-
tropia) e Support Vector Machines (SVM). 
Il Naïve Bayes è un modello probabilistico versati -
le, impiegato sia per la classificazione binaria che 
per quella multi-classe. L'algoritmo Maximum En-
tropy è utilizzato nei compiti di classificazione in 
NLP ( Natural Language Processing , Elaborazione 
del Linguaggio Naturale) e assegna la probabilità 
congiunta P(x,y), che rappresenta la probabilità del 
dato osservato ( x) e della sua etichetta corrispon -
dente ( y). La SVM ( Support Vector Machine ) è un 
algoritmo di apprendimento discriminativo super -
visionato principalmente utilizzato per la classifica -
zione binaria, il cui obiettivo primario è identificare 
un iperpiano all'interno dello spazio dei dati capa -
ce di separare i campioni in modo ottimale. 
L'implementazione pratica di questi metodi, come 
SVM e Naïve Bayes, richiede una serie di passaggi 
tecnici preparatori, tra cui l'installazione delle libre -
rie necessarie, l'impostazione del random seed  
(seme casuale per la riproducibilità), l'aggiunta del 
corpus, la pre-elaborazione dei dati ( Data Pre-pro-
cessing), la preparazione dei dataset di Train e 
Test, l'Encoding (Codifica) e la Word Vectorisation 
(Vettorizzazione delle Parole), prima di poter utiliz -
zare i metodi ML per le predizioni finali. 
IV. Architetture di Apprendimento Profondo 
(Deep Learning ) e Meccanismi di Addestramen -
to 
Il Deep Learning  offre architetture avanzate che 
possono automaticamente imparare e classificare i 
dati, in particolare quelli non strutturati. 
A. Reti Neurali Feed-Forward  Multistrato 
(MFFNN) 
La Rete Neurale Feed-Forward Multistrato ( Multi-
layer Feed-Forward Neural Network ) è una rete 
neurale con una struttura in avanti ( forward-structu-
re) che stabilisce una mappatura tra un insieme di 
vettori di input e un insieme di vettori di output in 
modo completamente connesso tra i suoi strati. 
Un diagramma tipico di questa architettura mostra 
quattro strati distinti. Il primo strato è lo Strato di 
Input (Layer 1), dove vengono alimentate le varia -
bili di input (ad esempio, quattro variabili di input), 
ma dove non avvengono calcoli. Seguono due 
Strati Nascosti (Hidden Layers, Layer 2 e 3). In cia -
scun neurone di questi strati, tutti i valori in ingres -
so vengono sommati (una somma pesata dei se -
gnali di input) e successivamente processati attra -
verso una funzione di attivazione ( activation func -
tion). La funzione di attivazione è un elemento cru -
ciale all'interno del neurone artificiale. Infine, lo 
Strato di Output  (Layer 4) riceve i valori sommati 
da tutti i nodi precedenti, li elabora con una fun -
zione, spesso la funzione softmax in caso di classi -
ficazione, per produrre le probabilità. 
B. Architetture Specializzate: CNN e RNN 
Le Reti Neurali Convoluzionali (CNNs)  ( Convolu-
tional Neural Networks ) costituiscono un tipo spe -
cifico di rete neurale feed-forward. I loro strati na -
scosti sono composti da una sequenza di filtri con -
voluzionali e di pooling (sottocampionando il 
dato). Gli strati convoluzionali hanno il compito di 
selezionare le feature dall'input di testo, mentre gli 
strati di pooling ( pooling layers ) riducono la di -
mensione ( downsample) dei vettori di feature per 
ottenere una rappresentazione dei dati più com -
patta. L'adozione delle CNNs in compiti di Classifi -
37
cazione di Argomento e Classificazione di Senti -
mento (Sentiment Classification) dal 2014 ha porta-
to a miglioramenti sostanziali delle prestazioni ri -
spetto agli algoritmi ML tradizionali, confermando 
la loro elevata accuratezza sia in Computer Vision 
(Visione Artificiale) che in NLP . Il diagramma di una 
CNN, sebbene mostrato per la classificazione di 
immagini, illustra chiaramente la sequenza: Input 
image (Immagine di input), Convolutional layers  
(Strati convoluzionali, con convoluzione e pooling), 
Fully connected layer  (Strato completamente con -
nesso) e Output class (Classe di output). 
Le Reti Neurali Ricorrenti (RNNs) (Recurrent Neu-
ral Networks) o Reti Neurali Ricorsive, rappresenta -
no un'altra classe di reti neurali profonde che ap -
plicano il medesimo insieme di pesi in modo ricor -
sivo su un dato input, che può essere testuale o 
visivo. Queste architetture sono ampiamente im -
piegate nell'NLP per l'apprendimento di sequenze. 
La struttura ricorsiva opera sui nodi della rete e 
viene espansa in una sequenza. La feccia indietro, 
tiene conto non solamente del laser precedente 
ma di una serie storica. RNN: Ripetere in modo 
ricorsivo la funzione.  
C. Il Processo di Addestramento e Retropropa -
gazione 
L'addestramento ( learning o training) di una rete 
neurale è concepito come un processo di ottimiz -
zazione della loss function  (funzione di perdita). 
L'obiettivo è determinare i parametri ottimali del 
modello che garantiscano il miglior adattamento ai 
dati di addestramento in relazione alla loss func -
tion. La loss function  serve a misurare la distanza 
tra le predizioni generate dal modello e gli output 
desiderati. 
Il meccanismo di Backpropagation (Retropropaga-
zione) è ciò che consente di abbassare il valore 
della loss functionaggiornando i parametri (o pesi) 
della rete. Il processo si articola in tre fasi: 
1. Forward Pass (Passaggio in avanti): La rete 
esegue una predizione basandosi sui pesi 
correnti, confronta questa predizione con 
la risposta effettiva e calcola l'errore o per -
dita (loss). 
2. Backward Pass  (Passaggio all'indietro): 
Questa fase è il nucleo della backpropaga-
tion. Inizia dallo strato di output, calcola il 
contributo di ciascun peso all'errore totale, 
e si muove all'indietro strato per strato. 
Durante questo passaggio, vengono calco-
lati i gradients (gradienti), che indicano la 
direzione e la pendenza del cambiamento 
dell'errore (inclinazione della curva). 
3. Weight Update (Aggiornamento dei pesi): 
Infine, ogni peso viene aggiustato in base 
al suo contributo all'errore, utilizzando un 
learning rate (tasso di apprendimento) che 
ne controlla l'entità. L'obiettivo è minimiz -
zare l'errore nel forward pass successivo. 
D. Iperparametri del Deep Learning 
Gli iperparametri giocano un ruolo cruciale nella 
configurazione e nell'addestramento dei modelli di 
Deep Learning. Essi sono suddivisi per categoria: 
• Dataset: Include il rapporto di divisione 
Train-Test (Addestramento-Test), che tipi -
camente segue la regola pratica 80/20. 
• Functions (Funzioni):  Riguarda la scelta 
dell'algoritmo di ottimizzazione, della fun -
38

zione di attivazione utilizzata nello strato 
della rete neurale e della loss function  
(funzione di perdita) che il modello impie -
gherà. 
• Layers (Strati):  Comprende il numero di 
strati nascosti nella rete neurale, il numero 
di unità di attivazione in ogni strato, la di -
mensione degli strati convoluzionali e la 
dimensione del pooling. 
• Iterations (Iterazioni):  Fa riferimento al 
numero di iterazioni ( epochs) utilizzate nel-
l'addestramento della rete neurale e alla 
dimensione del batch (batch size), ovvero il 
numero di campioni processati prima che il 
modello venga aggiornato. 
V. Valutazione delle Prestazioni dei Sistemi di 
Classiﬁcazione 
La valutazione delle prestazioni è indispensabile 
per misurare l'efficacia di un sistema di classifica -
zione. A tal fine, vengono impiegati concetti chiave 
come True Positive (TP), True Negative (TN), False 
Positive (FP) e False Negative(FN). 
A. Matrice di Confusione e Deﬁnizioni di Errore 
La Matrice di Confusione (Confusion Matrix) è uno 
strumento visivo e concettuale che permette di  
cogliere le prestazioni 
complessive di un sistema. 
In un contesto di classifica -
zione, un dataset  viene 
fornito con campioni e le 
loro etichette reali. Il siste -
ma di classificazione ese -
gue delle predizioni che 
vengono poi confrontate con queste etichette rea -
li. 
Se, ad esempio, consideriamo un dataset con af -
fermazioni "bad" (cattivo) e "good" (buono), e 
definiamo "good" come la classe positiva e "bad" 
come la classe negativa: 
• True Positive (TP):  Il modello identifica 
correttamente un'istanza come apparte -
nente alla classe positiva (es. un'afferma -
zione "good" viene classificata come 
"good"). 
• True Negative (TN):  Il modello identifica 
correttamente un'istanza come apparte -
nente alla classe negativa (es. un'afferma -
zione "bad" viene classificata come 
"bad"). 
• False Positive (FP): Errore in cui il modello 
identifica erroneamente un'istanza negati -
va come positiva (es. un'affermazione 
"bad" viene classificata erroneamente 
come "good"). 
• False Negative (FN):  Errore in cui il mo -
dello identifica erroneamente un'istanza 
positiva come negativa (es. un'affermazio -
ne "good" viene classificata erroneamente 
come "bad"). 
Il diagramma della Matrice di Confusione organizza 
queste quattro possibilità incrociando l'Etichetta 
Reale ( Actual) con la Predizione ( Prediction), for -
nendo una visione strutturata degli esiti della clas -
sificazione. 
B. Precisione, Richiamo e F1-Score 
Per quantificare le prestazioni, vengono utilizzate 
metriche derivate direttamente dai valori TP , TN, 
FP e FN. 
• Precisione ( Precision): Misura la propor -
zione di predizioni positive che erano effet-
tivamente corrette. 
• Richiamo (Recall): Misura la proporzione di 
tutti i campioni positivi reali che sono stati 
identificati correttamente dal modello. 
• F1-Score (o F-Measure):  Questa metrica 
funge da media che tiene conto in qualche 
modo sia della Precisione che del Richia -
mo. 
39

La rappresentazione grafica o tabellare di queste 
tre metriche è utile per descrivere al meglio le pre -
stazioni di un sistema di classificazione. 
C. Esempio Pratico di Calcolo delle Metriche 
Considerando un problema di classificazione su 
100 affermazioni etichettate, un modello che pro -
ducesse i seguenti risultati: TP = 65, FP = 20 e FN 
= 15, le metriche di prestazione si calcolerebbero 
come segue: 
• Precisione: 65 / (65 + 20) = 65 / 85 = 0.76. 
• Richiamo: 65 / (65 + 15) = 65 / 80 = 0.81. 
• F-Measure: 0.78 (ottenuto dal calcolo 
1.231 / 1.57). 
Questi risultati (0.76 per la Precisione, 0.81 per il 
Richiamo e 0.78 per l'F-Measure) offrono una valu -
tazione quantitativa delle prestazioni del sistema. 
Inoltre, il confronto ( benchmarking) tra due sistemi 
di classificazione testuale, come S1 e S2, richiede il 
calcolo e l'analisi di queste metriche per determi -
nare quale sistema sia più performante sulla base 
dei risultati osservati. Ad esempio, confrontando 
S1 (TP = 65, FN = 5, FP = 30) con S2 (TP = 62, FN 
= 12, FP = 26), l'analisi delle metriche derivate sa -
rebbe essenziale per la valutazione finale. 
40



---

# Document: Lecture_01.5_Handouts_SQL_queries.pdf

Revising SQL queries
Handouts on Join, Select, and Projection in SQL
Data Mining and T ext Analytics
Postgraduate Programme in Artificial Intelligence for Business and Society
Professor Alessandro Bruno
SQL –Structured 
Query 
Language
• Let's revise some SQL functions and the 
results when applied on an SQL DB.
• Figure out a relational DB represented 
by the ER diagram on the righthand 
side.

Processing 
Data with 
SQL

Creating a TABLE with SQL
• CREATE TABLE Customers (
customer_id INT PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
age INT,
country VARCHAR(50));
-- Insert sample data
INSERT INTO Customers (customer_id, first_name, last_name, age, country)
VALUES
(1, 'John', 'Doe', 31, 'USA'),
(2, 'Robert', 'Luna', 22, 'USA'),
(3, 'David', 'Robinson', 22, 'UK'),
(4, 'John', 'Reinhardt', 25, 'UK'),
(5, 'Betty', 'Doe', 28, 'UAE');
Running SQL
• Let's run the SQL Compiler at the following links:
• https://www.programiz.com/sql/online-compiler
• https://sqliteonline.com/
• SELECT  - Example:
SELECT first_name, last_name FROM Customers WHERE country = "USA" ORDER BY age DESC;
SELECT

JOIN
• SELECT c.first_name, o.item, o.amount
• FROM Customers c
• JOIN Orders o ON c.customer_id = o.customer_id;
This is an INNER JOIN (default type if you just say JOIN).
It means:
“Only return rows where a customer in the Customers table has a matching 
customer_id in the Orders table.”
JOIN (INNER)

TYPES of JOIN
• INNER JOIN→only matching rows
• LEFT JOIN→all rows from left table, matching ones from right
• RIGHT JOIN→all rows from right table
• FULL JOIN→all rows from both sides
LEFT JOIN
SELECT c.first_name, c.last_name, o.item, o.amount
FROM Customers c
LEFT JOIN Orders o ON c.customer_id = o.customer_id;
Meaning: Return all customers, even those who have no orders. If they haven’t 
ordered anything, the item and amount will be NULL.
Results –LEFT JOIN

RIGHT JOIN
SELECT c.first_name, c.last_name, o.item, o.amount
FROM Customers c
RIGHT JOIN Orders o ON c.customer_id = o.customer_id;
Meaning:
• Return all orders, even if there’s no matching customer.
• If the customer doesn’t exist in the Customers table, customer fields 
will be NULL.
FULL JOIN
SELECT c.first_name, c.last_name, o.item, o.amount
FROM Customers c
FULL JOIN Orders o ON c.customer_id = o.customer_id;
Meaning:
Return all customers and all orders, matching when possible.
If a customer has no orders →order info is NULL.
If an order has no customer →customer info is NULL.
PROJECTION
• A Projection selects only certain columns (attributes) from a table.
Example: Display only customer names and countries.
SELECT first_name, last_name, country
FROM Customers;
PROJECTION
• Check out the result down below



---

# Document: Lecture_01_Data_Mining_Introduction_2025_2026.pdf

Data Mining Introduction
Prof Alessandro Bruno
IULM University – Faculty of Communication
Postgraduate Programme in Artificial Intelligence for 
Business and Society
Data Mining and Text 
Analytics 2025/2026
Lecture_01
Outline
 Data and Noise
 A formal definition of Data 
Mining 
 Data Mining as the Evolution 
of Information Technology
 Knowledge Discovery Process
 What kind of data can be 
mined? 
 What kinds of Patterns can be 
mined? 
 Mining Frequent Patterns, 
Associations, and Correlations
Data and Noise 
“To find signals in data, we must 
learn to reduce the noise - not just 
the noise that resides in the data, 
but also the noise that resides in us 
(bias). It is nearly impossible for 
noisy minds to perceive anything 
but noise in data.”
Stephen Few, Signal: Understanding 
What Matters in a World of Noise
Noise: Some Examples
 Let's have a look at the 
given picture.
 How would you describe its 
content?
Image Denoising Techniques to remove 
additive noise
 The scientific literature offers 
a wide plethora of 
techniques to help enhance 
the image quality in terms of 
pixel content.
 Let's apply a common 
image filtering technique 
named "median filter" and 
see the outcome.
Data 
without 
Noise
Here is the original picture

Data Mining. Why?
 What is data mining for?
 Imagine digging a hole while you look for something precious.
 You will go through excavation, rock and stone residuals, and other elements that might not exactly be what you 
are seeking.
 You need some tools and techniques to find your way to your goal: INFORMATION
 Before extracting INFORMATION, you need to put together some little pieces or components that, once 
combined, will foster the composition of the INFORMATION itself.
 Those little pieces are called PATTERNS.
 PATTERNS are an ensemble of elements that are in data and express "sequences", "motifs", "codes", and so on.
Patterns in Stock Price
 Stock price analysis is a critical topic. Fluctuations in stock price might reveal events of 
interest to the market.
 Here is an example with a stock price series.
 Pt is the stock price at t time
 ϵt is an additive factor
 Try now draw the trend of the stock price series.

Trends of the Stock Price
The so-called zig-zag effect is shown on the diagram

Trends and hidden patterns
 A pattern can be easily observed by using average function on the stock trend values.
 The red-dotted line shows the "hidden trend" emphasizing the linearly increasing function

Data Mining. Some examples.
 To find correlations in financial and business intelligence data
 Hospitals can spot trends and anomalies in their patient 
records
 Search engines can do better ranking and ad placement
 Environmental and public health agencies can spot patterns 
and abnormalities in their data. 
 Monitoring of the energy consumption of household 
appliances
 Pattern analysis in bioinformatics and pharmaceutical data
 Spotting trends in blogs, Twitter, and many more 
 The big question is: how should we analyze the data? 

What is data mining
Starting off with a formal definition:
 “Data mining, also popularly referred to as Knowledge Discovery 
from Data (KDD), is the automated or convenient extraction of 
patterns representing knowledge implicitly stored or captured in 
large databases, data warehouses, the Web, other massive 
information repositories, or data streams”1
1”Data Mining. Concepts and Techniques”. Jiawei Han, Micheline Kamber, Jian Pei
Data Mining 
Informally, Data Mining is the 
process of using a computer 
program to find patterns or 
relationships in data. 
Looking for combinations of 
symptoms that are reliable 
indicators of a given disease
Looking for products that 
customers tend to purchase 
together.
Grouping data showing some 
sort of correlations.
Patterns
What do patterns 
reveal in data? 
1
A pattern refers to 
anything that 
repeatedly exhibits 
a consistent form 
or organization 
2
Patterns show data 
correlations 
•A sequence of signals 
manifest periodically 
•Some items exhibit a 
linear progression
3
Patterns can be 
found in structured 
and unstructured 
data
4

Structured vs Semi-Structure 
vs Unstructured Data 
Content (formal 
perspective)
 Structured Data: Data with 
high degree of organisation 
( in a spreadsheet-like 
manner). 
 Semi-structured Data: Data 
with some degree of 
organisation (forms)
 Unstructured Data: Data 
with no predefined 
organisation (a text file 
without pre-define 
scheme).

Structure vs Unstructured Data
Structured Data Semi-structured Data Unstructured Data
Excel 
spreadsheets; Comma-
separated value 
file; Relational Database 
Tables.
HTML files; Json files; XML 
files.
Images (.jpeg or .png files); 
videos (.mp4); sound files (.wav, 
.mp3 files); PDF files; Word Files, 
Plain text files.
Around 20% of worldwide 
data is structured.
Characterised by 
hierarchical structure.
Most of data that is created today 
is unstructured. (Tweets, Facebook 
posts, social media comments).
Data Management Hierarchy
Database
Data Warehouse
Data Lake
Databases
A database can be an 
organized collection of 
structured information, 
or data, typically stored 
electronically in a 
computer system. A 
database is usually 
controlled by 
a database 
management system 
(DBMS).2
Table 1 Table 2
Table 3 Table 4
Table 5 Table 6
Relationships
Data Warehouses
A data warehouse is a type 
of data management system 
that is designed to enable and 
support BI (business 
intelligence) activities, 
especially analytics. 
Data warehouses are meant to 
perform queries and analysis 
They often contain 
large amounts of 
historical data. 
The data within a data 
warehouse is usually derived 
from a wide range of sources
application log files 
and transaction 
applications.
A data warehouse centralizes 
and consolidates data from 
multiple sources. Over time, it 
builds a historical record that 
can be invaluable to data 
scientists and business analysts. 
Because of these 
capabilities, a data 
warehouse can be 
considered an 
organization’s “single 
source of truth.”
Data Warehouses
 Enterprise Data Warehouse: It collects all information about 
subjects spanning the entire organisation. It typically can 
range in size from hundreds of gigabytes to terabytes or 
beyond. It supports corporate-wide data integration (cross 
functional in its scope). 
 Data Mart: A data mart contains a subset of corporate-
wide data that is of value to a specific group of users,  such 
as those within a business department. The scope is 
confined to specific subjects. 
o A markteing data mart may confine its subjects to customer, 
item, marketing channels and sales. 
o A risk control data mart may focus on customer credit, risk, and 
different type of frauds. 
Data Lakes
 In some companies, there are a massive number of complicated data 
sources with a wild variety in data types, formats, and quality (business 
data, communication records between customers and the organisation, 
regulations, market analysis, etc.)
 It might be difficult to design a Data Warehouse, where data is integrated, 
structured, and loaded according to specific criteria. 
 What is the concept of data lake? 
o A data lake is a single repository of all enterprise data in the natural format 
[relational data, semistructured data, unstructured data, binary data (audio, 
images, video)]
o A data lake often stores both raw data copies and transformed data (data that 
undergo processing) archived in cloud or distributed data repositories. 
Databases (DBs), Data Warehouses (DWs), 
and Data Lakes (DLs)
 Databases are for fast, transactional processing of 
structured data.
 Data Warehouses are for analytical querying of structured 
data with a top-down perspective (goal-oriented)
 Data Lakes store raw, unstructured, or semi-structured data 
for large-scale analytics.

Real Scenarios with DBs DWs and DLs 
 Database Transactional Processing
 An e-commerce website employs a relational database (MySQL) to store 
and deal with customer orders, inventory, and user accounts. When a 
customer places an order, the database processes the transaction in real 
time, updating product quantities and recording order details.
 Data Warehouse - Analytical Querying
 A retail company uses Amazon Redshift as a data warehouse to analyze 
sales trends over the last five years. The data warehouse aggregates sales 
data from different stores, allowing the business to run complex queries to 
understand customer behavior, seasonal trends, and profitability.
 Data Lake – Dealing with Raw, Unstructured Data
 A video streaming service uses Amazon S3 as a data lake to store large 
volumes of raw video files, user interaction logs, and metadata. Data 
scientists access this raw data to run machine learning algorithms that 
recommend content to users based on their viewing history and 
preferences.

Data and Information Technology Evolution
Evolution of Information Technology
“Necessity, who is the 
mother of invention.” – 
Plato 
Huge growth of 
available data volume
Computerization of our 
society
Fast development of 
powerful data 
collection and storage 
tools.
Some figures on Data 
Growth
720,000 hoursof video are 
uploaded every day to 
YouTube
1.3 billion images are shared 
on Instagram daily
500 million tweets are posted 
daily
More than 300 million photos 
get uploaded to Facebook 
per day
Every minute there are 
510,000 comments posted 
and 293,000 statuses 
updated
Data Age
Y-axis: Data 
Volume in 
Zettabytes
1 Zettabyte = 1 billion Terabytes
Zooming in on Business Data 
Sales transactions, stock trading 
records, product descriptions, sales 
promotions, company profiles and 
performance, and customer 
feedback are only some examples 
of data coming out of businesses 
Wal-Mart, handle hundreds of 
millions of transactions per week at 
thousands of branches around the 
world. 
Retail sales are currently mined 
over several variables.
Scientific findings reveal weather 
can impact retail sales*
The top five most weather -
dependent categories cover a 
range of different product types, 
with health foods emerging as the 
most susceptible to the weather.*
*Rose, N., Dolega, L. It’s the Weather: Quantifying the Impact of Weather on Retail Sales.
Appl. Spatial Analysis 15, 189–214 (2022). https://doi.org/10.1007/s12061-021-09397-0
Exploring queries over time is a good starting point
 Extracting stats out of queries can tell about what the current and past 
trends are.
 Give a go at Google Trends https://trends.google.com/trends/?geo=IT 
 Users can easily compare different trends using keywords and see 
percentages over time. 

Stats and Trends
Stats and trends can help discover some 
correlationship between data
If some patterns are easy to catch, at the 
same time, some others are not that easy to 
extract.
Data Mining comes into play to discover 
knowledge from the available data.
Knowledge Discovery Process consists of 
several steps. 

Knowledge Discovery Process
1
Data Cleaning
2
Data Integration
3
Data Selection
4
Data 
Transformation
5
Data Mining
6
Pattern 
Evaluation
7
Knowledge 
Presentation
Knowledge 
Discovery 
Process

KDD steps and explanation
• (Removing noise and inconsistent data) Data Cleaning
•  (where multiple data sources may be 
integrated)
Data 
Integration
•  (where data are transformed and consolidated 
into forms appropriate for mining by performing 
summary or aggregation operations)
Data 
Transformation
KDD steps and explanation
•(Intelligent methods are applied to extract 
patterns or construct models)Data Mining
•(Identifying interesting patterns or models 
representing knowledge based on specific 
measures)
Pattern/Model 
Evaluation
•(Visualisation and Knowledge Representation 
are used to show mined knowledge to users)
Knowledge 
Presentation
Descriptive vs Predicitive Data Mining
Descriptive Mining 
deals with 
properties of the 
dataset of interest
Predictive Mining 
performs induction 
on the dataset to 
make prediction
What kinds of data can be mined? 
Database 
Data
Data 
Warehouses
Transactional 
Data 
Other kinds of 
Data
Database Data 
 A database system, also 
called a database 
management system 
(DBMS), consists of a 
collection of interrelated 
data, known as a 
database, and a set of 
software programs to 
manage and access the 
data. 
 Imagine having something 
arranged similarly to 
spreadsheet files with 
columns and rows showing 
how data are handled. 

Database Data 
What would you 
pick up if I asked 
you to get the 
attribute that 
uniquely identifies 
a company’s 
data? 
Hint: Which 
column contains 
attributes that 
univocally identify 
a company? 
Answer
Given the premise that two companies do not 
have the same name, the attribute “Company 
Names” univocally identifies a company. 
On the other side, different companies can have 
the same amount of revenue in February (the 
same goes for all other months). 
In this example, Company Names is the primary 
key 
Relational Scheme
A relational 
database is a 
collection of 
tables, each of 
which is 
assigned a 
unique name. 
Each table consists 
of a set of attributes 
(columns or fields) 
and usually stores a 
large set of tuples 
(records or rows). 
Each tuple in a 
relational table 
represents an 
object identified 
by a unique key 
(primary key) and 
described by a set 
of attribute values. 
Relations 
between different 
tables can be 
established 
through external 
keys
Relational Database for AllElectronics 
(example)
Consider AllElectronics being a fictious 
company for practical examples in this 
Unit. 
The company is described by the 
following relation tables: customer, item, 
employee, and branch. 
Database Logic Scheme
 When one deals with Databases, it is recommended 
having a look at the so-called Logic Schemes, which 
includes the following: 
 Tables (Entities): Data points in the system.
 Attributes (Fields): Properties or characteristics of the 
entities.
 Relationships: how entities are related to each other (e.g., 
one-to-one, one-to-many).
 Constraints: Rules that govern how data can be entered or 
linked (e.g., primary keys, foreign keys, unique constraints).
AllElectronics relation tables
 Here are the logic schemes related to AllElectronics relation tables: 
 customer (cust ID, name, address, age, occupation, annual income, credit information, category, . . . )
 item (item ID, brand, category, type, price, place made, supplier, cost, . . . )
 employee (empl ID, name, category, group, salary, commission, . . . ) 
 branch (branch ID, name, address, . . . )
 purchases (trans ID, cust ID, empl ID, date, time, method paid, amount) 
 items sold (trans ID, item ID, qty)
 works_at (empl ID, branch ID) 
 In simple words, each of the above lines corresponds to a table with the within-brackets attributes.
Relational Scheme for a relational database, AllElectronics
Access to Relational 
Databases
Structured Query-based Languages like SQL allow accessing DBs (Databases) 
in order to run some queries. 
An SQL query allows retrieving information out of databases. 
Join, Selection, Projection are the most popular relational-based query 
instructions
Example: Show me a list of all items that have been sold since January 2022”
It should be noted that relational languages also use aggregate functions 
such as sum, avg (average), count, max (maximum), and min (minimum).
Example: Show me the total sales of the last month grouped by branch
Quiz time! 
https://forms.gle/sHYeh1GbGaajVwco6 

What about Data Mining Relational Databases? 
Using data mining to search for data patterns
Data Mining can analyse customer data to predict the credit risk of new customers based on 
income, age, previous credit information. 
Data deviation is another essential task accomplished by Data Mining.
Items with sales far from those expected in comparison with the previous year
Deviations like that can be further explored 
Data Mining may discover there has been a change in packaging.
Data Warehouses
Imagine AllElectronics turning into a successful international company with 
several branches all around the world.
Each branch has its own set of databases.
You are interested in having in place the analysis of a specific company’s 
branch over item types.
Thinking of the task above is such a complex task if we refer to it only by using 
Relational Scheme Databases. 
Here is when Data Warehouse comes into play!
Data Warehouses
What is a Data Warehouse?
A data warehouse is a 
repository of information 
collected from multiple 
sources with a unified 
schema
Data Warehouses are 
constructed via Data 
Cleaning, Data Integration, 
Data Transformation, Data 
Loading, Data Refreshing.
The data in a Data 
Warehouse is usually 
organized around major 
subjects to help the process 
of decision making 
(customers, items, suppliers 
and activities).
Data are stored to provide 
historical perspectives (i.e. 
summarization of data over 
the last 6-12 months).
A Data Warehouse has a 
multidimensional data 
structure (Data Cube)
Each dimension 
corresponds to an attribute 
or a set of attributes.
Each cell stores the value of 
some aggregate measure: 
sum(sales_amount)
Data Warehouse – Drill-down, Roll-Up
 A Data Warehouse allows drill-down and roll-up, corresponding to different views of 
data. 
 Drill-down dissects data by zooming in on certain attributes 
 On the other side, Roll-up allows encompassing attributes into a more compact 
representation.
 Data warehouses provide online analytical processing (OLAP) tools for the interactive 
analysis of multidimensional data of varied granularities
 Example: 
 AllElectronics’ Sales are stored according to item (types), time (quarters), address (cities)
Figure 1.7 take from “Data Mining. Concepts and Techniques”. 
Address (cities) 
Time (quarters) 
Drill-down on Time data for Q1
Time (months)
Roll-up on address
Address (Countries) 
Transactional Data
Each record in a transactional database captures a transaction, 
such as a customer’s purchase, a flight booking, or a user’s clicks 
on a web page.
It generally includes a transaction ID and a list of items making 
up the transaction (the items purchased in the transaction). 
It should be noted that Transactional Databases can contain 
other tables related to purchased items (item description, 
information about the shop or salesperson). 
An example of transactional database for AllElectronics is now 
given
AllElectronics Transactional DB
 Example: Zooming in on AllElectronics Transactional DB it can be noticed a column for 
transaction ID and a second one for the list of item IDs. 
 The information provided by transactional DB like this allows bundling items into a market 
bucket. That is a pragmatic example for for boosting sales.
*Jiawei Han. “Data Mining” 

Other Kinds of Data
 Time—related or sequence data (stock exchange; historical records; time 
series; biological sequence data)
 Hypertext and multimedia data (text; image; video and audio data)
 Graph and networked data (Social and Information networks)
 Stock Exchange can be mined to retrieve trends for investment strategies
 Computer Network data streams can be mined to check anomalies in the 
network (Intrusion detection systems)
 Images can be mined with machine learning methods to classify objects in 
them. Semantic labels are then assigned to categorise an image dataset. 
What Patterns can be mined? 
Classes or 
Concepts
Associations 
and 
Correlations
Classification 
and 
Regression
Cluster 
Analysis 
Outlier 
Analysis
Class and Concepts
 Data Entries can be associated with classes or concepts. 
 AllElectronics store sells several items that can be grouped into categories according 
to their cost (BigSpender, budgetSpenders).
 Individual classes and concepts are summarised with detailed terms. 
 Such descriptions are called “concepts” or “class”. 
 These description can be derived using data characterisation or by using data 
discrimination
 Data Characterisation is a summarization of the general characteristics of a target 
class of data (characteristics of software tools with sales incremented by 10% over 
the last year). 
 Data Discrimination is a comparison of the general features of the target data class 
objects 
Characterisation & Discrimination
 Data Characterisation and Discrimination 
output examples: 
 pie charts, bar charts, curves, multidimensional 
data cubes, and multidimensional tables

Examples
 Data Characterisation Task:
 Summarize the characteristics of customers who spend more than $5000 a year at 
AllElectronics.
 Result: A general profile of these customers (e.g. they are in the range 40 through 40 years of 
age, employed, excellent credit ratings)
 Data Discrimination Task: 
 A customer relationship manager at AllElectronics wants to compare two groups of customers 
according to their purchased items. In greater detail, the manager wants to compare the 
customers who regularly buy items and those who rarely shop the same items. 
 Result: A comparative profile of these customers. For instance, 80% of the customers who 
frequently purchase computer products are in the range 20 through 40 years of age, they 
have an university education.  60% of customers who rarely purchase the same items have no 
university degree and are older/younger than the first customers’ group. 
Frequent 
Patterns 
Patterns in data can be found in the 
form of items that are frequently present 
in databases. 
Set of Items often appear regularly 
together in a transactional dataset (milk 
and bread are usually purchased 
together).
Mining frequent patterns allows 
extracting associations and correlations 
within data.  
Example: Association Analysis
You want to know which items are frequently purchased together at 
AllElectronics 
An example of Association Analysis is given below:
Buys(X,”computer”)=> buys(X,”software”) [support = 1%, confidence=50%]
The example above tells about the association between customers and 
purchased items. 
X is a variable representing a customer while computer and software are 
purchased items. 
Example: Association Analysis
Buys(X,”computer”)=> buys(X,”software”) [support = 1%, confidence = 50%]
Support = 1% means that 1% of all transactions analysed show that computer 
and software are purchased together. 
50% of confidence means that if a customer buys a computer there is a 50% 
chance that they will purchase software as well. 
Associations are usually taken in consideration only if the confidence is above a 
certain threshold.
Classification for Predictive Analysis
What is classification? 
• Classification is the process of finding a model or a function that 
distinguishes data classes or concepts.
• In order to run classification tasks, a model needs to trained over the so -
called training set (the items in the training set are with known labels)
• Running a classification task means to make predictions on new input 
data by using a model that inferred knowledge from the training set. 
Classification can be carried out using several approaches:
• IF THEN ELSE (rule-based classification)
• Decision Tree (A network with nodes representing several tests)
• Neural Network (Training sets are needed to infer knowledge from 
labelled data).
Regression
Whereas Classification returns discrete values (labels), 
regression functions return values in a continuous range. 
Regression is used to predict missing or unavailable numerical 
data values rather than class labels. 
Regression analysis is a statistical methodology that is most 
often used for numeric prediction. It also deals with the 
identification of distribution trends. 
Classification needs labelled data, Regression ingests 
numbers to make statistical predictions (for instance, 
predictions on future trends based on past data sequences).
Example: Classification Vs Regression
In this case, a classification system will return one out of the given classes
A sales manager from 
AllElectronics wants to 
classify a large set of 
items in the store, based 
on three kinds of 
responses to a sales 
campaign:
good response
 mild response
no response (meaning 
that we have three 
labels). 
Example: Classification vs Regression
 Suppose you are asked to forecast the possible revenue for an upcoming sale of a 
specific item. 
 What you are supposed to do is to show forecasts across different months
 In cases like this, classification does not suit the purpose!
 Regression provides a curve in a diagram.

Cluster Analysis
Unlike classification and regression, cluster analysis groups data samples without 
consulting labels. 
In some case scenarios, labelled data are not available. 
Cluster analysis can be used to generate labelled data. 
Example: Suppose you are asked to identify subpopulation groups from the customers 
of your company. For instance, you might be asked to divide the company’s 
customers into three different groups according to customers’ locations.
Cluster Analysis
Customers from Italy
Customers from Spain
Customers from Portugal
What Technologies are used? 

Statistics
Data Mining has an 
inherent connection with 
statistics:
Statistic studies 
collections, analysis, 
interpretation of data
A statistical model is a Set of Mathematical 
Functions that describe the behaviour of 
variables in a dataset.
The behaviour is 
described with random 
variables and associated 
probability distributions. 
Statistics can be used 
to represent a data 
noise model 
Statistics can be used 
to summarise 
collections of data
Statistics
Inferential Statistics models data to draw inferences about 
the population under investigation
A Statistical Hypothesis Test is paramount to the process of 
statistical decision on top of experimental patterns
A result is “Statistically Significant” whether it does not happen 
by chance
There are several tests allowing to determine whether a result 
is Statistically Significant
Quiz time! 
https://forms.gle/L75iyiRbUqvwnnWKA 


---

# Document: Lecture_02_Clustering_Techniques.pdf

Data Mining and Text 
Analytics
•I U L M  U N I V E R S I T Y  –
P O S T G R A D U A T E  P R O G R A M M EI N  
" A R T I F I C I A L  I N T E L L I G E N C E  F O R  
B U S I N E S S  A N D  S O C I E T Y "
•L E C T U R E _ 0 2
•T O P I C :  C L U S T E R I N G  
•P R O F E S S O R  A L E S S A N D R O  B R U N O
Unearthing Structure in the 
Unknown
• The word "Unknown" refers to the lack of labelled data. 
• Because of the missing labels, we must dive into the "Unknown" 
without supervision. 
• That takes us to a journey to Unsupervised Learning. What is it about? 
• Unsupervised learningis a branch of machine learning where 
algorithms try to find patterns in data without labelled examples or 
direct guidance.
• Other than supervised learning, which works with labelled data (input-
output pairs), unsupervised learning works with unlabelled data, 
discovering the inherent structure on its own.

Unearthing Structure in the Unknown
What are the key characteristics of unsupervised learning?
• No labels or target outputs are provided during training
• The algorithm must identify patterns, relationships, and structures independently
• There's often no single "correct" answer - different algorithms may find different valid 
structures
• Evaluation can be challenging since there's no ground truth to compare against
Supervised 
Learning and 
Ground Truth
In data science, Ground Truth refers to the true, verified values or labelsused 
as a benchmark to train and evaluate models.
It represents the actual outcome or classification that a model should ideally 
predict.
Ground truth is crucial in supervised learning, where models learn from 
labelled data.
Here is an example: images labelled as "cat" or "dog," or customer reviews 
tagged as "positive" or "negative." 
During evaluation, model predictionsare compared against the ground truth
to calculate performance metrics like accuracy, precision, and recall. 
Essentially, the ground truth acts as the gold standard for validating how well 
a model generalizes from the data.
Reviewing the importance of 
Unsupervised Learning
• Unsupervised learning is particularly valuable when:
• You have large amounts of unlabelled data
• You want to discover hidden patterns without 
preconceived notions
• Labelling data would be prohibitively expensive or time-
consuming
• You need to understand the natural structure of your data 
before applying other techniques
• Some examples follow to let you have a better grasp of 
the above-mentioned concepts. 

Discover 
hidden patterns 
without 
preconceived 
notions
An e-commerce site analyzes customer purchase 
data.
Instead of testing predefined marketing 
hypotheses, unsupervised learning might 
unexpectedly reveal that customers who buy 
gardening tools also frequently purchase bird 
feeders.
That's a connection that marketers did not 
anticipate, which opens up new cross -selling 
opportunities.
You have large amounts of 
unlabelled data
• A social media platform tracks millions of daily user 
interactions. 
• Rather than manually categorizing users, unsupervised 
learning can be used to automatically identify different user 
segments based on behaviour patterns.
• For instance, clustering might reveal distinct groups like 
"content creators," "passive scrollers," and "social 
connectors" without anyone having to define these 
categories in advance.
Labelling data would be prohibitively expensive 
or time-consuming
• There is a medical research project featuring 10,000 brain scans. 
• Having specialists manually label each scan could take months and cost hundreds of 
thousands of dollars. 
• Unsupervised learning can group similar scans together, allowing experts to examine just a 
few representative examples from each cluster rather than every individual scan.
• Using unsupervised learning techniques might help save a lot of time and working hours. 
Understanding the natural structure of data before 
applying other techniques
• A company analyzes customer service calls. 
• Before building a supervised classification system, they use unsupervised learning to discover 
the natural categories of calls. 
• This reveals there are seven distinct types of customer issues rather than the three categories 
they were using in their manual system. 
• This insight helps them design a better supervised modelwith more appropriate target labels.
Let's get back on track with Clustering!
• What is clustering? 
• Let's have a defintion for Clustering: 
• Clustering is a technique in machine learning and data analysis that groups similar data points 
together based on their characteristics or features. It's an unsupervised learning method, 
meaning it doesn't require labelled data to find patterns.
Clustering
• The main goal of clustering is to organize data into 
meaningful groups where:
o Items within the same cluster are similar to 
each other
o Items in different clusters are dissimilar 
from each other
Clustering 
• The simplest and most fundamental version of cluster analysis 
is partitioning.
• In partitioning clustering, the objects of a given dataset are 
organised into several exclusive groups or clusters. 
• The number of clusters in partitioning clustering is given in 
advance. 
• The number of clusters is the starting point for partitioning 
clustering methods.
• Formally, given a dataset, D, of n objects, and being k the 
number of clusters to form, a partitioning algorithm organises 
the objects into k partitions (k lower or equal to n). 
• One of the most representative partitioning clustering 
methods is K-means
Clustering
• There are several clustering 
approaches in the scientific literature. 
• Here are some of the most popular: 
o K-means
o Hierarchical clustering
o DBSCAN (Density-Based Spatial 
Clustering of Applications with Noise)
K-means 
• K-means is a popular and relatively simple algorithm used in various fields 
like customer segmentation, image analysis, and document clustering.
o "K" is the number of clusters you want. You must decide this beforehand.
o It's an iterative process. It keeps refining the clusters until they stabilize.
o It aims to group similar data points together.
K-means (pseudocode) part 1
1. You pick a number (that's the "K" in K-means).
This number tells you how many groups (clusters) you want to find. Let's say you pick 3, so 
you want to find 3 groups.
2. You randomly place "K" (in our example, 3) "centres" on the map (centroids).Think of these 
as initial guesses for the centre of each group. They could be anywhere.
3. Each dot on the map is analysed accordingto its distance to the 3 centres. You then assign 
each dot to the group of that closest centre. So, all the dots closest to the first centre form 
group 1, all the dots closest to the second centre form group 2, and so on.
K-means (pseudocode) part 2
4. Recalculating the "centre" of each group.
For each group, you look at all the dots that belong to it and find the average position (the 
new centre) of those dots. This new centre is hopefully a better representation of where the 
group is located.
5. Repeating steps 3 and 4.
You re-assign each dot to the closest new centre, and then you recalculate the centres of 
the groups based on the new assignments.
6. Keep doing this until the centres don't move much anymore, or the groups don't change 
significantly. When this happens, it means the algorithm has found a stable set of clusters.
K-means scatter plot 
The scatter plot you can see on the 
right is an example of K-means 
with K=3. 
You can notice the three centroids 
(C1, C2, C3) within the three 
clusters. 
C1
C2 C3
K-means Pros
• Pros
• Simplicity: Conceptually straightforward and easy to 
implement
• Efficiency: Fast with linear time complexity O( n·k·d·i) where n 
is the number of data points, k is the number of clusters, d is 
the dimensionality, and i is the number of iterations
• Scalability: Works well on large datasets with high dimensions
• Guaranteed convergence : Will always converge to a local 
optimum
• Adaptability: Can be modified (k-means++, mini-batch k-
means) to improve performance
• Interpretability: Results are easy to understand and explain
K-means Cons
• Cons
• Requires specifying k:  the number of clusters in advance must be decided in advance
• Sensitive to initialization: Final clusters can vary based on initial centroid placement
• Limited to spherical clusters: Performs poorly when clusters have complex shapes
• Sensitive to outliers: Outliers can significantly distort the mean calculation
• Euclidean distance limitation: Standard implementation uses Euclidean distance, which may 
not be appropriate for all data types
• Not deterministic: Different runs can produce different results due to random initialization
Running K-means over a customer purchasing 
dataset
• Check out the following GitHub repository 
https://github.com/alessandrobruno10/IULM 
• Open your terminal, browse your working folder and type as follows to clone the repo on your 
folder: 
• $ git clone https://github.com/alessandrobruno10/IULM 
• You'll have a K-means solution clustering a customer purchasing dataset, which is a .csv file. 
Hierarchical Clustering
• Hierarchical clustering is generally considered the opposite of partitioning clustering methods 
like K-means.
• What are the most meaningful differences between Partitioning Clustering and Hierarchical 
Clustering? 
Partitioning Clustering 
• Creates a single-level, flat partition of data points
• Requires specifying the number of clusters in 
advance
• Optimizes a global objective function
• Allows data points to move between clusters 
during optimization
• Typically produces disjoint clusters
Hierarchical Clustering
• Creates a multi-level hierarchy of nested clusters
• Doesn't require pre-specifying the number of 
clusters
• Makes local decisions at each step (which clusters 
to merge/split)
• Once a point is assigned to a cluster, it cannot be 
reassigned
• Produces a complete dendrogram showing 
relationships between clusters at different levels
Hierarchical Clustering
• Agglomerative (bottom-up): 
• Starts with each data point as its own cluster
• Progressively merges the closest clusters
• Continues until all points belong to a single cluster
• Divisive (top-down): 
• Starts with all points in one cluster
• Recursively splits clusters
• Continues until each point is in its own cluster

Agglomerative Clustering
1. Assign each point to its own cluster
2. Compute distances between all cluster pairs
3. Merge the two closest clusters
4. Update distances between the new cluster 
and all others
5. Repeat steps 3-4 until only one cluster 
remains

Clusters distance
• Distance between clusters can be measured using different 
approaches:
• Single linkage: Distance between the closest points in two clusters
• Complete linkage: Distance between the farthest points in two 
clusters
• Average linkage: Average distance between all point pairs across 
clusters
• Ward's method: Minimizes the increase in within-cluster variance


Dendrogram description 
• The dendrogram is a visual representation generated (Ward’s method is used here) for hierarchical 
(agglomerative) clustering.
• Each vertical line represents a cluster merge, and the height at which two clusters are joined 
reflects the distance (or dissimilarity) between them. 
• You can "cut" the dendrogram at any height to choose the number of clusters you want, for 
example, cutting at a certain height might give you 3 clusters.
Hierarchical 
Clustering 
(Pros)
Allows for a visual hierarchy (dendrogram)
Does not require pre-specifying cluster 
count
Versatile with different distance metrics
Can discover clusters of various shapes
Useful for exploring data structure
Hierarchical Clustering (Cons)
Computationally expensive (O(n³) time complexity)
Can't undo merge/split decisions
Sensitive to noise and outliers
Challenging to interpret with large datasets
Hierarchical Clustering in Retail Supply Chain Optimization
• The Business Problem
• A national retail chain with over 500 stores was struggling with inventory management 
challenges:
o Frequent stockouts at some locations
o Excess inventory at others
o Rising logistics costs
o Declining customer satisfaction
• Traditional approaches using geographic zones or store size weren't effectively capturing the 
complex patterns in demand and inventory needs.
Hierarchical Clustering in Retail Supply Chain Optimization
• The supply chain analytics team implemented hierarchical clustering to identify natural 
groupings of stores with similar operational patterns:
• Data Collection: They gathered 18 months of data for each store including: 
o Sales velocity by product category
o Seasonal demand fluctuations
o Return rates
o Delivery lead times
o Storage capacity
o Local market characteristics
Hierarchical Clustering in Retail Supply Chain Optimization
• Clustering Approach: They used agglomerative hierarchical clustering with 
Ward's linkage to group stores based on operational similarities rather than 
just geography.
• Dendrogram Analysis: By analyzing the dendrogram, they identified seven 
distinct store clusters that represented natural breakpoints in operational 
patterns.
Coding Hierarchical 
Clustering
Open your terminal, browse your working folder to 
clone the repository with the code snippets:
$ git clone 
https://github.com/alessandrobruno10/IULM.git
Look at the csv file containing the dataset
Run the python program to launch Hierarchical 
Clustering and check out the dendogram

DBSCAN (Density-Based Spatial Clustering of Applications with 
Noise)
• What is DBSCAN for? 
• What does it make DBSCAN different from Hierarchical Clustering and K-means? 
• Let's dig into it! 
• First, DBSCAN is specifically designed to find clusters of arbitrary shapes in data while 
effectively identifying and isolating noise points.
DBSCAN
• Finding Arbitrary-Shaped Clusters: Unlike k-means which finds circular/spherical clusters, 
DBSCAN can identify clusters of any shape.
• Noise Detection: DBSCAN automatically identifies outliers as "noise" points that don't belong 
to any cluster.
• No Pre-defined Cluster Count: You don't need to specify the number of clusters in advance 
(unlike k-means).
DBSCAN in a nutshell
• DBSCAN functioning relies on two parameters:
• Epsilon (ε): The maximum distance between two 
points to be considered neighbors
• MinPts: Minimum number of points required to 
form a dense region
• The algorithm classifies points as Core, Border, 
and Noise points.
DBSCAN in a nutshell
• Core points: Have at least MinPts neighbours 
within ε distance
• Border points: Within ε of a core point but have 
fewer than MinPts neighbours
• Noise points: Neither core nor border points
• DBSCAN is valuable when you don't know how 
many clusters exist in your data and when your 
clusters might have complex, non -convex shapes 
that algorithms like k -means would struggle with.

Let's have a look at DBSCAN 
vs K-means 
• Consider a spatial datapoint distribution
• We want to have a better grasp of DBSCAN and K-
means working on the data and creating clusters. 
• A graphical animation helps us out with the 
understanding of the different clustering 
approaches. 
White dots represent data 
points that we want 
DBSCAN to cluster. 
Picture credits: 
https://medium.com/@jdseo/understanding-dbscan-a-practical-guide-for-beginners-with-business-applications-
9458792d1df8
K-means in action on the 
same data points. 
Noticeably, the spatial 
cluster distribution 
depends on centroids' 
coordinates. 
Picture credits: 
https://medium.com/@jdseo/understanding-dbscan-a-practical-guide-for-beginners-with-business-applications-
9458792d1df8
Take-home 
Messages
• Unsupervised Learning is adopted whensamples in our dataset are not 
labelled
• Clustering is an unsupervised learning approach grouping similar 
datapoints 
• Clustering methods are mainly grouped into partitioning and 
hierarchical (there is also density-based clustering methods though). 
• K-means is a partitioning clustering method (K is to be given in 
advance)
• Hierarchical Clustering can be agglomerative or divisive
• Hierarchical Clustering is visually represented by a dendrogram.
• DBSCAN is a density-based clustering approach that relies on two 
parameters ε, and MinPts.


---

# Document: Lecture_03_Perceptron_and_Learning_Process.pdf

From the First 
Artificial Neuron to 
Multilayer 
Perceptron
Lecture_03 Data Mining and Text Analytics 
Postgraduate Programme in Artificial Intelligence for 
Business and Society
IULM University 
A. Y . 2025/2026
Professor Alessandro Bruno
Seeking 
Patterns
Back in the 1950s, ethologists discerned some patterns in the behaviour of 
animals.
"Newly hatchedducklingsexhibit the abilityto tell apartthe properties ofthe 
things they see moving around them. It turns out thatducklingscan imprint not 
just on the first living creature they see moving, but on inanimatethigs as well.
Mullard ducklings can imprint 
on relational concepts embodiedby the 
objects around them.
"If upon birth the ducklings see two moving 
red objects, they will later follow two 
objects of the same colour (even if those 
latter objects are blue, not red)".
They also exhibit the ability todiscern dissimilarity. If the first moving 
objects they see are, for example, acube and a rectangular prism, theywill 
recognise that the objects have different shapes. They will laterfollow two 
objects that aredifferent in shape(a pyramid and a cone) while they will 
ignore two objects having the same shape.
Seeking 
Patterns
Newly hatched ducklings detect patterns in what they see 
(similarity and dissimilarity) with the briefest exposure to 
sensory stimuli.
They can act upon sensorystimuli once they 
detect similarity and/or dissimilarity.
Today's AIis way far 
from implementingsuch tasks. 
However,it does have something 
in common with the ducklings.
That's the ability to pick out 
and learn about patterns in 
data
When Frank Rosenblattinvented the Perceptron in the late 
1950s, that represented a breakthrough in the AI landscape 
as it was the firstoutstanding"brain-inspired" algorithm that 
could learn about patterns in data simply by examiningthe 
data.
Perceptron's 
roots
Perceptron's roots
• "The perceptron's roots lie in a paper published in 1943 by 
an unlikely combination of a philosophically minded 
neuroscientist in his mid-forties and a homeless 
teenager."
• Warren McCulloch was an American neurophysiologist 
trained in philosophy,psychology, and medicine.
• During the 1930s, he worked on neuroanatomy, creating 
maps of the connectivity of parts of monkey brains. 
Afterward, he focused on the "logic of the brain" . 
• The work of mathematicians and philosophers, such 
as Alan Turing, Alfred North Whitehead, and Bertrand 
Russell suggested ties and connections between 
computation and logic.
Perceptron's 
roots
Here is an example of a logical proposition - "If P is true 
AND Q is true, then S is true" 
The assertion was that all computaion could be 
reduced to such logic.
Here is the big question that prompted Warren 
McCulloch's research at that time: "If the brain is a 
computational device, as many think it is, how does 
it implement such logic?"
Perceptron's 
roots
McCulloch met Walter Pitts (a prodigiously talented 
teenager) in the 1940s at the University of Illinois.
Walter Pittswas a "runaway" from a family that could 
not appreciate hisgenius.
McCulloch and his wife, Rook,gave Walter Pitts a 
home and followedendless evenings discussinghow the 
brain worked.
In 1943, a paper co-authored by McCulloch and Pittsand 
titled "A LogicalCalculus of the Ideas Immanentin 
Nervous Activity" was published.
In that work both authors proposed a simple modelof a 
biological neuron.
Perceptron's roots
• Let's begin with a biological neuron:
o The neuro's cell body receives inputs via its treelike 
projections (DENDRITES).
o The cell body performs some computation on the inputs.
o Based on the computation results, the cell body may send 
signals (spiking signals) along another longer projection 
called AXON.
o The mentioned signal travels through Axon terminals to 
communicate with neighbouring neurons .
Dendrites
Perceptron's roots
• McCulloch and Pitts turned out with a simple 
computational model, an artificial neuron.
• The artificial neuron, also called NEURODE 
(neuron + node), could implement basic 
BOOLEAN logical operations such as AND, OR, 
NOT , and so on, which are the building blocks of 
the digital computation.
Zooming in 
on Neurode
How does a Neurode work?
• The  NEURODE performs a simple computation:
• Given the Inputs: x1, x2 ∈ {0, 1}
• Sum the inputs.
• Compare the sum to a threshold ( θ).
• Output: y equals 1 if the sum of x1 and x2 is greater than the threshold, 0 otherwise.
   1  if (x1 + x2) ≥ θ
• y  =
 0  else
• This mechanism can implement basic Boolean logic operations: AND, OR, NOT, forming fundamental 
building blocks of digital computation.
Graphical Representation of Neurode
NEURODE
y = x1 + x2
Moving on to Perceptron - Rosenblatt
b + b)
How does 
Perceptron 
differ from 
Neurode?
As noticeable in the previous slide, new elements 
make their way into Perceptron with respect to 
Neurode.
What are wi and b?
We will get there in a minute. 
Firstly, it is worth diving into Rosenblatt's intuition 
and the way he tackled "learning" processes.
Rosenblatt's Intuition
• Rosenblatt looked up to McCulloch and Pitts' contribution (Neurode) and extended their breakthrough into 
AI by extending a computational model into something new: 
• "artificial neurons that reconfigure as they learn, embodying information in 
the strengths of their connections" .
• In the summer of 1958, the editor of the Cornell Aeronautical Laboratory's 
Research Trends magazine devotedto Rosenblatt.
• The article was titled "The Design of an Intelligent Automation: Introducing 
the Perceptron – a Machine that Senses, Recognises, Remembers, and 
Responds like the Human Mind" .
Rosenblatt and Perceptron
• Rosenblatt chose Perceptron to describe his work, although it 
became one of his great regrets, as the word sounded way too 
much like a machine.
• By "perceptron" Rosenblatt meant a class of models of the 
nervous system
Perceptron

Perceptron (1958)
• Rosenblatt was a psychologist and did not have hardware computational resource to test his 
theory
• Therefore, he borrowed time on an IBM 704 from the Cornell Aeronautical Laboratory
• IBM 704 is a 5-ton, room size, behemoth (in simple terms, a gigantic computer)
• Have look at the whole IBM 700 series of computers
o https://www.ibm.com/history/700  (IBM (n.d.))
o https://www.youtube.com/watch?v=DKaVvv15Heo (YouTube video, 6 June 2024)
Overall Perceptron Architecture
• Each input (xi) is multiplied by its 
corresponding weight (wi). You may also notice 
an extra input b.
• The computation carried out by the perceptron 
goes like this:
• sum = w1x1 + w2x2 + … + wnxn + b
• If sum > 0  y = 1
• Else  y= -1
Overall Perceptron 
Architecture
• The output is either 1 or –1 (instead of 0 and 1 as for 
the McCulloch and Pitts' Neurode)
• b is an extra parameter accounting for BIAS
• Crucially, unlike with the Neurode, the Perceptron 
can learn the correct value for the weights and the 
bias for solving some problem.
• Hold on!
• How does it work?
y
Overall Perceptron Architecture and 
Learning process
• Imagine a simple perceptron that decides whether someone would enjoy a pizza based on two inputs: 
spiciness level (x1) and cheese amount (x2). We'll use a threshold of 0 and train the perceptron to predict 
pizza enjoyment.
• Initial setup:
• Weights: w1 (spiciness) = 0.5, w2 (cheese) = 0.5
• Bias: -1 (arbitrarily chosen)
• Threshold activation function: 
• If (w1x1 + w2x2 + bias) > 0, output = 1 (will enjoy pizza)
• If (w1x1 + w2x2 + bias) ≤ 0, output = -1 (will not enjoy pizza)
Perceptron Learning Process
• Training examples:
• Given the starting weight values (w1 = 0.5, and w2 = 0.5) and the arbitrarily assigned value for bias set 
to -1, let's work out some examples:
• Training Example (a): 
• Mild spicy (x1 = 2), lots of cheese (x2 = 3), target (+1, the training example is labelled as "enjoy the pizza")
Let's use those values in the numerical expression 
y=w1x1 + w2x2 + b
• y = 0.5 * 2 + 0.5 * 3 - 1 = 2.5 - 1 = 1.5
• 1.5 > 0 → (Correct Prediction)→Actually enjoys pizza (output= +1) 
Perceptron Learning Process
• Training Example (b)
• Very spicy (5), little cheese (1), Label "dislikes pizza" (target = -1)
• Using the given values with the threshold activation function:
• y = 0.5 * 5 + 0.5 * 1 –1 = 2.5 + 0.5 - 1 = 2
• The predicted value is 2 > 0 meaning that the output is (+1) "likes pizza" .There is a mismatch between the 
training target (-1) and the predicted value (+1).
• The learning algorithm will adjust weights based on prediction errors, gradually finding the 
right balance to correctly classify pizza preferences.
• Each misclassification triggers a weight update that moves the decision boundary closer to perfectly 
separating "enjoy" and "don't enjoy" pizza scenarios.
Rolling down training process
Let's recap from Training Example (b).
Training Example (b):
• Inputs: x1 = 5 (very spicy), x2 = 1 (little cheese)
• Target = -1 (dislikes pizza)
• Step 1: Compute weighted sum y = w1x1 + w2x2 + b y = (0.5 * 5) + (0.5 * 1) - 1 = 2.5 + 0.5 - 1 = 2
Step 2: Activation
• Since y = 2 > 0, the current weights predict +1 (enjoys pizza)
• But the actual target is -1 (dislikes pizza)
• This means we have a misclassification
Rolling down training process
Step 3: Weight Update
• Learning rate (let's use α = 0.1)
• Update rule: Δwi = α * (target - prediction) * xi
• Δw1 = 0.1 * (-1 - (+1)) * 5 = 0.1 * (-2) * 5 = -1
• Δw2 = 0.1 * (-1 - (+1)) * 1 = 0.1 * (-2) * 1 = -0.2
• Δbias = 0.1 * (-1 - (+1)) = -0.2
New weights after update:
• w1 = 0.5 - 1 = -0.5
• w2 = 0.5 - 0.2 = 0.3
• bias = -1 - 0.2 = -1.2
The training process keeps going on until some requirements are met (see the next slide).
When does the training 
process stop?
The Perceptron training typically stops under these conditions:
Convergence Criteria:
• All training examples are correctly classified
• No weight updates are needed in a complete pass through the 
training data
Practical Stopping Mechanisms:
• Maximum iteration limit
• No weight changes beyond a small threshold in an entire 
epoch
• No misclassifications in the last complete pass

Perceptron 
constraints and 
limitations
Linearly 
Separable 
Data
Linearly separable data  refers to a set of data points 
that can be perfectly divided into two distinct classes by 
drawing a single straight line (in 2D) or a hyperplane (in 
higher dimensions) .
In the context of the Perceptron algorithm, linear 
separability is a crucial concept because it determines 
the algorithm's ability to find a perfect decision boundary. 
When data is linearly separable, the Perceptron learning 
algorithm is guaranteed to converge , meaning it will 
find a set of weights that can correctly classify all training 
examples after a finite number of iterations.
Conversely, if the data is not linearly separable , the 
Perceptron will not converge and will continue to make 
classification errors indefinitely.
Linearly Separable Data
• Figure out the following scenario:
o Some data points are represented upon two features 
(A and B).
o That might be, for instance, the representation of 
customers on geographiclocation (A) and 
expenditure (B) feature
o If "customers" data points can be dividedby a single 
straight line (as in the diagramon the right side), that 
means they are linearly separable.
Practical 
Applications
A practical 
perceptron 
application 
(spam, non-
spam 
classification)
https://github.com/alessandrobruno10/perceptron
Check out the Python project at the link below:
https://github.com/alessandrobruno10/perceptron
Set up a new Python virtual environment on your 
laptop and run it to assess performances. 
MultiLayer Perceptron

MultiLayer Perceptron (MLPerceptron)
• Multilayer Perceptron (MLP) represents a neural architecture that relies upon the primary concepts as in 
Perceptron.
• Main differences:
o Multiple layers: input layer, hidden layer(s), output layer
o Introduces non-linear activation functions  (e.g., sigmoid, ReLU)
o Can create complex, non -linear decision boundaries
o Learns hierarchical feature representations
MLP can model intricate relationships between inputs and outputs. They rely upon hidden layers to learn higher 
level features (starting from raw data, it can learn how to represent highly representative features from data).
Learning Mechanism: Uses backpropagation to update weights across all layers (getting all the way back 
from output to intermediate layers).
Hidden Layers
• Mathematically, hidden layers transform the input space into a more separable feature space where complex 
classifications become possible.
• Let's address Hidden Layers by tackling Functional Purposes, Computational Mechanisms, and  Key 
Characteristics.
• Functional Purposes:
o They represent Intermediate layers between input and output  layers
• They transform input features through weighted linear combinations
• They apply non-linear activation functions  to introduce complexity (so that even non-linearly separable data can 
be handled)
Hidden Layers
• Computational Mechanisms:
o They receive weighted inputs from previous layer
• They apply activation function (e.g., ReLU – Rectified Linear Unit, Sigmoid)
• They generate transformed features passed to subsequent layers (as you go along with layers, you find higher level 
features).
• Key Characteristics:
o Not directly observable  from outside the network ( black box)
o Number of neurons  determines representational capacity
o Weights in hidden layer learn intermediate feature representations
o Non-linear activation functions enable modelling of complex, non -linear relationships
Sigmoid Function & ReLU
Both introduce nonlinearities to the architecture allowing it to handle with non-linearly separable data
Sigmoid ReLU
Why do Perceptron 
and MLPerceptron 
matter today?
• Perceptron allows us to learn some of the most 
meaningful concepts in AI:
o Training Process
o Weighted sum of inputs + Bias
o Learning rate
o Prediction Error (difference between classification 
and prediction outputs)
o Linearly Separable Data
• MultiLayer Perceptron overcomes Perceptron due 
to nonlinearities it adds to the learning process 
with activation functions and hidden layers.
o It is currently broadly adopted due its relatively low 
computational cost, compared with deep learning 
methods
o It can infer knowledge from plenty scenarios as in 
reality data are rich of nonlinearities.


---

# Document: Lecture_04. Text Mining_1.pdf

Data Mining and 
Text Analytics
Postgraduate 
Programme in "AI for 
Business and Society " 
A.Y. 2025-2026 
Lecture_04
Prof. Alessandro Bruno
Dr Alessandro Bruno 
Outline
 Definitions
 Basic Concepts
 Textual Content
 Text Mining and 
NLP
 Application 
domains
 Main Tasks
 LLMs 
(foundation 
models and 
GPT-based)
 Text 
Classification
 Text Clustering
 Topic Model
 Topic Detection 
and Tracking
 Information 
Extraction
 Text 
Summarisation
 Challenges
 Word-Vector 
Representation 
(Embeddings)

Definitions: 
•“The non-trivial 
extraction of implicit, 
previously unknown, 
interesting facts from 
a collection of texts.”
•“The non-trivial 
extraction of implicit, 
previously unknown, 
and potentially useful 
information from 
data.”
There is no 
canonical 
definition for 
Text Mining. 
We will 
borrow one 
from the 
Data 
Mining:
Data Mining 
definition:
Data 
Mining-
based 
definition for 
Text Mining
Credits go Rob Sanderson from Liverpool University to https://ucrel.lancs.ac.uk/events/htm06/RobSandersonHTM06.pdf 
Definitions: 
Gartner glossary provides a 
definition for Text Mining:
“The process of extracting 
information from collections 
of textual data and utilising it 
for business objectives.”
Source: https://www.gartner.com/en/information-technology/glossary/text-mining
Gartner, Inc. is an American research and advisory firm focusing on business and technology topics
Some Basic Concepts
• Analysis & Modeling of unstructured 
natural language context
Main text 
mining goals:
• almost always unstructured (unlike 
databases and data warehouse)
• described by natural language (ruling 
out graphics and images)
Textual content
Structured vs Semi-Structure vs 
Unstructured Textual Content 
 Structured Data: Data with high degree of organisation ( in a spreadsheet-like manner). 
 Semi-structured Data: Data with some degree of organisation. 
 Unstructured Data: Data with no predefined organisation.
 Some examples:
Structured Data Semi-structured Data Unstructured Data
Excel spreadsheets; 
Comma-separated value 
file; Relational Database 
Tables.
HTML files; Json files; XML 
files.
PDF files; Word Files, Plain 
text files. 
Around 20% of worldwide 
data is structured.
Characterised by 
hierarchical structure.
Most of data that is created 
today is unstructured. 
(Tweets, Facebook posts, 
social media comments).
Text Mining 
An integrated technology 
of NLP (Natural Language 
Processing), Pattern 
Classification, and ML 
(Machine Learning).
Mining refers to tasks such 
as discovery, search, 
induction, and 
refinement.
Subsequently, targets 
being sought are often 
not found 
straightforwardly. 
Target-related 
information is frequently 
hidden and concealed in 
text.
Text Mining and NLP: Objectives
NLP (Natural Language Processing) 
and Text Mining goals are different. 
NLP aims to understand human 
language through the analysis of 
text, speech, or grammatical syntax.
Text mining is used to extract 
information from unstructured and 
structured content. It focuses on 
structure rather than the meaning of 
content.
Text Mining
Two main scenarios 
can be described in 
Text Mining upon users
Users’ questions are 
specific but they do 
not know the answer 
(scenario 1)
Users know the 
general aims and 
scope but do not 
have specific 
questions (scenario 2).
Text Mining Application Domains
Economy
Social 
Management
Information 
Services
Security
 Risk 
Management 
Customer 
Care Service
Fraud 
Detection 
Business 
Intelligence
Social Media 
Analysis
Customer 
Churn 
Prediction
Q&A Systems
Marketing
Some historical hints
Traditional data mining relies on structured data such as database tables (relational 
model).
In the late 90s, researchers started using text as data, giving rise to text mining. 
Early text mining applied data mining and machine learning algorithms on text data 
without using NLP techniques.
NLP (Natural Language Processing) has a longer history. It all started back in 1950s.
•GOAL: Make computers understand Human Language.
Later on, Text Mining started using NLP techniques. Subsequently, in the past 10 year, 
NLP and Text Mining have tackled some common points, albeit with different goals. 
Professor Bing Liu's Interview from Sharon Dexter (Project, It Manager, Green Book)
Link to interview
Text Data Mining Figures
 CAGR in business and finance 
stands for Compound Annual 
Growth Rate
 Here is a diagram with figures 
on Text Analytics over the next 
few years.
URL: https://www.mordorintelligence.com/industry-reports/text-analytics-market 

Main Tasks 
of Text 
Mining
Text Mining is often hidden within several 
applications:
•For instance, Q&A (Question & Answering) systems 
have text data mining deal with tasks such as 
knowledge base search, inference and filtering of 
candidate answers, question parsing
In this unit, 7 main tasks are considered: 
•Text Classification
•Text Clustering
•Topic Model 
•Text Sentiment Analysis and Opinion Mining
•Topic Detection and Tracking
•Information extraction
•Automatic Text Summarisation
It’s raining LLMs 

LLMs for 
text mining 
and NLP 
The seven steps listed in the previous slide 
refer to standard Text Mining and NLP 
methods that are still in use. 
LLMs (Large Language Models) have made 
their way through Text Mining and NLP field.
In this unit, standard Text Mining and NLP as 
well as LLMs will be covered. 
In this slide-deck some insights into LLMs will 
be given. 
LLMs (Large Language Models)
Still under development, 
but they have learned to 
perform many kinds of 
tasks, including:
Following your instructions and completing your requests thoughtfully
Using their knowledge to answer your questions in a comprehensive and informative way,even if they are open 
ended, challenging,or strange
Generating different creative text formats and content,like poems, code, scripts, musical pieces,email, letters, etc.
Foundation models are typically trained on massive amounts of text data, and they can be used to generate text, translate languages, 
write different kinds of creative content, and answer your questions in an informative way. 
LLM foundation model is a large, pretrained language model that can be used for a variety of natural language processing (NLP) tasks. 
Foundation Models and ChatGPT
An LLM 
foundation model 
and ChatGPT
are both large language models 
(LLMs), but they have some key 
differences.
LLM Features
large, pre-trained language 
model used for a variety of 
natural language processing 
(NLP) tasks. 
trained on massive amounts of 
text data, used to generate text, 
translate languages, write 
different kinds of creative 
content, and answer your 
questions in an informative way. 
ChatGPT
is a specific LLM that has been 
fine-tuned for conversational 
dialogue. It was trained on a 
dataset of text and code, and it 
can be used to generate 
realistic and coherent chat 
conversations.
Foundation Models and ChatGPT
Feature LLM foundation model ChatGPT
Purpose General-purpose NLP
Conversational 
dialogue
Training data
Massive amounts of text 
data
Dataset of text and 
code
Tasks
Generate text, translate 
languages, write different 
kinds of creative content, 
answer questions
Generate realistic and 
coherent chat 
conversations
Strengths Versatility, accuracy Fluency, realism
Weaknesses Bias, computational cost Limited scope
Quiz time!
 Scan the QR code or visit the link below to run a quiz
 https://forms.gle/z7mKKrptZNdLwXHP9 

Text Classification
www.sina.com
Goal: Divide test into 
predefined text types
Type: It is a pattern 
classification technology 
Example: Chinese Library 
Classification www.sina.com 
All books are grouped into 5 
categories and 22 
subcategories. The 
classification task is run on 
the content. 
Link to Google Colab Project on Text Classification 
Text Clustering
Text Clustering divides a given text into 
different categories. 
Clustering does not include predefined 
categories. The number and type of 
categories depend on some criteria, 
evaluation and indices. 
Example: Some text can be clustered into 
news, entertainment, sports, finance. 
Based on users’ viewpoint, a piece of text 
can be clustered into positive categories 
(positive and supportive attitudes) and 
negative categories (negative and passive 
attitudes). 

Topic Model
 A topic can be 
generally expressed by 
words having strong 
conceptual and 
semantic relationships. 
 Topic Model is a 
statistical approach 
assigning a topic 
probability value to 
each word. 
 Each topic carries to a 
specific dictionary 

Text Sentiment Analysis and Opinion Mining
Subjective information 
expressed by text’s 
authors
Revealing authors’ 
viewpoint and attitude Main GOAL: 
Sentiment 
Classification and 
Attribute Extraction. 
Sentiment 
Classification can be 
considered as a 
special case of Text 
Classification with text 
being classified upon 
some subjective views 
and attributes.
After a special event, 
news reports users’ 
comments will flood 
the Internet. 
Tendentiousness. A 
company releases a 
product and wants to 
timely catch 
customers’ evaluations 
and opinions. 
Topic Detection and Tracking
Mining and Screening 
of text topics from 
news reports and 
comments
Topics most people 
care about (hot 
topics). 
Hot topics detection, 
discovery and tracking 
are used in opinion 
analysis.
Example:
Hot Topics Today is a 
report on what is most 
attracting readers’ 
attention from the 
news. 
Information Extraction
Extraction of factual information such 
as, entities, entity attributes, 
relationships between entities, events 
from unstructured and semi-
structured text. 
Sources: Web News, Academic 
Documents, Social Media
Main Information Extraction tasks:
• Named Entity Recognition
• Entity Disambiguation
• Relationship Extraction
• Event Extraction
Information Extraction
Information Extraction has recently become popular across several application 
domains, such as, biomedical/medical text mining, financial field, social reputation. 
It should be noted that the relation in information extraction usually refers to some 
semantic relation between two or more concepts.
In daily life, the way people describe events refers to aspects such as, when, where, 
and what happened. 
In event extraction, the event usually refers to a specific state expressed by a certain 
predicate framework. 
“John meets Mary” 
In daily life, people think of a story
In event extraction, the “event” is “triggered” by a verb and is nothing more than a state
or an action. 
Automatic 
Text 
Summarisation
https://www.textcompactor.com/
Technology focusing on automatically generating 
summaries using natural language processing 
(NLP) methods. 
Visit the link https://www.textcompactor.com/ 
That is an online tool for text summarisation. 
When information is saturated, several companies 
employs text summarisation to cut the chase and 
extract the most meaningful excerpts from text. 
Homework assignment No. 1
 “Obviously, language is not only about computation. The most 
difficult thing to do is to create a tool that is “smart”, i.e. it can 
understand not only grammar but also the semantics of a 
text.”
 Above is a quote from the article by Marco Belmondo 
(Chief Marketing Officer at Datrix group) titled “Why use an 
automatic text summarization tool for digital content?”
 Read the whole article and answer the question below:
 What are the benefits of Text Summarisation for Businesses? 
(Max 100 words).

Text Mining applications in Marketing 
Sentiment analysisis 
an excellent tool for 
marketers
Categorizing survey 
responses
Scoring survey 
results
Understanding the 
customer 
experience
Gauging customers’ 
interest in your new 
products.
Main challenges in Text Mining
Today’s challenges for 
Text Mining
Noise or ill-formed 
expressions
Ambiguous expression 
and concealment of 
text semantics
Difficulty in collecting 
and annotating 
samples
Complexity in 
streamlining text 
mining results (hot 
words extraction and 
conversion into story 
outlines)
Semantic 
Representation vs 
Computational 
Models.
Main Challenge in Text Mining 
 Noise or ill-formed expression:
 Literary works, academics publications, political article, news article 
from TV channels and other media channels stick to some standard 
semantic rules. 
 If we compare the above-mentioned scenarios with online text, 
things change dramatically 
 Several ill-formed expressions are in online websites
 Ill-formed expressions make it harder to NLP and Text Mining tasks to 
be accurate.
 CWS (Chinese Word Segmentation) achieves accuracy rates over 
than 95% when fed by People’s Daily
 CWS (Chinese Word Segmentation) accuracy rates drop on online 
text (below 90%). 
Main Challenge in Text Mining
Ambiguous expression and concealment of text 
semantics
• “Bank” may refer to a financial bank or a river bank
• “Apple” may refer to the fruit or to a product such as Apple Iphone, 
Apple Macbook, etc.
• “I saw a boy with a telescope”
• The sentence above is ambiguous: it may refer to a boy holding a 
telescope being seen by me; it may refer to a boy being seen by me 
through a telescope.
• The correct parsing of statements like this is challenging for NLP 
systems.
• There are no effective methods to sort out this challenge.
Main Challenges in Text Mining
Data 
Collection 
and 
Annotation
The mainstream text mining methods are 
machine learning-based
Traditional statistical-based machine learning 
Deep Learning 
Large collections of annotated data are 
necessary 
Obtaining large amount of data from online 
websites might be difficult due to copyright 
protected contents. 
Even when there is no copyright related 
issues, online content is generally unwell 
formatted and needs several processing 
steps 
On top of that, if contents pertains to a 
specific area, experts are needed to 
manually annotate the content itself.
Main Challenges in Text Mining
 One of the most well-know challenges regards the word-vector representation

Word Vector Representation 
Word to vector representation, also known as word embedding, is a technique used in 
natural language processing (NLP) to represent words and phrases as numerical 
vectors.
There are many different methods for word embedding, but they all share the same 
basic goal of capturing the semantic and syntactic relationships between words . 
One popular method is called word2vec, which was developed by Google. 
Word2vec uses two architectures: continuous bag -of-words (CBOW) and continuous 
skip-gram. Both architectures work by predicting the surrounding words given a target 
word.
Word2Vec
A phrase like “The King is born” is divided into words. 
Each word is converted into numerical vectors (Embeddings).
Embedding
Main Challenges in Text Mining
Word Vector representation  has been broadly adopted in Machine 
Learning methods. 
The challenge is about the connection of lexical semantics of words 
to phrase, sentence, paragraph, and discourse semantics .
On a side, Machine Learning methods can be effective on semantics 
representations of words. 
On another side, semantics representation of “ ensemble of words” 
such as statements, sentences, and paragraphs are not 
straightforward to be processed with ML methods
Takeaway points
 Text mining can be defined as the non-
trivial extraction of implicit, previously 
unknown, interesting facts from a 
collection of texts
 Text content is almost always unstructured
 The following seven topics will be tackled 
in this unit: Text Classification; Text 
Clustering; Topic Model; Text Sentiment 
Analysis and Opinion Mining; Topic 
Detection and Tracking; Information 
extraction; Automatic Text Summarisation
 LLMs Foundation models and fine-tuned 
versions (ChatGPT) are also used to 
address NLP tasks



---

# Document: Lecture_05 Text_Mining_2.pdf

Data Mining and Text 
Analytics 
Lecture_05 "Text 
Mining_2"
Postgraduate Programme in 
AI for Business and Society
Prof Alessandro Bruno
Data Annotation and Processing
Outline
 Data Annotation 
 Preprocessing Steps 
 IMDB case study 
 Web Scraping (Crawling)
 Robots.txt
 Tokenization
 Word Form Normalisation
 NER (Named Entity Recognition) 
 Syntax and Dependecy Tree
Data 
Acquisition
Data Acquisition sources →
Different Mining Tasks
Data Sources
Open Domain 
Data
Social Media 
Networks
Data Sources
Closed Domain 
Data 
Financial field
Healthcare systems
Data Acquisition
Acquiring data from by solely relying on a specific domain 
might not be sufficient 
Why is that so? 
specific domain implies professional domain knowledge.
Healthcare systems:
• EHR (Electronic Health Records) are full of medica terms 
Financial Field
• Very specific terms referring to investments, fundings. 

Data 
Acquisition
Closed Domain 
Publicly available data sources 
are often used to 
counterbalance the missing 
information from closed domain 
scenarios
Wikipedia 
Baidu
Encyclopedia
Textbooks 
It should be noted that Public Networks usually contain much 
more noisy and ill-formed expression. 
Overhead processing: Cleaning, Pre-processing routines are 
needed!
Data Acquisition: 
the IMDb use case
 IMDb is a pretty popular 
website that provides users 
with comments on movies. 
 IMDb webpages are full of 
links to movies
Website link to IMDb: https:// www.imdb.com  
The IMDb use 
case
Users can easily check out 
rates and comments.
Lots and lots of comments 
can be read by clicking on the 
yellow star. 

The IMDb use case
One can easily scroll down the users’ reviews
all the way down to the bottom of the page.
Is there a way to automatically crawl the whole  
“reviews” contents? 
Python programming language library named 
urllib2 helps users download the entire section 
contents
That goes under the name of Web Crawling (or Web 
Scraping)
 
Top
Bottom
Webpage content crawling
https://www.imdb.com/robots.txt
Python Programming Language 
Urllib2 library 
Checking out the robots protocol of the website 
Robots.txt is a file containing all the limitations 
enforced against crawling 
https://www.imdb.com/robots.txt  → this URL 
contains the robots protocol with a limitation list 

Webpage content extraction
 Since no restriction are in place to download reviews 
content, the owner allows users/developers to crawl these 
contents.
 Webpage content crawling is recommended during low 
networking activity, usually overnight. 
 Beautiful Soup is a Python based toolkit to extract content 
and obtain the link to the next webpage. 
 It should also be noted that webpage contents are full of 
special symbols with no semantic meaning.  
 The task of content analysis is named “parsing”
 Special symbols like “&nbsp”, “&It” represent space and 
less-than, respectively.  
Does robots.txt enforce limitations by the 
Law? 
Introduced as "Robots Exclusion Protocol"
The file robots.txt does not enforce legal 
constraints against web scraping. 
Nevertheless, it plays an important role in 
setting the expectations and permissions of 
a website owner regarding automated 
access.
Special 
Symbols in 
Web Data

What is the end for Special 
Symbols? 
 Remove Special Symbols
o Noise Reduction: Eliminates irrelevant characters that can hinder analysis.
o Standardization:  Ensures consistent data format for efficient processing.
o Improved Accuracy:  Focuses on essential text elements for accurate 
insights.
 Impact on Text Mining Techniques
o Sentiment Analysis:  More precise sentiment detection without distractions.
o Topic Modeling:  Clearer identification of underlying themes.
o Text Classification:  Enhanced categorization accuracy.
Webpage Content 
Extraction
Once the reviews content 
is obtained, it undergoes 
data cleaning.
Furthermore, any noise 
word is removed. 
Zooming in on Content Processing 
within Data Acquisition
Noise Processing 
Removal of comments that are too short 
(meaningless)
Mappings of labels 
Noise Processing
The IMDb website may 
contain symbols such as 
“@”, advertisement links, 
and so on. 
“@” may be followed by 
a user name. 
Are those textual 
elements and symbols 
meaningful to Text 
Mining? 
They are not meaningful 
to it. 
Rule-based or template -
based approaches are 
used to remove noisy 
symbols or textual 
elements within contents
Removal of too 
short text
 Depending on the content language, there needs 
word segmentation in order to have the correct 
word counting in place. 
 For instance, counting the number of words in 
English content is straightforward as it can be done 
by counting the number of spaces. 
 In Chinese content, you may have some separate 
characters to be combined to form words. 
 A simple rule-based system sees removal of words 
shorter than a certain threshold. (i.e. remove all words 
consisting of less than 3 characters).
Mappings of labels
Websites "hide" labels within their “html” code.
Those labels might be different in numbers and name than 
the ones considered by a classifier.
A label mapping steps is needed to sort out any forms of 
ambiguity between the two groups of labels-categories
Mappings of labels
Some examples of labels and categories
• Download Evaluation score uses a 5 -point system
• A sentiment classifier uses only a 2 -point system
• A label mapping is necessary to avoid any mismatch
• Generally 1 and 2 for the Download Evaluation score represent 
negative feedback
• At the same time, 4 and 5 are positive feedback 
• If we cast it upon a sentiment scale, 3 is halfway through it (it could be 
considered as a neutral feedback).
• Solution: 1 and 2 are mapped into Negative Feedback;
• 4 and 5 are mapped into Positive Feedback
• 3 is removed as it represent a neutral evaluation of the download 
process.
Data Preprocessing 
Tokenization
Removing 
stop wordsNormalisation 
Tokenisation
https://platform.openai.com/tokenizer
What is Tokenisation? 
How does it work? 
Give it a go at the link below:
https://platform.openai.com/tokenizer  
Type in a paragraph of your choice and check out the generated 
tokens
Tokenization
 Preprocessing steps come into play Immediately after data 
acquisition. 
 Tokenization refers to a process of segmenting a given text into 
“lexical” units. 
 Latin and inflectional languages (e.g. English) use spaces as 
word separators.
 Only space and punctuation marks are required to realise 
lexicalization.
 Other than above, languages with no separation marks 
(Chinese), and some agglutinative languages (e.g. Japanes, 
Korean, Vietnamese) go first with word segmentation. 
 
Removal of stop words
Functional words: auxiliary words, prepositions, conjunctions, modal words, high 
frequency words that often appear in documents carrying only little text information.
“The, is, at, which, on” are examples of functional words. 
GOAL: Minimising the storage space for text mining.
Functional Words are discarded during the phase of text representation.
In the implementation phase of a Text Mining module, a list of stop words is established. 
All stop words are removed before proceeding to feature extraction
Word Form Normalisation
• Lemmatisation 
• Stemming
Word form normalisation consists of two concepts:
• Lemmatisation is the restoration of arbitrarily deformed words into 
original forms 
(e.g. cats → cat, did → do)
• Stemming is the process of removing all affixes to obtain roots 
(fisher → fish, effective → effect)
Definitions
Word Form Normalisation
 It is usually realised by rules of regular expressions
 Porter stemming is a a widely employed stemming algorithm consisting 
of four main steps:
 1. Dividing letters into vowels and consonants
 2. utilising rules to process words ending with suffixes of –s, -ing, and 
–ed.
 3. designing special rules to address complicated suffixes (e.g. –
ational)
 4. fine-tuning the processing results by rules.
 It should be noted that several stemming algorithms exist and bring 
different results (even with the same language).
 On an application oriented note, NLTK toolkit in Python provides calling 
functions for Porter stemming algorithm.
Data 
Annotation

Data Annotation
It represents the foundation of 
Supervised Machine Learning 
tasks
Data (e.g. statements 
extracted from the Internet)
Annotated Data 
Statements on Marketing Topics
Statements on topics different than 
Marketing
Classifier
Data Annotation 
Bigger volumes 
of annotated 
data can take to 
higher quality 
results
Broader 
coverage can 
make better-
trained model 
performances
Data Annotation, some examples:
 Here is a textual description of a patient’s postoperative course after heart failure 
symptoms appear.
 Mr Shinabery is a 73-year-old gentleman who returned to Surgluthe Leon Calcner 
Healthcare to the emergency room on 9/9/02 with crescendo spontaneous angina 
and shortness of breath. He is three-and-one-half months after a presentation with 
subacute left cyrcumflex thrombosis, ischemic mitral regurgitation, pulmonary 
edema and a small nontransmural myocardial infarction. Dilation of the left 
circumflex resulted in extensive dissection but with eventual achievement of a very 
good angiographic and clinical result after placement of multiple stents, and his 
course was that of gradual recovery and uneventful return home.
Textual excerpt Data Annotation
Mr Shinabery is a 73-year-old gentleman who returned to 
[Surgluthe Leon Calcner Healthcare]Hosp to the emergency room 
on [9/9/02]Time with [crescendo spontaneous angina]sym and 
[shortness of breath]sym. He is [three-and-one-half months]dur after 
a presentation with [subacute left cyrcumflex thrombosis]dis, 
[ischemic mitral regurgitation]dis, [pulmonary edema]dis and a 
small [non-transmural myocardial infarction]dis. [Dilation of the left 
circumflex]Treat treat resulted in extensive dissection but with 
eventual achievement of a very good [angiographic and clinical 
result]TR after [placement of multiple stents]Treat, and his course 
was that of gradual recovery and uneventful return home.
Hospital, Time, symptoms, duration, disease, Treatment,
Treatment Result
Data Annotation - Challenges
As in the last example, 
data annotation task is 
not a straightforward 
one! 
Professional Knowledge 
can be necessary in 
order to get the right 
labels and words.
Data Mining techniques 
have also multimodal 
data annotation in 
place especially when 
text, videos and images 
are to be annotated. 
Data Annotation (some definitions)
Lexicon: A lexicon 
generally has a highly 
structured form.
It stores the meanings and 
uses of each word.  It 
encodes the relations 
between words and 
meanings.
Corpus: a corpus is a 
collection of authentic text 
or audio organized into 
datasets. Authentic here 
means text written or audio 
spoken by a native of the 
language or dialect. 
A corpus can be made up 
of everything from 
newspapers, novels, 
recipes, radio broadcasts 
to television shows, movies, 
and tweets.
In natural language 
processing, a corpus 
contains text and speech 
data that can be used to 
train AI and machine 
learning systems.
Text Mining 
and NLP

Basic Tools of NLP
Text Mining involves 
several tasks from 
NLP (Natural 
Language 
Processing), pattern 
classification, and 
machine learning. 
Here is a list of basic 
NLP tools:
•Word segmenters;
•Syntatic parsers;
•Part-of-speech taggers;
•Chunkers

NLP tool (1) Tokenisation
It separates text into a sequence of “words” called “tokens”.
• “That’s” → tokenisation → that, ‘s (two tokens)
• “rule-based” → tokenisation → rule, -, based (3 tokens)  
Examples:
The NLTK toolkit provides a tokenization package. 
NLTK toolkit URL:  https://www.nltk.org/api/nltk.tokenize.html 
NLP tool (1) Tokenisation
You are asked to run tokenisation on a given paragraph from a 
marketing website: 
“The Gatherverse community is squarely focused on the metaverse 
and the community implications these new technologies present to 
business leaders and organizations.  The group leads with wellness, 
ethics, and safety which is a refreshing change from many other tech 
events that are more focused on ROI and business outcomes. Very 
much like the tenets of my Metaverse Manifesto, there is a strong focus 
on digital citizenship, inclusion, and accessibility of the metaverse for 
all.”
Copy and paste it onto the form at link below:
http://text-processing.com/demo/tokenize/ 
NLP tools (some 
considerations)
When using statistical methods, 
words sharing the same stem are 
to be considered as the same 
word. 
Think of the following words: 
Take, takes, taken, took, taking 
(different forms of the same 
word due to grammatical 
reasons)
Token, tokenize, tokenization 
NLP Tools (2) Syntactic Parser
Syntactic parsing refers to mining 
phrase structure, and 
dependency
Automatic analysis of phrase 
structure relation in a sentence 
Output: Syntactic structure tree of 
the parsing sentence
Streamlining Text Mining 
 Several Processes, such as POS (Part-of-Speech) Tagging 
and NER (Named Entity Recognition), come into play to 
streamline Text Mining tasks. 
 POS tagging, for instance, works out all grammatical 
functions played by each word in a sentence. 
 That gives rise to a tree-shaped scheme, called 
dependency tree!
 We may also have some complementary information 
provided by syntactic tree, providing us with phrase-level 
information. 
 Some examples are shown in the next slides. 
Syntax Tree 

Dependency Tree

Syntactic and Dependency Tree
 A few differences are drawn below: 
 Dependency Tree:  
o Shows direct relationships between words; 
o Each word connects directly to its head word
o Focus on word-to-word relationships
o No intermediate nodes 
 Syntactic Tree: 
o Shows hierarchical phrase structure 
o Uses intermediate nodes
o Groups words into constituents
o Shows how phrases are built up
Syntactic and Dependency Tree
 Dependency Tree: 
o Better for showing grammatical relationships
o Useful for relation extraction
o More compact representation 
o Easier to process computationally
 Syntactic Tree: 
o Better for showing phrase structure
o Useful for understanding sentence composition
o Shows nested relationships
o Important for grammar analysis 
Syntactic and Dependency Tree
 Dependency Tree: 
o Word level analysis 
o Focus on functional relationships
o Direct grammatical connections
 Syntactic Tree:
o Phrase level analysis
o Focus on structural composition
o Hierarchical organization
NER – Named Entity Recognition
 Named Entity Recognition serves as a crucial preprocessing 
component in text analysis and NLP workflows. 
 Its integration into the preprocessing pipeline enhances text 
understanding and preparation for downstream tasks. 
NER – Named Entity Recognition
 Smart Content Filtering - Isolates meaningful entities from text automatically - 
Helps focus analysis on key information (e.g., extracting prominent figures and 
locations from news articles) 
 Enhanced Text Cleaning - Removes non-essential content strategically - Focuses 
on maintaining identified entities while eliminating noise
 Advanced Feature Creation - Transforms recognized entities into model-ready 
features - Adds entity-type context (e.g., Person, Location, Organization) to 
improve model performance 
 Standardization Techniques - Creates consistent entity representations across 
texts - Enables anonymization through entity-type placeholders (e.g., converting 
"Sarah Johnson" to ``) 
 Knowledge Connection - Identifies entities for external database linking - 
Enriches content through connections to knowledge bases (e.g., linking 
company names to their database entries) 
 Intelligent Text Segmentation - Preserves multi-word entities as single units - 
Improves tokenization accuracy (e.g., maintaining "San Francisco" as one entity) 
 Specialized Processing - Adapts to domain-specific needs (e.g., medical terms, 
financial indicators) - Extracts field-relevant entities (e.g., gene names in 
biological texts, company symbols in financial reports) This structured 
preprocessing approach using NER helps prepare text data more effectively for 
various analytical tasks, ensuring important entities are properly identified and 
handled throughout the analysis pipeline.
NER – an example
Let's say we want 
process a sentence 
and map entities in it. 
"Tim Cook met with 
Microsoft executives in 
Seattle last Friday to 
discuss AI 
developments worth 
$50 million."
NER output
 The output shows these entities:
 "Tim Cook" - PERSON (People, including fictional)
 "Microsoft" - ORG (Companies, agencies, institutions)
 "Seattle" - GPE (Countries, cities, states)
 "Friday" - DATE (Absolute or relative dates or periods)
 "AI" - ORG (Companies, agencies, institutions)
 "$50 million" - MONEY (Monetary values, including unit)
*GPE stands for Geo-political Entity.


---

# Document: Lecture_06 Text Classification.pdf

Data Mining and Text Analytics
Lecture_06: Text Classification and Insights into Machine Learning 
and Architectures
Postgraduate Programme in AI for Business and Society 
A.Y. 2025/2026 
Prof Alessandro Bruno 
Traditional vs Newer Machine 
Learning approaches 
 There are plenty of machine learning methods applied on so many 
scenarios, which can be grouped into two families: Traditional and Newer 
Machine Learning approaches. 
 The major different lies within a specific step: feature extraction 
 In traditional Machine Learning approaches feature extraction is detached 
from all steps involved in training, validation and testing. 
 You need to use feature extraction methods to set up arrays and vectors 
that better fit your experiments or your application. 
 In some cases, you may use statistical descriptors as features representative 
of a given input data. 
 The features are then ingested by the "traditional" machine learning 
architecture for training purposes. 
 The punch line is as follows: you need to be good at extracting features 
that help a model discriminating categories of interest for your application. 
Traditional vs Newer Machine Learning 
Approaches
 "Newer" machine learning approaches mostly refers to 
Deep Learning, which relies on DNNs (Deep Neural 
Networks). 
 Deep Learning approaches learn hierarchical 
representations automatically (no manual feature 
engineering needed)
 They Improve their performance with more data and 
computational power ("scale up" well)
 They get through huge data volume and extract complex 
patterns (in unstructured data, such as images, text, 
speech).

Traditional Machine Learning methods for 
Text Classification
Input Text 
(words, 
phrases, 
sentences) 
Feature 
Selection 
Machine 
Learning 
Model 
Training
Machine 
Learning 
Model 
Validation
Machine 
Learning 
Model 
Testing
Corpus Word Embeddings
Please note: a word embedding is a numerical array to represent 
a word (statements, documents, etc.)
Text Classification
Text classification is also known as text tagging or text categorization
Text classification is the process of categorizing text into organised groups. 
Text classifiers can automatically analyse text and then assign a set of pre -defined tags or categories based on its 
content.
For instance, one might be interested in classifying ”good” and ”bad” statements. 
Text Classification 
System
“You’re the best”
 Positive
Input Output
Traditional Framework of Text 
Classification
The traditional framework 
of text classification 
consists of three separate 
components: 
•Text Representation
•Feature Selection
•Classification  
Text representation plays 
a critical role. 
•it must reflect the 
content of the text and 
have sufficient ability to 
distinguish different types 
of text. 
The choice of text 
representation
•depends on the 
classification algorithm. 
SVM (Support Vector Machine) 
is a popular classification  
method
•It uses the vector space 
model (VSM) as text 
representation method. 
Feature Selection
Feature selection is the process of selecting a subset of features for text 
representation and classification. 
Feature selection methods normally include supervised and unsupervised 
approaches. 
Unsupervised approaches are applied to a corpus without category annotation. 
They generally rely on TF (Term Frequency) and DF (Document Frequency). 
Supervised approaches rely on category annotation, which can more effectively 
select a better subset of features for text classification. 
Traditional Machine Learning algorithms for 
Text Classification
Straight after text representation and feature selection, follows a classification algorithm. 
The most widely used text classification algorithms used in traditional machine learning are naïve Bayes, 
Maximum Entropy, and Support Vector Machines (SVM)
Naïve Bayes is a probabilistic model for binary and multi -class classification. 
Maximum Entropy is used for NLP classification tasks as it assigns P(x,y). 
•P(x,y) indicates the the joint probability of data observed (x) and the corresponding label (y).  
SVM (Support Vector Machine) is a supervised discriminative learning algorithm used for binary classification. 
The main goal is to identify an hyperplane in the data space where data samples can be separated into. 
Running Text Classification using SVM and 
Naïve Bayes
 Try and configure the off-the-shelf solution 
at the link below: 
 https://github.com/Gunjitbedi/Text -
Classification 
 You are given raw data (for instance, text 
from a webpage) 
 You will use SVM and Naïve Bayes to classify 
text. Some steps are to be accomplished 
before getting to classification )
 Installing required libraries
 Set random seed 
 Add the corpus
 Data Pre-processing
 Prepare Train and Test Datasets
 Encoding 
 Word Vectorisation 
 Using ML methods to run predictions 
Multilayer Feed-Forward Neural Network
 Forward-structure neural network that maps a set of input vectors to a set of 
output vectors in a multilayer fully connected manner. 
Figure. Feedforward neural network for classification task (Courtesy: Alteryx.com)

The network consists of 4 different layers:
one input layer (layer 1), two hidden layers (layer 2 and 3) and one output layer (layer 4)
There are four input variables which are fed into different nodes in the the neural network through 
input layer (1st layer). No computations happen in the input layer.
Layer 1 Layer 2 Layer 3 Layer 4
Layer 2: At each neuron, all incoming values are added together (weighted sum of input signals) 
and then fed into an activation function. 
Layer 1 Layer 2 Layer 3 Layer 4
Layer 3: At each neuron in layer three, all incoming values are added together and then processed 
with an activation function same as that used in layer 2
Layer 1 Layer 2 Layer 3 Layer 4
Output Layer: At each node in the output layer, all incoming values are added together in different 
nodes and then processed with a function such as softmax function to output the probabilities (in 
case of classification).
Layer 1 Layer 2 Layer 3 Layer 4
What happens in training steps?
Learning or training can be viewed as the process of optimizing the loss 
function, that is, determining the optimal parameters of the model that best fits 
the training data according to the loss function
What is the loss function for? 
Loss function determines the distance between model’s predictions and 
desired outputs. 
Backpropagation works to lower loss function value by updating the network 
parameters (or weights).

Backpropagation 
Taking the stock of 
backpropagation
 Forward Pass (Starting Point):
o The network makes a prediction with current weights
o Compares prediction to actual answer
o Calculates the error/loss
 Backward Pass  (The Core of Backpropagation ):
o Starts at output layer
o Calculates how much each weight contributed to the error
o Moves backward layer by layer
o Compute gradients (Direction and steepness of error change)
 Weight Update:
o Adjusts each weight based on its contribution to the error
o Uses learning rate to control size of adjustments
o Aims to reduce error in next forward pass
Activation 
Function

Convolutional Neural Networks (CNNs)
Convolutional Neural Network is a special kind of feed-forward neural network. 
The CNN’s hidden layers consists of a series of convolutional and pooling filters (convolutional layers 
select features out of the text unput). 
Pooling layers downsample the feature vectors and obtain a smaller representation of data. 
Topic and Sentiment Classification tasks started being accomplished with CNNs in 2014. Results 
showed substantial improvements compared to traditional machine learning algorithms. 
CNNs turned out very accurate in classification tasks (Computer Vision and NLP)
Convolutional Neural Network 
Figure: Courtesy https://www.nvidia.com/en-us/glossary/data-science/convolutional-neural-network/
Assignment (2): Text Classification via CNN
 Try and configure the following GitHub Project:
 https://github.com/cezannec/CNN_Text_Classification
Recurrent Neural Networks (RNNs)
 Recurrent (or Recursive) Neural 
Networks are a kind of deep neural 
network that applies the same set of 
weights recursively over an input 
(be it a textual input or a visual 
input). 
 Widely adopted in learning 
sequences in NLP (Natural 
Language Processing)
 A structure runs recursively on the 
network nodes
 A structure is expanded to a 
sequence.

Deep Learning Hyperparameters
Dataset
Train-test split ratio 
(rule-of-thumb: 80/20) 
Functions
Choice of optimization 
algorithm 
Choice of activation 
function in a neural 
network layer
The choice of loss 
function the model will 
use
Layers
Number of hidden 
layers in a neural 
network
Number of activation 
units in each layer
Convolutional Layers 
size
Pooling size
Iterations
Number of iterations 
(epochs) in training a 
neural network
Batch size (The batch 
size is a number of 
samples processed 
before the model is 
updated)
Text Classification performances
It is helpful to rate performances of classification systems.
•Concepts such as False Positive (FP), True Positive (True Positive), False Negative (FN), and True Negative come at handy 
and concur in determining performances metrics values. 
Here is a short list summarising the meaning of all the above-mentioned concepts: 
True Positive (TP) - The model correctly identifies a class (“good”)
True Negative (TN) - The model correctly identifies a negative class (“bad”).
False Positive (FP) - The model incorrectly identifies a negative class (a ”bad” statement is 
misclassified as “good”).
False Negative (FN) - The model incorrectly identifies a positive class (a “good” statement is 
misclassified as “bad”).
Confusion Matrix 
 Confusion Matrix helps to catch the overall performance of a given system.
 Premise: A given dataset is provided with sample and corresponding labels. 
A classification system runs predictions
to be compared with actual labels.
For instance, a given dataset consists of 
“bad” and ”good” statements.
The classification system makes predictions on 
input statements. 
”good” represents the positive class while 
“bad” plays as the negative class.
Precision, Recall, F-Measure (F1-score) 

Text Classification Performances
 F1-score (or F-measure) somewhat accounts for Precision and Recall
 However, you may want to diagram all three metrics values to better depict a classification 
system performances.
 Given a statement classification problem with 100 labelled statements. 
 Your model runs through them with the following results:
 TP = 65
 FP = 20
 FN = 15
 Calculate Precision, Recall and F-measure and lay out your considerations. 
Solution
 Precision = 65/85 = 0.76
 Recall = 65/80 = 0.81
 F-measure = 1.231/1.57 = 0.78 
0.76
0.81
0.78
PRECISION RECALL F-MEASURE
Classification Performances
Comparing two text classification systems
 Given two Text Classification systems, S1 and S2. You are asked to benchmark them 
on top the following results: 
 S1
 TP = 65
 FN = 5
 FP = 30
 S2 
 TP = 62
 FN = 12
 FP = 26



---

