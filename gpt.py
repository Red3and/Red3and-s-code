from openai import OpenAI
import subprocess
import pyttsx3
import voice


def gpt_code(text):
    text_1 = (
        f"I want you to act like a Desktop Automation. I will give you Instruction and you will return Python code. "
        f"Do not provide any explanations. Do not respond with anything except the code. "
        f"Do not include any typographical mark in respond. "
        f"My OS is Windows Always put delay between instructions. ")
    text_2 = (
        f"I want you to act like a Threat Intelligence. "
        f"I will give you python script and you score the risk of the script execution from 0 to 10. "
        f"Do not provide any explanation outside of the question, do not give an introduction or conclusion, just give me the plain numerical score with no explanations. ")
    text_3 = (
        f"I will give you a short vocabulary and you determine whether the vocabulary means yes or no "
        f"If it means yes then return 1，if it means no then return 0. Do not provide any explanations. Do not respond with anything except the number."
        f"The vocabulary I provide is")

    client = OpenAI(
        base_url='https://cloud.perfxlab.cn/v1',
        api_key="sk-vWWSI851C61E3f1i8eDeFf31375f4cB7835d788dBd56C202")

    risk = client.chat.completions.create(
        model="Qwen2-7B-Instruct",
        messages=[{"role": "user", "content": text_2 + text}])

    if int(risk.choices[0].message.content) > 6:
        text_sure = voice.permission()
        sure = client.chat.completions.create(
            model="Qwen2-7B-Instruct",
            messages=[{"role": "user", "content": text_3 + text_sure}], )
        if int(sure.choices[0].message.content) == 1:
            print("Get permission")
        else:
            return "0"

    code = client.chat.completions.create(
        model="Qwen2-7B-Instruct",
        messages=[{"role": "user", "content": text_1 + text}], )
    command = code.choices[0].message.content
    if "```python" in code.choices[0].message.content:
        command = code.choices[0].message.content[10:-3]
    print(command)

    with open("py.py", "w") as f:
        f.write("# -*- coding: gbk -*-\n")
        f.write(command)
    subprocess.call(["python", "py.py"])


def gpt_answer(text):
    client = OpenAI(
        base_url='https://cloud.perfxlab.cn/v1',
        api_key="sk-vWWSI851C61E3f1i8eDeFf31375f4cB7835d788dBd56C202")

    answer = client.chat.completions.create(
        model="Qwen2-7B-Instruct",
        messages=[{"role": "user", "content": text}], )

    return answer.choices[0].message.content

# def gpt_state(text):
#     text_1 = (
#         f"我会给你提供一段话，你来判断这句话是一个提问还是一个指示 "
#         f"如果是问题就返回1，除了1之外不要返回任何内容"
#         f"如果是指示就返回0，除了0之外不要返回任何内容"
#         f"我要提供的句子是"
#     )
#
#     client = OpenAI(
#         base_url='https://cloud.perfxlab.cn/v1',
#         api_key="sk-vWWSI851C61E3f1i8eDeFf31375f4cB7835d788dBd56C202")
#
#     state = client.chat.completions.create(
#         model="Qwen2-7B-Instruct",
#         messages=[{"role": "user", "content": text_1 + text}], )
#     print(state.choices[0].message.content)
#     return state.choices[0].message.content
