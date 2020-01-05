# -*- coding: utf-8 -*-
#（3）函数集成了判断德尔塔和求解的全部步骤，但函数的写法有所不同

#函数定义部分（函数负责判断解的情况以及求解数值）


def solution(a, b, c):
    import math
    delta = b**2 - 4*a*c

    if delta < 0:
        print("该方程无实根")
    elif delta == 0:
        x = (-b) / 2*a
        print("有两个相等的实数解：")
        return x
    elif delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("有两个不同的实数解：")
        return x1, x2


#求解部分，可以学习借鉴一下两个函数嵌套，简化代码
a = float(input('输入a的数值'))
b = float(input('输入b的数值'))
c = float(input('输入c的数值'))
x = solution(a, b, c)
print(x)

#这种写法中，“solution”函数相当于“半功能型函数”,
#函数本身有很多判断步骤，相当于“功能型”的部分，
#而函数的返回值也被用到了，最后解的数值是return给出的
#只不过如果调用函数的时候如果不加入“x=solution; print(x)”，或者“print(solution(a,b,c))”，
#就得不到解的数值，只能实现函数中判断的部分，所以这种写法实际上并不提倡
