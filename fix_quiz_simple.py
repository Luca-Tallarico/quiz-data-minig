
import re

def simple_tokenize(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return set(text.split())

def main():
    path = '/Users/lucatallarico/Desktop/quiz/simulazione_esame_completa.txt'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('---')
    questions_text = parts[0]
    
    lines = questions_text.split('\n')
    
    # 1. Parse File into Blocks
    # Blocks can be: SectionHeader, QuestionBlock (ID + Text + Options), ExplanationBlock
    
    blocks = []
    
    q_pattern = re.compile(r'^\s*(\d+)\.\s+(.*)')
    expl_pattern = re.compile(r'^\s*\*\*Spiegazione:\*\*\s*(.*)')
    section_pattern = re.compile(r'^###\s+(.*)')
    
    current_block = None
    
    for line in lines:
        stripped = line.strip()
        
        m_sec = section_pattern.match(line)
        m_q = q_pattern.match(line)
        m_exp = expl_pattern.match(line)
        
        if m_sec:
            if current_block: blocks.append(current_block)
            current_block = {'type': 'section', 'content': [line]}
            
        elif m_q:
            if current_block: blocks.append(current_block)
            q_id = int(m_q.group(1))
            current_block = {'type': 'question', 'id': q_id, 'content': [line], 'text_for_match': line}
            
        elif m_exp:
            if current_block: blocks.append(current_block)
            exp_text = m_exp.group(1)
            current_block = {'type': 'explanation', 'content': [line], 'text_for_match': exp_text}
            
        else:
            if current_block:
                current_block['content'].append(line)
                if stripped:
                    current_block['text_for_match'] = current_block.get('text_for_match', '') + " " + stripped
            else:
                # Header or initial noise
                pass
                
    if current_block: blocks.append(current_block)

    questions = [b for b in blocks if b['type'] == 'question']
    explanations = [b for b in blocks if b['type'] == 'explanation']
    
    print(f"Questions: {len(questions)}")
    print(f"Explanations: {len(explanations)}")
    
    # 2. Match
    stopwords = {'il', 'lo', 'la', 'i', 'gli', 'le', 'un', 'uno', 'una', 'di', 'a', 'da', 'in', 'con', 'su', 'per', 'tra', 'fra', 'è', 'ha', 'ho', 'sono', 'che', 'non', 'si', 'chi', 'che', 'cosa', 'quale', 'quali', 'dove', 'come', 'quando', 'perché', 'risposta', 'corretta', 'domanda', 'seguente', 'opzioni', 'del', 'della', 'dei', 'delle', 'al', 'allo', 'alla', 'agli', 'alle', 'nel', 'nello', 'nella', 'nei', 'negli', 'nelle', 'sul', 'sullo', 'sulla', 'sugli', 'sulle', 'l', 'all'}

    matches = {} # q_id -> explanation_block
    used_explanations = set()
    
    for q in questions:
        q_tokens = simple_tokenize(q['text_for_match']) - stopwords
        
        best_e = None
        best_score = 0
        best_e_idx = -1
        
        # Heuristic: Search in a window around the question index?
        # Assuming Q_index ~ E_index +/- offset.
        # But let's try global search first.
        
        for idx, e in enumerate(explanations):
            if idx in used_explanations: continue
            
            e_tokens = simple_tokenize(e['text_for_match']) - stopwords
            score = len(q_tokens.intersection(e_tokens))
            
            if score > best_score:
                best_score = score
                best_e = e
                best_e_idx = idx
                
        if best_e and best_score >= 1: # Threshold?
            matches[q['id']] = best_e
            used_explanations.add(best_e_idx)
            print(f"Q{q['id']} MATCH: {best_score} overlap. Q: {q['text_for_match'][:30]}... E: {best_e['text_for_match'][:30]}...")
        else:
            print(f"Q{q['id']} NO MATCH. Q: {q['text_for_match'][:30]}...")

if __name__ == "__main__":
    main()
