# -*- coding: gbk -*-
import time
import win32com.client

# 启动浏览器
browser = win32com.client.Dispatch("InternetExplorer.Application")
browser.Visible = 1
time.sleep(2)

# 打开哔哩哔哩网站
browser.navigate("https://www.bilibili.com")
time.sleep(5)
