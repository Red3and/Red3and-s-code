from tkinter import messagebox

import pyttsx3
from openai import OpenAI
from pocketsphinx import LiveSpeech
from PIL import Image, ImageTk, ImageSequence
import tkinter as tk
import tkinter.font as tkFont
import threading
import voice
import gpt
import os


class GUI:
    def __init__(self):
        self.font = None
        self.frame_index = None
        self.frames = None
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes('-transparentcolor', 'white', '-topmost', 'true')
        self.canvas = tk.Canvas(self.root, width=800, height=1600, bg='white', highlightthickness=0)
        self.canvas.pack()
        self.photo1 = ImageTk.PhotoImage(Image.open("image/wait.png").resize((100, 100)))
        self.photo2 = ImageTk.PhotoImage(Image.open("image/listen.png").resize((100, 100)))
        self.photo3 = ImageTk.PhotoImage(Image.open("image/3.png").resize((100, 100)))
        self.photo4 = ImageTk.PhotoImage(Image.open("image/4.png").resize((100, 100)))
        self.gif_image1 = Image.open("image/111.gif")
        self.frames = ImageSequence.Iterator(self.gif_image1)
        self.frame_index = 0
        self.is_running = True
        self.text = None
    def show(self):

        self.root.after(100, self.update_image)
        self.canvas.create_text(100, 150, text="欢迎使用该智能语音", font=("Arial", 12))
        threading.Thread(target=self.thread).start()
        self.root.bind("<<myEvent1>>", self.handel_listen)
        self.root.bind("<<myEvent2>>", self.handel_code)
        self.root.bind("<<myEvent3>>", self.handel_respond)
        self.canvas.bind('<B1-Motion>', self.on_drag)
        self.update_image()
        self.root.mainloop()


        # Start the animation loop

    def update_image(self):
        if not self.is_running:
            return

        try:
            frame = next(self.frames)
            photo = ImageTk.PhotoImage(frame.resize((500, 500)))

            # 假设你之前已经有一个图像在画布上，需要先删除它
            # 你需要保存对之前图像的引用，这里为了简单，我们直接覆盖
            # 如果你需要删除之前的图像，你需要跟踪所有创建的图像并删除它们
            self.canvas.create_image(200, 200, image=photo, anchor=tk.CENTER, tags="animated_image")
            self.canvas.image = photo  # 保持对图像的引用

            self.root.after(50, self.update_image)
        except StopIteration:
            self.frames = ImageSequence.Iterator(self.gif_image1)


    def on_drag(self, event):
        x = event.x_root
        y = event.y_root
        self.root.geometry(f'+{x}+{y}')

    def wait(self):
        self.root.event_generate('<<myEvent1>>')

    def handel_wait(self, event):
        self.is_running = False
        # 清理帧迭代器
        self.frames = None
        self.canvas.delete("animated_image")
        self.canvas.delete('all')
        self.canvas.create_image(0, 0, image=self.photo1, anchor=tk.NW)
        self.canvas.create_text(50, 150, text="我正在等待", font=("Arial", 12))
        self.canvas.update()

    def listen(self):
        self.root.event_generate('<<myEvent1>>')

    def handel_listen(self, event):
        self.is_running = False
        # 清理帧迭代器
        self.frames = None
        self.canvas.delete("animated_image")
        self.canvas.delete('all')
        self.canvas.create_image(0, 0, image=self.photo2, anchor=tk.NW)
        self.canvas.create_text(50, 150, text="我正在听", font=("Arial", 12))
        self.canvas.update()

    def code(self):
        self.root.event_generate('<<myEvent2>>')

    def handel_code(self, event):
        self.canvas.delete('all')
        self.canvas.create_image(0, 0, image=self.photo1, anchor=tk.NW)
        self.canvas.create_text(50, 150, text="我正在帮助你", font=("Arial", 12))
        self.canvas.update()

    def respond(self):
        self.root.event_generate('<<myEvent3>>')

    def handel_respond(self, event):
        self.canvas.delete('all')
        self.canvas.create_image(0, 0, image=self.photo1, anchor=tk.NW)
        text_id = self.canvas.create_text(270,120, text = self.text, width=300)
        self.canvas.update_idletasks()
        text_bbox = self.canvas.bbox(text_id)  # 获取文本的边界框

        # 计算边框的位置和大小（这里简单地在文本周围加一个5像素的边框）
        border_x0 = text_bbox[0] - 5
        border_y0 = text_bbox[1] - 5
        border_x1 = text_bbox[2] + 5
        border_y1 = text_bbox[3] + 5

        # 创建边框
        self.canvas.create_rectangle(border_x0, border_y0, border_x1, border_y1, outline="black")
        self.canvas.update()

    def thread(self):
        print("test")
        speech = LiveSpeech(
            verbose=False,
            sampling_rate=16000,
            buffer_size=2048,
            no_search=False,
            full_utt=False,
            hmm=os.path.join(os.getcwd(), 'model/cmusphinx-zh-cn-5.2/cmusphinx-zh-cn-5.2/zh_cn.cd_cont_5000'),
            lm=os.path.join(os.getcwd(), 'model/cmusphinx-zh-cn-5.2/cmusphinx-zh-cn-5.2/zh_cn.lm'),
            dic=os.path.join(os.getcwd(), 'model/cmusphinx-zh-cn-5.2/cmusphinx-zh-cn-5.2/zh_cn.dic'))
        print("test")
        for phrase in speech:
            print("test")
            print("phrase:", phrase)
            print(phrase.segments(detailed=True))
            if str(phrase) in ["助手", "小助手", "住手", "出手", "祝寿", "入手", "株洲","如","如书","女","动手",""]:
                print("correct")
                self.listen()
                text = voice.voice()
                if text == "0":
                    print("未能识别到有效内容")
                    self.wait()
                elif "帮" in text:
                    self.code()
                    gpt.gpt_code(text)
                    self.wait()
                else:
                    self.text = gpt.gpt_answer(text)
                    self.respond()
                    engine = pyttsx3.init()
                    engine.setProperty('rate', 150)
                    engine.setProperty('volume', 1)
                    engine.say(self.text)
                    engine.runAndWait()
                    self.wait()


if __name__ == '__main__':
    gui = GUI()
    gui.show()
