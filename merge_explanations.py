
import re

def parse_with_explanations(filepath):
    """Parses a quiz file and returns a map of {normalized_text: explanation}"""
    explanations = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by "## Domanda" or similar to isolate blocks
    # Logic in `risposte_quiz.txt` seems to be:
    # ## Domanda X
    # **Question Text**
    # - Options...
    # **Spiegazione:** ...
    
    blocks = re.split(r'## Domanda \d+', content)
    for block in blocks:
        if "**Spiegazione:**" in block or "Spiegazione:" in block:
            # Extract plain text question (approximate) to match
            # The question text is usually in **...** right at start
            q_match = re.search(r'\*\*(.*?)\*\*', block, re.DOTALL)
            if not q_match:
                 # Try finding just text before options
                 continue
            
            q_text = q_match.group(1).strip()
            # Normalize: remove newlines, extra spaces
            q_norm = " ".join(q_text.split())
            
            # Extract Explanation
            # Search for **Spiegazione:** ... up to **Riferimento** or End
            exp_match = re.split(r'\*\*Spiegazione:\*\*', block)
            if len(exp_match) < 2:
                continue
                
            explanation_part = exp_match[1]
            # Cut off at next section or "Riferimento"
            explanation_clean = explanation_part.split("**Riferimento")[0].strip()
            
            explanations[q_norm] = explanation_clean
            
    return explanations

def apply_explanations(target_file, explanations_map):
    with open(target_file, 'r', encoding='utf-8') as f:
        target_content = f.read()
        
    lines = target_content.split('\n')
    new_lines = []
    
    current_q_text_norm = None
    parsing_q = False
    
    # We need to detect when a question ends (usually blank line before next number)
    # and insert explanation if we have one for the current question.
    
    # Actually, simpler: Read line by line. 
    # If line starts with "N. Question Text", parse text.
    # When we hit blank line or next question, insert explanation if pending.
    
    pending_explanation = None
    
    q_start_pattern = re.compile(r'^\s*(\d+)\.\s+(.*)')
    
    for i, line in enumerate(lines):
        # Check if new question starts
        m = q_start_pattern.match(line)
        if m:
            # If we had a pending explanation for previous question that wasn't inserted, insert it?
            # No, we insert immediately after options usually.
            # But options are multiple lines.
            
            # Reset
            pending_explanation = None
            
            # Try to match this question text
            q_text = m.group(2).strip()
            # Need to handle multi-line question text? 
            # Simplified matching.
            
            # Attempt fuzzy match
            best_match = None
            q_text_norm = " ".join(q_text.split())[:50] # Check first 50 chars
            
            for k, v in explanations_map.items():
                if q_text_norm in k or k in q_text_norm:
                    best_match = v
                    break
            
            if best_match:
                pending_explanation = best_match
        
        new_lines.append(line)
        
        # When to insert explanation?
        # Insert before the next question starts OR at the end of the block (blank line)
        # Check if next line is blank or next question
        if pending_explanation:
            is_end_of_block = False
            if i + 1 >= len(lines):
                is_end_of_block = True
            elif lines[i+1].strip() == "":
                is_end_of_block = True
            elif q_start_pattern.match(lines[i+1]):
                 is_end_of_block = True
            
            if is_end_of_block:
                # Insert Explanation here
                # Check if already has one
                already_has = False
                # Look back in new_lines for "Spiegazione:"
                # (Simple check only last few lines)
                for lookback in new_lines[-10:]:
                    if "**Spiegazione:**" in lookback:
                        already_has = True
                        break
                
                if not already_has:
                    new_lines.append(f"\n   **Spiegazione:** {pending_explanation}")
                
                pending_explanation = None # Consumed

    return "\n".join(new_lines)


# Load explanations
exps1 = parse_with_explanations('risposte_quiz.txt')
exps2 = parse_with_explanations('risposte_quiz_2.txt')
all_exps = {**exps1, **exps2}

# Apply
final_content = apply_explanations('simulazione_esame_completa.txt', all_exps)

with open('simulazione_esame_completa.txt', 'w', encoding='utf-8') as f:
    f.write(final_content)

print(f"Merged {len(all_exps)} explanations.")
