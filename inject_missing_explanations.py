
import re

# Missing: [102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 121, 122, 124, 125, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137]

missing_explanations = {
    102: "Ground Truth (verità fondamentale) si riferisce ai dati etichettati e verificati usati come standard di riferimento per addestrare o valutare i modelli.",
    104: "NER (Named Entity Recognition) è la task che estrae e classifica entità come Nomi, Organizzazioni e Luoghi dal testo.",
    106: "Il Data Mart è un sottoinsieme del Data Warehouse, progettato per soddisfare le esigenze specifiche di un dipartimento o gruppo di utenti.",
    108: "Topic Modeling (es. LDA) è l'approccio probabilistico che assegna distribuzioni di argomenti (topic) ai documenti e parole agli argomenti.",
    110: "Il Perceptron garantisce la convergenza solo se i dati di input sono linearmente separabili (teorema di convergenza del Perceptron).",
    112: "Il processo KDP (Knowledge Discovery Process) ha tipicamente 5-7 step, ma negli appunti ne vengono spesso elencati 7 principali (Cleaning...Presentation).",
    114: "HTML è un classico esempio di dato Semi-strutturato: ha tag che definiscono la struttura, ma il contenuto è spesso testo libero.",
    116: "Lemmatization riduce le parole al lemma: 'pescatore' resta 'pescatore' (nome), 'giocare' resta 'giocare' (verbo). 'Pesca' sarebbe errato (radice diversa).",
    118: "Nei sistemi di Partitional Clustering (es. K-Means), ogni punto appartiene a uno e un solo cluster (esclusività), a differenza del Fuzzy Clustering.",
    120: "I w(i) sono i 'weights' (pesi) sinaptici associati a ogni input, che determinano l'importanza del segnale nel calcolo dell'attivazione.",
    121: "Un Data Warehouse è un sistema che integra dati da diverse fonti eterogenee per supportare l'analisi decisionale.",
    122: "I primi step del KDP sono, in ordine: Data Cleaning, Integration, Selection, Transformation (prima del Data Mining vero e proprio).",
    124: "KDD sta per 'Knowledge Discovery from Data' (o talvolta in Databases), che è il nome formale del processo complessivo.",
    125: "Le proprietà chiave di un DB Relazionale sono: Tabelle (righe/colonne), Primary Key (identità) e Foreign Key (relazioni).",
    127: "Nella gerarchia del valore/analisi: Database (livello basso/operativo) -> Data Warehouse (integrazione/tattico) -> Data Mining (conoscenza/strategico).",
    128: "Il Drill-down è l'operazione OLAP che permette di scendere nel dettaglio (zoom-in), aumentando la granularità dell'analisi.",
    129: "I risultati sono statisticamente significativi se superano un test di ipotesi (p-value < soglia), indicando che non sono dovuti al caso.",
    130: "OLAP (On-line Analytical Processing) supporta analisi multidimensionali complesse e veloci su grandi moli di dati storici.",
    131: "Per generare etichette da dati non classificati ('uncategorised'), si usa il Clustering Analysis per trovare raggruppamenti naturali.",
    132: "Per analizzare trend continui nel tempo (es. interesse d'acquisto), la Regressione è la tecnica statistica più indicata.",
    133: "Se si dispone di un Training Set (dati etichettati), l'approccio corretto è la Classificazione (Supervised Learning).",
    134: "I dati Non Strutturati (testo, video, audio) costituiscono la stragrande maggioranza (spesso citato >80%) dei dati sul Web.",
    135: "KDD (Knowledge Discovery from Data) è l'acronimo/termine formale che racchiude il Data Mining come uno dei suoi step.",
    136: "Una confidenza del 45% significa che, dato l'acquisto di X (tastiera), c'è una probabilità condizionata del 45% di acquistare Y (laptop).",
    137: "Per estrarre dati specifici di transazioni singole, si lavora con un DBMS Transazionale (OLTP), non con un Data Warehouse (OLAP)."
}

def inject_missing(filepath, exp_dict):
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
        
        if current_q_id and current_q_id in exp_dict:
             # Look ahead check
             should_insert = False
             if i + 1 >= len(lines):
                 should_insert = True
             elif q_start_pattern.match(lines[i+1]) or lines[i+1].startswith("### "):
                 should_insert = True
                 
             if should_insert:
                 # Double check we don't duplicate
                 # Scan back current block
                 block_start = max(0, i-15) 
                 # simplistic
                 recent_text = "".join(lines[block_start:i+1])
                 if "**Spiegazione:**" not in recent_text:
                     new_lines.append(f"\n   **Spiegazione:** {exp_dict[current_q_id]}\n")
                     del exp_dict[current_q_id] # Done

    return "".join(new_lines)

final_text = inject_missing("simulazione_esame_completa.txt", missing_explanations)
with open("simulazione_esame_completa.txt", "w", encoding='utf-8') as f:
    f.write(final_text)

print("Injected remaining missing explanations.")
