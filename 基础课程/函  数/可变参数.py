# 定义以列表为可变参数的函数
def average_1(numbers):
    sum = 0
    n = 0
    for num in numbers:
        sum = sum + num
        n = n+1
    ave = sum / n
    return ave

array = [1,2,3,4,5,6,7]
ave = average_1(array)
print("【测试1】平均值: = %d" %ave)


# 定义可变位置参数个数的函数
def average_2(*numbers):
    sum = 0
    n = 0
    for num in numbers:
        sum = sum + num
        n = n+1
    ave = sum / n
    return ave

ave = average_2(1, 23, 49)
print("【测试2】平均值: = %d" %ave)


# 在第二种情况下，如果要传入一个列表，也是可以的，只需要在列表前加一个 * ：
ave = average_2(*array)
print("【测试3】平均值: = %d" %ave)

