from sys import exit
from time import sleep
import turtle
import tkinter
from tkinter import colorchooser

def palette():
    global Usercolor
    Usercolor = colorchooser.askcolor()[1]
    turtle.color(Usercolor)

def Penspeed10():
    global Penspeed
    Penspeed = 10
    PenSpeedLabel.config(text=f"Шаг пера {Penspeed}")
    
def Penspeed20():
    global Penspeed
    Penspeed = 20
    PenSpeedLabel.config(text=f"Шаг пера {Penspeed}")
    
def Penspeed30():
    global Penspeed
    Penspeed = 30
    PenSpeedLabel.config(text=f"Шаг пера {Penspeed}")
    
def Penspeed40():
    global Penspeed
    Penspeed = 40
    PenSpeedLabel.config(text=f"Шаг пера {Penspeed}")
    
def Penspeed50():
    global Penspeed
    Penspeed = 50
    PenSpeedLabel.config(text=f"Шаг пера {Penspeed}")

def Penspeed60():
    global Penspeed
    Penspeed = 60
    PenSpeedLabel.config(text=f"Шаг пера {Penspeed}")

def ChangeLayers():
    if turtle.isdown() == True:
        turtle.up()
    else:
        turtle.down()

class Thickness:
    def minus():
        if turtle.pensize() != 1:
            turtle.pensize(turtle.pensize() - 1)
            thickness.config(text=f"Толщина {turtle.pensize()}")

        else:
            pass

    def plus():
        turtle.pensize(turtle.pensize() + 1)
        thickness.config(text=f"Толщина {turtle.pensize()}")

class Look:
    background = "#202020"
    button = "#404040"

def appcontent():
    license.destroy()

    # TURTLE
    
    global Usercolor
    Usercolor = "black"
    global Penspeed
    Penspeed = 10

    turtle.setup(640, 480)
    turtle.title("Холст")

    turtle.speed(0)
    turtle.left(135)

    # TKINTER

    global Userfont
    Userfont = ("Bahnschrift", 10, "normal")

    root = tkinter.Tk()
    root.title("XPaint")
    root.configure(bg=Look.background, padx=15, pady=15)
    root.resizable(False, False)

    tkinter.Label(root, text="Управление движением", bg=Look.background, fg="white", font=Userfont).pack(padx=5, pady=5)

    toparrows = tkinter.Frame(root, bg=Look.background)
    toparrows.pack()

    tkinter.Button(toparrows, text="  ↖  ", bg=Look.button, fg="white", font=Userfont, command=lambda: turtle.goto(turtle.xcor() - Penspeed, turtle.ycor() + Penspeed)).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(toparrows, text="  ↑  ", bg=Look.button, fg="white", font=Userfont, command=lambda: turtle.sety(turtle.ycor() + Penspeed)).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(toparrows, text="  ↗  ", bg=Look.button, fg="white", font=Userfont, command=lambda: turtle.goto(turtle.xcor() + Penspeed, turtle.ycor() + Penspeed)).pack(side=tkinter.LEFT, padx=5, pady=5)

    centerarrows = tkinter.Frame(root, bg=Look.background)
    centerarrows.pack()

    tkinter.Button(centerarrows, text="  ←  ", bg=Look.button, fg="white", font=Userfont, command=lambda: turtle.setx(turtle.xcor() - Penspeed)).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(centerarrows, text=" ⬕ ", bg=Look.button, fg="white", font=Userfont, command=ChangeLayers).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(centerarrows, text="  →  ", bg=Look.button, fg="white", font=Userfont, command=lambda: turtle.setx(turtle.xcor() + Penspeed)).pack(side=tkinter.LEFT, padx=5, pady=5)

    bottomarrows = tkinter.Frame(root, bg=Look.background)
    bottomarrows.pack()

    tkinter.Button(bottomarrows, text="  ↙  ", bg=Look.button, fg="white", font=Userfont, command=lambda: turtle.goto(turtle.xcor() - Penspeed, turtle.ycor() - Penspeed)).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(bottomarrows, text="  ↓  ", bg=Look.button, fg="white", font=Userfont, command=lambda: turtle.sety(turtle.ycor() - Penspeed)).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(bottomarrows, text="  ↘  ", bg=Look.button, fg="white", font=Userfont, command=lambda: turtle.goto(turtle.xcor() + Penspeed, turtle.ycor() - Penspeed)).pack(side=tkinter.LEFT, padx=5, pady=5)

    specframe = tkinter.Frame(root, bg=Look.background)
    specframe.pack()

    tkinter.Button(specframe, text=" Закрыть ", font=Userfont, bg="#5C0000", fg="#FFBBBB", command=exit).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(specframe, text=" Центрировать ", font=Userfont, bg="#005C00", fg="#BBFFBB", command=lambda: turtle.goto(0,0)).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(specframe, text=" Отменить ", font=Userfont, bg="#00005C", fg="#BBBBFF", command=turtle.undo).pack(side=tkinter.LEFT, padx=5, pady=5)

    speedframe = tkinter.Frame(root, bg=Look.background)
    speedframe.pack()

    tkinter.Label(speedframe, text="", bg=Look.background, fg="white", font=Userfont).pack(padx=5, pady=5)
    global PenSpeedLabel
    PenSpeedLabel = tkinter.Label(speedframe, text=f"Шаг пера {Penspeed}", bg=Look.background, fg="white", font=Userfont)
    PenSpeedLabel.pack(padx=5, pady=5)

    tkinter.Button(speedframe, text="   10   ", font=Userfont, bg="#005568", fg="#BBF3FF", command=Penspeed10).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(speedframe, text="   20   ", font=Userfont, bg="#006729", fg="#BCFFD7", command=Penspeed20).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(speedframe, text="   30   ", font=Userfont, bg="#646600", fg="#FEFFB8", command=Penspeed30).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(speedframe, text="   40   ", font=Userfont, bg="#6A5300", fg="#FFEFB4", command=Penspeed40).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(speedframe, text="   50   ", font=Userfont, bg="#682500", fg="#FFD2B8", command=Penspeed50).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(speedframe, text="   60   ", font=Userfont, bg="#5C0000", fg="#FFBBBB", command=Penspeed60).pack(side=tkinter.LEFT, padx=5, pady=5)

    superframe = tkinter.Frame(root, bg=Look.background)
    superframe.pack()

    tkinter.Label(superframe, text="", bg=Look.background, fg="white", font=Userfont).pack(padx=5, pady=5)

    fillframe = tkinter.Frame(superframe, bg=Look.background)
    fillframe.pack(side=tkinter.LEFT)

    tkinter.Label(fillframe, text="Заливка", bg=Look.background, fg="white", font=Userfont).pack(padx=5, pady=5)

    tkinter.Button(fillframe, text="   Начать   ", bg=Look.button, fg="white", font=Userfont, command=turtle.begin_fill).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(fillframe, text=" Закончить ", bg=Look.button, fg="white", font=Userfont, command=turtle.end_fill).pack(side=tkinter.LEFT, padx=5, pady=5)

    tkinter.Label(superframe, text="     ", bg=Look.background, fg="white", font=Userfont).pack(side=tkinter.LEFT, padx=5, pady=5)

    pensizeframe = tkinter.Frame(superframe, bg=Look.background)
    pensizeframe.pack(side=tkinter.LEFT)

    global thickness
    thickness = tkinter.Label(pensizeframe, text=f"Толщина {turtle.pensize()}", bg=Look.background, fg="white", font=Userfont)
    thickness.pack(padx=5, pady=5)

    tkinter.Button(pensizeframe, text="   -   ", bg=Look.button, fg="white", font=Userfont, command=Thickness.minus).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(pensizeframe, text="   +   ", bg=Look.button, fg="white", font=Userfont, command=Thickness.plus).pack(side=tkinter.LEFT, padx=5, pady=5)

    toolsframe = tkinter.Frame(root, bg=Look.background)
    toolsframe.pack()

    tkinter.Label(toolsframe, text="", bg=Look.background, fg="white", font=Userfont).pack(padx=5, pady=5)

    tkinter.Button(toolsframe, text=" Добавить текст ", bg=Look.button, fg="white", font=Userfont, command=lambda: turtle.write(turtle.textinput("Текст", "Введите текст для вставки на холст:"), align="left", font=(turtle.textinput("Текст", "Введите название шрифта:"), int(turtle.textinput("Текст", "Введите размер шрифта:")), "normal"))).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(toolsframe, text=" Очистить холст ", bg=Look.button, fg="white", font=Userfont, command=turtle.clear).pack(side=tkinter.LEFT, padx=5, pady=5)

    colorframe = tkinter.Frame(root, bg=Look.background)
    colorframe.pack()

    tkinter.Button(colorframe, text=" Выбрать цвет ", bg=Look.button, fg="white", font=Userfont, command=palette).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(colorframe, text=" Применить к фону ", bg=Look.button, fg="white", font=Userfont, command=lambda: turtle.bgcolor(Usercolor)).pack(side=tkinter.LEFT, padx=5, pady=5)

    root.mainloop()

# ЛИЦЕНЗИЯ
    
license = tkinter.Tk()
license.title("XPaint - Лицензионное соглашение")
license.configure(bg=Look.background, padx=15, pady=15)
license.geometry("640x640")
license.resizable(False, False)

licensetext = "ЧТОБЫ ПРОДОЛЖИТЬ РАБОТУ С ДАННЫМ ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ, ВАМ НЕОБХОДИМО ПРИНЯТЬ УСЛОВИЯ ЛИЦЕНЗИОННОГО СОГЛАШЕНИЯ:\n\n[RU] Copyright (c) 2024 Котов Ярослав\n\nДанная лицензия разрешает лицам, получившим копию данного программного обеспечения и сопутствующей документации (далее — Программное обеспечение), безвозмездно использовать Программное обеспечение без ограничений, включая неограниченное право на использование, копирование, изменение, слияние, публикацию, распространение, сублицензирование и/или продажу копий Программного обеспечения, а также лицам, которым предоставляется данное Программное обеспечение, при соблюдении следующих условий:\n\nУказанное выше уведомление об авторском праве и данные условия должны быть включены во все копии или значимые части данного Программного обеспечения.\n\nДАННОЕ ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ «КАК ЕСТЬ», БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ, ЯВНО ВЫРАЖЕННЫХ ИЛИ ПОДРАЗУМЕВАЕМЫХ, ВКЛЮЧАЯ ГАРАНТИИ ТОВАРНОЙ ПРИГОДНОСТИ, СООТВЕТСТВИЯ ПО ЕГО КОНКРЕТНОМУ НАЗНАЧЕНИЮ И ОТСУТСТВИЯ НАРУШЕНИЙ, НО НЕ ОГРАНИЧИВАЯСЬ ИМИ. НИ В КАКОМ СЛУЧАЕ АВТОРЫ ИЛИ ПРАВООБЛАДАТЕЛИ НЕ НЕСУТ ОТВЕТСТВЕННОСТИ ПО КАКИМ-ЛИБО ИСКАМ, ЗА УЩЕРБ ИЛИ ПО ИНЫМ ТРЕБОВАНИЯМ, В ТОМ ЧИСЛЕ, ПРИ ДЕЙСТВИИ КОНТРАКТА, ДЕЛИКТЕ ИЛИ ИНОЙ СИТУАЦИИ, ВОЗНИКШИМ ИЗ-ЗА ИСПОЛЬЗОВАНИЯ ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ ИЛИ ИНЫХ ДЕЙСТВИЙ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ.\n\n[EN] Copyright 2024 Kotov Yaroslaw\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."

text_widget = tkinter.Text(license, wrap="word", font=("Arial", 10, "normal"), bg=Look.background, fg="#FFFFFF")
text_widget.insert("1.0", licensetext)
text_widget.config(state="disabled")

scrollbar = tkinter.Scrollbar(license, command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar.set)

scrollbar.pack(side="right", fill="both")
text_widget.pack(expand=True, fill="both")

tkinter.Button(license, text=" Не принимать условия лицензии ", bg="#5C0000", fg="#FFBBBB", font=("Arial", 10, "normal"), command=exit).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(license, text=" Принять условия лицензии ", bg="#005C00", fg="#BBFFBB", font=("Arial", 10, "normal"), command=appcontent).pack(side=tkinter.RIGHT, padx=5, pady=5)

license.mainloop()