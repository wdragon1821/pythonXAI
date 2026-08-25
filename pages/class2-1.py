#比較運算子
print(1 == 1)   #True
print(1 != 1)   #False
print(1 > 1)    #False
print(1 < 1)    #False
print(1 >= 1)   #True
print(1 <= 1)   #True

# 邏輯運算子
#and 運算子，只要有一個條件為false，結果就會是false
print(True and True)   #True
print(True and False)  #False
print(False and False) #False
print(True or True)    #True
print(True or False)   #True
print(False or False)  #False
print(not True)        #False
print(not False)       #True



#or 運算子，只要有一個條件為true，結果就會是true
print(True or True)    #True
print(True or False)   #True
print(False or False)  #False
print(False or True)   #True



#not 運算子
print(not True)     #False
print(not False)    #True





#密碼門檢查
password = input("pls input codeword")
if password == "1234":
    print("welcome Jeffrey")
elif password =="5678":
    print("welcome Tim")
elif password == "0000":
    print("welcome Chole")
else:
    print("codeword wrong")


#連續使用if跟使用if elif else的差別
#elif可以排除前面有判斷過的條件，所以縮短判斷條件的複雜度，也節省時間
#但是如果是使用多個if來獨立判斷，則每個if都會被執行，所以效率較低