# -*- coding: utf-8 -*-
# （1）函数仅作为求根公式，判断德尔塔的步骤由其他的代码完成

# 函数定义部分（函数只负责求根公式）


def solution(a, b, c):
    import math
    delta = b**2 - 4*a*c
    s1 = (-b + math.sqrt(delta)) / (2*a)
    s2 = (-b - math.sqrt(delta)) / (2*a)
    return s1, s2


# 求解步骤（在求解步骤中判断解的情况）
print("请根据提示输入一元二次方程的相关系数")
a0 = input("a=")
b0 = input("b=")
c0 = input("c=")
# 将输入的字符型数据转换为整型数据
a = int(a0)
b = int(b0)
c = int(c0)

d = b**2 - 4*a*c
if d < 0:
    print("无实数解")
elif d == 0:
    print("有两个相同的解")
    (x1, x2) = solution(a, b, c)
    print("x1=x2=", x1)
elif d > 0:
    print("有两个不同的解")
    (x1, x2) = solution(a, b, c)
    print("x1=", x1)
    print("x2=", x2)
print("求解完成")
