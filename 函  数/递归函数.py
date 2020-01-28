# 定义一个递归函数 fact()，其中最后一句 “return n * fact(n - 1)” 调用了它自己
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

print("输入要求的数字")
num = input()

num = int(num)
result = fact(num)

print("\n")
print("计算结果为：%d! = %d" % (num, result))
