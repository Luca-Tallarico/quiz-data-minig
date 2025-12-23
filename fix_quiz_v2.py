
import re
import difflib

def better_tokenize(text):
    # Keep some punctuation relevant for math/code
    # Lowercase
    text = text.lower()
    # Remove only non-content punctuation. Keep numbers, chars, +, -, ^, etc.
    # Actually just split by whitespace and strip trim chars
    tokens = text.split()
    clean_tokens = set()
    for t in tokens:
        # Remove common punctuation from ends
        t = t.strip('.,;:"\'()[]{}')
        if len(t) > 1 or t in {'k', 'n', 'o'}: # Keep single variables often used
            clean_tokens.add(t)
    return clean_tokens

def main():
    path = '/Users/lucatallarico/Desktop/quiz/simulazione_esame_completa.txt'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('---')
    questions_part = parts[0]
    tail_part = '---' + parts[1] if len(parts) > 1 else ""

    lines = questions_part.split('\n')
    
    # 1. Parse content
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
            current_block = {'type': 'section', 'lines': [line]}
            
        elif m_q:
            if current_block: blocks.append(current_block)
            q_id = int(m_q.group(1))
            current_block = {'type': 'question', 'id': q_id, 'lines': [line], 'text_for_match': line}
            
        elif m_exp:
            # Separate explanation
            # If we are in a question block, we finish strictly the question part? 
            # No, we want to extract the explanation text.
            exp_text = m_exp.group(1)
            
            # If current block is Question, we just continue adding lines to it (so we don't break order)
            # BUT we extract the text to a pool.
            if current_block:
                current_block['lines'].append(line)
                # But mark this block as "containing an explanation" so we can strip it later?
                # Actually, filtering lines starting with **Spiegazione:** during reconstruction is safer.
            
            # Add to separate pool
            blocks.append({'type': 'explanation_source', 'text': exp_text})
            
        else:
            if current_block:
                current_block['lines'].append(line)
                if stripped and current_block['type'] == 'question' and not stripped.startswith('**Spiegazione'):
                    description_words = " ".join(stripped.split())
                    current_block['text_for_match'] += " " + description_words
                elif current_block['type'] == 'explanation_source':
                    current_block['text'] += " " + stripped
    
    if current_block: blocks.append(current_block)
    
    questions = [b for b in blocks if b['type'] == 'question']
    explanations_pool = [b for b in blocks if b['type'] == 'explanation_source']
    
    print(f"Questions: {len(questions)}")
    print(f"Explanations: {len(explanations_pool)}")
    
    # 2. Match
    stopwords = {'il', 'lo', 'la', 'i', 'gli', 'le', 'un', 'uno', 'una', 'di', 'a', 'da', 'in', 'con', 'su', 'per', 'tra', 'fra', 'è', 'ha', 'ho', 'sono', 'che', 'non', 'si', 'chi', 'che', 'cosa', 'quale', 'quali', 'dove', 'come', 'quando', 'perché', 'risposta', 'corretta', 'domanda', 'seguente', 'opzioni', 'del', 'della', 'dei', 'delle', 'al', 'allo', 'alla', 'agli', 'alle', 'nel', 'nello', 'nella', 'nei', 'negli', 'nelle', 'sul', 'sullo', 'sulla', 'sugli', 'sulle', 'l', 'all', "dell'", "l'", "un'", "c'è"}

    matched_map = {}
    used_explanations = set()
    
    for q in questions:
        q_text = q['text_for_match']
        q_tokens = better_tokenize(q_text) - stopwords
        
        best_e = None
        best_score = 0
        best_idx = -1
        
        # Candidate search
        for idx, e in enumerate(explanations_pool):
            if idx in used_explanations: continue
            
            e_text = e['text']
            e_tokens = better_tokenize(e_text) - stopwords
            
            # Intersection score
            score = len(q_tokens.intersection(e_tokens))
            
            # Boost score if specific rare words match?
            # Basic intersection + Jaccard?
            
            if score > best_score:
                best_score = score
                best_e = e_text
                best_idx = idx
        
        # Threshold
        if best_e and best_score >= 2: # At least 2 meaningful words
            matched_map[q['id']] = best_e
            used_explanations.add(best_idx)
            # print(f"Matched Q{q['id']} (Score {best_score})")
        else:
            matched_map[q['id']] = None
            
    # 3. Rewrite
    new_lines = []
    
    for b in blocks:
        if b['type'] == 'section':
            new_lines.extend(b['lines'])
            
        elif b['type'] == 'question':
            # Add Question lines, excluding any old explanations
            cleaned_lines = []
            skip = False
            for l in b['lines']:
                if "**Spiegazione:**" in l:
                    skip = True
                elif skip and l.strip() == "":
                    skip = False # End of explanation block usually followed by empty line
                    # But we want to keep the empty line if it separates Qs?
                    # The standard format: Q... Expl... \n\n Q...
                    pass
                elif skip and l.strip() != "":
                    pass # Skip explanation continuation
                else:
                    cleaned_lines.append(l)
            
            # Trim trailing empty lines
            while cleaned_lines and not cleaned_lines[-1].strip():
                cleaned_lines.pop()
                
            new_lines.extend(cleaned_lines)
            
            # Add New Explanation
            expl = matched_map.get(b['id'])
            if expl:
                new_lines.append("")
                new_lines.append(f"   **Spiegazione:** {expl}")
            
            new_lines.append("") # Spacer
            
        # Ignore raw explanation blocks (they are re-inserted)
    
    final_content = "\n".join(new_lines) + "\n" + tail_part
    final_content = re.sub(r'\n{3,}', '\n\n', final_content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    print("Rewritten.")

if __name__ == "__main__":
    main()
