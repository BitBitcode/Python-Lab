import time, random
from kkb_robot import send_message

feature_text = '''
大家好！我是您的聊天机器人小K。
我有问必答，有人会问我“今天深圳天气怎么样？”，也有人问我“您喜欢我吗？”
快来问我问题呀，欢迎来撩！

【温馨提示】如果您要删除自己输入的内容，要按两次删除，才可以删掉一个汉字奥！
（因为在计算机世界里，中文是占两个字符的！）

>'''

user1 = input(feature_text)

time.sleep(1)
userid = str(random.randint(1, 1000000000000000000000))
jsrobot1 = send_message(userid, user1)
print(jsrobot1)

time.sleep(2)
user2 = input('''
再来问我点啥吧！我把我知道的都告诉您，嘻嘻！
>''')

jsrobot1 = send_message(userid, user2)
time.sleep(1)
print(jsrobot1)

user3 = input('''

我有点困了，再和您聊完最后一句，我就要下线啦！您还有什么要问我的？

>''')

jsrobot1 = send_message(userid, user3)
time.sleep(1)
print(jsrobot1)
time.sleep(1)
print('\n我走啦，拜拜！')