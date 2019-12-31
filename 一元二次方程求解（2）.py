# -*- coding: utf-8 -*-
#（2）函数集成了判断德尔塔和求解的全部步骤

#函数定义部分（函数负责判断解的情况以及求解数值）
def solution(a,b,c):
    import math
    delta = b**2 - 4*a*c
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    
    if delta<0:
        print("该方程无实根")
    elif delta==0:
        print("有两个相等的实数解:x1=x2=%s" %(x1))
        return
    elif delta>0:
        print("有两个不同的实数解：x1=%s, x2=%s" %(x1,x2))
        return

#求解部分（仅负责获取用户输入的参数）
print("请根据提示输入一元二次方程的相关系数")
a0 = input("a=")
b0 = input("b=")
c0 = input("c=")
# 将输入的字符型数据转换为整型数据
a = int(a0)
b = int(b0)
c = int(c0)
solution(a,b,c)

#这种写法中，函数“solution(a,b,c)” 是一个“功能型”函数，
#它虽然有输入值，看起来也有输出值，但其实输出值是由print函数实现的，
#return的值即便不是None，在最后的调用阶段也没有调用到返回值