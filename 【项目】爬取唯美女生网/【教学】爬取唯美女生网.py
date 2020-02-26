"""
【项目】爬取 “唯美女生” 网
    ·依赖库：requests
    ·任务目标：保存图片
    ·来源：https://www.bilibili.com/video/av75562300/
"""


# 【依赖项】
import requests
import re
import time
import Kiana_record


# 记录
file_path = "C:\\GitHub\\Python-Lab\\爬取唯美女生网\\log.txt"


# 【请求网页】
#（1）直接请求
# content = requests.get("https://www.vmgirls.com/12985.html")    # content 为获取的内容
# print("【直接请求】不采取伪装头部的做法，请求网页时服务器识别的“headers”为：\n", content.request.headers)
# print("【检查点：1】\n")
# Kiana_record.rec_solo(file_path, content.request.headers)
# i = i + 1

#（2）伪装头部（反爬）
# F12开发者工具 > Network（菜单栏）> Name（选项卡）> 选中“12985.html” > headers（选项卡）> 找到“user-agent”
headers_camouflage = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 Edg/80.0.361.57"
    }
# 请求网站内容
content = requests.get("https://www.vmgirls.com/12985.html", headers = headers_camouflage)
# 请求网站内容
html_code = content.text
# print("【伪装头部】请求到网页的源代码为：\n", html_code)
# print("【检查点：2】\n")
# Kiana_record.rec_solo(file_path, html_code)

# 【解析网页】
# 这里用的是正则表达式来寻找所有图片的链接地址
images_urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html_code)
print(images_urls)
Kiana_record.rec_solo(file_path, images_urls)
print("【检查点：3】\n")


#【保存图片】
# 直接保存
for single_url in images_urls:
    time.sleep(1)                       # 延迟：1秒，减轻服务器负担
    save_name = single_url.split("/")[-1]      # 图片保存的文件名
    response_content = requests.get(single_url, headers = headers_camouflage)
    with open(save_name, "wb") as image_file:
        image_file.write(response_content.content)

# 创建文件夹保存