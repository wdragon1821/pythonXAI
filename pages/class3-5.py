import random
import streamlit as st
import time
ss = st.session_state
if "ans" not in ss:
    ss.ans = random.randint(1, 100)
if "max_num" not in ss:
    ss.max_num = 100
if "min_num" not in ss:
    ss.min_num = 1
st.title("number game!")
num = st.number_input(f"pls enter a number between {ss.min_num} and {ss.max_num}",step = 1)
if st.button("start to guess , ? Quick :("):
    if num > ss.ans:
        st.write("too high")
        if num < ss.max_num:
            ss.max_num = num
    elif num < ss.ans:
        st.write("too low")
        if num > ss.min_num:
            ss.min_num = num
    else:
        st.write("correct!")   
        st.balloons()
    time.sleep(1)
    st.rerun