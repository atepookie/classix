from sys import exit
from os import name
import turtle
import tkinter
from tkinter import colorchooser

def Penspeed10():
    global Penspeed
    Penspeed = 10
    PenSpeedLabel.config(text=f"Шаг пера: {Penspeed}")
    
def Penspeed20():
    global Penspeed
    Penspeed = 20
    PenSpeedLabel.config(text=f"Шаг пера: {Penspeed}")
    
def Penspeed30():
    global Penspeed
    Penspeed = 30
    PenSpeedLabel.config(text=f"Шаг пера: {Penspeed}")
    
def Penspeed40():
    global Penspeed
    Penspeed = 40
    PenSpeedLabel.config(text=f"Шаг пера: {Penspeed}")
    
def Penspeed50():
    global Penspeed
    Penspeed = 50
    PenSpeedLabel.config(text=f"Шаг пера: {Penspeed}")

def Penspeed60():
    global Penspeed
    Penspeed = 60
    PenSpeedLabel.config(text=f"Шаг пера: {Penspeed}")

def ChangeLayers():
    if turtle.isdown() == True:
        turtle.up()
        IsPenUpState.config(text=f"  ○  ")
    else:
        turtle.down()
        IsPenUpState.config(text=f"  ●  ")

class Thickness:
    def minus():
        if turtle.pensize() != 1:
            turtle.pensize(turtle.pensize() - 1)
            thickness.config(text=f"Толщина: {turtle.pensize()}")

        else:
            pass

    def plus():
        turtle.pensize(turtle.pensize() + 1)
        thickness.config(text=f"Толщина: {turtle.pensize()}")

class Look:
    background = "#202020"
    button = "#404040"
    text = "#DADADA"

    global UColor
    global UBgcolor

    def ChColor():
        UColor = colorchooser.askcolor()[1]
        turtle.color(UColor)
        PenColor.config(activebackground=UColor, activeforeground=Look.background)
                     
    def ChBg():
        UBgcolor = colorchooser.askcolor()[1]
        turtle.bgcolor(UBgcolor)
        BgColor.config(activebackground=UBgcolor, activeforeground=Look.background)


def Undo():
    turtle.undo()
    if turtle.isdown() == True:
        IsPenUpState.config(text=f"  ●  ")
    else:
        IsPenUpState.config(text=f"  ○  ")
    thickness.config(text=f"Толщина: {turtle.pensize()}")

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

    root = tkinter.Tk()
    root.title("XPaint 10")
    root.configure(bg=Look.background, padx=15, pady=15, cursor="left_ptr")
    root.resizable(False, False)

    tkinter.Label(root, text="Управление движением", bg=Look.background, fg=Look.text, font=Userfont).pack(padx=5, pady=5)

    toparrows = tkinter.Frame(root, bg=Look.background)
    toparrows.pack()

    tkinter.Button(toparrows, text="  ↖  ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=lambda: turtle.goto(turtle.xcor() - Penspeed, turtle.ycor() + Penspeed), cursor="top_left_corner").pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(toparrows, text="   ↑   ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=lambda: turtle.sety(turtle.ycor() + Penspeed), cursor="top_side").pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(toparrows, text="  ↗  ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=lambda: turtle.goto(turtle.xcor() + Penspeed, turtle.ycor() + Penspeed), cursor="top_right_corner").pack(side=tkinter.LEFT, padx=5, pady=5)

    centerarrows = tkinter.Frame(root, bg=Look.background)
    centerarrows.pack()

    tkinter.Button(centerarrows, text="  ←  ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=lambda: turtle.setx(turtle.xcor() - Penspeed), cursor="left_side").pack(side=tkinter.LEFT, padx=5, pady=5)
    global IsPenUpState
    IsPenUpState = tkinter.Button(centerarrows, text="  ●  ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=ChangeLayers, cursor="gobbler")
    IsPenUpState.pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(centerarrows, text="  →  ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=lambda: turtle.setx(turtle.xcor() + Penspeed), cursor="right_side").pack(side=tkinter.LEFT, padx=5, pady=5)

    bottomarrows = tkinter.Frame(root, bg=Look.background)
    bottomarrows.pack()

    tkinter.Button(bottomarrows, text="  ↙  ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=lambda: turtle.goto(turtle.xcor() - Penspeed, turtle.ycor() - Penspeed), cursor="bottom_left_corner").pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(bottomarrows, text="   ↓   ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=lambda: turtle.sety(turtle.ycor() - Penspeed), cursor="bottom_side").pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(bottomarrows, text="  ↘  ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=lambda: turtle.goto(turtle.xcor() + Penspeed, turtle.ycor() - Penspeed), cursor="bottom_right_corner").pack(side=tkinter.LEFT, padx=5, pady=5)

    specframe = tkinter.Frame(root, bg=Look.background)
    specframe.pack()

    tkinter.Button(specframe, text=" Закрыть ", font=Userfont, bg=Look.button, fg=Look.text, bd=0, command=exit, cursor="X_cursor", activebackground="#FF8080", activeforeground=Look.background).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(specframe, text=" Центрировать ", font=Userfont, bg=Look.button, fg=Look.text, bd=0, command=lambda: turtle.goto(0,0), cursor="tcross", activebackground="#D0FF80", activeforeground=Look.background).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(specframe, text=" Отменить ", font=Userfont, bg=Look.button, fg=Look.text, bd=0, command=Undo, cursor="sb_left_arrow", activebackground="#80D0FF", activeforeground=Look.background).pack(side=tkinter.LEFT, padx=5, pady=5)
    
    tkinter.Label(root, text="", bg=Look.background, fg=Look.text, font=Userfont).pack(padx=5, pady=5)

    global PenSpeedLabel
    PenSpeedLabel = tkinter.Label(root, text=f"Шаг пера: {Penspeed}", bg=Look.background, fg=Look.text, font=Userfont)
    PenSpeedLabel.pack(padx=5, pady=5)

    speedframe = tkinter.Frame(root, bg=Look.background)
    speedframe.pack()

    tkinter.Button(speedframe, text="  10  ", font=Userfont, bg=Look.button, fg=Look.text, bd=0, command=Penspeed10, cursor="cross", activebackground="#80D0FF", activeforeground=Look.background).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(speedframe, text="  20  ", font=Userfont, bg=Look.button, fg=Look.text, bd=0, command=Penspeed20, cursor="cross", activebackground="#80FFFF", activeforeground=Look.background).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(speedframe, text="  30  ", font=Userfont, bg=Look.button, fg=Look.text, bd=0, command=Penspeed30, cursor="cross", activebackground="#80FF80", activeforeground=Look.background).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(speedframe, text="  40  ", font=Userfont, bg=Look.button, fg=Look.text, bd=0, command=Penspeed40, cursor="cross", activebackground="#FFFF80", activeforeground=Look.background).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(speedframe, text="  50  ", font=Userfont, bg=Look.button, fg=Look.text, bd=0, command=Penspeed50, cursor="cross", activebackground="#FFD080", activeforeground=Look.background).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(speedframe, text="  60  ", font=Userfont, bg=Look.button, fg=Look.text, bd=0, command=Penspeed60, cursor="cross", activebackground="#FF8080", activeforeground=Look.background).pack(side=tkinter.LEFT, padx=5, pady=5)

    tkinter.Label(root, text="", bg=Look.background, fg=Look.text, font=Userfont).pack(padx=5, pady=5)

    superframe = tkinter.Frame(root, bg=Look.background)
    superframe.pack()
    
    fillframe = tkinter.Frame(superframe, bg=Look.background)
    fillframe.pack(side=tkinter.LEFT)

    tkinter.Label(fillframe, text="Заливка", bg=Look.background, fg=Look.text, font=Userfont).pack(padx=5, pady=5)

    tkinter.Button(fillframe, text=" Начать ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=turtle.begin_fill, cursor="spraycan", activebackground="#80D0FF", activeforeground=Look.background).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(fillframe, text=" Закончить ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=turtle.end_fill, cursor="spraycan", activebackground="#80FF80", activeforeground=Look.background).pack(side=tkinter.LEFT, padx=5, pady=5)

    tkinter.Label(superframe, text="     ", bg=Look.background, fg=Look.text, font=Userfont).pack(side=tkinter.LEFT, padx=5, pady=5)

    pensizeframe = tkinter.Frame(superframe, bg=Look.background)
    pensizeframe.pack(side=tkinter.LEFT)

    global thickness
    thickness = tkinter.Label(pensizeframe, text=f"Толщина: {turtle.pensize()}", bg=Look.background, fg=Look.text, font=Userfont)
    thickness.pack(padx=5, pady=5)

    tkinter.Button(pensizeframe, text="   -   ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=Thickness.minus, cursor="sb_left_arrow", activebackground="#80D0FF", activeforeground=Look.background).pack(side=tkinter.LEFT, padx=5, pady=5)
    tkinter.Button(pensizeframe, text="   +   ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=Thickness.plus, cursor="sb_right_arrow", activebackground="#FF8080", activeforeground=Look.background).pack(side=tkinter.LEFT, padx=5, pady=5)

    tkinter.Label(root, text="", bg=Look.background, fg=Look.text, font=Userfont).pack(padx=5, pady=5)

    superframe2 = tkinter.Frame(root, bg=Look.background)
    superframe2.pack()

    toolsframe = tkinter.Frame(superframe2, bg=Look.background)
    toolsframe.pack(side=tkinter.LEFT)

    tkinter.Label(toolsframe, text="Инструменты", bg=Look.background, fg=Look.text, font=Userfont).pack(padx=5, pady=5)

    tkinter.Button(toolsframe, text=" Добавить текст ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=lambda: turtle.write(turtle.textinput("Текст", "Введите текст для вставки на холст:"), align="left", font=(turtle.textinput("Текст", "Введите название шрифта:"), int(turtle.textinput("Текст", "Введите размер шрифта:")), "normal")), cursor="top_tee", activebackground="#D0FF80", activeforeground=Look.background).pack(padx=5, pady=5)
    tkinter.Button(toolsframe, text=" Очистить холст ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=turtle.clear, cursor="pirate", activebackground="#FF8080", activeforeground=Look.background).pack(padx=5, pady=5)

    tkinter.Label(superframe2, text="     ", bg=Look.background, fg=Look.text, font=Userfont).pack(side=tkinter.LEFT, padx=5, pady=5)

    colorframe = tkinter.Frame(superframe2, bg=Look.background)
    colorframe.pack(side=tkinter.LEFT)

    tkinter.Label(colorframe, text="Выбрать цвет", bg=Look.background, fg=Look.text, font=Userfont).pack(padx=5, pady=5)

    global PenColor
    PenColor = tkinter.Button(colorframe, text=" Для пера ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=Look.ChColor, cursor="spraycan")
    PenColor.pack(padx=5, pady=5)
    global BgColor
    BgColor = tkinter.Button(colorframe, text=" Для фона ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=Look.ChBg, cursor="spraycan")
    BgColor.pack(padx=5, pady=5)

    root.mainloop()

# ЛИЦЕНЗИЯ

if name == "nt":
    Userfont = ("Bahnschrift", 9, "normal")
else:
    Userfont = ("Ubuntu", 9, "normal")

license = tkinter.Tk()
license.title("XPaint - Лицензионное соглашение")
license.configure(bg=Look.background, padx=15, pady=15, cursor="left_ptr")
license.geometry("640x640")
license.resizable(False, False)

licensetext = "ИСПОЛЬЗУЯ ДАННОЕ ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ, ВЫ ПРИНИМАЕТЕ СЛЕДУЮЩЕЕ ЛИЦЕНЗИОННОЕ СОГЛАШЕНИЕ:\n\n[RU] Copyright (C) 2024 Котов Ярослав\n\nДанная лицензия разрешает лицам, получившим копию данного программного обеспечения и сопутствующей документации (далее — Программное обеспечение), безвозмездно использовать Программное обеспечение без ограничений, включая неограниченное право на использование, копирование, изменение, слияние, публикацию, распространение, сублицензирование и/или продажу копий Программного обеспечения, а также лицам, которым предоставляется данное Программное обеспечение, при соблюдении следующих условий:\n\nУказанное выше уведомление об авторском праве и данные условия должны быть включены во все копии или значимые части данного Программного обеспечения.\n\nДАННОЕ ПРОГРАММНОЕ ОБЕСПЕЧЕНИЕ ПРЕДОСТАВЛЯЕТСЯ «КАК ЕСТЬ», БЕЗ КАКИХ-ЛИБО ГАРАНТИЙ, ЯВНО ВЫРАЖЕННЫХ ИЛИ ПОДРАЗУМЕВАЕМЫХ, ВКЛЮЧАЯ ГАРАНТИИ ТОВАРНОЙ ПРИГОДНОСТИ, СООТВЕТСТВИЯ ПО ЕГО КОНКРЕТНОМУ НАЗНАЧЕНИЮ И ОТСУТСТВИЯ НАРУШЕНИЙ, НО НЕ ОГРАНИЧИВАЯСЬ ИМИ. НИ В КАКОМ СЛУЧАЕ АВТОРЫ ИЛИ ПРАВООБЛАДАТЕЛИ НЕ НЕСУТ ОТВЕТСТВЕННОСТИ ПО КАКИМ-ЛИБО ИСКАМ, ЗА УЩЕРБ ИЛИ ПО ИНЫМ ТРЕБОВАНИЯМ, В ТОМ ЧИСЛЕ, ПРИ ДЕЙСТВИИ КОНТРАКТА, ДЕЛИКТЕ ИЛИ ИНОЙ СИТУАЦИИ, ВОЗНИКШИМ ИЗ-ЗА ИСПОЛЬЗОВАНИЯ ПРОГРАММНОГО ОБЕСПЕЧЕНИЯ ИЛИ ИНЫХ ДЕЙСТВИЙ С ПРОГРАММНЫМ ОБЕСПЕЧЕНИЕМ.\n\n[EN] Copyright (C) 2024 Kotov Yaroslaw\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."

text_widget = tkinter.Text(license, wrap="word", font=Userfont, bg=Look.background, fg=Look.text, bd=0, cursor="double_arrow")
text_widget.insert("1.0", licensetext)
text_widget.config(state="disabled")
text_widget.pack(padx=5, pady=5, expand=True, fill="both")

tkinter.Button(license, text=" Отказаться ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=exit, cursor="X_cursor", activebackground="#FF8080", activeforeground=Look.background).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(license, text=" Принять условия лицензии ", bg=Look.button, fg=Look.text, bd=0, font=Userfont, command=appcontent, cursor="heart", activebackground="#D0FF80", activeforeground=Look.background).pack(side=tkinter.RIGHT, padx=5, pady=5)

license.mainloop()