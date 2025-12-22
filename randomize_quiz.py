
import re
import random

file_path = '/Users/lucatallarico/Desktop/quiz/simulazione_esame_completa.txt'

with open(file_path, 'r') as f:
    content = f.read()

# Separate content from answers
if '---' in content:
    parts = content.split('---')
    main_content = parts[0]
    answer_section = parts[1]
else:
    # Fallback if delimiter missing, though file view shows it
    print("Error: Delimiter '---' not found")
    exit(1)

# Parse existing answers to know which text is correct
answer_map = {}
matches = re.findall(r'(\d+):([A-D])', answer_section)
for q_id, char in matches:
    answer_map[int(q_id)] = char

new_answer_map = {}
final_output_lines = []

current_q_id = None
buffer_q_lines = []
buffer_options = {}

q_start_pattern = re.compile(r'^\s*(\d+)\.\s+(.*)')
opt_pattern = re.compile(r'^\s+([A-D])\.\s+(.*)')

def process_question(q_id, q_lines, options):
    global final_output_lines, new_answer_map
    
    correct_char = answer_map.get(q_id)
    if not correct_char or correct_char not in options:
        # Fallback if something is wrong: just print as is
        for l in q_lines: final_output_lines.append(l)
        keys = sorted(options.keys())
        for k in keys: final_output_lines.append(f"   {k}. {options[k]}")
        final_output_lines.append("")
        if correct_char: new_answer_map[q_id] = correct_char
        return

    correct_text = options[correct_char]
    
    # Randomize
    opt_keys = ['A', 'B', 'C', 'D']
    # If question has fewer options ?? Usually 4.
    # Get values
    texts = list(options.values())
    if len(texts) != 4:
        # Verify valid structure, otherwise just keep as is to be safe
        opt_keys = sorted(options.keys())
        
    random.shuffle(texts)
    
    # Map new keys to randomized texts
    new_options = {}
    for i, k in enumerate(opt_keys):
        if i < len(texts):
            new_options[k] = texts[i]
            
    # Find new correct char
    new_correct_char = None
    for k, text in new_options.items():
        if text == correct_text:
            new_correct_char = k
            break
    
    new_answer_map[q_id] = new_correct_char
    
    # Output
    for l in q_lines:
        final_output_lines.append(l)
    
    for k in opt_keys:
        if k in new_options:
            final_output_lines.append(f"   {k}. {new_options[k]}")
            
    final_output_lines.append("") # Spacer

lines = main_content.split('\n')

for line in lines:
    stripped = line.strip()
    m_q = q_start_pattern.match(line)
    m_opt = opt_pattern.match(line)
    is_header = stripped.startswith("###")
    
    if m_q:
        # New question starts
        if current_q_id is not None:
            process_question(current_q_id, buffer_q_lines, buffer_options)
        
        current_q_id = int(m_q.group(1))
        buffer_q_lines = [line]
        buffer_options = {}
        
    elif is_header:
        # Header starts
        if current_q_id is not None:
             process_question(current_q_id, buffer_q_lines, buffer_options)
             current_q_id = None
        final_output_lines.append(line)
        final_output_lines.append("") # Add spacing after header
        
    elif m_opt:
        # Option line
        if current_q_id is not None:
            buffer_options[m_opt.group(1)] = m_opt.group(2)
        else:
            final_output_lines.append(line)
            
    else:
        # Other content
        if current_q_id is not None:
            if buffer_options:
                # We are in a question, have options, and see text.
                # Assuming empty lines between questions
                pass
            else:
                # Question text continuation
                if stripped != "":
                    buffer_q_lines.append(line)
        else:
            # Outside question
            if stripped != "": 
                final_output_lines.append(line)

# Flush match
if current_q_id is not None:
    process_question(current_q_id, buffer_q_lines, buffer_options)

# Rebuild answer block
new_footer = "---"
new_footer += "\n### RISPOSTE CORRETTE\n\n"

sorted_ids = sorted(new_answer_map.keys())
chunk_size = 10
for i in range(0, len(sorted_ids), chunk_size):
    chunk = sorted_ids[i:i+chunk_size]
    # Format "1:A"
    parts_list = []
    for qid in chunk:
        parts_list.append(f"{qid}:{new_answer_map[qid]}")
    new_footer += ", ".join(parts_list)
    if i + chunk_size < len(sorted_ids):
        new_footer += ",\n"
    else:
        new_footer += "\n"

final_text = "\n".join(final_output_lines).strip() + "\n\n" + new_footer

with open(file_path, 'w') as f:
    f.write(final_text)

print("Randomization complete.")
