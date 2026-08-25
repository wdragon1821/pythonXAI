import streamlit as st  # 匯入streamlit模組並重新命名

#st.number_input()可以讓使用者輸入數字，設定step = 1可以讓使用者每次增加或減少一個整數
# ，min_value和max_value分別設定輸入數字的最小值和最大值，value設定預設值
number = st.number_input("請輸入數字", min_value=0, max_value=100, step=1)
#st.markdown()可以讓使用者在網頁上輸入Markdown語法，並顯示出來
st.markdown(f"您輸入的數字是: {number}")



st.markdown("---")
st.markdown("### 練習")
score = st.number_input("請輸入你的分數", min_value=0, max_value=100, step=1)
if score >= 90:
    st.write("你的等級是 A")
elif score >= 80:
    st.write("你的等級是 B")
elif score >= 70:
    st.write("你的等級是 C")
elif score >= 60:
    st.write("你的等級是 D")
else:
    st.write("你的等級是 F")







st.markdown("---")
st.markdown("### 按鈕練習")
#st.button()可以在網頁上顯示一個按鈕，使用者按下按鈕後
#key是按鈕的唯一識別碼，label是按鈕上顯示的文字
#如果使用者按下按鈕，st.button()會回傳True，否則回傳False
st.button("請按我",key="button1")
if st.button("請按我",key="balloon"):
    st.balloons()
if st.button("請按我",key="snow"):
    st.snow()
st.markdown("---")






import streamlit as st

st.title("🎉 My Effects Machine")

if st.button("🎈 Balloons"):
    st.balloons()

if st.button("❄️ Snow"):
    st.snow()

if st.button("🎉 Confetti"):
    st.balloons()