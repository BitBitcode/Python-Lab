# 定义一个计算n次方的函数
def power(x, n):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s