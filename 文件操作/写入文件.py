# 导入 datetime 库
import datetime

output_file = open("C:\\GitHub\\Python-Lab\\文件操作\\output.txt",
                   "a", encoding="utf-8")
# 注意：
#   （1）虽然文件路径可以是相对路径，但如果只写文件名称，实际保存位置和代码位置不相同（而是上一级目录），所以建议写为绝对路径
#   （2）路径中的 “\” 最好用转义字符 “\\” 来替代，虽然实测 “\” 也可以运行成功
#   （3）"w"为覆盖写入，"a"为追加写入


i = 0               #【整型变量】循环变量
while(i < 10):
    n = str(i+1)    #【字符型变量】编号（需要将整形数据转换为字符型数据，否则无法打印）
    output_file.write("[" + n + "]\n")    # 输出时对内容编号
    
    # 业务代码开始（即实际使用时需要替换的部分）
    output_file.write("这是一条记录\n情况：良好\n")  
    # 业务代码结束

    i = i+1
else:
    current_date_time = datetime.datetime.now()  #【定义对象】
    time_str = datetime.datetime.strftime(current_date_time,'%Y-%m-%d %H:%M:%S')    # 格式化
    output_file.write("【结束】修改日期：" + time_str + "\n\n")  # 循环写入结束后追加一条记录日期时间


# 关闭打开的文件
output_file.close()
