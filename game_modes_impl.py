
# -----------------------------------------------------------------------------
# SURVIVAL MODE
# -----------------------------------------------------------------------------
def show_survival_mode(all_questions):
    st.markdown("## 🔥 Survival Mode")

    # If game over
    if st.session_state.game_lives <= 0:
        st.error(f"GAME OVER! Streak: {st.session_state.game_score}")
        if st.button("Riprova"):
            st.session_state.game_score = 0
            st.session_state.game_lives = 1
            st.session_state.current_question = None
            st.session_state.verified_ids = set() # abuse verified_ids to track seen in this session
            st.rerun()
        return

    # Score Board
    col1, col2 = st.columns(2)
    col1.metric("Streak", st.session_state.game_score)
    col2.metric("Vite", "❤️" * st.session_state.game_lives)
    
    # Get Question
    if st.session_state.current_question is None:
        # Pick one random not recently seen if possible
        pool = [q for q in all_questions if q['id'] not in st.session_state.verified_ids]
        if not pool:
            pool = all_questions # reset pool if exhausted
            st.session_state.verified_ids = set()
            
        q = random.choice(pool)
        st.session_state.current_question = q
        st.session_state.verified_ids.add(q['id'])
    
    q = st.session_state.current_question
    
    # Display Question
    st.markdown(f"### {q['text']}")
    
    # Options
    options = q['options'][:] # copy
    # random.shuffle(options) # Optional shuffle
    
    # Interaction
    # We use a key based on score/streak so it resets every question
    selection = st.radio("Scegli la risposta:", options, key=f"surv_{st.session_state.game_score}")
    
    if st.button("Conferma"):
        correct_char = q['correct']
        selected_char = selection.split(".")[0]
        
        if selected_char == correct_char:
            st.success("Corretto! +1 Streak")
            st.session_state.game_score += 1
            st.session_state.current_question = None # Force new question
            st.balloons()
            time.sleep(1)
            st.rerun()
        else:
            st.error(f"Sbagliato! La risposta era {correct_char}.")
            st.session_state.game_lives -= 1
            if st.session_state.game_lives <= 0:
                pass # Will show game over next rerun
            st.rerun()

# -----------------------------------------------------------------------------
# TIME ATTACK MODE
# -----------------------------------------------------------------------------
def show_time_attack_mode(all_questions):
    st.markdown("## ⚡ Time Attack")
    
    # Timer Logic
    now = datetime.now()
    remaining = (st.session_state.game_end_time - now).total_seconds()
    
    if remaining <= 0:
        st.error(f"TEMPO SCADUTO! Punteggio Finale: {st.session_state.game_score}")
        if st.button("Riprova"):
            st.session_state.game_score = 0
            st.session_state.game_end_time = datetime.now() + timedelta(seconds=60)
            st.session_state.current_question = None
            st.session_state.verified_ids = set()
            st.rerun()
        return

    # Dashboard
    c1, c2 = st.columns(2)
    c1.metric("Punteggio", st.session_state.game_score)
    c2.metric("Tempo Rimasto", f"{int(remaining)}s", delta_color="normal")
    
    st.progress(max(0.0, min(1.0, remaining / 60.0))) # Visual approximate usage (assuming 60s base)
    
    # Get Question
    if st.session_state.current_question is None:
        q = random.choice(all_questions)
        st.session_state.current_question = q
    
    q = st.session_state.current_question
    st.markdown(f"**{q['text']}**")
    
    options = q['options']
    
    # We need buttons for speed! Radio is slow.
    cols = st.columns(2)
    for i, opt in enumerate(options):
        # opt string "A. text"
        # We want clicking the button to trigger check
        with cols[i % 2]:
            if st.button(opt, key=f"ta_{st.session_state.game_score}_{i}", use_container_width=True):
                # Check Answer
                correct_char = q['correct']
                selected_char = opt.split(".")[0]
                
                if selected_char == correct_char:
                    st.toast("Corretto! +5s", icon="✅")
                    st.session_state.game_score += 100
                    st.session_state.game_end_time += timedelta(seconds=5)
                else:
                    st.toast("Errato! -10s", icon="❌")
                    st.session_state.game_end_time -= timedelta(seconds=10)
                
                st.session_state.current_question = None
                st.rerun()

    # Manual refresh hack to keep timer ticking visually? 
    # Streamlit doesn't auto-refresh. User must interact. 
    # We can add st.empty() loop for pure visuals but it blocks interaction.
    # Better: just rely on interaction updates.

# -----------------------------------------------------------------------------
# REVERSE MODE
# -----------------------------------------------------------------------------
def show_reverse_mode(all_questions):
    st.markdown("## 🃏 Reverse Quiz")
    st.info("Indovina la domanda a partire dalla spiegazione!")
    
    if st.session_state.current_question is None:
        # Pick a question that HAS a good explanation
        candidates = [q for q in all_questions if q.get('explanation') and len(q['explanation']) > 15]
        target = random.choice(candidates)
        
        # Pick 3 distractors
        distractors = random.sample([q for q in all_questions if q['id'] != target['id']], 3)
        
        options = [target] + distractors
        random.shuffle(options)
        
        st.session_state.current_question = target
        st.session_state.reverse_options = options
        
    target = st.session_state.current_question
    options = st.session_state.reverse_options
    
    # Display Explanation
    st.markdown(f"""
    <div style="padding:20px; border-radius:10px; background-color:#f0f2f6; border-left: 5px solid #8b5cf6;">
        <h4>📝 Spiegazione</h4>
        <p style="font-size:1.1rem; font-style:italic;">{target['explanation']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("### Qual era la domanda?")
    
    selection = st.radio("Scegli:", [opt['text'] for opt in options], key=f"rev_{target['id']}")
    
    if st.button("Conferma"):
        if selection == target['text']:
            st.success("Indovinato!")
            st.balloons()
            time.sleep(1)
            st.session_state.current_question = None
            st.rerun()
        else:
            st.error(f"Sbagliato! La domanda corretta era: {target['text']}")
            if st.button("Prossima"):
                st.session_state.current_question = None
                st.rerun()
