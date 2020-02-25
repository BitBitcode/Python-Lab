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
import os


# 【请求网页】
# 伪装头部
headers_camouflage = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 Edg/80.0.361.57"}
# 请求网站内容
response_content = requests.get("https://www.vmgirls.com/13433.html", headers = headers_camouflage)
# 转换内容格式为文字
html_code = response_content.text

print("【检查点：1】\n")


# 【解析网页】
# 这里用的是正则表达式来寻找所有图片的链接地址
images_urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">', html_code)
#print(images_urls)

print("【检查点：2】\n")


#【保存图片】
# 按照网页中写真系列名称建立文件夹
folder_name = re.findall('<h1 class="post-title h3">(.*?)</h1>', html_code)[-1]
if not os.path.exists(folder_name):
    os.mkdir(folder_name)


for single_url in images_urls:
    time.sleep(1)                              # 延迟：1秒，减轻服务器负担
    save_name = single_url.split("/")[-1]      # 图片保存的文件名
    response_content = requests.get(single_url, headers = headers_camouflage)
    with open(folder_name + "/" +save_name, "wb") as image_file:
        image_file.write(response_content.content)


print("【检查点：3】\n")
