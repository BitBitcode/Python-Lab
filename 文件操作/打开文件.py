file_object = open("C:\\GitHub\\Python-Lab\\文件操作\\source.txt",
                   mode="r", encoding="utf-8")

content = "X"    # 【字符型变量】定义 content 为接收所有读取结果的变量
text = "X"       # 【字符型变量】定义 text 为接收单行读取结果的变量


# content = file_object.read()        # read()读取一定数目的数据，括号内的参数为读取字节长度，省略则全部读取
# content = file_object.readline()    # 将读取一行
# content = file_object.readlines()   # 将返回该文件中包含的所有行。括号内的参数为读取字节长度，并且将这些字节按行分割。

# text = file_object.readline()
# 【注意】读取操作如果进行了多次，第二次读取的时候其实指针位置已经不在开头了，需要十分注意！

# print("全部读取结果为：\n" + content + "\n")
# print("单行读取：\n" + text + "\n")


# 业务代码开始（以求和为例）
sum = 0
num = 0

for text in file_object:
    num = int(text)         # 一定要转换数据类型（直接读取到的是字符串类型）
    print("读取：", num)
    sum = sum + num

print("求和结果为：", sum)
# 业务代码结束


# 最后必须做关闭文件的处理
file_object.close()


# 各参数解释：
# file: 必需，文件路径（相对或者绝对路径）。
# mode: 可选，文件打开模式
# t	文本模式 (默认)。
# x	写模式，新建一个文件，如果该文件已存在则会报错。
# b	二进制模式。
# +	打开一个文件进行更新(可读可写)。
# U	通用换行模式（Python 3 不支持）。
# r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。
# w	打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
# w+	打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。
# a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
# buffering: 设置缓冲
# encoding: 一般使用utf-8
# errors: 报错级别
# newline: 区分换行符
# closefd: 传入的file参数类型
# opener:
