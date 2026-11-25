from gigachat import GigaChat
import os

key="" #вставить ключ

sys_prompt="""Ты - ассистент для решения задач по основам программирования.
Ты должен помогать ученикам и студентам решать задачи по программированию
твои задачи:
1. Объясняй решение простым языком специально для новичков.
2. Сначала пошагово разбери задачу.
3. Поясняй каждую часть кода.
4. Не давай сразу готовое решение, приходи к нему пошагово через наводящие вопросы и ответы от обучающегося.
5. Если обучающийся прислал код с ошибкой найди ее и объясни в чем проблема."""

def creat():
    return GigaChat(
        credentials=key,
        scope = "GIGACHAT_API_PERS",
        verify = False,
        model="GigaChat",
    )

def chat():
    print("Напиши условие задачи или вопрос")
    print("Для выхода напиши: выход")

    massages = [{"role":"system","content": sys_prompt,}]

    student=creat()

    while True:
        soob=input("ты: ")
        if soob.lower() in ["выход", "Выход"]:
            print("Пока-пока! :D")
            break
        if not soob:
            continue
        massages.append({"role":"user","content":soob,})
        try:
            response=student.chat.create(messages=massages)
            assistant_reply = response.messages[0].content[0].text

            print("Ассистент:")
            print(assistant_reply)
            print()

            massages.append({"role":"assistant","content":assistant_reply,})
        except Exception as e:
            print(f"Ошибка:{e}")


if __name__ == "__main__":
    chat()
