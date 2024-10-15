# -*- coding: gbk -*-
import win32com.client
powerpoint = win32com.client.Dispatch("PowerPoint.Application")
powerpoint.Visible = 1
presentation = powerpoint.Presentations.Open("C:\\路径\\到\\你的\\幻灯片\\文件名.pptx")