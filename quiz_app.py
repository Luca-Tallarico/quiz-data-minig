import streamlit as st
import re
import os
import random
import base64
import urllib.parse
from datetime import datetime, timedelta

# Set page config
st.set_page_config(
    page_title="Simulazione Esame - Data Mining",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
    <style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }
    
    /* Radio Button Styling - FIXED HOVER */
    .stRadio > div {
        background-color: #f8fafc;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        margin-bottom: 12px;
        transition: all 0.2s ease;
    }
    .stRadio > div:hover {
        border-color: #cbd5e1;
        background-color: #f1f5f9;
    }
    .stRadio label {
        color: #334155 !important; /* Force text color strictly */
    }
    /* Force inner p tag to respect color too */
    .stRadio p {
         color: #334155 !important;
    }
    
    /* Dark Mode Overrides */
    @media (prefers-color-scheme: dark) {
        .card-container {
            background: #1e293b;
            border-color: #334155;
        }
        .stRadio > div { 
            background-color: #1e293b; 
            border-color: #334155; 
            color: #e2e8f0 !important;
        }
        /* User requested: On hover, box becomes white, text becomes black */
        .stRadio > div:hover {
            background-color: #ffffff !important;
            border-color: #cbd5e1 !important;
        }
        .stRadio > div:hover * {
            color: #0f172a !important; /* Forces black text on hover */
        }
        .stRadio > div:hover label {
            color: #0f172a !important;
        }
        .stRadio > div:hover p {
            color: #0f172a !important;
        }
        
        /* Default state (no hover) */
        .stRadio * { color: #e2e8f0 !important; }
        .stRadio label, .stRadio p { color: #e2e8f0 !important; }
    }
    
    /* Feedback Colors */
    .correct-answer {
        background-color: #dcfce7;
        padding: 10px;
        border-radius: 8px;
        border-left: 5px solid #22c55e;
        color: #14532d;
    }
    .wrong-answer {
        background-color: #fee2e2;
        padding: 10px;
        border-radius: 8px;
        border-left: 5px solid #ef4444;
        color: #7f1d1d;
    }

    /* CARD SYSTEM (Antigravity Grid) */
    .card-container {
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        background: rgba(255, 255, 255, 0.95);
        border-radius: 24px; /* Rounded-XL equivalent */
        padding: 24px;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); /* Elegant Shadow */
        border: 1px solid rgba(255, 255, 255, 0.5);
        backdrop-filter: blur(10px); /* Glassmorphism */
        height: 100%;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .card-container:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    }

    /* Card Accents */
    .card-blue {
        border-top: 6px solid #3b82f6; /* Blue-500 */
        background: linear-gradient(to bottom right, #eff6ff, #ffffff);
    }
    .card-green {
        border-top: 6px solid #10b981; /* Emerald-500 */
        background: linear-gradient(to bottom right, #ecfdf5, #ffffff);
    }

    .card-purple {
        border-top: 6px solid #8b5cf6; /* Violet-500 */
        background: linear-gradient(to bottom right, #f5f3ff, #ffffff);
    }

    /* Typography */
    .card-title {
        font-size: 1.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        letter-spacing: -0.025em;
    }
    .text-blue { color: #1e40af; }
    .text-green { color: #065f46; }
    .text-purple { color: #5b21b6; }
    
    .card-desc {
        font-size: 0.95rem;
        color: #64748b;
        margin-bottom: 1.5rem;
        line-height: 1.5;
    }

    /* Feature List */
    .feature-list {
        list-style: none;
        padding: 0;
        margin: 0;
        flex-grow: 1; /* Pushes button down if flex container */
    }
    .feature-item {
        display: flex;
        align-items: center;
        margin-bottom: 0.75rem;
        font-size: 0.95rem;
        color: #334155;
        font-weight: 500;
    }
    .icon-box {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 32px;
        height: 32px;
        border-radius: 8px;
        margin-right: 12px;
        font-size: 1.1rem;
    }
    .bg-blue-light { background-color: #dbeafe; color: #2563eb; }
    .bg-green-light { background-color: #d1fae5; color: #059669; }
    .bg-purple-light { background-color: #ede9fe; color: #7c3aed; }
    
    /* Button Styling Override */
    div[data-testid="column"]:nth-of-type(1) button {
         border-radius: 12px;
         font-weight: 600;
         border: 2px solid #bfdbfe;
         transition: all 0.2s;
    }
    div[data-testid="column"]:nth-of-type(1) button:hover {
         border-color: #3b82f6;
         background-color: #eff6ff;
         color: #1d4ed8;
    }

    div[data-testid="column"]:nth-of-type(2) button {
         border-radius: 12px;
         font-weight: 600;
         border: 2px solid #a7f3d0;
    }
     div[data-testid="column"]:nth-of-type(2) button:hover {
         border-color: #10b981;
         background-color: #ecfdf5;
         color: #047857;
    }
    
    div[data-testid="column"]:nth-of-type(3) button {
         border-radius: 12px;
         font-weight: 600;
         border: 2px solid #ddd6fe;
    }
     div[data-testid="column"]:nth-of-type(3) button:hover {
         border-color: #8b5cf6;
         background-color: #f5f3ff;
         color: #5b21b6;
    }
    
    /* Dark Mode Overrides */
    @media (prefers-color-scheme: dark) {
        .card-container {
            background: #1e293b;
            border-color: #334155;
        }
        .card-blue { background: linear-gradient(to bottom right, #1e293b, #0f172a); border-top-color: #3b82f6; }
        .card-green { background: linear-gradient(to bottom right, #1e293b, #0f172a); border-top-color: #10b981; }
        .card-purple { background: linear-gradient(to bottom right, #1e293b, #0f172a); border-top-color: #8b5cf6; }
        
        .card-title { color: #f1f5f9; }
        .feature-item { color: #cbd5e1; }
        .bg-blue-light { background-color: #1e3a8a; color: #93c5fd; }
        .bg-green-light { background-color: #064e3b; color: #6ee7b7; }
        .bg-purple-light { background-color: #4c1d95; color: #a78bfa; }
        
        .text-blue { color: #60a5fa; }
        .text-green { color: #34d399; }
        .text-purple { color: #a78bfa; }
        
        .stRadio > div { background-color: #1e293b; border-color: #334155; }
        .stRadio * { color: #e2e8f0 !important; }
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# PARSING LOGIC
# -----------------------------------------------------------------------------
def load_quiz_data(file_path):
    if not os.path.exists(file_path):
        return None, None
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('---')
    if len(parts) < 2:
        return None, None
    
    questions_text = parts[0]
    answers_text = parts[1]

    # Parse Questions
    questions = {}
    q_blocks = re.split(r'\n(\d+)\.\s+', questions_text)
    
    lines = questions_text.split('\n')
    parsed_questions = []
    current_q = None
    
    q_start_pattern = re.compile(r'^\s*(\d+)\.\s+(.*)')
    opt_pattern = re.compile(r'^\s+([A-D])\.\s+(.*)')
    section_pattern = re.compile(r'^###\s+(.*)')
    
    current_section_title = ""
    
    for line in lines:
        stripped = line.strip()
        m_sec = section_pattern.match(line)
        if m_sec:
            current_section_title = m_sec.group(1)
            continue
            
        m_q = q_start_pattern.match(line)
        if m_q:
            if current_q:
                parsed_questions.append(current_q)
            q_id = int(m_q.group(1))
            q_text = m_q.group(2)
            current_q = {
                "id": q_id,
                "text": q_text,
                "options": {},
                "section": current_section_title,
                "lines": [q_text]
            }
            continue
            
        m_opt = opt_pattern.match(line)
        if m_opt:
            if current_q:
                opt_key = m_opt.group(1)
                opt_val = m_opt.group(2)
                current_q["options"][opt_key] = opt_val
            continue
            
        if current_q and not current_q['options'] and stripped:
             current_q['lines'].append(stripped)
             current_q['text'] = " ".join(current_q['lines'])

        # Capture Explanation (after options)
        if current_q and current_q['options'] and "Spiegazione:" in line:
             current_q['explanation'] = line.split("Spiegazione:", 1)[1].strip()
        elif current_q and current_q['options'] and stripped and 'explanation' in current_q:
             # Append multi-line explanation
             current_q['explanation'] += " " + stripped

    if current_q:
        parsed_questions.append(current_q)

    answer_map = {}
    matches = re.findall(r'(\d+):([A-D])', answers_text)
    for q_id, char in matches:
        answer_map[int(q_id)] = char
        
    return parsed_questions, answer_map

# -----------------------------------------------------------------------------
# STATE MANAGEMENT
# -----------------------------------------------------------------------------
def init_session_state():
    if 'mode' not in st.session_state:
        st.session_state.mode = None # 'practice', 'exam', None
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False
    if 'verified_ids' not in st.session_state:
        st.session_state.verified_ids = set()
    
    # Exam specific
    if 'exam_questions' not in st.session_state:
        st.session_state.exam_questions = []
    if 'exam_start_time' not in st.session_state:
        st.session_state.exam_start_time = None

def reset_state():
    st.session_state.answers = {}
    st.session_state.submitted = False
    st.session_state.verified_ids = set()
    st.session_state.exam_start_time = None
    st.session_state.exam_questions = []

# -----------------------------------------------------------------------------
# LOGIC: STRATIFIED SAMPLING
# -----------------------------------------------------------------------------
def generate_exam_questions(all_questions, total_needed=20):
    """
    Selects 20 questions ensuring they are distributed across sections 
    proportionally to the section size.
    """
    if not all_questions:
        return []
    
    # 1. Group by section
    sections = {}
    for q in all_questions:
        sec = q.get('section', 'Unknown')
        if sec not in sections:
            sections[sec] = []
        sections[sec].append(q)
    
    # 2. Calculate quotas
    total_q = len(all_questions)
    selected_questions = []
    
    # Prepare to track remainder
    quotas = {}
    for sec, q_list in sections.items():
        # Raw proportion
        proportion = len(q_list) / total_q
        count = proportion * total_needed
        quotas[sec] = {
            'list': q_list,
            'target': int(count),
            'remainder': count - int(count)
        }
    
    # 3. Initial Fill
    current_count = 0
    for sec, data in quotas.items():
        # Sample the integer part
        k = min(data['target'], len(data['list']))
        if k > 0:
            picked = random.sample(data['list'], k)
            selected_questions.extend(picked)
            current_count += len(picked)
            # Remove picked from list to avoid dups if we needed to pull more? 
            # (Not needed as random.sample is unique, but we won't sample again from same pool unless logic specifically asks)
    
    # 4. Fill Gap (Round-robin based on largest remainder)
    needed = total_needed - current_count
    if needed > 0:
        # Sort sections by remainder descending
        sorted_secs = sorted(quotas.keys(), key=lambda s: quotas[s]['remainder'], reverse=True)
        
        for sec in sorted_secs:
            if needed == 0:
                break
            
            # Check if we have questions left to pick in this section?
            # We already picked 'target'. Let's pick one more if possible.
            # But wait, random.sample returned a new list. We need to respect unique IDs.
            # Simplified approach:
            # Re-sample from the full list excluding already selected IDs is safer.
            
            # Let's verify:
            # quotas[sec]['list'] is the full list of that section.
            # We picked `quotas[sec]['target']` amount.
            # If len > target, we can pick 1 more.
             
            already_picked_count = quotas[sec]['target']
            total_available = len(quotas[sec]['list'])
            
            if total_available > already_picked_count:
                # We need to pick one that wasn't already picked.
                # Since we didn't store exactly WHICH were picked in step 3 (we just extended selected_questions),
                # we need effectively "sample k+1" instead of "sample k".
                
                # To make this clean, let's just update the target in quotas and re-run sampling at the end? 
                # No, simpler: just increment target for these top remainder sections.
                quotas[sec]['target'] += 1
                needed -= 1

    # 5. Final Execution
    # Now valid targets are set. Let's do the actual sampling here.
    final_selection = []
    for sec, data in quotas.items():
        k = data['target']
        # Safety clamp
        k = min(k, len(data['list']))
        if k > 0:
            final_selection.extend(random.sample(data['list'], k))
            
    # If still short (e.g. small sections), fill with random remaining
    if len(final_selection) < total_needed:
        selected_ids = {q['id'] for q in final_selection}
        pool = [q for q in all_questions if q['id'] not in selected_ids]
        needed = total_needed - len(final_selection)
        final_selection.extend(random.sample(pool, min(needed, len(pool))))
        
    # Shuffle final list so topics are mixed (simulating real exam)
    random.shuffle(final_selection)
    
    return final_selection

# -----------------------------------------------------------------------------
# MODES
# -----------------------------------------------------------------------------

def show_home_page(all_questions):
    st.markdown("<h1 style='text-align: center; margin-bottom: 50px; font-weight: 800; font-size: 3rem; background: -webkit-linear-gradient(45deg, #3b82f6, #10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>🎓 Data Mining & Text Analytics</h1>", unsafe_allow_html=True)
    
    # Grid System with Gap (3 items now) and adjusted logic
    col1, col2, col3 = st.columns(3, gap="medium")
    
    with col1:
        # Card HTML Content
        st.markdown("""
        <div class="card-container card-blue">
            <div>
                <div class="card-title text-blue">🏋️ Quizzone</div>
                <div class="card-desc">La modalità classica per esercitarsi senza pressione.</div>
                <ul class="feature-list">
                    <li class="feature-item"><span class="icon-box bg-blue-light">📚</span> Accesso a&nbsp;<b>142&nbsp;domande</b></li>
                    <li class="feature-item"><span class="icon-box bg-blue-light">♾️</span> Senza limiti di tempo</li>
                    <li class="feature-item"><span class="icon-box bg-blue-light">💡</span> Feedback immediato</li>
                    <li class="feature-item"><span class="icon-box bg-blue-light">🔍</span> Verifica passo-passo</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div style="margin-top: -15px;"></div>', unsafe_allow_html=True)
        if st.button("🚀 Avvia Quizzone", key="btn_practice", use_container_width=True):
            reset_state()
            st.session_state.mode = 'practice'
            st.rerun()

    with col2:
        # Card HTML Content
        st.markdown("""
        <div class="card-container card-green">
            <div>
                <div class="card-title text-green">⏱️ Simulazione d'esame</div>
                <div class="card-desc">Mettiti alla prova con una simulazione realistica.</div>
                <ul class="feature-list">
                    <li class="feature-item"><span class="icon-box bg-green-light">🎯</span> <b>20 Domande</b> - 30 min</li>
                    <li class="feature-item"><span class="icon-box bg-green-light">✅</span> <b>+1.5</b>&nbsp;Corretta</li>
                    <li class="feature-item"><span class="icon-box bg-green-light">❌</span> <b>-0.5</b>&nbsp;Errata</li>
                    <li class="feature-item"><span class="icon-box bg-green-light">⚪</span> <b>0</b>&nbsp;Omessa</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div style="margin-top: -15px;"></div>', unsafe_allow_html=True) 
        if st.button("📝 Avvia Simulazione", key="btn_exam", use_container_width=True):
            reset_state()
            st.session_state.mode = 'exam'
            st.session_state.exam_start_time = datetime.now()
            st.session_state.exam_questions = generate_exam_questions(all_questions, 20)
            st.rerun()

    with col3:
        # Card HTML Content
        st.markdown("""
        <div class="card-container card-purple">
            <div>
                <div class="card-title text-purple">📂 Materiale</div>
                <div class="card-desc">Accedi a tutte le lecture e agli appunti del corso.</div>
                <ul class="feature-list">
                    <li class="feature-item"><span class="icon-box bg-purple-light">📄</span> <b>Slide</b>&nbsp;e&nbsp;Dispense</li>
                    <li class="feature-item"><span class="icon-box bg-purple-light">📥</span> <b>Download</b> PDF</li>
                    <li class="feature-item"><span class="icon-box bg-purple-light">👁️</span> Visione in-app</li>
                    <li class="feature-item"><span class="icon-box bg-purple-light">🗂️</span> Archivio Completo</li>
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div style="margin-top: -15px;"></div>', unsafe_allow_html=True) 
        if st.button("📚 Apri Materiale", key="btn_materials", use_container_width=True):
            st.session_state.mode = 'materials'
            st.rerun()

    # Introduction / Footer Text
    st.markdown("""
    <div style="text-align: center; margin-top: 50px; color: gray; font-size: 1.1rem; max-width: 800px; margin-left: auto; margin-right: auto; line-height: 1.6;">
        Questa piattaforma è stata creata per supportare gli studenti nella preparazione all'esame di <i>Data Mining & Text Analytics</i>. 
        Attraverso quiz interattivi, simulazioni d'esame temporizzate e accesso diretto alle risorse didattiche, 
        potrai consolidare le tue conoscenze teoriche e pratiche in modo efficace e mirato.
    </div>
    """, unsafe_allow_html=True)

def run_materials_mode():
    st.sidebar.button("🏠 Torna alla Home", on_click=lambda: st.session_state.update(mode=None))
    st.title("📂 Materiale Didattico")
    st.markdown("Qui puoi visionare e scaricare tutto il materiale del corso.")
    st.divider()

    files_map = {
        "📘 Lecture 01 - Intro": "Lecture_01_Data_Mining_Introduction_2025_2026.pdf",
        "📙 Lecture 01.5 - SQL Handouts": "Lecture_01.5_Handouts_SQL_queries.pdf",
        "📗 Lecture 02 - Clustering Techniques": "Lecture_02_Clustering_Techniques.pdf",
        "📕 Lecture 03 - Perceptron & Learning": "Lecture_03_Perceptron_and_Learning_Process.pdf",
        "📔 Lecture 04 - Text Mining 1": "Lecture_04._Text_Mining_1.pdf",
        "📓 Lecture 05 - Text Mining 2": "Lecture_05_Text_Mining_2.pdf",
        "📒 Lecture 06 - Text Classification": "Lecture_06_Text_Classification.pdf",
        "📝 APPUNTI COMPLETI": "APPUNTI_LEZIONE_mining_copia.pdf"
    }

    # Layout for viewer
    col_list, col_view = st.columns([1, 2])
    
    with col_list:
        st.subheader("Elenco Files")
        selected_file_key = st.radio("Seleziona un file da visionare:", list(files_map.keys()))
        
        filename = files_map[selected_file_key]
        file_path = os.path.join("static", filename)
        
        
        
        # Access Control Logic for "APPUNTI COMPLETI"
        is_protected = "APPUNTI COMPLETI" in selected_file_key
        
        if is_protected:
            st.warning("🔒 **File Protetto**")
            st.info("Per scaricare questi appunti è necessaria l'approvazione dell'autore.")
            
            # Pre-filled Email Link
            email_subject = urllib.parse.quote("Richiesta Appunti Data Mining")
            email_body = urllib.parse.quote("Ciao Luca,\n\nVorrei richiedere una copia degli appunti completi di Data Mining.\n\nGrazie.")
            mailto_link = f"mailto:luca.tallarico99@gmail.com?subject={email_subject}&body={email_body}"
            
            st.markdown(f'''
                <a href="{mailto_link}" target="_blank" style="
                    display: inline-block;
                    background-color: #d9534f;
                    color: white;
                    padding: 12px 24px;
                    text-align: center;
                    text-decoration: none;
                    border-radius: 8px;
                    font-weight: bold;
                    font-size: 16px;
                    width: 100%;
                ">📨 Richiedi Copia via Email</a>
                <p style="margin-top: 10px; font-size: 0.9em; color: gray;">
                    Cliccando verrai reindirizzato al tuo client di posta.<br>
                    L'invio del file è a discrezione dell'autore.
                </p>
            ''', unsafe_allow_html=True)

        else:
            # Standard Download for non-protected files
            if os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    st.download_button(
                        label=f"⬇️ Scarica {filename}",
                        data=f,
                        file_name=filename,
                        mime="application/pdf",
                        use_container_width=True
                    )
            else:
                st.error(f"File {filename} non trovato in {file_path}.")

    with col_view:
        st.subheader("Anteprima")
        
        if is_protected:
             st.image("https://img.icons8.com/clouds/200/lock.png", width=150)
             st.markdown("### 🚫 Anteprima non disponibile")
             st.write("Questo contenuto è riservato. Invia una richiesta per ottenerlo.")
        else:
            filename = files_map[selected_file_key]
            file_path = os.path.join("static", filename)
            
            if os.path.exists(file_path):
                # STATIC SERVING (For the 'New Tab' link)
                encoded_filename = urllib.parse.quote(filename) 
                pdf_url = f"static/{encoded_filename}"
                
                # BASE64 ENCODING (For the internal preview - Most Reliable)
                with open(file_path, "rb") as f:
                    base64_pdf = base64.b64encode(f.read()).decode('utf-8')

                # 1. External Link (Still uses static URL as fallback because data: links are blocked in top-frame)
                st.markdown(f'''
                    <a href="{pdf_url}" target="_blank" style="
                        display: block; 
                        text-align: center; 
                        margin-bottom: 20px; 
                        padding: 15px; 
                        background-color: #f8f9fa; 
                        border: 2px solid #e9ecef;
                        border-radius: 8px; 
                        text-decoration: none; 
                        font-weight: 700; 
                        color: #0f172a;
                    ">
                        📄 Apri PDF in una nuova scheda (Consigliato)
                    </a>
                ''', unsafe_allow_html=True)
                
                # 2. Embedded Viewer (Using Base64 Data URI)
                pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="900px" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)
            else:
                st.warning(f"File non trovato nella cartella static: {file_path}")

def run_practice_mode(questions, correct_answers):
    st.sidebar.button("🏠 Torna alla Home", on_click=lambda: st.session_state.update(mode=None))
    st.title("🏋️ Quizzone - Tutte le Domande")
    
    # Sync widgets logic (Critical for Progress Bar)
    for q in questions:
        qid = q['id']
        key = f"q_{qid}"
        if key in st.session_state and st.session_state[key]:
            val = st.session_state[key]
            letter = val.split(".")[0]
            st.session_state.answers[qid] = letter

    # Sidebar
    with st.sidebar:
        st.title("📊 Controllo")
        total_q = len(questions)
        answered_q = len(st.session_state.answers)
        progress = answered_q / total_q if total_q > 0 else 0
        st.progress(progress)
        st.caption(f"Risposte: {answered_q}/{total_q}")
        
        if not st.session_state.submitted:
            if st.button("📝 INVIA QUIZ", type="primary", use_container_width=True):
                st.session_state.submitted = True
                st.rerun()
        else:
            if st.button("🔄 Reset Quizzone", type="secondary", use_container_width=True):
                reset_state()
                st.session_state.mode = 'practice' # Keep mode
                st.rerun()
        
        st.divider()
        # Navigation Grid
        with st.expander("🗺️ Navigatore", expanded=False):
            render_nav_grid(questions, correct_answers)

    # Render Questions (Practice Logic)
    render_questions(questions, correct_answers, is_exam=False)

def run_exam_mode(questions, correct_answers):
    # Timer Logic
    time_limit = timedelta(minutes=30)
    
    # Placeholder for timer
    timer_placeholder = st.empty()
    
    # We need to loop to update the timer visually
    # But we can't loop forever or it blocks usage. 
    # Streamlit rerun is triggered by interactions.
    # To make it "smooth" without blocking, we use st.empty() and just calculate diff.
    # But for REAL-TIME countdown we need a loop or Streamlit's fragment/autorefresh.
    # Simple fix: Just update calculation on every interaction (which is default).
    # "Fluid" usually means it ticks down. Streamlit can't do that easily without custom component or experimental_fragment.
    # Let's try `time.sleep` loop? No, blocks UI.
    # BEST APPROACH for standard Streamlit: Show "Ends at HH:MM" and current remaining specific to reload.
    # OR: use st_autorefresh (external lib) -> not available standard.
    # OR: use a simple async loop with `rerun`? No, too much flickering.
    
    # Compromise: We show the end time and the current remaining time.
    # To make it "tick", we can use `stream` generator or just accept static update.
    # USER WANTS SMOOTH: Only way in pure python streamlit is `st.empty` loop? 
    # Actually, let's use a small JS injection for visual countdown if possible, OR
    # just stick to "Update on interaction" but make it clear.
    
    # WAIT! New `st.markdown` with auto-refresh script? 
    # Let's use a simpler trick: `time.sleep(1)` inside a `while` loop is bad.
    
    # Let's Implement a "Poor Man's Live Timer" using st.asyncio or just
    # Rely on the fact user answers questions frequently.
    
    # ACTUALLY: Let's try adding a simple JS script to update a DOM element.
    # Streamlit 1.30+ supports `st.stream`.
    
    # LET'S DO THIS:
    end_time = st.session_state.exam_start_time + time_limit
    now = datetime.now()
    remaining = end_time - now
    
    if remaining.total_seconds() <= 0:
        if not st.session_state.submitted:
            st.session_state.submitted = True
            st.error("⏰ TEMPO SCADUTO!")
            st.rerun()
            
    # Display Timer
    mins, secs = divmod(int(remaining.total_seconds()), 60)
    timer_color = "red" if mins < 5 else "#60a5fa" # Lighter blue for dark mode contrast
    
    # Dynamic JS Timer (Components approach for stability)
    import streamlit.components.v1 as components
    
    # Simple visual countdown
    timer_html = f"""
    <div style="
        font-family: 'Inter', sans-serif;
        font-size: 20px; 
        font-weight: 700; 
        color: {timer_color}; 
        background-color: rgba(255,255,255,0.05); /* Slight tint */
        padding: 15px; 
        border: 2px solid {timer_color}; 
        border-radius: 12px; 
        text-align: center;
        margin-bottom: 20px;">
        ⏱️ Tempo Rimanente: <span id="timer-display">{mins:02d}:{secs:02d}</span>
        <div style="font-size: 11px; font-weight: 400; margin-top: 5px; opacity: 0.8;">
            (Al termine del tempo il quiz verrà inviato e corretto in automatico)
        </div>
    </div>
    <script>
    // Self-contained timer logic
    (function() {{
        var timeLeft = {int(remaining.total_seconds())};
        var display = document.getElementById('timer-display');
        
        var timerInterval = setInterval(function() {{
            if (timeLeft <= 0) {{
                clearInterval(timerInterval);
                display.textContent = "00:00";
                return;
            }}
            
            timeLeft--;
            var m = Math.floor(timeLeft / 60);
            var s = timeLeft % 60;
            
            m = m < 10 ? "0" + m : m;
            s = s < 10 ? "0" + s : s;
            
            display.textContent = m + ":" + s;
        }}, 1000);
    }})();
    </script>
    """
    
    # Use Components to render isolated HTML/JS
    components.html(timer_html, height=100) # Fixed height to avoid scrollbar

    st.sidebar.button("🏠 Torna alla Home", on_click=lambda: st.session_state.update(mode=None))
    
    st.title("⏱️ Simulazione Esame")

    # Sync widgets
    for q in questions:
        qid = q['id']
        key = f"q_{qid}"
        if key in st.session_state and st.session_state[key]:
            val = st.session_state[key]
            letter = val.split(".")[0]
            st.session_state.answers[qid] = letter

    # Sidebar
    with st.sidebar:
        st.title("📊 Esame")
        st.markdown(f"**Tempo:** {mins:02d}:{secs:02d}")
        
        answered_q = len(st.session_state.answers)
        st.caption(f"Risposte: {answered_q}/{len(questions)}")
        
        if not st.session_state.submitted:
            if st.button("📝 TERMINA ESAME", type="primary", use_container_width=True):
                st.session_state.submitted = True
                st.rerun()
        else:
            if st.button("🔄 Nuovo Esame", type="secondary", use_container_width=True):
                 # Revert to home or restart exam? Let's restart exam logic
                 reset_state()
                 st.session_state.mode = 'exam'
                 st.session_state.exam_start_time = datetime.now()
                 # Need to re-sample questions, handled by caller logic usually, but here we are inside function.
                 # Better to go home or reload manually. 
                 # Let's just go home for safety or re-init here.
                 # To re-sample we need all questions.
                 # Let's just set mode to None to force home
                 st.session_state.mode = None
                 st.rerun()

        st.divider()
        with st.expander("🗺️ Navigatore", expanded=True):
             render_nav_grid(questions, correct_answers)

    # Render Questions (Exam Logic)
    render_questions(questions, correct_answers, is_exam=True)

    # Grading (Specific to Exam)
    if st.session_state.submitted:
        calculate_exam_grade(questions, correct_answers)


def calculate_exam_grade(questions, correct_answers):
    st.divider()
    score = 0
    details = []
    
    correct_count = 0
    wrong_count = 0
    blank_count = 0
    
    for q in questions:
        qid = q['id']
        u_ans = st.session_state.answers.get(qid)
        c_ans = correct_answers.get(qid)
        
        if not u_ans:
            blank_count += 1
            # 0 points
        elif u_ans == c_ans:
            score += 1.5
            correct_count += 1
        else:
            score -= 0.5
            wrong_count += 1
            
    # Max score possible: 20 * 1.5 = 30
    # Min score possible: 20 * -0.5 = -10 (but usually floor at 0 or 18 for display?) 
    # User asked for "Voto in 30esimi".
    
    final_vote = max(0, score) # No negative grades on transcript typically
    
    st.markdown(f"## 📝 Risultati Esame")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Voto Finale", f"{final_vote:.1f} / 30")
    col2.metric("✅ Corrette (+1.5)", correct_count)
    col3.metric("❌ Errate (-0.5)", wrong_count)
    col4.metric("⬜ Non date (0)", blank_count)
    
    if final_vote >= 18:
        st.success("🎉 ESAME SUPERATO!")
        st.balloons()
    else:
        st.error("🚫 ESAME NON SUPERATO.")


# Helper for Grid
def render_nav_grid(questions, correct_answers):
    st.markdown("""
    <style>
    .nav-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 5px; }
    .nav-item { 
        display: flex; align-items: center; justify_content: center; 
        padding: 5px; border-radius: 5px; font-size: 12px; font-weight: bold; 
        text-decoration: none; color: black !important;
    }
    .nav-answered { background-color: #d1e7dd; border: 1px solid #badbcc; }
    .nav-empty { background-color: #f8f9fa; border: 1px solid #dee2e6; }
    .nav-wrong { background-color: #f8d7da; border: 1px solid #f5c6cb; }
    .nav-correct { background-color: #198754; color: white !important; }
    
    @media (prefers-color-scheme: dark) {
            .nav-empty { background-color: #343a40; border-color: #495057; color: white !important; }
            .nav-answered { background-color: #0f5132; border-color: #146c43; color: white !important; }
    }
    </style>
    """, unsafe_allow_html=True)
    
    html_grid = '<div class="nav-grid">'
    for q in questions:
        qid = q['id']
        css_class = "nav-item nav-empty"
        
        if st.session_state.submitted:
            u_ans = st.session_state.answers.get(qid)
            c_ans = correct_answers.get(qid)
            if u_ans == c_ans:
                css_class = "nav-item nav-correct"
            elif u_ans:
                css_class = "nav-item nav-wrong"
        else:
            if qid in st.session_state.answers:
                css_class = "nav-item nav-answered"
        
        html_grid += f'<a href="#q_{qid}" class="{css_class}">{qid}</a>'
    html_grid += '</div>'
    st.markdown(html_grid, unsafe_allow_html=True)


# Helper for Questions
def render_questions(questions, correct_answers, is_exam):
    # Group by sections if Practice, or just List if Exam?
    # Exam usually just list or maybe Sections if available.
    # Let's keep sections logic if available, otherwise just list.
    
    if is_exam:
        # Just simple list 1 to 20
        for i, q in enumerate(questions):
            render_single_question(q, correct_answers, i+1)
    else:
        # Group by sections
        sections = {}
        for q in questions:
            sec = q['section']
            if sec not in sections: sections[sec] = []
            sections[sec].append(q)
            
        for sec_name, sec_questions in sections.items():
            st.header(sec_name)
            for q in sec_questions:
                render_single_question(q, correct_answers)
                
    # Practice Mode Results (at buttom)
    if not is_exam and st.session_state.submitted:
         st.divider()
         score = 0
         total = len(questions)
         for q in questions:
             if st.session_state.answers.get(q['id']) == correct_answers.get(q['id']):
                 score += 1
         st.markdown(f"### 🏆 Risultato: {score} / {total}")
         st.progress(score/total)


def render_single_question(q, correct_answers, display_num=None):
    q_id = q['id']
    title_text = f"{display_num}. {q['text']}" if display_num else f"{q_id}. {q['text']}"
    
    # Anchor
    st.markdown(f"<div id='q_{q_id}'></div>", unsafe_allow_html=True)
    
    show_feedback = st.session_state.submitted or (q_id in st.session_state.verified_ids)
    
    status_md = ""
    if show_feedback:
        u_ans = st.session_state.answers.get(q_id)
        c_ans = correct_answers.get(q_id)
        if not u_ans:
            status_md = "⚠️ Non risposta"
        elif u_ans == c_ans:
            status_md = f"✅ Corretto ({c_ans})"
        else:
            c_text = q['options'].get(c_ans, "N/A")
            status_md = f"❌ Errato. Corretta: **{c_ans}** ({c_text})"
    
    with st.container(border=True):
        st.markdown(f"**{title_text}**")
        
        opts = q['options']
        options_display = [f"{k}. {v}" for k, v in opts.items()]
        
        index = None
        if q_id in st.session_state.answers:
            saved = st.session_state.answers[q_id]
            for i, o in enumerate(options_display):
                if o.startswith(f"{saved}."):
                    index = i
                    break
        
        sel = st.radio(
            "Opzioni:", 
            options_display, 
            index=index, 
            key=f"q_{q_id}", 
            disabled=show_feedback,
            label_visibility="collapsed"
        )
        
        if sel:
            st.session_state.answers[q_id] = sel.split(".")[0]
            
        # Verify Button (Only in Practice)
        if st.session_state.mode == 'practice' and not show_feedback:
             if st.button("Verifica", key=f"btn_ver_{q_id}"):
                 st.session_state.verified_ids.add(q_id)
                 st.rerun()
                 
        if show_feedback:
            # Feedback Logic
            if "✅" in status_md: 
                st.success(status_md)
            elif "❌" in status_md: 
                st.error(status_md)
            else: 
                st.warning(f"⚠️ Non risposta. La risposta corretta era: **{c_ans}**")

            # Show Explanation if available
            explanation = q.get('explanation')
            if explanation:
                st.info(f"**Spiegazione:** {explanation}")


# -----------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------
def main():
    FILE_PATH = "simulazione_esame_completa.txt"
    all_questions, correct_answers = load_quiz_data(FILE_PATH)
    
    if not all_questions:
        st.error("File dati non trovato.")
        return

    init_session_state()

    if st.session_state.mode is None:
        show_home_page(all_questions)
        
    elif st.session_state.mode == 'practice':
        run_practice_mode(all_questions, correct_answers)
        
    elif st.session_state.mode == 'exam':
        # Ensure we have exam questions selected
        if not st.session_state.exam_questions:
             # Fallback if empty (shouldn't happen if initialized correctly)
             st.session_state.exam_questions = random.sample(all_questions, 20)
        
        run_exam_mode(st.session_state.exam_questions, correct_answers)
        
    elif st.session_state.mode == 'materials':
        run_materials_mode()

if __name__ == "__main__":
    main()
