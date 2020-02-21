# 来源：https://www.py.cn/jishu/jichu/13151.html

# 导入 datetime 库
import datetime

# （1）获取日期和时间
current_time = datetime.datetime.now()  # 获取原始日期时间
current_time.year      # 获取年
current_time.month     # 获取月
current_time.day       # 获取日
current_time.hour      # 获取时
current_time.minute    # 获取分
current_time.second    # 获取秒
current_time.date()    # 获取日期

print("原始日期时间：", current_time)


# （2）格式化
# 通过datetime.datetime.now()，我们获取到的时间格式为：2019-07-06 14:55:56.873893，类型：<class 'datetime.datetime'>
# 我们可以使用strftime()转换成我们想要的格式。处理之后的返回的值为2019-07-06、07/06等目标形式，类型为str
date_str = current_time.strftime("%Y-%m-%d")        # 【年-月-日】形式
# date_str = current_time.strftime("%m.%d")         #【月.日】形式

print("格式化日期为字符串：" + date_str)


h = str(current_time.hour)
m = str(current_time.minute)
s = str(current_time.second)
print("时间字符串：" + h + ":" + m + ":" + s)       #【时:分:秒】形式


# （3）类型转换
# 时间一般通过：时间对象，时间字符串，时间戳表示
# 通过datetime获取到的时间变量，类型为：datetime，那么datetime与str类型如何互相转换呢？
# datetime-->str
# time_str = datetime.datetime.strftime(current_time,'%Y-%m-%d %H:%M:%S')
# str-->datetime
# time_str = '2019-07-06 15:59:58'
# curr_time = datetime.datetime.strptime(time_str,'%Y-%m-%d %H:%M:%S')
