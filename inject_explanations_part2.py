import re

explanations_part2 = {
    51: "L'Accuracy è la frazione di predizioni corrette (TP+TN) sul totale dei casi valutati.",
    52: "I Falsi Positivi (Errore di I tipo) sono casi negativi erroneamente classificati come positivi (allarme falso).",
    53: "La Precision indica quanti dei positivi predetti sono realmente positivi (TP / (TP+FP)).",
    54: "La Recall (o Sensibilità) indica quanti dei positivi reali sono stati correttamente individuati (TP / (TP+FN)).",
    55: "L'F1-Score è la media armonica tra Precision e Recall, utile quando le classi sono sbilanciate.",
    56: "Il Cross-Validation (es. K-Fold) serve a stimare l'affidabilità del modello dividendo i dati in K parti e ruotando training/test.",
    57: "L'Unsupervised Learning lavora con dati non etichettati, cercando strutture intrinseche (clustering, associazione, ecc.).",
    58: "Il Supervised Learning richiede un dataset etichettato (con coppie input-output target) per l'addestramento.",
    59: "Il Reinforcement Learning apprende tramite interazioni con un ambiente, ricevendo ricompense o penalità per le azioni svolte.",
    60: "La Normalizzazione (es. Min-Max scaling) scala i valori dei dati in un intervallo standard (solitamente [0,1]) per facilitare l'apprendimento.",
    61: "Big Data: Volume (quantità), Velocità (flusso continuo), Varietà (diversi formati), Veridicità (qualità) e Valore.",
    62: "NoSQL Database (es. MongoDB) sono database non relazionali progettati per scalabilità e flessibilità con dati non strutturati.",
    63: "Il Teorema di Bayes è la base dei classificatori Naive Bayes, calcolando probabilità condizionate.",
    64: "Naive Bayes assume l'indipendenza condizionale tra le feature, semplificando il calcolo della probabilità (spesso efficace per il testo).",
    65: "Decision Tree è un modello ad albero dove ogni nodo interno rappresenta un test su un attributo e le foglie le classi.",
    66: "Entropy e Information Gain sono metriche usate nei Decision Tree per scegliere il miglior attributo per dividere i dati.",
    67: "Random Forest è un metodo di ensemble che usa molti alberi decisionali per migliorare la robustezza e ridurre l'overfitting.",
    68: "Gradient Descent è un algoritmo di ottimizzazione iterativo per trovare i minimi di una funzione (es. minimizzare l'errore della rete).",
    69: "L'Epoch nel Deep Learning è un passaggio completo dell'intero training set attraverso la rete neurale.",
    70: "Il Learning Rate determina la dimensione del passo di aggiornamento dei pesi durante l'ottimizzazione; troppo alto o basso causa problemi.",
    71: "Underfitting avviene quando il modello è troppo semplice per catturare la struttura dei dati (alto bias).",
    72: "La Stopword Removal nel Text Mining elimina parole molto comuni ma poco informative per ridurre la dimensione del vocabolario.",
    73: "TF (Term Frequency) misura quante volte una parola appare in un documento specifico.",
    74: "IDF (Inverse Document Frequency) diminuisce il peso delle parole che appaiono in troppi documenti del corpus, considerandole meno distictive.",
    75: "La Cosine Similarity misura la similarità tra due vettori (es. documenti) calcolando il coseno dell'angolo tra loro.",
    76: "Il Corpus è l'intera collezione di documenti testuali oggetto di analisi.",
    77: "Bag of Words perde l'informazione sull'ordine delle parole e sulla struttura sintattica delle frasi.",
    78: "Word2Vec può usare due architetture: CBOW (predice parola da contesto) e Skip-Gram (predice contesto da parola).",
    79: "Le RNN soffrono del problema del 'Vanishing Gradient' su sequenze lunghe, spesso mitigato da architetture come LSTM.",
    80: "LSTM (Long Short-Term Memory) è un tipo di RNN capace di apprendere dipendenze a lungo termine grazie a 'gate' speciali.",
    81: "Nel K-Means, 'K' rappresenta il numero di cluster che l'utente deve definire a priori.",
    82: "Il 'Centroid' è il punto centrale (media) di un cluster nel K-Means.",
    83: "Outlier Analysis è il processo di identificazione di dati che si discostano significativamente dalla norma.",
    84: "Apriori Algorithm è usato per trovare itemset frequenti e generare regole di associazione in database transazionali.",
    85: "Support è la proporzione di transazioni che contengono un determinato itemset (frequenza relativa).",
    86: "Intelligence Density (ID) nel Data Mining si riferisce al valore della conoscenza estratta rispetto alla mole di dati (Yield).",
    87: "Knowledge Representation è la fase finale in cui la conoscenza scoperta viene presentata all'utente (grafici, regole, report).",
    88: "I dati Nominali (o Categorici) non hanno un ordine intrinseco (es. Colore: Rosso, Blu).",
    89: "I dati Ordinali hanno un ordine ma non una distanza misurabile costante (es. Gradi: Basso, Medio, Alto).",
    90: "I dati a Intervallo hanno un ordine e distanze costanti, ma non uno zero assoluto (es. Temperatura Celsius).",
    91: "I dati di Rapporto (Ratio) hanno ordine, distanza e uno zero assoluto (es. Peso, Altezza, Stipendio).",
    92: "Il Data Mining è interdisciplinare: unisce Statistica, Database, AI/Machine Learning e Visualizzazione.",
    93: "Scalabilità ed Efficienza sono sfide cruciali nel Data Mining dovute alla crescita esponenziale dei dati.",
    94: "Privacy e Sicurezza sono aspetti etici critici nel Data Mining, specialmente con dati personali.",
    95: "Il Web Mining si applica a contenuti (Text), struttura (Link) e utilizzo (Log) del Web.",
    96: "Sentiment Analysis è spesso chiamata anche Opinion Mining.",
    97: "La Lemmatization richiede un dizionario morfologico e analisi grammaticale, a differenza dello Stemming che è puramente algoritmico.",
    98: "Un Percettrone a singolo strato può risolvere solo problemi linearmente separabili (limite di XOR).",
    99: "Per una RNN applicata al testo, l'input tipico è una sequenza di vettori, dove ogni vettore rappresenta una parola (Word Embedding).",
    100: "Il KDD è descritto come un processo *iterativo e interattivo*, non lineare e automatico al 100%, richiedendo spesso il feedback umano."
}

def inject_explanations(filepath, exp_dict):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    new_lines = []
    current_q_id = None
    q_start_pattern = re.compile(r'^\s*(\d+)\.')
    
    # Simple state machine similar to part 1
    # We load explanations part 2
    
    for i, line in enumerate(lines):
        m = q_start_pattern.match(line)
        if m:
            current_q_id = int(m.group(1))
        
        new_lines.append(line)
        
        if current_q_id and current_q_id in exp_dict:
            # Check end of block
            if i + 1 < len(lines) and q_start_pattern.match(lines[i+1]):
                if "**Spiegazione:**" not in "\n".join(lines[max(0, i-5):i+1]):
                     new_lines.append(f"\n   **Spiegazione:** {exp_dict[current_q_id]}\n")
                     del exp_dict[current_q_id]
            elif i + 1 >= len(lines):
                 if "**Spiegazione:**" not in "\n".join(lines[max(0, i-5):i+1]):
                     new_lines.append(f"\n   **Spiegazione:** {exp_dict[current_q_id]}\n")

    return "".join(new_lines)

final_text = inject_explanations("simulazione_esame_completa.txt", explanations_part2)
with open("simulazione_esame_completa.txt", "w", encoding='utf-8') as f:
    f.write(final_text)

print("Injected explanations for Q51-100")
