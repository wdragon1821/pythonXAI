# for 迴圈
#for 會搭配in 來使用 ， in 後面接一個有範圍的東西
#range(5) 會產生一個數列，從0開始到4結束 ， 不包含 5
# i 是迴圈的變數可以自己取名
#迴圈變數每回合會從範圍裡面取出一個雌料出來
for i in range(5):
    print(i)


#range可以設定起始值與結束直， 不包含結束直
#range(1, 5) 會產生 1, 2, 3, 4
for i in range(1, 5):
    print(i)

# range 可以設定起始值、結束值與步長， 不包含結束值
# range(1, 10, 2) 會產生 1, 3, 5, 7, 9
for i in range(1, 10, 2):
    print(i)


for i in range(5):
   a = i * 2    # i * 2 的結果會存入 a
print(a)    #在終端機顯示 a 的值
