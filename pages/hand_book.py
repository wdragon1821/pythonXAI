import streamlit as st

with st.expander("課堂筆記 CLASS 1"):
    '''當然可以！我幫你把今天的 Python 內容整理成一份**國小學生也容易看懂、適合考前複習的筆記**。我會把比較難的說法換成簡單的比喻，並保留你今天學到的重點。

# 🐍 Python 今日課程整理筆記

## 1. `print()`：把東西顯示出來

`print()` 就像是 Python 的**喇叭**，可以把文字或數字顯示在終端機上。

```python
print("Hello World!")
print("楊博翔")
print(604)
```

結果：

```text
Hello World!
楊博翔
604
```

### 換行 `\n`

`\n` 代表「換到下一行」。

```python
print("不要低頭\n雙下巴會出來")
```

會變成：

```text
不要低頭
雙下巴會出來
```

---

# 2. 註解：寫給自己看的文字

**註解不會被 Python 執行。**

### 單行註解

在前面加 `#`：

```python
# 這是我的註解
print("Hello")
```

Python 會忽略 `#` 後面的內容。

### 多行註解

可以使用：

```python
"""
這是
多行註解
"""
```

適合一次寫很多行的說明。

### ⭐ 快速註解

在 VS Code 中：

**Control + /**

可以快速把程式碼變成註解，再按一次可以取消註解。

---

# 3. Python 的基本資料型態

Python 裡面的資料有不同種類，就像生活中有：

* 數字
* 文字
* 是或不是

Python 常見的基本型態有 4 種：

| 型態      | 名稱  | 例子                  |
| ------- | --- | ------------------- |
| `int`   | 整數  | `1`、`100`、`-5`      |
| `float` | 浮點數 | `1.5`、`3.14`        |
| `str`   | 字串  | `"apple"`、`"Hello"` |
| `bool`  | 布林值 | `True`、`False`      |

### 🔢 `int`：整數

```python
print(1)
print(12345)
```

就是沒有小數點的數字。

### 🥧 `float`：浮點數

```python
print(1.5)
print(3.14)
```

就是有小數點的數字。

### 🔤 `str`：字串

```python
print("apple")
print("Hello")
```

**有引號包起來的文字通常就是字串。**

注意：

```python
1
```

是數字。

但是：

```python
"1"
```

是文字！

### ✅ `bool`：布林值

只有兩種：

```python
True
False
```

可以想成：

**True = 是 / 對 / 成立**

**False = 否 / 錯 / 不成立**

---

# 4. 變數：幫資料取名字

變數可以想成一個**有名字的盒子**。

例如：

```python
a = 1
```

意思就是：

> 建立一個叫 `a` 的盒子，把 `1` 放進去。

之後：

```python
print(a)
```

就可以拿出 `a` 裡面的東西。

結果：

```text
1
```

---

### 🔄 變數可以改變

```python
a = 1
print(a)

a = "apple"
print(a)
```

結果：

```text
1
apple
```

所以變數裡面的資料可以被換掉。

### ⭐ `=` 是什麼？

```python
a = 1
```

這裡的 `=` **不是「等於」的意思**。

它比較像：

> 「把右邊的東西放進左邊。」

所以：

```python
a = 10
```

就是把 `10` 存進 `a`。

---

# 5. 運算子：讓 Python 幫我們算數學

Python 可以直接做數學運算。

### ➕ 加法

```python
print(1 + 1)
```

結果：

```text
2
```

### ➖ 減法

```python
print(5 - 2)
```

結果：

```text
3
```

### ✖️ 乘法

```python
print(3 * 4)
```

結果：

```text
12
```

### ➗ 除法

```python
print(10 / 2)
```

結果：

```text
5.0
```

### `//`：取商

```python
print(10 // 3)
```

結果：

```text
3
```

因為：

10 ÷ 3 = 3 …… 1

只留下**商 3**。

### `%`：取餘數

```python
print(10 % 3)
```

結果：

```text
1
```

因為：

10 ÷ 3 = 3 …… **1**

所以 `%` 就是找「剩下多少」。

### `**`：次方

```python
print(2 ** 3)
```

意思是：

```text
2 × 2 × 2
```

結果：

```text
8
```

---

# 6. 運算順序

如果一題裡面有很多運算，Python 不會亂算，而是有固定順序。

記住：

### 🥇 第一：`()` 括號

### 🥈 第二：`**` 次方

### 🥉 第三：`* / // %`

### 🏅 第四：`+ -`

例如：

```python
print(2 + 3 * 4)
```

會先算：

```text
3 × 4 = 12
```

再算：

```text
2 + 12 = 14
```

所以答案是：

```text
14
```

如果寫：

```python
print((2 + 3) * 4)
```

就會先算括號：

```text
2 + 3 = 5
5 × 4 = 20
```

答案就是：

```text
20
```

---

# 7. 字串也可以做運算！

Python 不只可以算數字，**文字也可以做一些運算。**

## 🔗 字串相加

```python
print("apple" + "pen")
```

結果：

```text
applepen
```

就是把兩個文字接在一起。

如果希望中間有空格：

```python
print("apple " + "pen")
```

結果：

```text
apple pen
```

---

## ✖️ 字串乘法

```python
print("apple " * 3)
```

結果：

```text
apple apple apple
```

意思就是把同一個字串重複 3 次。

---

# 8. f-string：把變數放進文字裡

這個非常實用！

例如：

```python
num = 30
item = "book"

print(f"a {item} is {num}$")
```

結果：

```text
a book is 30$
```

前面的 `f` 很重要：

```python
f"..."
```

然後用 `{}` 把變數放進去。

---

### 再看一個例子

```python
name = "apple"
age = 18

print(f"Hello, my name is {name}, I'm {age} years old.")
```

Python 會把：

```python
{name}
```

換成：

```text
apple
```

把：

```python
{age}
```

換成：

```text
18
```

所以最後變成：

```text
Hello, my name is apple, I'm 18 years old.
```

### ⭐ 記法

> **f-string = 把變數塞進文字裡**

---

# 9. 型態轉換

有時候我們需要把一種資料變成另一種資料。

就像：

> 把「文字版的 10」變成「真正的數字 10」。

---

### `int()` → 變成整數

```python
int(1.0)
```

變成：

```text
1
```

例如：

```python
int(1.234)
```

會變成：

```text
1
```

⚠️ 小數部分會被去掉。

---

### `float()` → 變成小數

```python
float(1)
```

變成：

```text
1.0
```

也可以：

```python
float("1.234")
```

把文字 `"1.234"` 變成數字 `1.234`。

---

### `str()` → 變成文字

```python
str(1)
```

會變成：

```text
"1"
```

---

### `bool()` → 變成 True 或 False

例如：

```python
bool(1)
```

結果：

```text
True
```

---

### ⚠️ 不能亂轉

例如：

```python
int("hello")
```

會發生錯誤。

因為：

```text
"hello"
```

不是數字，Python 沒辦法把它變成整數。

---

# 10. `input()`：讓使用者輸入東西

`input()` 就像是在問使用者問題。

```python
name = input("請輸入你的名字：")
```

螢幕會出現：

```text
請輸入你的名字：
```

然後等待你輸入。

例如你輸入：

```text
小明
```

那麼：

```python
name
```

就會存著：

```text
小明
```

---

## ⭐ 非常重要：`input()` 預設是字串

例如：

```python
a = input("請輸入數字：")
```

就算你輸入：

```text
10
```

Python 還是會把它當成：

```python
"10"
```

也就是**字串**。

如果要拿來計算，要轉成整數：

```python
a = input("請輸入數字：")
print(int(a) + 10)
```

如果輸入：

```text
20
```

結果：

```text
30
```

---

# 11. 小實作：計算圓形面積

你今天做了一個很棒的小程式：

```python
half = input("請輸入半徑：")
print(int(half) * int(half) * 3.14)
```

它會先問：

```text
請輸入半徑：
```

假設輸入：

```text
5
```

程式就會計算：

```text
5 × 5 × 3.14
```

得到：

```text
78.5
```

也就是圓形面積。

公式：

> **圓形面積 = 半徑 × 半徑 × 3.14**

---

# 12. Streamlit：把 Python 做成網頁

前面的 Python 大多是在**終端機**裡看到結果。

而 `Streamlit` 可以幫我們把 Python 程式做成比較漂亮的**網頁介面**。

首先：

```python
import streamlit as st
```

意思可以簡單理解成：

> 「把 Streamlit 這個工具拿進來使用。」

`st` 是我們給 Streamlit 取的簡短名字。

---

# 13. `st.title()`：網頁的大標題

```python
st.title("這是標題")
```

會在網頁上顯示一個大標題：

# 這是標題

---

# 14. `st.write()`：顯示內容

```python
st.write("Hello World!")
```

可以用來顯示很多不同類型的內容。

例如文字、數字等。

你可以把它想成：

> **Streamlit 版本的 `print()`**

---

# 15. `st.text()`：顯示普通文字

```python
st.text("這是一段文字")
```

它主要就是顯示**純文字**。

不會特別幫你做粗體、標題等格式。

---

# 16. `st.markdown()`：讓文字變漂亮

`st.markdown()` 可以使用 Markdown 語法來排版。

例如：

```python
st.markdown("**粗體**")
```

會變成：

**粗體**

---

### ⭐ 常見 Markdown

| 寫法          | 功能     |
| ----------- | ------ |
| `# 標題`      | 最大標題   |
| `## 標題`     | 第二大標題  |
| `### 標題`    | 第三大標題  |
| `**文字**`    | **粗體** |
| `*文字*`      | *斜體*   |
| `- 項目`      | 項目清單   |
| `---`       | 分隔線    |
| `` `程式碼` `` | 程式碼    |

---

# 🧠 今天最重要的觀念

如果要考試，我會特別記住這些：

### ⭐ Python 基本功

```text
print()       → 顯示東西
#             → 單行註解
""" """       → 多行註解

int           → 整數
float         → 小數
str           → 字串
bool          → True / False

=             → 把右邊的資料放進左邊的變數

+             → 加
-             → 減
*             → 乘
/             → 除
//            → 取商
%             → 取餘數
**            → 次方

input()       → 讓使用者輸入
int()         → 轉整數
float()       → 轉小數
str()         → 轉字串
bool()        → 轉布林值

f"..."        → 把變數放進文字

import        → 匯入工具

st.title()    → Streamlit 大標題
st.write()    → Streamlit 顯示內容
st.text()     → Streamlit 純文字
st.markdown() → Streamlit Markdown 排版
```

## 🎯 一句話記住今天的 Python

> **Python 就像是在跟電腦說話：`input()` 負責問你、變數負責記住資料、運算子負責計算、`print()` 負責把答案說出來，而 Streamlit 可以把這些東西做成網頁！**

    '''


with st.expander("課堂筆記 CLASS 2"):
    '''
    # 🐍 Python 今日課程整理筆記：比較、判斷與 Streamlit 按鈕

今天學到的內容開始變得很有趣了！前面我們學會了**變數、輸入、運算**，今天則開始教 Python **「做決定」**。

你可以把今天的 Python 想成一個很聰明的小機器人：

> 🤖 「你給我條件，我就幫你判斷，然後決定要做什麼！」

---

## 1. 🔍 比較運算子

比較運算子就是拿兩個東西來**比一比**。

比較完之後，答案一定是：

```python
True
```

或

```python
False
```

也就是：

> ✅ 對 / 是
> ❌ 錯 / 不是

### 常見的比較運算子

| 運算子  | 意思    | 範例                 |
| ---- | ----- | ------------------ |
| `==` | 等於    | `1 == 1` → `True`  |
| `!=` | 不等於   | `1 != 1` → `False` |
| `>`  | 大於    | `5 > 3` → `True`   |
| `<`  | 小於    | `2 < 5` → `True`   |
| `>=` | 大於或等於 | `5 >= 5` → `True`  |
| `<=` | 小於或等於 | `4 <= 5` → `True`  |

### ⭐ 最容易搞錯的地方

```python
=
```

和

```python
==
```

是不一樣的！

### `=`

是把資料放進變數：

```python
score = 90
```

意思：

> 把 90 放進 `score`。

### `==`

是拿來**比較**：

```python
score == 90
```

意思：

> `score` 是不是 90？

---

# 2. 🧠 `and`：而且、兩個都要成立

`and` 就像在說：

> **「這兩個條件都要對！」**

例如：

```python
print(True and True)
```

結果：

```text
True
```

但是：

```python
print(True and False)
```

結果：

```text
False
```

因為 `and` 的規則是：

> ❗ **只要有一個 False，最後就是 False。**

### 可以想成：

你要進入遊樂園，必須：

* 🎫 有票
* 👟 穿鞋

兩個都符合才能進去。

| 條件 A  | 條件 B  | `A and B` |
| ----- | ----- | --------- |
| True  | True  | ✅ True    |
| True  | False | ❌ False   |
| False | True  | ❌ False   |
| False | False | ❌ False   |

### ⭐ 記法

> **AND = 全部都要有**

---

# 3. 🟢 `or`：或者、至少一個成立

`or` 就像在說：

> **「只要有一個條件對就可以！」**

例如：

```python
print(True or False)
```

結果：

```text
True
```

因為其中一個是 `True`。

只有：

```python
False or False
```

才會得到：

```text
False
```

### `or` 的表格

| 條件 A  | 條件 B  | `A or B` |
| ----- | ----- | -------- |
| True  | True  | ✅ True   |
| True  | False | ✅ True   |
| False | True  | ✅ True   |
| False | False | ❌ False  |

### ⭐ 記法

> **OR = 有一個就可以**

例如：

> 今天下雨「或」今天很冷 → 我就帶外套。

只要其中一個是真的，就可以帶外套。

---

# 4. 🔄 `not`：反過來

`not` 非常簡單：

> **把 True 變 False，把 False 變 True。**

```python
print(not True)
```

結果：

```text
False
```

而：

```python
print(not False)
```

結果：

```text
True
```

### ⭐ 記法

> **NOT = 反過來**

就像一個「反轉開關」：

```text
True  → not → False
False → not → True
```

---

# 5. 🚪 `if`：如果……

現在開始進入很重要的部分：

## `if`

`if` 就是：

> **「如果這個條件成立，就做這件事。」**

例如：

```python
if score >= 60:
    print("及格")
```

意思是：

> 如果分數大於或等於 60，就顯示「及格」。

---

# 6. 🔐 密碼門檢查

今天的程式非常像一個**密碼門**！

```python
password = input("pls input codeword")

if password == "1234":
    print("welcome Jeffrey")
elif password == "5678":
    print("welcome Tim")
elif password == "0000":
    print("welcome Chole")
else:
    print("codeword wrong")
```

我們來一步一步看。

### 第一步

```python
password = input("pls input codeword")
```

程式問：

> 🔑 請輸入密碼

使用者輸入的東西會放進：

```python
password
```

---

### 第二步

```python
if password == "1234":
```

意思：

> 如果密碼是 `1234`……

就執行：

```python
print("welcome Jeffrey")
```

---

### 第三步

```python
elif password == "5678":
```

`elif` 就是：

> **「不然如果……」**

如果前面的 `if` 不成立，就繼續檢查這個。

---

### 第四步

```python
else:
```

`else` 就是：

> **「以上全部都不是！」**

所以最後顯示：

```text
codeword wrong
```

---

# 7. 🧩 `if`、`elif`、`else`

這三個非常重要！

可以把它想成：

```text
if
 ↓
如果是這個
 ↓
不然如果是這個 elif
 ↓
不然如果是這個 elif
 ↓
全部都不是 → else
```

### 完整結構

```python
if 條件1:
    做事情1
elif 條件2:
    做事情2
elif 條件3:
    做事情3
else:
    做其他事情
```

---

# 8. 🤔 為什麼用 `elif`？

假設有：

```python
if score >= 90:
    print("A")

elif score >= 80:
    print("B")

elif score >= 70:
    print("C")
```

如果分數是 `95`：

Python 發現：

```text
95 >= 90
```

是 `True`。

所以就得到：

```text
A
```

後面的條件就不用再繼續判斷。

### ⭐ `elif` 的優點

可以：

* 讓程式比較簡單
* 減少不需要的判斷
* 程式更容易閱讀
* 避免同一個人得到很多個結果

---

# 9. 🏆 分數等級程式

今天做的這個非常重要：

```python
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
```

例如輸入：

```text
85
```

Python 會檢查：

```text
85 >= 90 ❌
85 >= 80 ✅
```

所以得到：

```text
你的等級是 B
```

---

# 10. 🌐 Streamlit：做網頁

今天又繼續使用 Streamlit。

首先：

```python
import streamlit as st
```

就是把 Streamlit 工具拿進來使用。

---

# 11. 🔢 `st.number_input()`

這個指令可以讓使用者在網頁上**輸入數字**。

例如：

```python
number = st.number_input(
    "請輸入數字",
    min_value=0,
    max_value=100,
    step=1
)
```

### 這些設定是什麼？

| 設定              | 意思         |
| --------------- | ---------- |
| `"請輸入數字"`       | 顯示給使用者看的文字 |
| `min_value=0`   | 最小可以輸入 0   |
| `max_value=100` | 最大可以輸入 100 |
| `step=1`        | 每次增加或減少 1  |

所以使用者可以在網頁上選：

```text
0
1
2
3
...
100
```

---

# 12. 📝 `st.markdown()`

我們之前已經學過：

```python
st.markdown()
```

今天也繼續使用它。

例如：

```python
st.markdown(f"您輸入的數字是: {number}")
```

如果使用者輸入：

```text
50
```

網頁就會顯示：

> 您輸入的數字是: 50

因為用了 `f`，所以 `{number}` 會被換成變數裡面的資料。

---

# 13. ➖ `st.markdown("---")`

```python
st.markdown("---")
```

可以在網頁上畫出一條分隔線。

像這樣：

---

可以用來把不同的內容分開。

---

# 14. 🔘 `st.button()`：做按鈕

這是今天非常好玩的東西！

```python
st.button("請按我")
```

會在網頁上出現一個：

**「請按我」**

的按鈕。

---

# 15. 🎈 按鈕可以做事情！

例如：

```python
if st.button("請按我"):
    st.balloons()
```

意思是：

> 如果使用者按下「請按我」，就放氣球！

🎈🎈🎈

---

# 16. ❄️ Snow 雪花效果

```python
if st.button("請按我"):
    st.snow()
```

按下按鈕後：

❄️❄️❄️❄️❄️

就會出現雪花效果。

---

# 17. 🔑 `key`：給按鈕一個名字

如果有很多按鈕，Python 需要知道：

> 「到底是哪一個按鈕？」

所以可以使用：

```python
key="balloon"
```

例如：

```python
st.button("請按我", key="balloon")
```

另一個：

```python
st.button("請按我", key="snow")
```

雖然兩個按鈕上面都是「請按我」，但 Python 可以靠 `key` 分辨它們。

### ⭐ 記住

> **`key` = 元件的專屬名字**

---

# 18. 🎉 今天最後的 Effects Machine

你最後做了一個很酷的小作品：

```python
import streamlit as st

st.title("🎉 My Effects Machine")

if st.button("🎈 Balloons"):
    st.balloons()

if st.button("❄️ Snow"):
    st.snow()

if st.button("🎉 Confetti"):
    st.balloons()
```

這個程式的概念就是：

```text
        🎉 My Effects Machine
                 ↓
      ┌─────────────────┐
      │ 🎈 Balloons     │ → 🎈🎈🎈
      └─────────────────┘

      ┌─────────────────┐
      │ ❄️ Snow         │ → ❄️❄️❄️
      └─────────────────┘

      ┌─────────────────┐
      │ 🎉 Confetti     │ → 🎉🎉🎉
      └─────────────────┘
```

這其實已經開始有點像真正的**網頁小遊戲**了！🎮

---

# 🧠 今天最重要的速記表

| 指令                  | 意思                 |
| ------------------- | ------------------ |
| `==`                | 是否等於               |
| `!=`                | 是否不等於              |
| `>`                 | 大於                 |
| `<`                 | 小於                 |
| `>=`                | 大於或等於              |
| `<=`                | 小於或等於              |
| `and`               | 而且，全部都要 True       |
| `or`                | 或者，一個 True 就可以     |
| `not`               | 把 True / False 反過來 |
| `if`                | 如果                 |
| `elif`              | 不然如果               |
| `else`              | 以上都不是              |
| `st.number_input()` | 讓使用者輸入數字           |
| `st.button()`       | 做一個按鈕              |
| `st.balloons()`     | 放氣球 🎈             |
| `st.snow()`         | 下雪 ❄️              |
| `key`               | 元件的專屬名字            |
| `st.markdown()`     | 顯示 Markdown / 排版文字 |

---

# 🏆 今天一定要會的 5 個觀念

### ① 比較

```python
5 > 3
```

➡️ `True`

### ② AND

```python
True and False
```

➡️ `False`

> **and：全部都要對。**

### ③ OR

```python
True or False
```

➡️ `True`

> **or：一個對就可以。**

### ④ IF 判斷

```python
if score >= 60:
    print("及格")
else:
    print("不及格")
```

> **if = 如果……就……**

### ⑤ 按鈕

```python
if st.button("🎈"):
    st.balloons()
```

> **按下按鈕 → 執行事情。**

---

## 🚀 把今天的課程想成一個 Python 機器人

```text
        🐍 Python
           │
           ▼
     🔍 比較條件
           │
           ▼
    🧠 and / or / not
           │
           ▼
      🤔 if 判斷
       /    |    \
      /     |     \
    if    elif    else
     │      │       │
     ▼      ▼       ▼
    🎈     ❄️      ❌
```

所以今天最大的進步就是：

> **以前你只能叫 Python 做事情，現在你開始可以讓 Python「自己判斷該做什麼事情」了！** 🐍💻🎮

    '''


with st.expander("課堂筆記 CLASS 3"):
    '''
    # 🐍 Python 今日課程整理筆記：欄位、記憶、迴圈與列表

今天的內容比前幾堂更進階了！我們開始學會讓 Streamlit 的網頁**分欄位、記住資料**，還學了 Python 很重要的兩個工具：

> 🔁 **for 迴圈**：讓電腦重複做事情
> 📦 **list 列表**：把很多資料放在同一個地方

---

# 1. 🏗️ `st.columns()`：把網頁分成幾欄

如果所有東西都從上排到下，看起來可能很單調。

`st.columns()` 可以把網頁分成不同欄位。

例如：

```python
col1, col2 = st.columns(2)
```

意思是：

> 把網頁分成 **2 欄**。

可以想成：

```text
┌─────────────┬─────────────┐
│    col1     │    col2     │
│             │             │
└─────────────┴─────────────┘
```

---

# 2. 🔘 在欄位裡放按鈕

例如：

```python
col1, col2 = st.columns(2)

col1.button("按鈕1", key="key1")
col2.button("按鈕2", key="key2")
```

就可以讓：

* `col1` 裡面有按鈕 1
* `col2` 裡面有按鈕 2

### ⭐ 重要觀念

以前我們寫：

```python
st.button("按鈕")
```

現在可以寫：

```python
col1.button("按鈕")
```

意思就是：

> 在 `col1` 這個欄位裡建立按鈕。

---

# 3. 📏 不同大小的欄位

我們也可以決定每一欄有多寬：

```python
col1, col2, col3 = st.columns([1, 2, 3])
```

這代表三欄的寬度比例是：

```text
col1 : col2 : col3
 1   :  2   :  3
```

所以：

```text
┌────┬────────┬─────────────┐
│ C1 │   C2   │     C3      │
│ 1  │   2    │      3      │
└────┴────────┴─────────────┘
```

### ⭐ 記住

`[1, 2, 3]` **不是數字本身的大小**，而是代表：

> **每個欄位的寬度比例。**

---

# 4. `with`：指定「接下來放在哪裡」

如果想在同一個欄位放很多東西，可以使用：

```python
with col1:
    ...
```

例如：

```python
with col1:
    st.write("this is col1")
    st.button("按鈕1")
```

意思就是：

> 接下來這些東西全部放到 `col1` 裡。

可以想成：

📦 `with col1:`
→ 「接下來的東西全部丟進 col1 這個盒子。」

---

# 5. 🎈 欄位也可以有互動效果

例如：

```python
with col1:
    if st.button("按鈕1"):
        st.balloons()
```

意思：

> 如果按下 `col1` 裡面的按鈕，就在 `col1` 裡觸發氣球效果。

這樣就可以做出比較漂亮的網頁！

---

# 6. 📝 `st.text_input()`：讓使用者輸入文字

之前我們學過：

```python
st.number_input()
```

它是輸入**數字**。

今天學：

```python
st.text_input()
```

它是輸入**文字**。

例如：

```python
text = st.text_input("pls input text", value="預設文字")
```

網頁會出現一個文字輸入框。

### `value`

```python
value="預設文字"
```

代表：

> 一開始輸入框裡面先放「預設文字」。

---

# 7. 📢 顯示使用者輸入的文字

```python
text = st.text_input("pls input text", value="預設文字")

st.write(f"text = {text}")
```

假設使用者輸入：

```text
Hello
```

網頁就會顯示：

```text
text = Hello
```

這裡又用到了我們之前學過的：

> ⭐ `f-string`

---

# 8. 🧠 `st.session_state`：讓 Streamlit 記住東西

這是今天非常重要的新觀念！

Streamlit 網頁有一個特別的地方：

> 當你按按鈕時，程式可能會重新執行。

所以如果想讓程式**記住以前的資料**，可以使用：

```python
st.session_state
```

你可以把它想成：

> 🧠 **Streamlit 的記憶盒子**

---

# 9. 📦 建立 `session_state` 裡的資料

例如：

```python
if "ans1" not in st.session_state:
    st.session_state.ans1 = 1
```

意思是：

> 如果記憶盒子裡沒有 `ans1`，就建立它，而且把它設成 `1`。

可以想成：

```text
🧠 Streamlit 記憶盒子

ans1 → 1
```

---

# 10. ➕ 讓按鈕讓數字一直增加

```python
if st.button("按下去ans加一"):
    st.session_state.ans1 = st.session_state.ans1 + 1
```

如果原本：

```text
ans1 = 1
```

按一下：

```text
ans1 = 2
```

再按：

```text
ans1 = 3
```

再按：

```text
ans1 = 4
```

所以它可以做出很簡單的：

🖱️ **點擊計數器！**

---

# 11. 🔄 `st.rerun()`：重新執行網頁

今天也碰到了：

```python
st.rerun()
```

它的意思是：

> **重新執行 Streamlit 程式。**

可以想成：

🔄「重新整理這個 Streamlit 畫面。」

例如：

```python
if st.button("重新整理畫面"):
    st.rerun()
```

按下按鈕後，Streamlit 就會重新跑一次程式。

---

# 12. 🔁 `for` 迴圈：重複做事情

這是今天 Python 非常重要的內容！

`for` 迴圈可以讓電腦：

> **重複做同一件事情很多次。**

例如：

```python
for i in range(5):
    print(i)
```

結果：

```text
0
1
2
3
4
```

---

# 13. 🔢 `range(5)` 是什麼？

```python
range(5)
```

會產生：

```text
0, 1, 2, 3, 4
```

⚠️ **不包含 5！**

所以：

```python
range(5)
```

其實就是：

> 從 `0` 開始，到 `5` 前面結束。

---

# 14. 🧑 `i` 是什麼？

```python
for i in range(5):
    print(i)
```

這裡的 `i` 是一個**迴圈變數**。

它會一次拿一個數字：

```text
第一次 → i = 0
第二次 → i = 1
第三次 → i = 2
第四次 → i = 3
第五次 → i = 4
```

所以：

```python
print(i)
```

就會把每次的 `i` 印出來。

### ⭐ `i` 不一定要叫 `i`

也可以：

```python
for number in range(5):
    print(number)
```

名稱可以自己取。

---

# 15. `range()` 可以設定開始和結束

```python
for i in range(1, 5):
    print(i)
```

結果：

```text
1
2
3
4
```

記住：

> `range(開始, 結束)`

而且：

> ⚠️ **不包含結束的數字。**

---

# 16. ⏩ `range()` 還可以設定步長

```python
for i in range(1, 10, 2):
    print(i)
```

結果：

```text
1
3
5
7
9
```

格式：

```python
range(開始, 結束, 每次跳幾格)
```

所以：

```python
range(1, 10, 2)
```

就是：

> 從 1 開始，每次 +2，直到 10 前面。

---

# 17. 🧮 `for` 迴圈裡也可以計算

```python
for i in range(5):
    a = i * 2

print(a)
```

每次都會計算：

```text
i = 0 → a = 0
i = 1 → a = 2
i = 2 → a = 4
i = 3 → a = 6
i = 4 → a = 8
```

最後：

```text
a = 8
```

所以最後 `print(a)` 會顯示：

```text
8
```

---

# 18. 🔺 數字金字塔

今天做了一個很酷的練習：

```python
import streamlit as st

st.title("數字金字塔")

num = st.number_input(
    "請輸入一個數字(1-9)",
    min_value=1,
    max_value=9,
    step=1
)

st.write("數字金字塔如下：")

for i in range(1, num + 1):
    st.write(str(i) * i)
```

假設輸入：

```text
5
```

就會得到：

```text
1
22
333
4444
55555
```

### 🤔 為什麼？

這一行：

```python
str(i) * i
```

就是把數字變成文字，再重複 `i` 次。

例如：

```python
str(3) * 3
```

就是：

```text
"333"
```

所以就可以做出數字金字塔！ 🔺

---

# 19. 📦 List：列表

現在進入另一個超級重要的東西：

## `list`

List 就像一個：

> 🎒 **可以裝很多東西的大背包。**

例如：

```python
a = [10, 20, 30]
```

這個列表裡有：

```text
10
20
30
```

---

# 20. 🪣 空列表

也可以先建立一個空的列表：

```python
b = []
```

現在裡面什麼都沒有：

```text
[]
```

之後再慢慢放東西進去。

---

# 21. 🎒 List 可以放不同種類的資料

例如：

```python
c = [10, "hello", 3.14]
```

裡面可以同時有：

```text
10      → int
"hello" → str
3.14    → float
```

甚至：

```python
me = ["Paul", 12, 11.9, False]
```

也可以！

---

# 22. 🔢 Index：列表的位置編號

這個一定要記！

Python 的 List **從 0 開始編號**。

例如：

```python
fruits = ["apple", "banana", "cherry"]
```

位置是：

```text
Index
  0       1         2
  ↓       ↓         ↓
apple   banana    cherry
```

所以：

```python
print(fruits[0])
```

結果：

```text
apple
```

而：

```python
print(fruits[1])
```

結果：

```text
banana
```

### ⭐ 最重要

> **List 的第一個位置是 `0`，不是 `1`！**

---

# 23. 📋 印出整個 List

如果直接：

```python
print(fruits)
```

會看到：

```text
['apple', 'banana', 'cherry']
```

就是整個列表。

---

# 24. ➕ `append()`：在最後面新增東西

例如：

```python
a = [1, 2, 3]

a.append(5)

print(a)
```

結果：

```text
[1, 2, 3, 5]
```

`append()` 就是：

> **在列表最後面加東西。**

可以想成往書包最後面塞進一本書。🎒📕

---

# 25. 🗑️ `remove()`：刪除指定的東西

例如：

```python
number = [2, 4, 6, 8]

number.remove(4)

print(number)
```

結果：

```text
[2, 6, 8]
```

`remove(4)` 的意思：

> 找到「4」，把它刪掉。

---

# 26. 🔃 `sort()`：排序

例如：

```python
numbers = [5, 2, 9, 1, 7]

numbers.sort()

print(numbers)
```

結果：

```text
[1, 2, 5, 7, 9]
```

預設是：

> **從小排到大。**

也就是「升序」。

⚠️ `sort()` 會直接改變原本的列表。

---

# 27. 📏 `len()`：看看有幾個東西

例如：

```python
a = [1, 2, 3, "a", "b", "c"]

print(len(a))
```

結果：

```text
6
```

因為裡面有：

```text
1
2
3
"a"
"b"
"c"
```

總共有 6 個。

### ⭐ 注意

`len()` 是算：

> **有幾個元素**

不是找最大的 index。

例如：

```text
元素：  A   B   C
index:  0   1   2
```

有 3 個元素，但最大 index 是 2。

所以：

```python
len(list)
```

和：

```text
最大的 index
```

是不一樣的。

---

# 28. 🗑️ `pop()`：按照位置刪除

例如：

```python
a = [1, 2, 3, "a", "b", "c"]

a.pop(0)
```

`pop(0)`：

> 刪掉 index 0 的東西。

所以 `1` 被刪掉。

列表變成：

```text
[2, 3, "a", "b", "c"]
```

---

## 如果不寫位置呢？

```python
a.pop()
```

就會刪掉：

> **最後一個元素。**

例如：

```text
[2, 3, "a", "b", "c"]
```

使用：

```python
a.pop()
```

就會刪掉：

```text
"c"
```

剩下：

```text
[2, 3, "a", "b"]
```

---

# 29. 🔁 用 `for` 走過 List

List 和 `for` 迴圈非常適合一起使用！

第一種方法：

```python
a = [1, 2, 3, "a", "b", "c"]

for i in range(0, len(a), 2):
    print(a[i])
```

這裡是在利用 index 找資料。

---

# 30. 🚶 直接把 List 裡的東西一個一個拿出來

還有更簡單的方法：

```python
a = [1, 2, 3, "a", "b", "c"]

for i in a:
    print(i)
```

Python 會：

```text
第一次 → i = 1
第二次 → i = 2
第三次 → i = 3
第四次 → i = "a"
第五次 → i = "b"
第六次 → i = "c"
```

所以會全部印出來。

### ⭐ 記住

如果只是想：

> 「把 List 裡面的每個東西拿出來。」

通常可以直接：

```python
for i in a:
```

---

# 31. 🗑️ 用迴圈找出要刪掉的東西

例如：

```python
a = ["f", "e", "d", "a", "b", "c"]

for i in a:
    if i == "a":
        a.remove(i)
```

意思是：

> 一個一個檢查 List 裡面的東西。

如果發現：

```text
i == "a"
```

就把 `"a"` 刪掉。

這裡把今天學到的：

* `for`
* `if`
* `list`
* `remove()`

全部結合在一起了！🔥

---

# 🧠 今天的超級重點

## 🌐 Streamlit

| 指令                 | 功能               |
| ------------------ | ---------------- |
| `st.columns()`     | 把網頁分成幾欄          |
| `col1.button()`    | 在指定欄位放按鈕         |
| `with col1:`       | 接下來的東西放進 col1    |
| `st.text_input()`  | 輸入文字             |
| `st.session_state` | 讓 Streamlit 記住資料 |
| `st.rerun()`       | 重新執行網頁           |

---

## 🔁 迴圈

| 指令                | 功能        |
| ----------------- | --------- |
| `for`             | 重複做事情     |
| `range(5)`        | 0～4       |
| `range(1, 5)`     | 1～4       |
| `range(1, 10, 2)` | 1、3、5、7、9 |

### ⭐ `range()` 最重要規則

> **開始有包含，結束沒有包含！**

---

## 📦 List

| 指令          | 功能                |
| ----------- | ----------------- |
| `[]`        | 建立 List           |
| `[1, 2, 3]` | 建立有資料的 List       |
| `list[0]`   | 取得第 1 個元素         |
| `append()`  | 最後面新增             |
| `remove()`  | 刪除指定的元素           |
| `sort()`    | 排序                |
| `len()`     | 計算有幾個元素           |
| `pop()`     | 刪除指定位置，沒寫位置就刪最後一個 |

---

# 🏆 今天最重要的 8 個觀念

### ① `columns`

> 🏗️ 把網頁分成不同欄位。

### ② `with`

> 📦 把接下來的東西放進指定欄位。

### ③ `session_state`

> 🧠 讓 Streamlit 記住資料。

### ④ `for`

> 🔁 重複做事情。

### ⑤ `range()`

> 🔢 產生一串數字，而且**不包含結束值**。

### ⑥ `list`

> 🎒 一個可以裝很多資料的容器。

### ⑦ `index`

> 🔢 List 裡每個東西的位置，而且**從 0 開始**。

### ⑧ `append / remove / pop`

> ➕ 新增 / 🗑️ 刪除指定內容 / 🗑️ 按位置刪除。

---

# 🐍 把今天的課程想成一個遊戲

你現在的 Python 已經可以做到：

```text
        🐍 Python 小遊戲
               │
       ┌───────┴───────┐
       ▼               ▼
    🌐 網頁          🧠 記憶
       │               │
   ┌───┴───┐       session_state
   ▼       ▼
  🔘按鈕   📝輸入
       │
       ▼
     🔁 for
       │
       ▼
     📦 List
       │
   ┌───┼───────────┐
   ▼   ▼     ▼     ▼
 append remove sort pop
```

## 🎯 一句話記住今天

> **`columns` 讓網頁變漂亮，`session_state` 讓程式記得事情，`for` 讓 Python 重複工作，而 `list` 就像一個大背包，可以裝很多資料！** 🐍🎒💻

    '''


with st.expander("課堂筆記 CLASS 4"):
    '''
    # 🐍 Python 今日課程筆記

## 🔁 while 迴圈、🎲 random、📖 字典、🖼️ 圖片與 Streamlit

今天學的東西很多！而且已經可以把前面學過的 **if、for、List、Streamlit** 和今天的新東西組合起來，做出真正的小遊戲了！🎮

---

# 1. 🔁 `while` 迴圈

`while` 的意思可以想成：

> **只要條件是 True，就一直做下去！**

基本寫法：

```python
while 條件:
    要做的事情
```

例如：

```python
i = 0

while i < 5:
    print(i)
    i += 1
```

結果：

```text
0
1
2
3
4
```

### 🧠 發生了什麼？

一開始：

```text
i = 0
```

Python 檢查：

```text
i < 5
0 < 5 → True ✅
```

所以執行一次。

接著：

```python
i += 1
```

就是：

```python
i = i + 1
```

所以：

```text
0 → 1 → 2 → 3 → 4 → 5
```

當：

```text
5 < 5 → False ❌
```

迴圈就停止了。

---

# 2. 🛑 `break`：直接跳出迴圈

`break` 就像一個：

> 🚪 **逃生門**

遇到 `break`，直接離開迴圈。

例如：

```python
i = 0

while i < 5:
    print(i)

    if i == 3:
        break

    i += 1
```

結果：

```text
0
1
2
3
```

因為 `i == 3` 的時候：

```python
break
```

就把迴圈結束了。

---

# 3. `break` 也可以放在 `for`

不只有 `while` 可以用 `break`。

```python
for i in range(5):

    print(i)

    if i == 3:
        break
```

結果：

```text
0
1
2
3
```

所以：

> 🔁 `for` 和 `while` 都可以使用 `break`。

---

# 4. 🎲 `random`：讓 Python 隨機抽東西

今天開始學會讓 Python：

> 🎰 **隨機選數字！**

首先：

```python
import random
```

意思是：

> 把 Python 的 `random` 隨機功能拿進來使用。

---

# 5. 🎲 `random.randrange()`

```python
random.randrange()
```

可以想成：

> 從一個數字範圍裡「抽籤」。

例如：

```python
print(random.randrange(7))
```

可能得到：

```text
0
1
2
3
4
5
6
```

⚠️ **7 不會被選到！**

---

## `randrange(開始, 結束)`

```python
random.randrange(1, 6)
```

可能得到：

```text
1、2、3、4、5
```

不會得到 `6`。

---

## `randrange(開始, 結束, 間隔)`

例如：

```python
random.randrange(1, 6, 2)
```

可能得到：

```text
1、3、5
```

格式：

```python
random.randrange(開始, 結束, 間隔)
```

---

# 6. 🎯 `random.randint()`

這個也非常重要：

```python
random.randint(1, 6)
```

它可以抽：

```text
1、2、3、4、5、6
```

### ⭐ 和 `randrange()` 最大的差別

```python
random.randrange(1, 6)
```

➡️ `1～5`

```python
random.randint(1, 6)
```

➡️ `1～6`

所以：

> 🎲 `randint()` 的**結束數字也可以被抽到**。

---

# 7. 🎯 1～100 猜數字遊戲

今天已經可以做出真正的小遊戲了！

```python
import random

answer = random.randint(1, 100)

low = 1
high = 100

print("🎯 Guess the Number!")

while True:
    print(f"Pick a number from {low} to {high}.")

    number = int(input())

    if number == answer:
        print("🎉 Correct!")
        break

    elif number < answer:
        print("⬆️ Higher!")
        low = number

    else:
        print("⬇️ Lower!")
        high = number
```

這裡一次用到了：

```text
🎲 random
🔁 while
🤔 if / elif / else
🛑 break
🧠 變數
📝 input
🔤 f-string
```

這就是把不同 Python 技能**組合起來**！🔥

---

# 8. 🌐 Streamlit 猜數字遊戲

今天還把猜數字遊戲做成了網頁版！

其中：

```python
ss = st.session_state
```

可以讓我們用比較短的方式使用：

```python
st.session_state
```

例如：

```python
if "ans" not in ss:
    ss.ans = random.randint(1, 100)
```

意思是：

> 如果還沒有答案，就隨機產生一個 1～100 的數字。

---

# 9. 🧠 `session_state` 的三個重要資料

今天的遊戲有：

```python
ss.ans
```

➡️ 🤫 正確答案

```python
ss.min_num
```

➡️ 🔽 目前最小數字

```python
ss.max_num
```

➡️ 🔼 目前最大數字

所以可以想成：

```text
🧠 session_state

ans     → 🤫 秘密答案
min_num → 🔽 最小範圍
max_num → 🔼 最大範圍
```

---

# 10. 🔢 `st.number_input()`

今天也用到了：

```python
st.number_input()
```

讓玩家輸入數字。

例如：

```python
num = st.number_input(
    "請輸入數字",
    min_value=1,
    max_value=100,
    step=1
)
```

意思是：

* `min_value` → 最小可以輸入多少
* `max_value` → 最大可以輸入多少
* `step` → 每次增加或減少多少

---

# 11. 🔄 `st.rerun()`

今天的程式最後有：

```python
st.rerun
```

⚠️ 這裡要注意！

如果你真的要**執行**重新整理，應該寫：

```python
st.rerun()
```

括號 `()` 很重要。

它的意思是：

> 🔄 重新執行 Streamlit 程式。

---

# 12. 📖 Dictionary 字典

今天開始學另一種非常重要的資料：

## `dict`

Dictionary 中文叫：

> 📖 **字典**

它不是用 index 找資料，而是用：

> 🔑 **key（鍵） → value（值）**

例如：

```python
d = {
    "a": 1,
    "b": 2,
    "c": 3
}
```

可以想成：

```text
🔑 key       💎 value

"a"    →      1
"b"    →      2
"c"    →      3
```

---

# 13. 🔑 Key 和 Value

### Key

就是：

> 🔑 找資料用的「名字」。

例如：

```text
"a"
"b"
"c"
```

### Value

就是：

> 💎 真正存放的資料。

例如：

```text
1
2
3
```

---

# 14. ⭐ Dictionary 的重要規則

### 🔑 Key 必須是唯一的

不能有兩個完全相同的 key。

### 💎 Value 可以重複

例如：

```python
d = {
    "apple": 10,
    "banana": 10
}
```

兩個 value 都是 `10` 沒問題。

### 📦 Value 可以放很多不同東西

Value 可以是：

* 整數
* 小數
* 字串
* List
* 另一個 Dictionary
* 等等

---

# 15. 🔍 取得 Dictionary 的 Keys

使用：

```python
d.keys()
```

例如：

```python
print(d.keys())
```

可以取得所有 key。

也可以用 `for`：

```python
for key in d.keys():
    print(key)
```

---

# 16. 💎 取得 Values

使用：

```python
d.values()
```

例如：

```python
for value in d.values():
    print(value)
```

就會一個一個取得 value。

---

# 17. 🔑💎 同時取得 Key 和 Value

使用：

```python
d.items()
```

例如：

```python
for key, value in d.items():
    print(key, value)
```

就可以同時拿到：

```text
key   value
 a      1
 b      2
 c      3
```

---

# 18. ➕ 新增 Dictionary 資料

例如：

```python
d["d"] = 4
```

就會新增：

```text
"d" → 4
```

---

# 19. ✏️ 修改 Dictionary 資料

如果 key 已經存在：

```python
d["a"] = 5
```

就不是新增，而是：

> ✏️ 把原本 `"a"` 的 value 改成 `5`。

例如：

```text
原本：
"a" → 1

修改後：
"a" → 5
```

---

# 20. 🗑️ `pop()` 刪除 Dictionary 資料

例如：

```python
d.pop("a")
```

意思：

> 把 key `"a"` 的資料刪掉。

而且會回傳被刪掉的 value。

---

## 🛡️ 如果 key 不存在

可以給一個「找不到時要顯示的東西」：

```python
d.pop("e", "not found")
```

如果沒有 `"e"`：

```text
not found
```

這樣比較安全。

---

# 21. 🔍 `in`：檢查有沒有這個 Key

例如：

```python
print("a" in d)
```

如果有：

```text
True
```

如果沒有：

```text
False
```

### ⚠️ Dictionary 的 `in`

主要是檢查：

> 🔑 **Key**

不是檢查 value。

---

# 22. 📦 List 和 Dictionary 的 `in`

這個要特別記！

List：

```text
📦 List → 用 index 找位置
```

Dictionary：

```text
📖 Dict → 用 key 找資料
```

所以兩個的概念不一樣。

---

# 23. 🧩 Dictionary 裡面還可以放 List 和 Dictionary

這就是今天比較進階的部分。

例如：

```python
d = {
    "a": [1, 2, 3],
    "b": {
        "c": 4,
        "d": 5
    }
}
```

這可以想成：

```text
📖 Dictionary
│
├── 🔑 a
│    └── 📦 [1, 2, 3]
│
└── 🔑 b
     └── 📖 Dictionary
          ├── c → 4
          └── d → 5
```

---

# 24. 🔍 一層一層找資料

```python
d["a"]
```

得到：

```text
[1, 2, 3]
```

再：

```python
d["a"][0]
```

得到：

```text
1
```

因為：

```text
d["a"] → [1, 2, 3]
             ↑
           index 0
```

---

## Dictionary 裡的 Dictionary

```python
d["b"]
```

得到：

```python
{"c": 4, "d": 5}
```

再：

```python
d["b"]["c"]
```

得到：

```text
4
```

就是：

> 🔑 先找 `b` → 再找 `c`。

---

# 25. 🏫 成績登記系統

今天做了一個很厲害的例子：

```python
grade = {
    "小明": {
        "國文": [90, 80, 70],
        "數學": [85, 75, 65],
        "英文": [95, 85, 75]
    },

    "小美": {
        "國文": [88, 78, 68],
        "數學": [83, 73, 63],
        "英文": [93, 83, 73]
    }
}
```

這個結構可以想成：

```text
🏫 成績系統
│
├── 👦 小明
│    ├── 國文 → 📦 [90,80,70]
│    ├── 數學 → 📦 [85,75,65]
│    └── 英文 → 📦 [95,85,75]
│
└── 👧 小美
     ├── 國文 → 📦 [88,78,68]
     ├── 數學 → 📦 [83,73,63]
     └── 英文 → 📦 [93,83,73]
```

這就是：

> 📖 Dictionary 裡面有 Dictionary，裡面又有 List！

---

# 26. 🧮 計算平均

例如小明的國文：

```python
chinese = [90, 80, 70]
```

使用：

```python
sum(chinese)
```

得到：

```text
240
```

再：

```python
len(chinese)
```

得到：

```text
3
```

所以：

```python
avg = sum(chinese) / len(chinese)
```

就是：

```text
240 ÷ 3 = 80
```

---

# 27. 🔢 `:.2f`

今天看到：

```python
f"{avg:.2f}"
```

這是用來控制小數位數。

`.2f` 意思是：

> **顯示小數點後 2 位。**

例如：

```text
80
```

可能顯示成：

```text
80.00
```

---

# 28. 🖼️ Streamlit 顯示圖片

今天也開始玩圖片了！

```python
st.image("image/apple.png", width=300)
```

意思是：

> 🖼️ 把指定路徑的圖片顯示在網頁上。

`width=300`：

> 📏 把圖片寬度設定成 300。

---

# 29. 📁 `os.listdir()`

今天還用了：

```python
import os
```

然後：

```python
image_files = os.listdir(image_folder)
```

它可以：

> 📁 找出資料夾裡有哪些檔案。

例如資料夾：

```text
image/
├── apple.png
├── banana.png
└── cat.png
```

使用：

```python
os.listdir("image")
```

可能得到：

```python
["apple.png", "banana.png", "cat.png"]
```

---

# 30. 🖼️ 用 `for` 一次顯示很多圖片

這裡把今天學的東西全部串起來了：

```python
for image_file in image_files:
    st.image(f"{image_folder}/{image_file}", width=image_size)
```

意思：

> 📁 把資料夾裡每一張圖片拿出來，然後顯示。

可以想成：

```text
📁 image
 │
 ├── 🍎 apple.png
 ├── 🍌 banana.png
 └── 🐱 cat.png
       │
       ▼
     🔁 for
       │
       ▼
   🖼️ 一張一張顯示
```

---

# 31. 📏 使用者控制圖片大小

今天還讓使用者自己選圖片大小：

```python
image_size = st.number_input(
    "請輸入圖片大小",
    min_value=50,
    max_value=500,
    step=50,
    value=100
)
```

所以使用者可以選：

```text
50
100
150
200
...
500
```

然後：

```python
st.image(..., width=image_size)
```

就會根據使用者輸入的大小顯示。

這就是：

> 🧑‍💻 **讓使用者控制程式！**

---

# 32. 🖼️ `use_container_width=True`

也可以：

```python
st.image(
    f"{image_folder}/{image_file}",
    use_container_width=True
)
```

意思是：

> 🖼️ 讓圖片盡量使用目前網頁容器的寬度。

---

# 33. ✅ `st.success()`

最後還學到了：

```python
st.success("購買成功")
```

它會在網頁上顯示一個成功訊息。

可以拿來做：

```text
✅ 購買成功
✅ 登入成功
✅ 遊戲成功
```

等等。

---

# 🧠 今日 Python 技能樹更新！

你之前的技能樹：

```text
🐍 Python 小遊戲
       │
       ├── 🌐 Streamlit
       ├── 🤔 if / elif / else
       ├── 🔁 for
       └── 📦 List
```

今天可以升級成：

```text
                 🐍 Python 小遊戲
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
      🌐 Streamlit                  🐍 Python
          │                           │
    ┌─────┼──────┐             ┌──────┼──────┐
    ▼     ▼      ▼             ▼      ▼      ▼
   🔘    📝     🖼️             🔁     🎲     📖
  Button Input  Image          while  random  Dict
    │                           │
    ▼                           ▼
 balloons                    🛑 break
 snow
 columns
 session_state
 rerun
    │
    ▼
  🤔 判斷
    │
 if / elif / else
    │
    ▼
  📦 List
    │
 append / remove / sort / pop
    │
    ▼
  📖 Dictionary
    │
 ┌──┼──────────────┐
 ▼  ▼       ▼      ▼
keys values items  pop
    │
    ▼
 🧩 巢狀資料
 Dict → Dict → List
```

# 🏆 今天最重要的 10 個重點

| ⭐  | 指令 / 概念        | 簡單意思               |
| -- | -------------- | ------------------ |
| 1  | `while`        | 條件是 True 就一直做      |
| 2  | `break`        | 直接離開迴圈             |
| 3  | `random`       | 讓 Python 隨機選東西     |
| 4  | `randrange()`  | 在範圍中隨機選數字，結束值不包含   |
| 5  | `randint()`    | 在範圍中隨機選整數，結束值包含    |
| 6  | `dict`         | 用 Key → Value 儲存資料 |
| 7  | `keys()`       | 取得所有 Key           |
| 8  | `values()`     | 取得所有 Value         |
| 9  | `items()`      | 同時取得 Key 和 Value   |
| 10 | `os.listdir()` | 找出資料夾裡有哪些檔案        |

## 🚀 今天最大的進步

你現在已經可以把：

**🎲 random + 🔁 while + 🤔 if + 📖 dict + 📦 list + 🌐 Streamlit + 🖼️ 圖片**

全部組合在一起。

這已經不是只會「印出 Hello World」的程度了 😂

你現在已經開始進入：

> 🎮 **Python 小遊戲 + 🌐 網頁程式 + 📊 資料處理**

的階段！🐍🔥

    '''


with st.expander("課堂筆記 CLASS 5"):
    '''
    # 🐍 Python 今日課程筆記

## 🛒 購物平台 + 🤖 AI 聊天機器人

今天的課程超級重要！🎉
因為你開始把以前學過的：

**Dictionary 📖 + List 📦 + Streamlit 🌐 + Button 🔘 + Session State 🧠 + AI 🤖**

全部組合起來，做出真正的**購物網站和 AI 聊天機器人**！

---

# 🛒 第一部分：Python 購物平台

## 1. 📖 用 Dictionary 存商品資料

今天的商品資料長這樣：

```python
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
    }
}
```

可以把它想成一間商店：

```text
🛒 商店
│
├── 🍎 apple
│   ├── 🖼️ 圖片
│   ├── 💰 價格
│   └── 📦 庫存
│
└── 🍊 orange
    ├── 🖼️ 圖片
    ├── 💰 價格
    └── 📦 庫存
```

每個商品都是一個 Dictionary。

---

# 2. 🧩 Dictionary 裡面放 Dictionary

例如：

```python
products["apple"]
```

可以得到：

```python
{
    "image": "image/apple.png",
    "price": 10,
    "stock": 10
}
```

再往裡面找：

```python
products["apple"]["price"]
```

就是：

```text
10
```

所以：

```python
products["apple"]["stock"]
```

就是：

```text
10
```

📌 記住：

```text
products
   ↓
"apple"
   ↓
"stock"
   ↓
10
```

---

# 3. 🧠 `session_state`

今天再次使用：

```python
st.session_state
```

它可以想成：

> 🧠 **Streamlit 的記憶盒子**

例如：

```python
if "products" not in st.session_state:
    st.session_state.products = products
```

意思是：

> 如果記憶盒裡還沒有 `products`，就把商品資料放進去。

---

## 為什麼需要它？

Streamlit 按下按鈕後，程式會重新執行。

如果沒有 `session_state`：

```text
買了一個蘋果
     ↓
程式重新執行
     ↓
🍎 庫存又變回 10 😱
```

有了 `session_state`：

```text
買了一個蘋果
     ↓
🧠 記住庫存
     ↓
🍎 10 → 9
```

所以：

> `session_state` = 🧠 **讓 Streamlit 記住資料**

---

# 4. 🏷️ `st.title()`

```python
st.title("購物平台")
```

就是在網頁上顯示：

# 購物平台

它適合用來做大標題。

---

# 5. 🔢 `st.number_input()`

```python
number = st.number_input(
    "請輸入欄位個數",
    min_value=1,
    max_value=5,
    step=1,
    value=4
)
```

讓使用者輸入數字。

這裡：

| 指令          | 意思     |
| ----------- | ------ |
| `min_value` | 最小值    |
| `max_value` | 最大值    |
| `step`      | 每次增加多少 |
| `value`     | 預設值    |

所以：

```python
min_value=1
max_value=5
```

代表：

> 可以選 1～5。

---

# 6. 📊 `st.columns()`

今天學到很重要的：

```python
columns = st.columns(number)
```

它可以把網頁切成幾個欄位。

例如：

```python
st.columns(2)
```

會變成：

```text
┌──────────┬──────────┐
│  欄位 1  │  欄位 2  │
└──────────┴──────────┘
```

如果：

```python
st.columns(4)
```

就是：

```text
┌────┬────┬────┬────┐
│ 1  │ 2  │ 3  │ 4  │
└────┴────┴────┴────┘
```

這非常適合拿來做：

> 🛒 商品排列

---

# 7. 📋 `list()`

今天看到：

```python
product_names = list(st.session_state.products.keys())
```

我們之前學過：

```python
products.keys()
```

可以取得所有商品的 Key。

例如：

```text
apple
orange
bg
banana
```

再使用：

```python
list()
```

把它變成 List。

結果：

```python
["apple", "orange", "bg", "banana"]
```

所以：

```text
Dictionary 🔑
     ↓
keys()
     ↓
list()
     ↓
📦 List
```

---

# 8. 🔁 `enumerate()`

今天看到：

```python
for i, name in enumerate(product_names):
```

`enumerate()` 可以讓我們一次得到：

> 🔢 編號 + 📦 資料

例如：

```python
fruits = ["apple", "banana", "orange"]
```

使用：

```python
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

結果：

```text
0 apple
1 banana
2 orange
```

所以：

```text
i       → 🔢 編號
name    → 🏷️ 商品名稱
```

---

# 9. 🛑 `break`

今天購物平台也使用：

```python
if i >= number:
    break
```

意思是：

> 如果商品數量已經超過我們設定的欄位數，就停止。

例如只有 2 個欄位：

```text
📊 欄位

🍎 apple     🍊 orange

第三個商品？
❌ 不顯示
```

---

# 10. 🖼️ 商品圖片

```python
st.image(
    product["image"],
    use_container_width=True
)
```

從商品 Dictionary 裡拿出：

```python
product["image"]
```

得到圖片位置。

然後用 `st.image()` 顯示。

---

# 11. 💰 商品價格

```python
st.write(f"price: {product['price']}")
```

如果價格是：

```python
10
```

就會顯示：

```text
price: 10
```

---

# 12. 📦 商品庫存

```python
st.write(f"left: {product['stock']}")
```

例如：

```text
left: 10
```

就是：

> 還剩 10 個。

---

# 13. 🔘 購買按鈕

```python
if st.button(f"buy {name}", key=f"buy_{name}"):
```

如果商品是 apple：

```text
🔘 buy apple
```

按下去後就會執行 `if` 裡面的程式。

---

# 14. 📦 庫存減少

這一行超重要：

```python
product["stock"] -= 1
```

它等於：

```python
product["stock"] = product["stock"] - 1
```

例如：

```text
原本：
📦 10

買一個：

📦 9
```

---

# 15. 🚫 判斷有沒有庫存

```python
if product["stock"] > 0:
```

意思：

> 如果庫存大於 0，就可以購買。

如果沒有：

```python
else:
    st.session_state.message = "庫存不足！"
```

就顯示：

```text
❌ 庫存不足！
```

---

# 16. ✅ `st.success()`

```python
st.success("購買成功！")
```

會顯示成功訊息：

```text
✅ 購買成功！
```

例如：

```python
st.success("新增庫存成功！")
```

就是：

```text
✅ 新增庫存成功！
```

---

# 📦 第二部分：新增商品庫存

今天還做了「補貨」功能！

---

# 17. 🔽 `st.selectbox()`

```python
selected_product = st.selectbox(
    "選擇商品",
    product_names
)
```

它會產生一個下拉選單。

例如：

```text
選擇商品 ▼

🍎 apple
🍊 orange
🍌 banana
```

使用者可以選一個商品。

---

# 18. ➕ 增加庫存

```python
st.session_state.products[selected_product]["stock"] += add_stock
```

這一行看起來很長，但拆開就很簡單：

```text
🧠 session_state
     ↓
products
     ↓
選擇的商品
     ↓
stock
     ↓
➕ add_stock
```

例如：

```text
🍎 apple
原本：10

新增：5

結果：15
```

---

# 🤖 第三部分：真正的 AI

今天開始學：

> 🤖 **Python + AI**

使用：

```python
import openai
```

就是把 OpenAI 的功能匯入 Python。

---

# 19. 🔐 `.env`：保護 API Key

今天用了：

```python
from dotenv import load_dotenv
import os

load_dotenv()
```

然後：

```python
openai.api_key = os.getenv("OPENAI_API_KEY")
```

可以把秘密的 API Key 放在環境變數裡。

### ⚠️ 非常重要

API Key 就像：

> 🔑 **AI 帳號的鑰匙**

不要把自己的 API Key 放在公開的 GitHub 或直接貼給別人。

---

# 20. 🤖 `openai.chat.completions.create()`

這是讓 Python：

> 📩 把問題送給 AI。

例如：

```python
response = openai.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": user_input
        }
    ]
)
```

可以想成：

```text
👤 你
  │
  │ 問問題
  ▼
🐍 Python
  │
  │ API
  ▼
🤖 AI
  │
  │ 回答
  ▼
🐍 Python
  │
  ▼
👤 你
```

---

# 21. 🧑‍💻 `role`

AI 對話裡有不同角色。

### `user`

```python
{"role": "user", "content": user_input}
```

代表：

> 👤 使用者說的話。

### `assistant`

```python
{"role": "assistant", "content": assistant_response}
```

代表：

> 🤖 AI 說的話。

### `system`

```python
{
    "role": "system",
    "content": "請用繁體中文進行後續對話"
}
```

代表：

> ⚙️ 給 AI 的規則或指示。

---

# 22. 🧠 AI 的聊天記憶

一開始：

```python
messages = [
    {
        "role": "system",
        "content": "請用繁體中文進行後續對話"
    }
]
```

然後使用者說話：

```python
messages.append({
    "role": "user",
    "content": user_input
})
```

AI 回答：

```python
messages.append({
    "role": "assistant",
    "content": assistant_response
})
```

所以 `messages` 會越來越長：

```text
📦 messages

👤 你好
🤖 你好！有什麼可以幫你？

👤 我叫 Paul
🤖 很高興認識你！

👤 我叫什麼？
🤖 你叫 Paul。
```

這就是：

> 🧠 **聊天記憶**

---

# 23. 📦 `append()`

今天再次使用：

```python
messages.append(...)
```

`append()` 的意思是：

> ➕ 把新的東西放到 List 最後面。

例如：

```python
a = []

a.append("Hello")
a.append("Hi")
```

結果：

```python
["Hello", "Hi"]
```

---

# 24. 🚪 `exit` 和 `quit`

今天的 AI 程式有：

```python
if user_input.lower() in ["exit", "quit"]:
    break
```

意思是：

如果使用者輸入：

```text
exit
```

或：

```text
quit
```

就：

```python
break
```

離開 `while`。

也就是：

> 🚪 輸入 exit / quit → 結束聊天。

---

# 25. 🔤 `.lower()`

```python
user_input.lower()
```

可以把英文變成小寫。

例如：

```text
EXIT
Exit
eXiT
```

都會變成：

```text
exit
```

所以程式比較容易判斷。

---

# 🌐 第四部分：把 AI 做成 Streamlit 網頁

今天最酷的部分！

你不只是做 Terminal AI，而是把它變成：

> 🌐 **網頁版 AI 聊天室**

---

# 26. 💬 `st.chat_input()`

```python
prompt = st.chat_input("請輸入想對話的訊息")
```

會在網頁下面產生聊天輸入框。

使用者可以輸入：

```text
┌──────────────────────────┐
│ 請輸入想對話的訊息       │
└──────────────────────────┘
```

---

# 27. 💬 `st.chat_message()`

```python
st.chat_message("user")
```

代表：

> 👤 使用者的聊天訊息。

```python
st.chat_message("assistant")
```

代表：

> 🤖 AI 的聊天訊息。

所以可以做出：

```text
👤 你好！

              🤖 哈囉！你好！
```

很像真正的 ChatGPT！🔥

---

# 28. 🧹 清除聊天紀錄

今天有：

```python
if st.button("🗑️"):
    ss.history = []
    st.rerun()
```

按下垃圾桶：

```text
🗑️
 ↓
📦 history 清空
 ↓
🔄 網頁重新執行
 ↓
💬 聊天紀錄消失
```

---

# 29. ⚙️ 可以選擇 AI 模型

今天使用：

```python
st.selectbox(
    "AI模型",
    ["gpt-4o-mini", "gpt-4", "gpt-4o-searcher-preview"]
)
```

這樣使用者可以從下拉選單選擇模型。

概念是：

```text
🤖 AI模型 ▼

gpt-4o-mini
gpt-4
其他模型
```

⚠️ 實際能不能使用某個模型，要看你的 API 帳號目前有哪些模型可以使用。

---

# 30. ⚙️ System Message

今天還可以讓使用者自己修改：

```python
ss.system_message = st.text_input(
    "系統提示",
    ss.system_message
)
```

例如輸入：

```text
你是一個很搞笑的 AI
```

AI 就會收到這個規則。

所以：

> `system_message` = 🧠 **告訴 AI「你應該怎麼回答」的規則**

---

# 🧠 今日超級重點

今天其實學了兩個大型專案。

## 🛒 購物平台

```text
                 🛒 購物平台
                      │
             ┌────────┴────────┐
             ▼                 ▼
        📖 Dictionary       🌐 Streamlit
             │                 │
       ┌─────┼─────┐      ┌────┼────┐
       ▼     ▼     ▼      ▼    ▼    ▼
     商品   價格  庫存   Button Image 欄位
                         │
                         ▼
                       🛒 購買
                         │
                         ▼
                    📦 stock - 1
                         │
                         ▼
                    🧠 session_state
```

---

## 🤖 AI 聊天機器人

```text
                  🤖 AI
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
    🐍 Python              🌐 Streamlit
        │                     │
        ▼                     ▼
   OpenAI API            chat_input
        │                     │
        ▼                     ▼
     AI 模型              chat_message
        │                     │
        └──────────┬──────────┘
                   ▼
               📦 history
                   │
                   ▼
                🧠 記憶
```

---

# 🏆 今天的技能表

| 🧠 東西               | 📚 你學到什麼            |
| ------------------- | ------------------- |
| `Dictionary`        | 儲存商品資料              |
| `List`              | 儲存聊天紀錄              |
| `keys()`            | 找商品名稱               |
| `list()`            | 把資料變成 List          |
| `enumerate()`       | 同時取得編號和資料           |
| `append()`          | 新增聊天紀錄              |
| `if / elif / else`  | 判斷購買和 AI 指令         |
| `break`             | 結束迴圈                |
| `session_state`     | 🧠 讓 Streamlit 記住資料 |
| `st.columns()`      | 📊 建立商品欄位           |
| `st.selectbox()`    | 🔽 下拉選單             |
| `st.number_input()` | 🔢 輸入數字             |
| `st.button()`       | 🔘 按鈕               |
| `st.chat_input()`   | 💬 AI 輸入框           |
| `st.chat_message()` | 💬 顯示聊天             |
| `st.success()`      | ✅ 成功訊息              |
| `st.rerun()`        | 🔄 重新執行網頁           |
| `openai`            | 🤖 連接 AI            |
| `messages`          | 🧠 保存 AI 對話         |
| `system`            | ⚙️ 告訴 AI 回答規則       |
| `user`              | 👤 使用者訊息            |
| `assistant`         | 🤖 AI 訊息            |
| `.env`              | 🔐 保護 API Key       |

---

# 🚀 你現在的 Python 技能樹

```text
                         🐍 PYTHON
                            │
          ┌─────────────────┴─────────────────┐
          ▼                                   ▼
       🎮 小遊戲                           🌐 網頁
          │                                   │
     ┌────┼────┐                    ┌─────────┼─────────┐
     ▼    ▼    ▼                    ▼         ▼         ▼
   🔁    🎲   🤔                  Button    Input    Columns
  while random if                  │         │         │
     │                             ▼         ▼         ▼
   break                       🛒 購物平台  💬 聊天   📊 排版
                                   │
                                   ▼
                              🧠 session_state
                                   │
                    ┌──────────────┴──────────────┐
                    ▼                             ▼
                 📦 List                      📖 Dict
                    │                             │
              append()                    keys / values
                                                │
                                                ▼
                                          🛒 商品資料
                                                │
                                                ▼
                                             🤖 AI
                                                │
                                          OpenAI API
                                                │
                                                ▼
                                          💬 AI 聊天
```

🎉 **這代表你現在已經開始學「把很多 Python 知識組合成完整的程式」了！**
從 `print()`、變數、`if`、`for`、List，一路到現在的 **購物平台 + AI 聊天機器人**，進步非常大。 🐍🔥

    '''
