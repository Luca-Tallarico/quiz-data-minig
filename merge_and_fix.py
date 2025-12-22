import re
import random

# File paths
MAIN_FILE = '/Users/lucatallarico/Desktop/quiz/simulazione_esame_completa.txt'
EXTRA_FILE_1 = '/Users/lucatallarico/Desktop/quiz/risposte_quiz.txt'
EXTRA_FILE_2 = '/Users/lucatallarico/Desktop/quiz/risposte_quiz_2.txt'

# 1. READ MAIN FILE
with open(MAIN_FILE, 'r') as f:
    main_content = f.read()

# Separate content from answer key
parts = main_content.split('---')
main_questions_text = parts[0]
if len(parts) > 1:
    main_answer_key_text = parts[1]
else:
    main_answer_key_text = ""

# Parse main questions to get the last ID
last_id = 0
q_matches = re.findall(r'^(\d+)\.', main_questions_text, re.MULTILINE)
if q_matches:
    last_id = int(q_matches[-1])

# Parse answers map
answer_map = {}
matches = re.findall(r'(\d+):([A-D])', main_answer_key_text)
for q_id, char in matches:
    answer_map[int(q_id)] = char

# 2. DEFINITION OF EXTRA PARSER
def parse_extra_file(file_path, start_id):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Split by "## Domanda" or distinctive markers
    raw_blocks = re.split(r'## Domanda \d+', content)
    # First block is header
    raw_blocks = raw_blocks[1:] 
    
    questions = []
    
    current_id = start_id
    
    for block in raw_blocks:
        # Extract Question Text
        # Usually starts with **Text** or just Text
        # Then - Opzione A: ...
        
        lines = block.strip().split('\n')
        q_text = ""
        options = {}
        correct_char = None
        explanation = ""
        
        # Regex for options: "- Opzione A: ..." or "- **Opzioni:**" checks.
        
        # Simple parser for the specific format seen in view_file
        # File 1:
        # **Question Text?**
        # - Opzione A: Text
        # ...
        # **Risposta Corretta:** Opzione A
        
        # File 2:
        # **Question Text** followed by *(It text)* ? No, File 2 has "Complete the following..."
        # - **Opzioni:**
        #     - Text A
        #     - Text B
        # Let's try to be generic or write specific parsers.
        
        # Combined Text block finding
        # We can detect correct answer line: "**Risposta Corretta:** ..."
        
        correct_line_match = re.search(r'\*\*Risposta Corretta:\*\*\s*(.+)', block)
        correct_val_raw = ""
        if correct_line_match:
            correct_val_raw = correct_line_match.group(1).strip()
            
        # Parse options
        # Format 1: "- Opzione A: ..."
        opts_1 = re.findall(r'- Opzione ([A-D]):\s*(.*)', block)
        
        # Format 2 (Quiz 2): "- **Opzioni:**" then indented points.
        # This is harder because they don't have letters A,B,C,D in text.
        # We need to assign them A, B, C, D in order.
        
        new_q_options = {} # { 'A': text, 'B': text ... }
        
        if opts_1:
            for letter, text in opts_1:
                new_q_options[letter] = text
            
            # Extract Correct Char from "Opzione X"
            if "Opzione A" in correct_val_raw: correct_char = 'A'
            elif "Opzione B" in correct_val_raw: correct_char = 'B'
            elif "Opzione C" in correct_val_raw: correct_char = 'C'
            elif "Opzione D" in correct_val_raw: correct_char = 'D'
            
        else:
            # Format 2
            # Find the list items after "**Opzioni:**"
            # Look for lines starting with "    - " or similar
            opt_lines = re.findall(r'^\s*-\s+(.*)', block, re.MULTILINE)
            # Filter out the "Opzioni:" line itself if caught
            opt_lines = [l for l in opt_lines if "**Opzioni:**" not in l]
            
            # Usually 3 or 4 options
            keys = ['A', 'B', 'C', 'D']
            for i, txt in enumerate(opt_lines):
                if i < 4:
                    new_q_options[keys[i]] = txt
                    
            # Determine correct char by matching text
            # correct_val_raw contains the full text string of the answer
            # We need to find which option matches this string
            
            # Normalize for matching
            norm_target = correct_val_raw.replace('*', '').strip().lower()
            
            for k, v in new_q_options.items():
                # v might have *(Translation)*, remove closing parenthesis etc?
                # Let's try flexible matching
                norm_v = v.replace('*', '').strip().lower()
                if norm_target in norm_v or norm_v in norm_target:
                    correct_char = k
                    break
            
            # File 2 specific fix: Q4 "None of the above" matching might be ambiguous if multiple none. 
            # But usually exact match works.
            
        # Extract Question Text
        # It's usually the first non-empty lines before options.
        # Remove "**" formatting
        q_text_lines = []
        for line in lines:
            if line.strip().startswith("-"): break # Options start
            if "Risposta Corretta" in line: break
            if line.strip() == "": continue
            q_text_lines.append(line.replace("**", "").strip())
        
        q_text = " ".join(q_text_lines).strip()
        
        if q_text and new_q_options and correct_char:
            questions.append({
                "id": current_id,
                "text": q_text,
                "options": new_q_options,
                "correct": correct_char
            })
            current_id += 1
            
    return questions, current_id

# 3. MERGE
new_qs_1, last_id = parse_extra_file(EXTRA_FILE_1, last_id + 1)
new_qs_2, last_id = parse_extra_file(EXTRA_FILE_2, last_id + 1) # last_id invalid? No, parse_extra returns NEXT id.

all_new_qs = new_qs_1 + new_qs_2

# 4. APPEND TEXT
append_text = "\n\n### PARTE INTEGRATIVA: NUOVE DOMANDE\n\n"

for q in all_new_qs:
    # Shuffle options for balance? User asked specifically to balance them previously. 
    # Let's just shuffle the placement of correct answer to be safe, or keep as is?
    # Keeping as is is safer for text matching, but user complained about correct answer position previously.
    # Let's shuffle.
    
    opts = q['options']
    vals = list(opts.values())
    keys = ['A', 'B', 'C', 'D'][0:len(vals)]
    
    # Identify correct text
    correct_val = opts[q['correct']]
    
    # Shuffle values
    random.shuffle(vals)
    
    # Remap
    new_opts = {}
    new_correct_char = 'A'
    for i, k in enumerate(keys):
        new_opts[k] = vals[i]
        if vals[i] == correct_val:
            new_correct_char = k
            
    # Add to global map
    answer_map[q['id']] = new_correct_char
    
    append_text += f"{q['id']}. {q['text']}\n"
    for k in keys:
        append_text += f"   {k}. {new_opts[k]}\n"
    append_text += "\n"

new_main_content = main_questions_text + append_text

# 5. FIX TERMINOLOGY (KDD vs KDP)
# "correggi tutte le parti che hai confuso il KDP con il KDD"
# User Rule: KDP = Process (7 steps), KDD = Data Mining (Synonym).
# So if text says "The KDD process has 7 steps", replace with "The KDP has 7 steps".
# If text says "KDD is only step 4", replace with "Data Mining (or KDD) is only step 4".

# Replacements:
# "il processo KDD" -> "il processo KDP"
# "KDD process" -> "KDP"
# "fasi del KDD" -> "fasi del KDP"

new_main_content = re.sub(r'processo KDD', 'processo KDP', new_main_content, flags=re.IGNORECASE)
new_main_content = re.sub(r'fasi del KDD', 'fasi del KDP', new_main_content, flags=re.IGNORECASE)
new_main_content = re.sub(r'steps of KDD', 'steps of KDP', new_main_content, flags=re.IGNORECASE)
new_main_content = re.sub(r'KDD process', 'Knowledge Discovery Process (KDP)', new_main_content, flags=re.IGNORECASE)

# 6. REBUILD ANSWER KEY
# Ensure footer is clean
new_footer = "---"
new_footer += "\n### RISPOSTE CORRETTE\n\n"

sorted_ids = sorted(answer_map.keys())
chunk_size = 10
for i in range(0, len(sorted_ids), chunk_size):
    chunk = sorted_ids[i:i+chunk_size]
    parts_list = []
    for qid in chunk:
        parts_list.append(f"{qid}:{answer_map[qid]}")
    new_footer += ", ".join(parts_list)
    if i + chunk_size < len(sorted_ids):
        new_footer += ",\n"
    else:
        new_footer += "\n"

final_text = new_main_content.strip() + "\n\n" + new_footer

with open(MAIN_FILE, 'w') as f:
    f.write(final_text)

print(f"Integration Complete. Total questions: {len(sorted_ids)}")
