
import re

def main():
    # 1. Read Validated Data
    with open('/Users/lucatallarico/Desktop/quiz/risposte_quiz.txt', 'r', encoding='utf-8') as f:
        risposte_content = f.read()
        
    # Parse risposte_quiz.txt
    # Format: **Question Text?** ... **Spiegazione:** ...
    
    validated_map = {} # Question Text -> Explanation Text
    
    # Split by "## Domanda"
    blocks = risposte_content.split('## Domanda')
    for b in blocks:
        if not b.strip(): continue
        
        # Extract Question Text
        # Matches **Text**
        m_q = re.search(r'\*\*(.*?)\*\*', b, re.DOTALL)
        m_exp = re.search(r'\*\*Spiegazione:\*\*\s*(.*?)\*\*Riferimento', b, re.DOTALL) 
        # Note: Spiegazione goes until "Riferimento" or End?
        # In the file viewed: **Spiegazione:** \n Text \n\n **Riferimento...**
        
        if not m_exp:
             m_exp = re.search(r'\*\*Spiegazione:\*\*\s*(.*)', b, re.DOTALL)
        
        if m_q and m_exp:
            q_text = m_q.group(1).strip().replace('\n', ' ')
            exp_text = m_exp.group(1).strip()
            validated_map[q_text] = exp_text
            
    print(f"Loaded {len(validated_map)} validated explanations.")
    
    # 2. Read Target File
    target_path = '/Users/lucatallarico/Desktop/quiz/simulazione_esame_completa.txt'
    with open(target_path, 'r', encoding='utf-8') as f:
        target_content = f.read()
        
    lines = target_content.split('\n')
    new_lines = []
    
    q_pattern = re.compile(r'^\s*(\d+)\.\s+(.*)')
    
    current_q_text = None
    skip_expl = False
    
    for line in lines:
        stripped = line.strip()
        m_q = q_pattern.match(line)
        
        if m_q:
            current_q_text = m_q.group(2).strip()
            new_lines.append(line)
            skip_expl = False
        elif "**Spiegazione:**" in line:
            # Check if we have a better explanation
            best_match_key = None
            if current_q_text:
                # Fuzzy match current_q_text with keys in validated_map
                # Validated keys are like "Cos'è CBOW?"
                # Current text is "Cos'è CBOW?" (matches!)
                
                # Check exact substring
                for k in validated_map:
                    if k in current_q_text or current_q_text in k:
                        best_match_key = k
                        break
            
            if best_match_key:
                # Use the validated explanation INSTEAD of the current line
                new_msg = f"   **Spiegazione:** {validated_map[best_match_key]}"
                new_lines.append(new_msg)
                skip_expl = True # Skip the text of the old explanation until empty line
            else:
                # Keep existing
                new_lines.append(line)
                skip_expl = False
        else:
            if skip_expl:
                if stripped == "":
                    skip_expl = False
                    new_lines.append(line)
                else:
                    pass # Skip old explanation lines
            else:
                # Accumulate multi-line question text to 'current_q_text' if needed?
                # No, simplistic is fine for now.
                new_lines.append(line)
                
    # Write back
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(new_lines))
        
    print("Merged validated explanations.")

if __name__ == "__main__":
    main()
