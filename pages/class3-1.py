import streamlit as st
st.title("欄位元件")
col1, col2 = st.columns(2)  #2col
col1.button("按鈕1", "key=1")   #col1建立一個按鈕st.button(""按鈕1"")
col2.button("按鈕2", "key=2")   #col2建立一個按鈕st.button(""按鈕2"")



col1, col2, col3 = st.columns([1, 2, 3])
col1.button("按鈕1", "key=5")   #col1建立一個按鈕st.button(""按鈕1"")
col2.button("按鈕2", "key=6")   #col2建立一個按鈕st.button(""按鈕2"")
col3.button("按鈕3", "key=7")   #col3建立一個按鈕st.button(""按鈕3"")

col1, col2 = st.columns([1,2])
with col1:  #在col1使用with語句放更多西
    if st.button("按鈕1", "key=8"):     #在col1建立一個button
        st.balloons()   #make a balloon in col1
    st.write("this is col1") #make a word in col1
with col2:  #在col2使用with語句放更多西
  if st.button("按鈕2", "key=9"):   #在col1建立一個button
    st.write("this is col2")    #make a word in col2




st.write("---")
st.title("文字元件")
#st.text格式st.text_input(tital, value = 預設文字)
text = st.text_input("pls input text", value="預設文字")
st.write(f"text = {text}")








if "ans1" not in st.session_state:  #如果session_state中沒有ans1就建立一個
     st.session_state.ans1 = 1  #建立    st.session_state.ans1 = 1

if st.button("按下去ans加一" , key="ans2"):     
    st.session_state.ans1 = st.session_state.ans1 + 1
st.write(f"ans1 = {st.session_state.ans1}")     #寫入session_state中的ans的值


if "apple" not in st.session_state:     #如果session_state中沒有apple就建立一個
     st.session_state.apple = 1     #建立    st.session_state.apple = 1





if st.button("重新整理畫面", key = "banana"):   #重新整理畫面

    st.rerun()     #重新整理畫面