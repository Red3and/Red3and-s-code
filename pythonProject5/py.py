# -*- coding: gbk -*-
import time
import win32com.client

# ���������
browser = win32com.client.Dispatch("InternetExplorer.Application")
browser.Visible = 1
time.sleep(2)

# ������������վ
browser.navigate("https://www.bilibili.com")
time.sleep(5)
