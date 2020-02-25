"""
【项目】爬取 “唯美女生” 网
    ·依赖库：requests
    ·任务目标：保存图片
    ·来源：https://www.bilibili.com/video/av75562300/
"""


# 【依赖项】
import requests

print("hello world")

# 【请求网页】
content = requests.get("https://www.vmgirls.com/12985.html")    # content 为获取的内容
print("【直接请求】不采取伪装头部的做法，请求网页时服务器识别的“headers”为：\n", content.request.headers)

# 伪装头部（反爬）
# F12开发者工具 > Network（菜单栏）> Name（选项卡）> 选中“12985.html” > headers（选项卡）> 找到“user-agent”


# headers_camouflage = {
#     user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 Edg/80.0.361.57
#     }
#result = requests.get("https://www.vmgirls.com/12985.html", headers=headers_camouflage)




