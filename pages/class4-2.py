import streamlit as st
import os
#st.image("pic路徑, lenth")
st.title("📁 pic")
st.image("image/apple.png", width=300)



image_folder = "image"
image_files = os.listdir(image_folder)
st.write(image_files)
print(image_files)
image_size = st.number_input("請輸入圖片大小", min_value = 50, max_value = 500, step = 50, value = 100 )
#圖片

for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=image_size)



for image_file in image_files:

    st.image(f"{image_folder}/{image_file}", use_container_width = True)


st.success("購買成功")