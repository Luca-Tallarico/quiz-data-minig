
import re

def check_missing_explanations(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    missing_ids = []
    
    # We expect questions 1 to 137
    for i in range(1, 138):
        # Locate question start
        q_start = re.search(f"^{i}\\. ", content, re.MULTILINE)
        if not q_start:
            # Maybe spacing differences?
            q_start = re.search(f"^\\s*{i}\\. ", content, re.MULTILINE)
            
        if not q_start:
            print(f"Could not find Question {i}")
            continue
            
        # Locate next question start or EOF
        if i < 137:
            next_q_start = re.search(f"^{i+1}\\. ", content, re.MULTILINE)
            if not next_q_start:
                 next_q_start = re.search(f"^\\s*{i+1}\\. ", content, re.MULTILINE)
        else:
            next_q_start = None
            
        # Extract block
        start_idx = q_start.start()
        end_idx = next_q_start.start() if next_q_start else len(content)
        
        block = content[start_idx:end_idx]
        
        if "**Spiegazione:**" not in block and "Spiegazione:" not in block:
            missing_ids.append(i)

    return missing_ids

missing = check_missing_explanations("simulazione_esame_completa.txt")
print(f"Missing Explanations for: {missing}")
