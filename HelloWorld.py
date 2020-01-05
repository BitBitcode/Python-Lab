# -*- coding: utf-8 -*-
# 分隔符
print("--------------------------------------------------")

# 在屏幕上显示字符串的示例：
print("你好Hello World")

# 通过将字符串赋值给变量，利用 print 函数显示变量内容的示例
msg = "Hello world !"
print(msg)

# 利用“,”依次输出多个字符串，逗号将输出为空格
print("hello", "world")
# 注意：如果输出的都是字符串，则两个"",""中间的逗号可以省略，否则不能省略（如其中一个是变量时）

# 利用“,”输出字符串和变量，变量不加引号
ans = 600+300
print("300 + 600 =", ans)

# 分隔符
print("--------------------------------------------------")

# 获取用户输入的内容
print("Enter your name:")
name = input()
print(name, "Ich Liber Dich")
# print(,,)中加逗号相当于将多行print()用一行写出来，简化了代码
#   例如，上一行代码实际与一下两行代码等价:
#       print(name)
#       print("Ich Liber Dich")

# input()函数也给大家提供了更加简便的显示提示语的方法：
name = input("Your name is...")
print("my name is:", name)

# 分隔符
print("--------------------------------------------------")
