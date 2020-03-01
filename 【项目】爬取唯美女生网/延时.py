import Kiana.record
import time


path = "C:\\GitHub\\Python-Lab\\【项目】爬取唯美女生网\\record_test.txt"

A = "你好！"
B = "我是小娜，让我来帮你"
C = "我们正在做一些配置"
D = "很快就好"


print(A)
Kiana.record.rec_solo(path, A)

time.sleep(1)
print(B)
Kiana.record.rec_solo(path, B)

time.sleep(1)
print(C)
Kiana.record.rec_solo(path, C)

time.sleep(1)
print(D)
Kiana.record.rec_solo(path, D)

