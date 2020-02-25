#-*- coding: utf-8 -*-

# 自己练习研究
print("自己练习研究")
i = 3
if i>5: 
    print("1")  # 冒号后不能没有缩进的代码，如果不缩进，则本行错误
    print("缩进")
    print("正常") # 不缩进的行出现代表if判断后执行的代码已经结束，不能再有缩进的代码，如果不缩进，则本行错误
print("Kiana") # 不缩进的代码相当于 else ...

#（1）if的基础功能
print("（1）if的基础功能")
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
# 根据Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做。

#（2）if...else...
print("（2）if...else...")
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')
# 如果if判断是False，不要执行if的内容，去把else执行了

#（3）elif实现多个分支
print("（3）elif实现多个分支")
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

#（4）input输入后转换数据类型的问题
print("（4）input输入后转换数据类型的问题")
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')
# 因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情

#（5）BMI指数计算
print("（5）BMI指数计算")
w = input("请输入体重（/kg）：")
h = input("请输入身高（/cm）：")
weigh = int(w)
high = int(h)

#BMI计算方法：体重除以身高的平方
BMI = weigh/((high/100)*2)
print("你的BMI指数为：",BMI)
if BMI<=18.5 :
    print("属于：过轻")
elif BMI>18.5 and BMI<=25:
    print("属于：正常")
elif BMI>25 and BMI<=28:
    print("属于：过重")
elif BMI>28 and BMI<=32:
    print("属于：肥胖")
else:
    print("属于：过度肥胖")