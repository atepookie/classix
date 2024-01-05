from sys import exit
from time import sleep
import turtle
import tkinter

class Mov:
    def up():
        turtle.sety(turtle.ycor() + Penspeed)

    def down():
        turtle.sety(turtle.ycor() - Penspeed)

    def left():
        turtle.setx(turtle.xcor() - Penspeed)

    def right():
        turtle.setx(turtle.xcor() + Penspeed)

    def upright():
        turtle.goto(turtle.xcor() + Penspeed, turtle.ycor() + Penspeed)

    def upleft():
        turtle.goto(turtle.xcor() - Penspeed, turtle.ycor() + Penspeed)

    def downright():
        turtle.goto(turtle.xcor() + Penspeed, turtle.ycor() - Penspeed)

    def downleft():
        turtle.goto(turtle.xcor() - Penspeed, turtle.ycor() - Penspeed)

class Color:
    def red():
        global Usercolor
        if Usercolor == "#FF3030":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#FF3030"
            turtle.color(Usercolor)

    def orange():
        global Usercolor
        if Usercolor == "#FF6B00":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#FF6B00"
            turtle.color(Usercolor)

    def yellow():
        global Usercolor
        if Usercolor == "#FFC700":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#FFC700"
            turtle.color(Usercolor)

    def green():
        global Usercolor
        if Usercolor == "#60DB00":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#60DB00"
            turtle.color(Usercolor)

    def skyblue():
        global Usercolor
        if Usercolor == "#00E0FF":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#00E0FF"
            turtle.color(Usercolor)

    def blue():
        global Usercolor
        if Usercolor == "#0085FF":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#0085FF"
            turtle.color(Usercolor)

    def purple():
        global Usercolor
        if Usercolor == "#BD00FF":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#BD00FF"
            turtle.color(Usercolor)

    def white():
        global Usercolor
        if Usercolor == "white":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "white"
            turtle.color(Usercolor)

    def black():
        global Usercolor
        if Usercolor == "black":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "black"
            turtle.color(Usercolor)

    def gray():
        global Usercolor
        if Usercolor == "#C0C0C0":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#C0C0C0"
            turtle.color(Usercolor)

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

class Layer:
    def Up():
        turtle.up()
        global isLayerUp
        isLayerUp = True

    def Down():
        turtle.down()
        global isLayerUp
        isLayerUp = False

    def CnahgeLayers():
        TemporaryColor = Usercolor
        if isLayerUp == True:
            Layer.Down()
            turtle.color(TemporaryColor)
        else:
            Layer.Up()
            turtle.color("#D9D9D9")

class Look:
    background = "#202020"
    button = "#404040"
    
# TURTLE

Usercolor = "black"
Penspeed = 10
isLayerUp = False

turtle.setup(640, 480)
turtle.title("XPaint - Холст")

turtle.speed(0)
turtle.left(135)

# TKINTER

Userfont = ("Bahnschrift", 10, "normal")
root = tkinter.Tk()
root.title("XPaint - Панель управления")
root.configure(bg=Look.background)
root.resizable(False, False)

topframe = tkinter.Frame(root, bg=Look.background)
topframe.pack()

tkinter.Label(topframe, text="Управление пером", bg=Look.background, fg="white", font=Userfont).pack(padx=5, pady=5)

tkinter.Button(topframe, text="  ↖  ", bg=Look.button, fg="white", font=Userfont, command=Mov.upleft).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(topframe, text="  ↑  ", bg=Look.button, fg="white", font=Userfont, command=Mov.up).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(topframe, text="  ↗  ", bg=Look.button, fg="white", font=Userfont, command=Mov.upright).pack(side=tkinter.LEFT, padx=5, pady=5)

centerframe = tkinter.Frame(root, bg=Look.background)
centerframe.pack()

tkinter.Button(centerframe, text="  ←  ", bg=Look.button, fg="white", font=Userfont, command=Mov.left).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(centerframe, text=" ⬕ ", bg=Look.button, fg="white", font=Userfont, command=Layer.CnahgeLayers).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(centerframe, text="  →  ", bg=Look.button, fg="white", font=Userfont, command=Mov.right).pack(side=tkinter.LEFT, padx=5, pady=5)

bottomframe = tkinter.Frame(root, bg=Look.background)
bottomframe.pack()

tkinter.Button(bottomframe, text="  ↙  ", bg=Look.button, fg="white", font=Userfont, command=Mov.downleft).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(bottomframe, text="  ↓  ", bg=Look.button, fg="white", font=Userfont, command=Mov.down).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(bottomframe, text="  ↘  ", bg=Look.button, fg="white", font=Userfont, command=Mov.downright).pack(side=tkinter.LEFT, padx=5, pady=5)

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

extraframe = tkinter.Frame(root, bg=Look.background)
extraframe.pack()

tkinter.Label(extraframe, text=" ", bg=Look.background, fg="white", font=Userfont).pack(padx=5, pady=5)

tkinter.Button(extraframe, text=" Начать заливку ", bg=Look.button, fg="white", font=Userfont, command=turtle.begin_fill).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(extraframe, text=" Очистить холст ", bg=Look.button, fg="white", font=Userfont, command=turtle.clear).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(extraframe, text=" Закончить заливку ", bg=Look.button, fg="white", font=Userfont, command=turtle.end_fill).pack(side=tkinter.LEFT, padx=5, pady=5)

toolsframe = tkinter.Frame(root, bg=Look.background)
toolsframe.pack()

tkinter.Button(toolsframe, text=" Убавить толщину ", bg=Look.button, fg="white", font=Userfont, command=lambda: turtle.pensize(turtle.pensize() - 1)).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(toolsframe, text=" Добавить текст ", bg=Look.button, fg="white", font=Userfont, command=lambda: turtle.write(turtle.textinput("Текст", "Введите текст для вставки на холст:"), align="left", font=(turtle.textinput("Текст", "Введите название шрифта:"), int(turtle.textinput("Текст", "Введите размер шрифта:")), "normal"))).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(toolsframe, text=" Прибавить толщину ", bg=Look.button, fg="white", font=Userfont, command=lambda: turtle.pensize(turtle.pensize() + 1)).pack(side=tkinter.LEFT, padx=5, pady=5)

extraframe2 = tkinter.Frame(root, bg=Look.background)
extraframe2.pack()

tkinter.Button(extraframe2, text="      ", font=Userfont, command=Color.red, bg="#FF3030").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(extraframe2, text="      ", font=Userfont, command=Color.orange, bg="#FF6B00").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(extraframe2, text="      ", font=Userfont, command=Color.yellow, bg="#FFC700").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(extraframe2, text="      ", font=Userfont, command=Color.green, bg="#60DB00").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(extraframe2, text="      ", font=Userfont, command=Color.skyblue, bg="#00E0FF").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(extraframe2, text="      ", font=Userfont, command=Color.blue, bg="#0085FF").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(extraframe2, text="      ", font=Userfont, command=Color.purple, bg="#BD00FF").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(extraframe2, text="      ", font=Userfont, command=Color.white, bg="white").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(extraframe2, text="      ", font=Userfont, command=Color.black, bg="black").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(extraframe2, text="      ", font=Userfont, command=Color.gray, bg="#C0C0C0").pack(side=tkinter.LEFT, padx=5, pady=5)

root.mainloop()