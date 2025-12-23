
import re
from collections import Counter

def main():
    path = '/Users/lucatallarico/Desktop/quiz/simulazione_esame_completa.txt'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.split('\n')
    current_section = "Unknown"
    
    sections = Counter()
    total = 0
    
    section_pattern = re.compile(r'^###\s+(.*)')
    q_pattern = re.compile(r'^\s*\d+\.\s+')
    
    for line in lines:
        m_sec = section_pattern.match(line)
        if m_sec:
            current_section = m_sec.group(1).strip()
            
        if q_pattern.match(line):
            sections[current_section] += 1
            total += 1
            
    print(f"Total Questions: {total}")
    print("\nBreakdown by Section:")
    
    # Calculate Quotas for N=20
    print(f"{'Section Name':<50} | {'Count':<5} | {'Expected Quota (20)'}")
    print("-" * 80)
    
    for sec, count in sections.most_common():
        files_portion = count / total
        quota = files_portion * 20
        print(f"{sec:<50} | {count:<5} | {quota:.2f}")

if __name__ == "__main__":
    main()
