# 智能助手
欢迎使用智能助手。该项目利用Qwen2-7B-Instruct语言模型的强大功能，使用语音命令，能够实现自动化操作或者是语音问答

## 先决条件
·本项目目前仅支持windows环境，请在win环境下运行

·Python3.7

## 开始
1.将此仓库克隆到您的本地计算机

2.通过以下命令安装所需要的依赖项：pip install -r requirements.txt

3.通过运行GUI.py以启动程序 注：首次运行将会自动加载语言模型，耗时较久，请耐心等待

4.该程序会主动侦听语音命令。通过说出“助手”以唤醒程序，当听到“我在，有什么指示”后以下达下一步指示，若指令为空，则程序会语音输出“未能识别到有效内容”然后回到侦听状态 注：语音模型仅能够识别中文，所以请使用全中文指令。由于python运行速度原因，请在程序语音输出完成后等待几秒后再下达指令，以确保稳定性

5.当下达指令后，若指令为“帮我XXX”样式，程序将认为这是一个操作命令，并对您的计算机执行该指令

6.在执行命令前，程序将判断此命令危险性，若过高会发出“这是一个高危操作，您确定要这样做吗”的询问，通过语音回答是否以继续操作

7.若指令不为一个计算机指令，程序将通过语音回应此指令

8.在执行完相应操作后，程序将重新回到侦听状态。通过说出“助手”以唤醒程序


## 示例用法

以下是您可以使用的语音命令的一些示例

·示例一：帮我打开微博

·示例二：帮我新建幻灯片

·示例三：讲一个笑话

·示例四：什么是语言大模型
