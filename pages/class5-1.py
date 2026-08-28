import streamlit as st

# -------------------------
# 商品資料
# -------------------------

products = {
    "apple": {
        "image": "image/apple.png",
        "price": 10,
        "stock": 10
    },
    "orange": {
        "image": "image/orange.png",
        "price": 10,
        "stock": 10
    },
    "bg": {
        "image": "image/bg.png",
        "price": 10,
        "stock": 10
    },
    "banana": {
        "image": "image/banana.png",
        "price": 10,
        "stock": 10
    }
}


# -------------------------
# Session State
# -------------------------

if "products" not in st.session_state:
    st.session_state.products = products

if "message" not in st.session_state:
    st.session_state.message = ""


# -------------------------
# 購物平台
# -------------------------

st.title("購物平台")


# 選擇一欄有幾個圖片
number = st.number_input(
    "請輸入欄為個數",
    min_value=1,
    max_value=5,
    step=1,
    value=4
)


# 建立欄位
columns = st.columns(number)


product_names = list(st.session_state.products.keys())


for i, name in enumerate(product_names):

    # 如果商品數量超過欄位數，就不顯示
    if i >= number:
        break

    product = st.session_state.products[name]

    with columns[i]:

        # 商品圖片
        st.image(product["image"], use_container_width=True)

        # 商品名稱
        st.subheader(name.upper())

        # 價格
        st.write(f"price: {product['price']}")

        # 庫存
        st.write(f"left: {product['stock']}")

        # 購買按鈕
        if st.button(f"buy {name}", key=f"buy_{name}"):

            if product["stock"] > 0:
                product["stock"] -= 1
                st.session_state.message = "購買成功！"
            else:
                st.session_state.message = "庫存不足！"


# 顯示購買結果
if st.session_state.message:
    st.success(st.session_state.message)


# -------------------------
# 新商品庫存
# -------------------------

st.title("新商品庫存")


# 選擇商品
selected_product = st.selectbox(
    "選擇商品",
    product_names
)


# 新增多少庫存
add_stock = st.number_input(
    "新增庫存數量",
    min_value=1,
    step=1
)


# 新增庫存按鈕
if st.button("新增庫"):

    st.session_state.products[selected_product]["stock"] += add_stock

    st.success("新增庫存成功！")


# -------------------------
# 顯示目前庫存
# -------------------------

st.write("目前庫存：")

st.write(
    f"apple {st.session_state.products['apple']['stock']}"
)

st.write(
    f"orange {st.session_state.products['orange']['stock']}"
)

st.write(
    f"bg {st.session_state.products['bg']['stock']}"
)

st.write(
    f"banana {st.session_state.products['banana']['stock']}"
)