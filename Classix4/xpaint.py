from sys import exit
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
        Usercolor = "#FF3030"
        turtle.color(Usercolor)

    def orange():
        global Usercolor
        Usercolor = "#FF6B00"
        turtle.color(Usercolor)

    def yellow():
        global Usercolor
        Usercolor = "#FFC700"
        turtle.color(Usercolor)

    def green():
        global Usercolor
        Usercolor = "#60DB00"
        turtle.color(Usercolor)

    def skyblue():
        global Usercolor
        Usercolor = "#00E0FF"
        turtle.color(Usercolor)

    def blue():
        global Usercolor
        Usercolor = "#0085FF"
        turtle.color(Usercolor)

    def purple():
        global Usercolor
        Usercolor = "#BD00FF"
        turtle.color(Usercolor)

    def white():
        global Usercolor
        Usercolor = "white"
        turtle.color(Usercolor)

    def black():
        global Usercolor
        Usercolor = "black"
        turtle.color(Usercolor)

    def gray():
        global Usercolor
        Usercolor = "#D9D9D9"
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
            turtle.color(TemporaryColor)
            Layer.Down()
        else:
            turtle.color("#D9D9D9")
            Layer.Up()

# TURTLE

Usercolor = "black"
Penspeed = 10
isLayerUp = False

turtle.setup(640, 480)
turtle.title("XPaint - Холст")

turtle.speed(0)
turtle.left(135)

# TKINTER

Userfont = ("Arial", 10, "normal")
root = tkinter.Tk()
root.title("XPaint - Панель управления")
root.resizable(False, False)

topframe = tkinter.Frame(root)
topframe.pack()

tkinter.Label(topframe, text="Управление пером", font=Userfont).pack(padx=5, pady=5)

tkinter.Button(topframe, text="  🢄  ", font=Userfont, command=Mov.upleft).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(topframe, text="  🢁  ", font=Userfont, command=Mov.up).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(topframe, text="  🢅  ", font=Userfont, command=Mov.upright).pack(side=tkinter.LEFT, padx=5, pady=5)

centerframe = tkinter.Frame(root)
centerframe.pack()

tkinter.Button(centerframe, text="  🢀  ", font=Userfont, command=Mov.left).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(centerframe, text="  🪶  ", font=Userfont, command=Layer.CnahgeLayers).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(centerframe, text="  🢂  ", font=Userfont, command=Mov.right).pack(side=tkinter.LEFT, padx=5, pady=5)

bottomframe = tkinter.Frame(root)
bottomframe.pack()

tkinter.Button(bottomframe, text="  🢇  ", font=Userfont, command=Mov.downleft).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(bottomframe, text="  🢃  ", font=Userfont, command=Mov.down).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(bottomframe, text="  🢆  ", font=Userfont, command=Mov.downright).pack(side=tkinter.LEFT, padx=5, pady=5)

specframe = tkinter.Frame(root)
specframe.pack()
tkinter.Button(specframe, text=" Закрыть приложение ", font=Userfont, bg="#FFE0E0", fg="#A40000", command=exit).pack(side=tkinter.LEFT, padx=5, pady=5)

speedframe = tkinter.Frame(root)
speedframe.pack()

tkinter.Label(speedframe, text="", font=Userfont).pack(padx=5, pady=5)
tkinter.Label(speedframe, text="Шаг пера", font=Userfont).pack(padx=5, pady=5)

tkinter.Button(speedframe, text="   10   ", font=Userfont, bg="#7AE7FF", command=Penspeed10).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(speedframe, text="   20   ", font=Userfont, bg="#4BFF93", command=Penspeed20).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(speedframe, text="   30   ", font=Userfont, bg="#E0FF25", command=Penspeed30).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(speedframe, text="   40   ", font=Userfont, bg="#FFC700", command=Penspeed40).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(speedframe, text="   50   ", font=Userfont, bg="#FF823C", command=Penspeed50).pack(side=tkinter.LEFT, padx=5, pady=5)

extraframe = tkinter.Frame(root)
extraframe.pack()

tkinter.Label(extraframe, text=" ", font=Userfont).pack(padx=5, pady=5)
tkinter.Button(extraframe, text=" Начать заливку ", font=Userfont, command=turtle.begin_fill).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(extraframe, text=" Очистить холст ", font=Userfont, command=turtle.clear).pack(side=tkinter.LEFT, padx=5, pady=5)
tkinter.Button(extraframe, text=" Закончить заливку ", font=Userfont, command=turtle.end_fill).pack(side=tkinter.LEFT, padx=5, pady=5)

extraframe2 = tkinter.Frame(root)
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
tkinter.Button(extraframe2, text="      ", font=Userfont, command=Color.gray, bg="#D9D9D9").pack(side=tkinter.LEFT, padx=5, pady=5)

root.mainloop()