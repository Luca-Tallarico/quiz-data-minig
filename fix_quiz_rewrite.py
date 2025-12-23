
import re
import os

def simple_tokenize(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return set(text.split())

def main():
    path = '/Users/lucatallarico/Desktop/quiz/simulazione_esame_completa.txt'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('---')
    questions_part = parts[0]
    tail_part = '---' + parts[1] if len(parts) > 1 else ""

    lines = questions_part.split('\n')
    
    # 1. Parse File into Blocks to preserve structure
    blocks = []
    
    # Regex
    q_pattern = re.compile(r'^\s*(\d+)\.\s+(.*)')
    expl_pattern = re.compile(r'^\s*\*\*Spiegazione:\*\*\s*(.*)')
    section_pattern = re.compile(r'^###\s+(.*)')
    
    current_block = None
    
    # We will treat text lines as belonging to the current block
    
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
            # Text for matching should include the question text
            # We will append subsequent lines (options) to text_for_match later
            current_block = {'type': 'question', 'id': q_id, 'lines': [line], 'text_for_match': line, 'expl_placeholder_index': -1}
            
        elif m_exp:
            if current_block and current_block['type'] == 'question':
                # This is an explanation currently attached to a question
                # We want to separate it out to the pool, AND mark where it was (or where it should be)
                # But actually we will just strip all explanations from the blocks and re-insert them.
                # So we just collect it for the pool.
                pass
            
            # We create an explicit explanation block to catch it? 
            # No, if it was inside a question block in the original file, we just ignore it for the structure 
            # (since we will regenerate it), but TAKE its content for the pool.
            
            exp_text = m_exp.group(1)
            # If we had a current block, finish it? 
            # Actually, the file structure usually has explanation AFTER options.
            # So it's part of the question block logic for now?
            # Let's separate "Explanation content" from "File Structure".
            
            # We'll treat Explanations as freestanding entities for the POOL.
            if current_block: blocks.append(current_block)
            current_block = {'type': 'explanation_source', 'text': exp_text}
            
        else:
            if current_block:
                if current_block['type'] == 'explanation_source':
                     current_block['text'] += " " + stripped
                elif current_block['type'] == 'question':
                    current_block['lines'].append(line)
                    # Add to match text if it's not empty (likely options)
                    if stripped:
                        current_block['text_for_match'] += " " + stripped
                elif current_block['type'] == 'section':
                    current_block['lines'].append(line)
            else:
                # Header or empty lines at start
                pass

    if current_block: blocks.append(current_block)

    # 2. Extract Pools
    questions = [b for b in blocks if b['type'] == 'question']
    
    # Explanation Pool: explicitly recognized explanation blocks
    explanations_pool = [b for b in blocks if b['type'] == 'explanation_source']
    
    print(f"Parsed: {len(questions)} Questions, {len(explanations_pool)} Explanations")
    
    # 3. Match Logic
    stopwords = {'il', 'lo', 'la', 'i', 'gli', 'le', 'un', 'uno', 'una', 'di', 'a', 'da', 'in', 'con', 'su', 'per', 'tra', 'fra', 'è', 'ha', 'ho', 'sono', 'che', 'non', 'si', 'chi', 'che', 'cosa', 'quale', 'quali', 'dove', 'come', 'quando', 'perché', 'risposta', 'corretta', 'domanda', 'seguente', 'opzioni', 'del', 'della', 'dei', 'delle', 'al', 'allo', 'alla', 'agli', 'alle', 'nel', 'nello', 'nella', 'nei', 'negli', 'nelle', 'sul', 'sullo', 'sulla', 'sugli', 'sulle', 'l', 'all'}

    used_explanations = set()
    matched_map = {} # q_id -> explanation text
    
    for q in questions:
        q_tokens = simple_tokenize(q['text_for_match']) - stopwords
        
        best_e = None
        best_e_idx = -1
        best_score = 0
        
        for idx, e in enumerate(explanations_pool):
            if idx in used_explanations: continue
            
            e_text = e['text']
            e_tokens = simple_tokenize(e_text) - stopwords
            
            score = len(q_tokens.intersection(e_tokens))
            
            if score > best_score:
                best_score = score
                best_e = e_text
                best_e_idx = idx
        
        if best_e and best_score >= 1:
            matched_map[q['id']] = best_e
            used_explanations.add(best_e_idx)
        else:
            # Fallback? Maybe assign the one at the same index if available and unused?
            # Or just leave empty to be safe rather than wrong.
            matched_map[q['id']] = None

    # 4. Reconstruction
    new_lines = []
    
    # We iterate over the ORIGINAL blocks sequence (excluding explanations since they are re-inserted)
    
    for b in blocks:
        if b['type'] == 'section':
            new_lines.extend(b['lines'])
        elif b['type'] == 'question':
            # Print Question Lines (Text + Options)
            # Remove any trailing empty lines from the question block to make it tight?
            # The 'lines' include the original text lines.
            
            # We need to print the lines, then append the explanation.
            for l in b['lines']:
                new_lines.append(l)
            
            # Insert Explanation
            expl_text = matched_map.get(b['id'])
            if expl_text:
                new_lines.append("") # Empty line before explanation
                new_lines.append(f"   **Spiegazione:** {expl_text}")
            
            new_lines.append("") # Empty line after block
            
        elif b['type'] == 'explanation_source':
            # Skip original explanation blocks
            continue
    
    # 5. Write File
    final_content = "\n".join(new_lines) + "\n" + tail_part
    
    # Remove excessive newlines?
    final_content = re.sub(r'\n{3,}', '\n\n', final_content)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print("File rewritten successfully.")

if __name__ == "__main__":
    main()
