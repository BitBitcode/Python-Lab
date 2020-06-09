#【定义固定数量的元素】
a = [0,0,0,0,0]
# 输入
i = 0
while(i < 5):
    a[i] = int(input("a[%d] = " %i))
    i = i + 1
# 输出
i = 0
while(i < 5):
    print("a[%d] = " %i  + "%d" %a[i])
    i = i + 1

print("\n")


#【定义可变数量的元素】
a = []
i = 0
n = int(input("请输入元素个数："))
while(i < n):
    a.append(int(input("a[%d] = " %i)))
    i = i + 1
print(a)
