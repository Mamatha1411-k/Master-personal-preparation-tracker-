import streamlit as st
import datetime
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="GATE Master", page_icon="🎯", layout="wide")

# --- INITIALIZE ALL SESSION STATES ---
if 'streak' not in st.session_state: st.session_state.streak = 0
if 'total_hours' not in st.session_state: st.session_state.total_hours = 0.0
if 'pyqs_solved' not in st.session_state: st.session_state.pyqs_solved = 0
if 'leetcode_solved' not in st.session_state: st.session_state.leetcode_solved = 0
if 'subjects_completed' not in st.session_state: st.session_state.subjects_completed = 0
if 'mock_scores' not in st.session_state: st.session_state.mock_scores = []

# --- THEME (Dark Mode Styling via Markdown Injection) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    div.stButton > button:first-child { background-color: #FF4B4B; color: white; border-radius:8px;}
    </style>
""", unsafe_style_html=True)

# --- APP BANNER & MAIN TOP APP HEADER ---
st.title("🎯 GATE Master AI")
st.caption("🚀 Preparation Kickoff: Day 1 Starts Tomorrow (July 1, 2026)!")

# --- BOTTOM / TOP STREAMLIT NAV TABS ---
nav_tab = st.radio("📱 Navigation Menu", 
                   ["🏠 Dashboard", "✅ Daily & Weekly Planner", "📚 Subject & PYQ Tracker", "📊 Analytics & Badges", "🤖 GATE Master AI"], 
                   horizontal=True)

st.markdown("---")

# --- DATE CALCULATIONS (FIXED TO YOUR TIMELINE) ---
today = datetime.date(2026, 6, 30) # Set to June 30, 2026
start_date = datetime.date(2026, 7, 1) # Prep starts July 1, 2026
exam_date = datetime.date(2027, 2, 7) # Typical GATE weekend Feb 2027

days_left = (exam_date - datetime.date.today()).days

# Calculate Current Prep Day string safely
if datetime.date.today() < start_date:
    current_day_str = "Day 0 (Kickoff Tomorrow!)"
else:
    day_count = (datetime.date.today() - start_date).days + 1
    current_day_str = f"Day {day_count} of 225"

# ==========================================
# 1. DASHBOARD NAVIGATION
# ==========================================
if nav_tab == "🏠 Dashboard":
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🔥 Current Streak", f"{st.session_state.streak} Days")
    with col2:
        st.metric("📊 Overall Syllabus", "0%")
        st.progress(0.0)
    with col3:
        st.metric("📅 Current Timeline", current_day_str)
    with col4:
        st.metric("🎯 Exam Countdown", f"{days_left} Days")

    st.subheader("🌙 Night Mode Configuration Active")
    st.info("💡 Reminders: Sleep early tonight. Get ready to lock in Session 1 tomorrow morning at 7:00 AM!")

# ==========================================
# 2. DAILY & WEEKLY PLANNER
# ==========================================
elif nav_tab == "✅ Daily & Weekly Planner":
    st.header("📅 Execution Center")
    
    # 7-Hour Tracker Component
    st.subheader("⏱ 7-Hour Mandatory GATE Timer Logs")
    hours_logged = st.slider("Select how many study sessions (1 hr each) completed today:", 0, 7, 0)
    st.progress(hours_logged / 7.0)
    
    col_d, col_w = st.columns(2)
    with col_d:
        st.subheader("✅ Daily Checklist")
        st.checkbox("College Study (2 Hours)")
        st.checkbox("English Communication")
        st.checkbox("1 LeetCode Problem")
        st.checkbox("Revision Framework")
        st.checkbox("Today's Gate PYQs")
        st.checkbox("Notes Updated")
        
    with col_w:
        st.subheader("📅 Weekend Routine Special")
        day_name = datetime.date.today().strftime("%A")
        st.write(f"Today is: **{day_name}**")
        if day_name == "Saturday":
            st.checkbox("🔥 PYQ Marathon Session")
            st.checkbox("📚 Comprehensive Weekly Revision")
        elif day_name == "Sunday":
            st.checkbox("📝 Live Mock Test (1hr 30m)")
            st.checkbox("📊 Post-Mock Mistakes Entry")
        else:
            st.write("Weekend tracking modules will load automatically here on Saturday & Sunday.")

# ==========================================
# 3. SUBJECT & PYQ TRACKER
# ==========================================
elif nav_tab == "📚 Subject & PYQ Tracker":
    st.header("📚 Syllabus & Question Engines")
    
    tab_sub, tab_pyq, tab_extra = st.tabs(["📚 Subjects Status", "📖 PYQ & Mock Logs", "🌐 Code & Certs"])
    
    with tab_sub:
        st.subheader("July Plan Kickoff Targets")
        st.markdown("**Aptitude:** 🔴 Scheduled (Starts July 1)")
        st.markdown("**Engineering Mathematics:** 🔴 Scheduled (Starts July 1)")
        st.markdown("**Discrete Mathematics:** 🔴 Scheduled (Starts July 1)")
        
    with tab_pyq:
        st.number_input("Update PYQs Solved Counter:", value=st.session_state.pyqs_solved, key="new_pyq")
        st.session_state.pyqs_solved = st.session_state.new_pyq
        
        st.subheader("📝 Latest Mock Test Entry")
        score = st.number_input("Enter your latest out-of-100 Mock Exam Score:", min_value=0.0, max_value=100.0, value=0.0)
        if st.button("Log Score"):
            st.session_state.mock_scores.append(score)
            st.success("Test record successfully added to trend database!")
            
    with tab_extra:
        st.subheader("💻 Portfolios & Up-skilling")
        st.checkbox("Push daily coding project patch to GitHub")
        st.checkbox("Complete Free NPTEL/Coursera Certification Lesson")

# ==========================================
# 4. ANALYTICS & GAMIFICATION
# ==========================================
elif nav_tab == "📊 Analytics & Badges":
    st.header("📊 Deep Performance Analytics")
    
    # Mock scores display
    st.subheader("📝 Mock Test Score Trajectory")
    if len(st.session_state.mock_scores) > 0:
        st.line_chart(st.session_state.mock_scores)
    else:
        st.info("No mock test data logged yet. Take your first test this weekend!")
    
    # Gamification Badges
    st.subheader("🏆 Your Earned Badges Hall")
    b_col1, b_col2, b_col3 = st.columns(3)
    with b_col1:
        st.write("🔒 *10-Day Streak Badge (Locked)*")
        st.write("🔒 *100-Hour Warrior Badge (Locked)*")
    with b_col2:
        st.write("🔒 *Subject Conqueror Badge (Locked)*")
        st.write("🔒 *500+ PYQs Badged (Locked)*")
    with b_col3:
        st.write("🔒 *100 LeetCode Badge (Locked)*")

# ==========================================
# 5. GATE MASTER AI 🤖
# ==========================================
elif nav_tab == "🤖 GATE Master AI":
    st.header("🤖 Your GATE Master AI Engine")
    
    ai_features = st.selectbox("Choose AI Utility tool:", 
                               ["📅 Smart Daily Study Plan Generator", "📊 Weak-Topic Deep Analysis", "🎯 Dynamic Revision Suggestions", "💬 Custom Motivational Charge"])
    
    if ai_features == "📅 Smart Daily Study Plan Generator":
        st.markdown("### 🤖 AI Plan for Day 1 (Tomorrow):")
        st.write("- **08:00 AM - 11:00 AM:** Foundation Setup: Linear Algebra / Set Theory Fundamentals.")
        st.write("- **12:00 PM - 02:00 PM:** General Aptitude (Percentage / Ratios basic module).")
        st.write("- **04:00 PM - 06:00 PM:** LeetCode Basic Array setups.")
        st.write("- **08:00 PM - 09:00 PM:** Summary notes creation for Day 1 materials.")
        
    elif ai_features == "📊 Weak-Topic Deep Analysis":
        st.markdown("### 📊 AI Error Log Evaluation:")
        st.info("Analysis engine requires at least 3 days of checklist logs to identify accuracy trends.")
        
    elif ai_features == "🎯 Dynamic Revision Suggestions":
        st.markdown("### 📖 Smart Revision Cards:")
        st.info("💡 **Formula Trigger Flash:** Matrix Rank Condition -> A system of $A \\cdot x = b$ is consistent if and only if $Rank(A) = Rank(A|b)$.")
        
    elif ai_features == "💬 Custom Motivational Charge":
        quotes = [
            "Tomorrow is Day 1. No excuses, no shortcuts. Your GATE 2027 rank journey starts now! 🔥",
            "Consistent 7 hours beats a 14-hour single burst every single time. Start strong tomorrow!",
            "Every single task you tick off tomorrow brings you closer to your dream IISc/IIT seat."
        ]
        st.success(random.choice(quotes))
      
