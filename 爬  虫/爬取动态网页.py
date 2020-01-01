# -*- coding: utf-8 -*-

# 调用库
from selenium import webdriver
import time

# 在解压目录调用PhantomJS
driver = webdriver.PhantomJS(executable_path= r"C:\Users\smile\AppData\Local\Programs\Python\phantomjs-2.1.1-windows\bin\phantomjs.exe")
# 打开页面网址
driver.get("https://study.163.com/course/introduction/1006277004.htm")
time.sleep(5) #睡5秒确保页面加载完成

#auto-id-1577844328933 不成功，可以逐级向上尝试ID：
data = driver.find_element_by_id("j-coursehead").text
print("原始爬到的数据：",data)

#由于获取精确的不成功，获取了上级的，所以信息较多，要筛选，用切片技术
a = data.find("\n")  #找到第一个换行符
b = data[a+1:].find("\n")  #找到第二个换行符
new_data = data[a+1:a+1+b]  #取两个换行符之间的部分，即学过人数
driver.quit()  #关闭页面
print("精确数据：",new_data)