print("楊博翔")
print("604")
print("不要低頭\n雙下巴會出來")



"""這是多行註解"""

#這是單行註解
print("Hello World!") #print是在終端機顯示文字的指令
# control + / 可以快速註解或取消註解




#基本型態
print(1)    #int整數            12345
print(1.5)  #float浮點數            ?.?   ??.?
print("1")  #str字串            "?" '?'
print("apple")  #str字串        "?" '?'
print(True) #bool布林值         true/false




#變數
a = 1           #新增一個儲存空間並取名為a "＝"的功能是將右邊的值10存入左邊a
print(a)        #在終端機顯示a所存的值
a = "apple"     #將a的值改為"apple"
print(a)        #在終端機顯示a所存的值





#運算子
print(1 + 1)        #整數加法運算（兩邊都是整數）
print(1 - 1)        #整數減法運算（兩邊都是整數）
print(1 * 1)        #整數乘法運算（兩邊都是整數）
print(1 / 1)        #整數除法運算（兩邊都是整數）
print(1 // 1)       #整數取商
print(1 % 1)        #整數取餘數
print(2 ** 3)       #整數次方


# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減





#字串運算
print("apple" + "pen")#字串加法
print("apple " * 3) #字串乘法




num = 30
item = "book"
print(f"a {item} is {num}$")



#字串格式化
name = "apple"
age = 18
print(f"Hello, my name is {name}, I'm {age} years old.")
#可以將變數或其他類型的資料型態的資料放到f字串裡面的{}，這樣就可以在字串顯示





#型態轉換
print(int(1.0))     # float into int
print(float(1))     #int to float
print(str(1))       #int to str
print(bool(1))      #int to bool
print(int(1.234))       #float to int
print(float("1.234"))     #str to float
print(str(1.234))       #float to str
print(bool(1.234))      #float to bool
#print(int("hello"))    這行會報錯，因為字串裡面如果有非數字的元數，無法換成數字





'''print("輸入開始")
#input()是一個方法，可以讓使用者輸入文字
#()裡面的文字是提示訊息會先顯示在終端機才會等待輸入
#input()預設輸入內容都是字串
a = input("請輸入一些文字：")
print("輸入結束")
print(int(a) + 10)
print(type(a))  #證明透過input()輸入內容都是字串'''




half = input("請輸入半徑：")
print(int(half) * int(half) * 3.14)
