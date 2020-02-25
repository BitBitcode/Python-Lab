'''
【Python代码运行日志记录模块】
模块名：Kiana_record.py
简介：
    ·帮助记录运行中的一些内容，否则关闭终端内容全无
库函数：
    ·rec_solo(record_path, origin_content, i)：记录单条日志
    ·rec_batch()：记录多条日志
开发计划（Todo List）：
        · rec_solo(record_path, origin_content) 函数没有检查输入参数以及抛出异常
        · 加入记录个数的统计
        · 编写：rec_batch() 批量记录函数
更多信息：
    ·个人邮箱：smilewwc@qq.com
    ·个人网页：https://bitbitcode.github.io/
    ·开源地址：https://github.com/BitBitcode
创建日期：2020.2.25
更新日志：

Copyright (c) BitBitcode. All rights reserved.

'''


__author__ = "BitBitcode"


# 【依赖库】
import datetime


# 【函数】记录单条日志
# 【来源】无
# 【参数】字符串，日志文件路径；信息对象，要记录的内容；整型，记录位置
# 【返回值】空类型
def rec_solo(record_path, origin_content, i):

    record_text = str(origin_content)
    output_file = open(record_path, "a", encoding="utf-8")
    output_file.write("【运行记录】位置：%d\n" %i + record_text + "\n" )

    current_date_time = datetime.datetime.now()  #【定义对象】
    time_str = datetime.datetime.strftime(current_date_time,'%Y-%m-%d %H:%M:%S')    # 格式化
    output_file.write("【记录时间】" + time_str + "\n\n")  # 循环写入结束后追加一条记录日期时间

    output_file.close()

#【测试】
""" 
p = "C:\\GitHub\\Python-Lab\\爬取唯美女生网\\record_test.txt"
r = "测试：这是一条记录"
i = 1

rec_solo(p, r, i)
i=i+1
rec_solo(p, "占个位置", i)
"""

# 【函数】记录多条日志
# 【来源】无
# 【参数】字符串，日志文件路径；信息对象，要记录的内容
# 【返回值】空类型
def rec_batch():
    pass