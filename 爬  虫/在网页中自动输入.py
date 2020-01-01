# -*- coding: utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path = r"C:\Users\smile\AppData\Local\Programs\Python\phantomjs-2.1.1-windows\bin\phantomjs.exe")
driver.get("https://www.baidu.com")
time.sleep(3) #等待3秒

driver.save_screenshot("baidu1.png")
driver.find_element_by_id("kw").send_keys("编程") #id定位更准确，定位至输入框，输入“编程”测试截图
driver.save_screenshot("baidu2.png")