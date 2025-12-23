import re

# Explanations for Questions 1-50
explanations = {
    1: "Data Mining è una fase specifica all'interno del processo più ampio di Knowledge Discovery Process (KDP), che include anche cleaning, integration e post-processing.",
    2: "La pulizia dei dati (Cleaning) avviene all'inizio del KDP per rimuovere rumore e incongruenze, preparando dati di qualità per l'analisi.",
    3: "Il Bias rappresenta una distorsione sistematica (es. pregiudizio nei dati di training) che può portare a modelli non rappresentativi o ingiusti.",
    4: "Data Mining è definito come l'estrazione automatizzata (o semi-automatizzata) di pattern, conoscenze e relazioni nascoste da grandi moli di dati.",
    5: "I dati strutturati (Structured Data) seguono un modello rigido, tipicamente organizzati in righe e colonne come nei database relazionali (RDBMS).",
    6: "La Data Integration serve a combinare dati da diverse fonti eterogenee (DB, file, API) in un unico repository coerente per l'analisi.",
    7: "Un Pattern è una struttura ricorrente o una relazione sistematica osservabile nei dati, che il Data Mining cerca di identificare.",
    8: "XML e JSON sono tipici esempi di dati Semi-strutturati: hanno una struttura interna (tag) ma non uno schema fisso e rigido come le tabelle relationali.",
    9: "Il Data Mining Predittivo usa il passato per stimare il futuro/sconosciuto; il Descrittivo cerca di caratterizzare le proprietà dei dati attuali.",
    10: "La sequenza logica standard è: Cleaning -> Integration -> Selection -> Transformation -> Data Mining -> Evaluation -> Presentation.",
    11: "Un DBMS è il software che gestisce la creazione, l'aggiornamento e l'interrogazione dei database, garantendo integrità e sicurezza.",
    12: "Il Data Warehouse è ottimizzato per l'analisi (OLAP) e il supporto alle decisioni, integrando dati storici, a differenza dei DB operazionali (OLTP).",
    13: "La Chiave Primaria (Primary Key) è l'attributo (o set di attributi) che identifica in modo univoco ogni record in una tabella.",
    14: "Il Data Lake è un repository che raccoglie grandi quantità di dati grezzi nel loro formato originale, senza imporre uno schema a priori (schema-on-read).",
    15: "Il Drill-down è l'operazione di 'zoom-in' che permette di visualizzare i dati con maggiore dettaglio (es. da anno a mese).",
    16: "Un Data Mart è un sottoinsieme del Data Warehouse focalizzato su un'area specifica o dipartimento (es. Marketing), per un accesso più rapido.",
    17: "OLAP (On-Line Analytical Processing) è la tecnologia per l'analisi multidimensionale interattiva dei dati (cubi OLAP).",
    18: "I Metadati sono 'dati sui dati': descrivono la struttura, l'origine, il formato e il significato dei dati stessi.",
    19: "SQL (Structured Query Language) è il linguaggio standard per interagire con i database relazionali.",
    20: "Big Data si riferisce a dataset così grandi, veloci o complessi (Volume, Velocity, Variety) da richiedere tecnologie specifiche oltre i tradizionali RDBMS.",
    21: "La Tokenization è il processo di suddivisione del testo in unità minime chiamate token (solitamente parole o punteggiatura).",
    22: "Le Stopwords sono parole comuni (es. 'il', 'di', 'a') che spesso vengono rimosse perchè portano poco significato semantico specifico.",
    23: "La Lemmatization riduce le parole alla loro forma base (lemma) considerando il contesto morfologico (es. 'andava' -> 'andare').",
    24: "Lo Stemming tronca le parole alla loro radice (stem) in modo euristico, spesso rimuovendo suffissi, senza garantire che la radice sia una parola valida.",
    25: "Bag of Words (BoW) rappresenta il testo come un insieme non ordinato di parole, contando la frequenza ma ignorando la grammatica e l'ordine.",
    26: "TF-IDF pesa l'importanza di una parola: aumenta se è frequente nel documento (TF) ma diminuisce se è comune in tutto il corpus (IDF).",
    27: "N-gram è una sequenza contigua di N item (parole) da un testo. Es. Bigramma: 'Data Mining'.",
    28: "POS Tagging (Part-of-Speech) assegna a ogni parola la sua categoria grammaticale (es. Nome, Verbo, Aggettivo).",
    29: "NER (Named Entity Recognition) identifica e classifica le entità nominate nel testo (es. Persone, Organizzazioni, Luoghi).",
    30: "Word Embedding (es. Word2Vec) mappa le parole in vettori numerici in uno spazio continuo, catturando relazioni semantiche.",
    31: "La Sentiment Analysis determina l'opinione o l'emozione espressa in un testo (Positiva, Negativa, Neutra).",
    32: "Topic Modeling è una tecnica non supervisionata per scoprire i temi (topic) astratti latenti in una collezione di documenti.",
    33: "La Classificazione è un compito di apprendimento supervisionato dove si prevede l'etichetta di classe discreta per nuovi dati.",
    34: "La Regressione predice un valore numerico continuo basandosi sulle variabili di input.",
    35: "Il Clustering raggruppa dati simili in insiemi (cluster) senza avere etichette predefinite (apprendimento non supervisionato).",
    36: "K-Means è un algoritmo di clustering a partizionamento che divide i dati in K gruppi minimizzando la varianza interna ai gruppi.",
    37: "Il Dendrogramma è il grafico ad albero usato per visualizzare la gerarchia dei cluster nel Clustering Gerarchico.",
    38: "DBSCAN è un algoritmo di clustering basato sulla densità, capace di trovare cluster di forma arbitraria e gestire il rumore.",
    39: "L'Association Rule Mining (es. Apriori) scopre regole del tipo 'Chi compra X compra anche Y' analizzando le transazioni.",
    40: "Supporto e Confidenza sono le metriche chiave per valutare la qualità delle regole di associazione.",
    41: "Una rete neurale artificiale (ANN) è un modello computazionale ispirato alla struttura dei neuroni biologici.",
    42: "Il Perceptron è l'unità base di una rete neurale, un classificatore lineare semplice.",
    43: "L'Activation Function (es. Sigmoide, ReLU) introduce non-linearità nella rete, permettendole di apprendere relazioni complesse.",
    44: "Backpropagation è l'algoritmo usato per addestrare le reti neurali, propagando l'errore all'indietro per aggiornare i pesi.",
    45: "Il Deep Learning utilizza reti neurali profonde con molti layer nascosti per apprendere rappresentazioni gerarchiche dei dati.",
    46: "Una CNN (Convolutional Neural Network) è specializzata ed efficiente per l'analisi di dati a griglia come le immagini.",
    47: "Una RNN (Recurrent Neural Network) è adatta per dati sequenziali (come il testo o serie temporali) grazie alla sua memoria interna.",
    48: "L'Overfitting avviene quando un modello impara troppo bene i dettagli (e il rumore) del training set, performando male su nuovi dati.",
    49: "Training Set e Test Set: il primo serve per istruire il modello, il secondo per valutarne le prestazioni su dati mai visti.",
    50: "La Confusion Matrix è una tabella usata per valutare le performance di un classificatore (Veri Positivi, Falsi Positivi, ecc)."
}

def inject_explanations(filepath, exp_dict):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    current_q_id = None
    
    q_start_pattern = re.compile(r'^\s*(\d+)\.')
    
    for i, line in enumerate(lines):
        m = q_start_pattern.match(line)
        if m:
            current_q_id = int(m.group(1))
        
        new_lines.append(line)
        
        # Check if we should insert explanation for the *previous* or *current* question
        # We assume we insert it at the end of the question block.
        # Simplest logic: Insert it BEFORE the next question starts, or at end of file.
        # But here we are iterating.
        
        # Let's peek ahead to see if block ends
        next_is_break = False
        if i + 1 >= len(lines):
            next_is_break = True
        elif q_start_pattern.match(lines[i+1]):
            next_is_break = True
        elif lines[i+1].strip() == "" and (i+2 < len(lines) and q_start_pattern.match(lines[i+2])):
             # Blank line then next question
             pass 
        
        # Actually simplest approach:
        # If we are inside a question (current_q_id is set)
        # And the next line starts a new question OR is the end of file
        # And we verify we haven't already inserted an explanation
        
        if current_q_id and current_q_id in exp_dict:
            # Check if this line is the end of options.
            # Usually options are indented.
            # If next line is a new question (regex match)
            if i + 1 < len(lines) and q_start_pattern.match(lines[i+1]):
                # Insert here
                # Check for duplicate
                if "**Spiegazione:**" not in "\n".join(lines[max(0, i-5):i+1]):
                     new_lines.append(f"\n   **Spiegazione:** {exp_dict[current_q_id]}\n")
                     del exp_dict[current_q_id] # Mark as done
            elif i + 1 >= len(lines):
                 # EOF
                 if "**Spiegazione:**" not in "\n".join(lines[max(0, i-5):i+1]):
                     new_lines.append(f"\n   **Spiegazione:** {exp_dict[current_q_id]}\n")

    return "".join(new_lines)

final_text = inject_explanations("simulazione_esame_completa.txt", explanations)
with open("simulazione_esame_completa.txt", "w", encoding='utf-8') as f:
    f.write(final_text)
    
print("Injected explanations for Q1-50")
