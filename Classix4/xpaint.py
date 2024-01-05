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
    def red1():
        global Usercolor
        if Usercolor == "#FF7D7D":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#FF7D7D"
            turtle.color(Usercolor)

    def orange1():
        global Usercolor
        if Usercolor == "#FFA96A":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#FFA96A"
            turtle.color(Usercolor)

    def yellow1():
        global Usercolor
        if Usercolor == "#FFDD66":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#FFDD66"
            turtle.color(Usercolor)

    def green1():
        global Usercolor
        if Usercolor == "#B1FF74":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#B1FF74"
            turtle.color(Usercolor)

    def skyblue1():
        global Usercolor
        if Usercolor == "#84F0FF":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#84F0FF"
            turtle.color(Usercolor)

    def blue1():
        global Usercolor
        if Usercolor == "#80C2FF":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#80C2FF"
            turtle.color(Usercolor)

    def purple1():
        global Usercolor
        if Usercolor == "#DF84FF":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#DF84FF"
            turtle.color(Usercolor)

    def pink1():
        global Usercolor
        if Usercolor == "#FF6FD7":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#FF6FD7"
            turtle.color(Usercolor)

    def gray1():
        global Usercolor
        if Usercolor == "#FFFFFF":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#FFFFFF"
            turtle.color(Usercolor)

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

    def pink():
        global Usercolor
        if Usercolor == "#FF00B8":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#FF00B8"
            turtle.color(Usercolor)

    def gray():
        global Usercolor
        if Usercolor == "#808080":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#808080"
            turtle.color(Usercolor)

    def red0():
        global Usercolor
        if Usercolor == "#8B0000":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#8B0000"
            turtle.color(Usercolor)

    def orange0():
        global Usercolor
        if Usercolor == "#8B3A00":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#8B3A00"
            turtle.color(Usercolor)

    def yellow0():
        global Usercolor
        if Usercolor == "#8C6D00":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#8C6D00"
            turtle.color(Usercolor)

    def green0():
        global Usercolor
        if Usercolor == "#3D8B00":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#3D8B00"
            turtle.color(Usercolor)

    def skyblue0():
        global Usercolor
        if Usercolor == "#007A8B":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#007A8B"
            turtle.color(Usercolor)

    def blue0():
        global Usercolor
        if Usercolor == "#00488A":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#00488A"
            turtle.color(Usercolor)

    def purple0():
        global Usercolor
        if Usercolor == "#67008B":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#67008B"
            turtle.color(Usercolor)

    def pink0():
        global Usercolor
        if Usercolor == "#8B0064":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#8B0064"
            turtle.color(Usercolor)

    def gray0():
        global Usercolor
        if Usercolor == "#000000":
            turtle.bgcolor(Usercolor)
        else:
            Usercolor = "#000000"
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
            turtle.color("#808080")

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

colorframe1 = tkinter.Frame(root, bg=Look.background)
colorframe1.pack()

tkinter.Button(colorframe1, text="       ", font=Userfont, command=Color.red1, bg="#FF7D7D").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe1, text="       ", font=Userfont, command=Color.orange1, bg="#FFA96A").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe1, text="       ", font=Userfont, command=Color.yellow1, bg="#FFDD66").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe1, text="       ", font=Userfont, command=Color.green1, bg="#B1FF74").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe1, text="       ", font=Userfont, command=Color.skyblue1, bg="#84F0FF").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe1, text="       ", font=Userfont, command=Color.blue1, bg="#80C2FF").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe1, text="       ", font=Userfont, command=Color.purple1, bg="#DF84FF").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe1, text="       ", font=Userfont, command=Color.pink1, bg="#FF6FD7").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe1, text="       ", font=Userfont, command=Color.gray1, bg="white").pack(side=tkinter.LEFT, padx=5, pady=5)

colorframe = tkinter.Frame(root, bg=Look.background)
colorframe.pack()

tkinter.Button(colorframe, text="       ", font=Userfont, command=Color.red, bg="#FF3030").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe, text="       ", font=Userfont, command=Color.orange, bg="#FF6B00").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe, text="       ", font=Userfont, command=Color.yellow, bg="#FFC700").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe, text="       ", font=Userfont, command=Color.green, bg="#60DB00").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe, text="       ", font=Userfont, command=Color.skyblue, bg="#00E0FF").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe, text="       ", font=Userfont, command=Color.blue, bg="#0085FF").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe, text="       ", font=Userfont, command=Color.purple, bg="#BD00FF").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe, text="       ", font=Userfont, command=Color.pink, bg="#FF00B8").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe, text="       ", font=Userfont, command=Color.gray, bg="#808080").pack(side=tkinter.LEFT, padx=5, pady=5)

colorframe0 = tkinter.Frame(root, bg=Look.background)
colorframe0.pack()

tkinter.Button(colorframe0, text="       ", font=Userfont, command=Color.red0, bg="#8B0000").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe0, text="       ", font=Userfont, command=Color.orange0, bg="#8B3A00").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe0, text="       ", font=Userfont, command=Color.yellow0, bg="#8C6D00").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe0, text="       ", font=Userfont, command=Color.green0, bg="#3D8B00").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe0, text="       ", font=Userfont, command=Color.skyblue0, bg="#007A8B").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe0, text="       ", font=Userfont, command=Color.blue0, bg="#00488A").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe0, text="       ", font=Userfont, command=Color.purple0, bg="#67008B").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe0, text="       ", font=Userfont, command=Color.pink0, bg="#8B0064").pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(colorframe0, text="       ", font=Userfont, command=Color.gray0, bg="black").pack(side=tkinter.LEFT, padx=5, pady=5)

root.mainloop()