from turtle import *
from . import Mov
from . import User

def exitonclick():
    up()
    goto(400, -300)
    write("Click to exit", align="right", font=("Verdana", User.fontsize, "bold"))
    exitonclick()

def indent(x, y):
    up()
    Mov.down(int(y))
    Mov.right(int(x))
    down()

def icon(text):
    down()
    Mov.right(19)
    Mov.down(19)
    begin_fill()
    write("  " + text, align="left", font=("Verdana", User.fontsize, "normal"))
    Mov.left(19)
    Mov.up(19)
    end_fill()
    Mov.down(19)

def window(x, y, title):        
    up()
    goto(- x / 2 - 1, y / 2 + 1)
    down()
    begin_fill()
    goto(x / 2 + 1, y / 2 + 1)
    goto(x / 2 + 1, -y / 2 - 1)
    goto(- x / 2 - 1, -y / 2 - 1)
    goto(- x / 2 - 1, y / 2 + 1)
    color(User.bg)
    end_fill()
    color(User.color)
    begin_fill()
    Mov.right(x + 2)
    Mov.down(21)
    Mov.left(x / 2 + 1)
    color(User.bg)
    write(title, align="center", font=("Verdana", User.fontsize, "bold"))
    color(User.color)
    Mov.left(x / 2 + 1)
    Mov.up(21)
    end_fill()
    Mov.down(21)
    up()