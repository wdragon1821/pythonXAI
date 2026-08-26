#list列表
#建立列表
a = [10, 20, 30]


#建立空列表
b = []


#列表內可以放不同雌料型態
c = [10, "hello", 3.14]



me = ["Paul", 12, 11.9, False]



fruits = ["apple", "banana", "cherry"]
#取單一值
print(fruits[0])  #apple
#印出整個列表
print(fruits)  #['apple', 'banana', 'cherry']





a = [90, 50, 20, 80, 70]
print(a[0])




a = [1, 2, 3, 4]
a.append(5) #append() 將元素新增到列表最後
print(a)





number = [2, 4, 6, 8]
number.remove(4) #remove() 將指定元素從列表中移除
print(number) #[2, 6, 8]



#sort() 將列表中的元素進行排序，預設為升序排列
#注意：sort() 方法會直接修改原始列表，不會產生新的列表
numbers = [5, 2, 9, 1, 7]
numbers.sort() #升序排列
print(numbers) #[1, 2, 5, 7, 9]





#list 取長度，也就是list中有幾個元素，不是index的最大值
a = [1, 2, 3, "a", "b", "c"]
print(len(a)) #6

#使用pop，可以移除指定的index的元素，並回傳該元素
a = [1, 2, 3, "a", "b", "c"]
a.pop(0) #移除index 0的元素，也就是1
#代表pop會移除指定index的元素
#如果不指定index，pop()會移除最後一個元素
a.pop() #移除最後一個元素，也就是"c"
print(a) #[2, 3, 'a', 'b']




#list走往元素
#可以透過取得index的方式來找到list中的元素
#也可以直接把list的元素取出來使用
#這兩種方式都可以，但是看使用的情況而定，哪一種方式比較方便
a = [1, 2, 3, "a", "b", "c"]
for i in range(0, len(a), 2):
    print(a[i]) 

for i in a:
    print(i)

a = ["f", "e", "d", "a", "b", "c",]
#如果想要移除所有符合的元素，可以使用迴圈
for i in a:
    if i == "a":
        a.remove(i)