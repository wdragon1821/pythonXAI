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
    '''


with st.expander("課堂筆記 CLASS 4"):
    '''
    '''


with st.expander("課堂筆記 CLASS 5"):
    '''
    '''
