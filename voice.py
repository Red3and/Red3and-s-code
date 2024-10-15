from vosk import Model
import speech_recognition as sr
import threading
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1)
    engine.say(text)
    engine.runAndWait()


def permission():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        threading.Thread(target=speak, args="这是一个高危操作，您确定要这样做吗").start()
        print("Listening...")
        audio = r.listen(source, 20, 5)
    r.vosk_model = Model(model_name="vosk-model-small-cn-0.22")
    text = r.recognize_vosk(audio, language='zh-cn')
    print(text)
    return text


def voice():
    # engine = pyttsx3.init()
    # engine.setProperty('rate', 150)
    # engine.setProperty('volume', 1)
    threading.Thread(target=speak, args=("我在，有什么指示",)).start()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        # threading.Thread(target=speak, args=(text,)).start()
        print("Listening...")
        audio = r.listen(source, 20, 5)
    r.vosk_model = Model(model_name="vosk-model-small-cn-0.22")
    text = r.recognize_vosk(audio, language='zh-cn')
    print(text)
    if len(text) == 17:
        speak("未能识别到有效内容")
        # engine.say("未能识别到有效内容")
        # engine.runAndWait()
        return "0"
    else:
        speak("收到")
        # engine.say("收到")
        # engine.runAndWait()
    return text
