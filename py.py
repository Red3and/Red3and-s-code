# -*- coding: gbk -*-
import win32com.client
powerpoint = win32com.client.Dispatch("PowerPoint.Application")
powerpoint.Visible = 1
presentation = powerpoint.Presentations.Open("C:\\·��\\��\\���\\�õ�Ƭ\\�ļ���.pptx")