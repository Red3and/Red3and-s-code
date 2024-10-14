from pocketsphinx import LiveSpeech
from PIL import Image, ImageTk
import tkinter as tk
import threading
import voice
import gpt
import os


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.overrideredirect(True)
        self.root.attributes('-transparentcolor', 'white', '-topmost', 'true')
        self.canvas = tk.Canvas(self.root, width=100, height=100, bg='white', highlightthickness=0)
        self.canvas.pack()
        self.photo1 = ImageTk.PhotoImage(Image.open("image/1.png").resize((100, 100)))
        self.photo2 = ImageTk.PhotoImage(Image.open("image/2.png").resize((100, 100)))
        self.photo3 = ImageTk.PhotoImage(Image.open("image/3.png").resize((100, 100)))
        self.photo4 = ImageTk.PhotoImage(Image.open("image/4.png").resize((100, 100)))

    def show(self):
        self.canvas.create_image(0, 0, image=self.photo1, anchor=tk.NW)
        threading.Thread(target=self.thread).start()
        self.root.bind("<<myEvent1>>", self.handel_listen)
        self.root.bind("<<myEvent2>>", self.handel_code)
        self.root.bind("<<myEvent3>>", self.handel_respond)
        self.canvas.bind('<B1-Motion>', self.on_drag)
        self.root.mainloop()

    def on_drag(self, event):
        x = event.x_root
        y = event.y_root
        self.root.geometry(f'+{x}+{y}')

    def wait(self):
        self.root.event_generate('<<myEvent1>>')

    def handel_wait(self, event):
        self.canvas.delete('all')
        self.canvas.create_image(0, 0, image=self.photo1, anchor=tk.NW)
        self.canvas.update()

    def listen(self):
        self.root.event_generate('<<myEvent1>>')

    def handel_listen(self, event):
        self.canvas.delete('all')
        self.canvas.create_image(0, 0, image=self.photo2, anchor=tk.NW)
        self.canvas.update()

    def code(self):
        self.root.event_generate('<<myEvent2>>')

    def handel_code(self, event):
        self.canvas.delete('all')
        self.canvas.create_image(0, 0, image=self.photo3, anchor=tk.NW)
        self.canvas.update()

    def respond(self):
        self.root.event_generate('<<myEvent3>>')

    def handel_respond(self, event):
        self.canvas.delete('all')
        self.canvas.create_image(0, 0, image=self.photo4, anchor=tk.NW)
        self.canvas.update()

    def thread(self):
        speech = LiveSpeech(
            verbose=False,
            sampling_rate=16000,
            buffer_size=2048,
            no_search=False,
            full_utt=False,
            hmm=os.path.join(os.getcwd(), 'model/cmusphinx-zh-cn-5.2/cmusphinx-zh-cn-5.2/zh_cn.cd_cont_5000'),
            lm=os.path.join(os.getcwd(), 'model/cmusphinx-zh-cn-5.2/cmusphinx-zh-cn-5.2/zh_cn.lm'),
            dic=os.path.join(os.getcwd(), 'model/cmusphinx-zh-cn-5.2/cmusphinx-zh-cn-5.2/zh_cn.dic'))

        for phrase in speech:
            print("phrase:", phrase)
            print(phrase.segments(detailed=True))
            if str(phrase) in ["助手", "小助手", "住手", "出手", "祝寿", "入手", "株洲"]:
                print("correct")
                self.listen()
                text = voice.voice()
                if text == "0":
                    print("未能识别到有效内容")
                elif "帮" in text:
                    self.code()
                    gpt.gpt_code(text)
                    self.wait()
                else:
                    self.respond()
                    gpt.gpt_answer(text)
                    self.wait()


if __name__ == '__main__':
    gui = GUI()
    gui.show()
