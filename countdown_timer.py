import time
import streamlit as st

# Streamlit UI Setup
st.set_page_config(page_title="Countdown Timer", layout="centered")
st.title("⏳ Countdown Timer")

# User input for time entry
seconds = st.number_input("⏱️ Enter time (seconds):", min_value=1, step=1, value=10)

# Timer display placeholder
timer_placeholder = st.empty()

# Initialize session state
if "running" not in st.session_state:
    st.session_state.running = False
if "time_left" not in st.session_state:
    st.session_state.time_left = seconds

# Buttons arranged horizontally
col1, col2 = st.columns(2)
with col1:
    start = st.button("▶️ Start")
with col2:
    stop = st.button("⏹️ Stop")

# Button functionality
if start:
    st.session_state.running = True
    st.session_state.time_left = seconds

if stop:
    st.session_state.running = False

# Countdown function
def countdown():
    while st.session_state.time_left > 0 and st.session_state.running:
        mins, secs = divmod(st.session_state.time_left, 60)
        timer_placeholder.markdown(f"## ⏲️ {mins:02d}:{secs:02d}")
        time.sleep(1)
        st.session_state.time_left -= 1
    if st.session_state.time_left == 0 and st.session_state.running:
        timer_placeholder.markdown("## 🎉 Time's Up!")
        st.session_state.running = False

# Run countdown in the loop
if st.session_state.running:
    countdown()

# Check out the output
# https://countdown-timer-python-project-v6d388rgwlrgw65rpeubxf.streamlit.app/
