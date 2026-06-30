import streamlit as st
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="GATE CSE Tracker", page_icon="📱", layout="wide")

# --- INITIALIZE SESSION STATE ---
# This mimics a database so your data persists while the app is running
if 'streak' not in st.session_state:
    st.session_state.streak = 5
if 'overall_progress' not in st.session_state:
    st.session_state.overall_progress = 12

# --- SIDEBAR: Countdown & Stats ---
st.sidebar.title("🎯 GATE Countdown")
# Assuming GATE Exam is around Feb 1, 2027 (Adjust as needed)
exam_date = datetime.date(2027, 2, 1)
today = datetime.date.today()
days_left = (exam_date - today).days

st.sidebar.metric(label="Days Remaining", value=f"{days_left} Days")
st.sidebar.markdown("---")
st.sidebar.subheader("🔥 Consistency")
st.sidebar.metric(label="Current Study Streak", value=f"{st.session_state.streak} Days")

# --- MAIN DASHBOARD ---
st.title("📱 GATE CSE Preparation Tracker")
st.subheader("🏠 Dashboard")

# Top Row Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.info(f"📅 **Current Day:** Day {225 - days_left} of 225")
with col2:
    # Simulating modern calculation
    st.metric(label="📊 Overall Syllabus Completion", value=f"{st.session_state.overall_progress}%")
    st.progress(st.session_state.overall_progress / 100)
with col3:
    st.success("⏱ **Today's Goal:** 7 Hours GATE + Tasks")

st.markdown("---")

# --- DAILY CHECKLISTS ---
left_col, right_col = st.columns([2, 1])

with left_col:
    current_day_name = today.strftime("%A")
    st.header(f"✅ Daily Checklist ({current_day_name})")
    st.write(f"**Date:** {today.strftime('%B %d, %Y')}")
    
    # 7 Hour Mandatory Gate Study
    st.subheader("💻 GATE Study (7 Hours Mandatory)")
    gate_sessions = [st.checkbox(f"Session {i+1} (1 Hour)") for i in range(7)]
    gate_completed = sum(gate_sessions)
    
    # Daily Tasks
    st.subheader("📋 Daily Routine Tasks")
    c1 = st.checkbox("College Study (2 Hours)")
    c2 = st.checkbox("English Communication")
    c3 = st.checkbox("1 LeetCode Problem")
    c4 = st.checkbox("Revision")
    c5 = st.checkbox("Today's PYQs")
    c6 = st.checkbox("Notes Updated")
    
    # Weekend Specific Additions
    if current_day_name == "Saturday":
        st.subheader("⚡ Saturday Special Tasks")
        sat1 = st.checkbox("PYQ Marathon")
        sat2 = st.checkbox("Weekly Revision")
    elif current_day_name == "Sunday":
        st.subheader("🧬 Sunday Special Tasks")
        sun1 = st.checkbox("Mock Test (1 hr 30 min)")
        sun2 = st.checkbox("Mock Analysis & Error Log")
        
    # Optional Tasks
    st.subheader("🚀 Optional/Side Tasks")
    o1 = st.checkbox("GitHub Project")
    o2 = st.checkbox("Free Certification")

with right_col:
    # --- END OF DAY LOGGING ---
    st.header("🏁 End of Day Log")
    
    actual_hours = st.number_input("Hours Studied Today:", min_value=0.0, max_value=24.0, value=float(gate_completed), step=0.5)
    productivity = st.select_slider("Productivity Rating:", options=["⭐", "⭐⭐", "⭐⭐ Crappy", "⭐⭐⭐ Decent", "⭐⭐⭐⭐ Focused", "⭐⭐⭐⭐⭐ Beast Mode"], value="⭐⭐⭐⭐ Focused")
    
    learned = st.text_area("What I Learned Today:")
    weak_topics = st.text_area("Weak Topics to Revise:")
    
    if st.button("Save & Submit Day"):
        st.balloons()
        st.success("Progress saved successfully! Keep the streak alive! 🔥")
        # Logic to update state/database would go here

st.markdown("---")

# --- MONTHLY TIMELINE ---
st.header("📆 Month-wise Syllabus Timeline")

tabs = st.tabs(["July", "August", "September", "October", "Nov-Dec", "Jan-Feb"])

with tabs[0]:
    st.subheader("📅 July Focus")
    st.checkbox("Aptitude", value=True)
    st.checkbox("Engineering Mathematics")
    st.checkbox("Discrete Mathematics")
    st.checkbox("July PYQs Completed")
    st.checkbox("July Revision Done")

with tabs[1]:
    st.subheader("📅 August Focus")
    st.checkbox("Digital Logic")
    st.checkbox("COA")
    st.checkbox("C Programming")
    st.checkbox("August PYQs")
    st.checkbox("August Revision")

with tabs[2]:
    st.subheader("📅 September Focus")
    st.checkbox("Data Structures")
    st.checkbox("Algorithms")
    st.checkbox("DBMS")
    st.checkbox("September PYQs")
    st.checkbox("September Revision")

with tabs[3]:
    st.subheader("📅 October (1–20) Focus")
    st.checkbox("Operating Systems")
    st.checkbox("Theory of Computation")
    st.checkbox("Playlist Completed")

with tabs[4]:
    st.subheader("📅 October 21 – December 19 Focus")
    st.checkbox("Full Revision Phase 1")
    st.checkbox("Weekly Mock Tests")
    st.checkbox("Weak Topics Covered")
    st.markdown("**December 20 – January 20:**")
    st.checkbox("Computer Networks")
    st.checkbox("Compiler Design")
    st.checkbox("Remaining Playlists")

with tabs[5]:
    st.subheader("📅 January 20 – February 10 (Final Push)")
    st.checkbox("Grand Mock Tests")
    st.checkbox("PYQ Mega Revision")
    st.checkbox("Formula Revision")
    st.checkbox("Error Log Completed")
