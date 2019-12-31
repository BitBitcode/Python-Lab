# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

word = input("输入查询单词：")
url = "http://www.youdao.com/w/eng/" + word

web_data = requests.get(url).text

# 打印爬到的内容
doc=open("Output.txt","w",encoding='utf-8')
print(web_data,file=doc)
doc.close()
# 打印结果是整个网页的源代码，保存在了同目录下的 “Output.txt” 文本文件
# 文档路径被保护，无法写入

# 爬取特定位置内容
soup = BeautifulSoup(web_data,"lxml")
meaning = soup.select("#phrsListTab > div.trans-container > ul > li") #获取所有“li”标签
# 获取第一个“li”标签：meaning = soup.select("#phrsListTab > div.trans-container > ul > li:nth-child(1)").get_text()
print("原提取内容：")
print(meaning) #打印获取的所有意思，但不优化显示

print("单词意思：")
for i in meaning:
    print(i.get_text())
#只提取意思