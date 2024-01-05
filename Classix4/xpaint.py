from sys import exit
from time import sleep
import turtle
import tkinter
from tkinter import colorchooser

def palette():
    global Usercolor
    Usercolor = colorchooser.askcolor()[1]
    turtle.color(Usercolor)
    print(turtle.color())

def Penspeed10():
    global Penspeed
    Penspeed = 10
    
def Penspeed20():
    global Penspeed
    Penspeed = 20
    
def Penspeed30():
    global Penspeed
    Penspeed = 30
    
def Penspeed40():
    global Penspeed
    Penspeed = 40
    
def Penspeed50():
    global Penspeed
    Penspeed = 50

def Penspeed60():
    global Penspeed
    Penspeed = 60

def ChangeLayers():
    if turtle.isdown() == True:
        turtle.up()
    else:
        turtle.down()

class Look:
    background = "#202020"
    button = "#404040"
    
# TURTLE

Usercolor = "black"
Penspeed = 10

turtle.setup(640, 480)
turtle.title("Холст")

turtle.speed(0)
turtle.left(135)

# TKINTER

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
tkinter.Label(speedframe, text="Шаг пера", bg=Look.background, fg="white", font=Userfont).pack(padx=5, pady=5)

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

tkinter.Label(pensizeframe, text="Толщина", bg=Look.background, fg="white", font=Userfont).pack(padx=5, pady=5)

tkinter.Button(pensizeframe, text="   -   ", bg=Look.button, fg="white", font=Userfont, command=lambda: turtle.pensize(turtle.pensize() - 1)).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(pensizeframe, text="   +   ", bg=Look.button, fg="white", font=Userfont, command=lambda: turtle.pensize(turtle.pensize() + 1)).pack(side=tkinter.LEFT, padx=5, pady=5)

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