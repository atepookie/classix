from os import system, name
from googletrans import Translator
from pyperclip import copy
from colorama import Fore, Back, Style, init
init(autoreset=True)

def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def title(text):
    if name == "nt":
        system("title " + str(text))
    else:
        None

acc = Fore.YELLOW
res = Fore.RESET

while True:
    title("XTrans")
    sourcelanguage = None
    destlanguage = None
    text = None
    
    while sourcelanguage == None or sourcelanguage.replace(" ", "") == "":
        clear()
        sourcelanguage = input(f"{res}\n С КАКОГО ЯЗЫКА ВЫ ХОТИТЕ ВЫПОЛНИТЬ ПЕРЕВОД?\n\n {acc}ru{res} - Русский\n {acc}en{res} - Английский\n {acc}fr{res} - Французский\n {acc}de{res} - Немецкий\n {acc}es{res} - Испанский\n {acc}ko{res} - Корейский\n {acc}jp{res} - Японский\n {acc}zh-CN{res} - Китайский (Китай)\n {acc}zh-TW{res} - Китайский (Тайвань)\n\n > {acc}")

    while destlanguage == None or destlanguage.replace(" ", "") == "":
        clear()
        destlanguage = input(f"{res}\n НА КАКОЙ ЯЗЫК ВЫ ХОТИТЕ ВЫПОЛНИТЬ ПЕРЕВОД?\n\n {acc}ru{res} - Русский\n {acc}en{res} - Английский\n {acc}fr{res} - Французский\n {acc}de{res} - Немецкий\n {acc}es{res} - Испанский\n {acc}ko{res} - Корейский\n {acc}jp{res} - Японский\n {acc}zh-CN{res} - Китайский (Китай)\n {acc}zh-TW{res} - Китайский (Тайвань)\n\n > {acc}")

    clear()

    title(f"XTrans ({sourcelanguage} - {destlanguage})")
    while text == None or text.replace(" ", "") == "":
        clear()
        text = str(input(res + "\n XTrans\n " + acc + sourcelanguage + " > " + destlanguage + res + "\n\n Введите текст для перевода:\n > " + acc))
    result = Translator().translate(text, src=sourcelanguage, dest=destlanguage)

    print(res + "\n Результат перевода:\n > " + acc + str(result.text))
    copy(str(result.text))
    
    input("\n Результат перевода был скопирован в буфер обмена\n Нажмите 'ENTER' чтобы продолжить\n\n ")