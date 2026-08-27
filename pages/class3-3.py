#while 回圈
#while會搭配一個條件
#條件式為 True 時會一直執行回圈
#如果條件式為 False 時就會停止執行
#每次回圈執行完都會重新檢查條件有沒有變成 False
i = 0 
while i < 5: 
    print(i) 
    i += 1 #i = i + 1



#break 可以跳出回圈
i = 0
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1 # 跳出回圈 屬於while回圈



for i in range(5):
    print(i)
    if i == 3:
        break # 跳出回圈








import random #匯入random模組


#random.randrange() 設定抽籤範圍的方式跟range()一樣
print(random.randrange(7)) #0 - 6
print(random.randrange(1, 6)) #1 - 5
print(random.randrange(1, 6, 2)) #1 - 5 間隔為2

#random.randrange(開始數字, 結束數字, 間隔)
#結束包含
print(random.randint(1, 6)) #1 - 6