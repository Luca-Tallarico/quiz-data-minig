
import re
import numpy as np

def simple_tokenize(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return set(text.split())

def main():
    path = '/Users/lucatallarico/Desktop/quiz/simulazione_esame_completa.txt'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex
    q_pattern = re.compile(r'^\s*(\d+)\.\s+(.*)')
    expl_pattern = re.compile(r'^\s*\*\*Spiegazione:\*\*\s*(.*)')
    
    questions = []
    explanations = []
    
    lines = content.split('\n')
    for line in lines:
        m_q = q_pattern.match(line)
        m_exp = expl_pattern.match(line)
        if m_q:
            questions.append({'id': int(m_q.group(1)), 'text': m_q.group(2)})
        elif m_exp:
            explanations.append({'text': m_exp.group(1)})
            
    print(f"Questions: {len(questions)}")
    print(f"Explanations: {len(explanations)}")
    
    stopwords = {'il', 'lo', 'la', 'i', 'gli', 'le', 'un', 'uno', 'una', 'di', 'a', 'da', 'in', 'con', 'su', 'per', 'tra', 'fra', 'è', 'ha', 'ho', 'sono', 'che', 'non', 'si', 'chi', 'che', 'cosa', 'quale', 'quali', 'dove', 'come', 'quando', 'perché', 'risposta', 'corretta', 'domanda', 'seguente', 'opzioni', 'del', 'della', 'dei', 'delle', 'al', 'allo', 'alla', 'agli', 'alle', 'nel', 'nello', 'nella', 'nei', 'negli', 'nelle', 'sul', 'sullo', 'sulla', 'sugli', 'sulle', 'l', 'all'}

    # For each explanation, find the Question with best overlap
    matches = []
    
    for e_idx, e in enumerate(explanations):
        e_tokens = simple_tokenize(e['text']) - stopwords
        if not e_tokens: continue
        
        best_q_idx = -1
        best_score = 0
        
        for q_idx, q in enumerate(questions):
            q_tokens = simple_tokenize(q['text']) - stopwords
            score = len(e_tokens.intersection(q_tokens))
            if score > best_score:
                best_score = score
                best_q_idx = q_idx
        
        if best_score > 1: # Threshold of at least 2 common words
            matches.append((e_idx, best_q_idx, best_score, e['text'][:20], questions[best_q_idx]['text'][:20]))
            
    # Visualize offsets
    offsets = [m[1] - m[0] for m in matches]
    
    from collections import Counter
    print("Offset Distribution (Q_index - E_index):")
    print(Counter(offsets).most_common(10))
    
    print("\nSample Matches:")
    for m in matches[:20]:
        print(f"E{m[0]} -> Q{m[1]} (Offset {m[1]-m[0]}) Score {m[2]}: {m[3]}... -> {m[4]}...")

if __name__ == "__main__":
    main()
