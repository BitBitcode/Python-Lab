@echo off
:: 切换字符编码为：UTF-8
chcp 65001
title 自动配置网页代码运行助手

if EXIST learning.py (
    python learning.py
    echo 网页代码运行助手已启动！
) else (
    echo 当前路径没有文件，重新引导至默认位置。。。
    cd C:\Users\WWC\OneDrive\文档\GitHub\Python-Lab\Learning_Tool
    echo 路径已引导
    if EXIST learning.py (
        python learning.py
        echo 默认位置运行成功！
    ) else (
        echo 默认位置没有文件!
    )
)
pause