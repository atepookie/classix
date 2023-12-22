import os
from turtle import *

setup (width=820, height=620)
ht()

class User:
    name = "Guest"
    color = "black"
    bg = "white"
    speed = 0
    fontsize = 10

class  Mov:
    def up(number):
        sety(ycor() + int(number))

    def down(number):
        sety(ycor() - int(number))

    def left(number):
        setx(xcor() - int(number))

    def right(number):
        setx(xcor() + int(number))

class Pig:
    def borders():
        up()
        goto(-401, 301)
        down()
        goto(401, 301)
        goto(401, -301)
        goto(-401, -301)
        goto(-401, 301)

    def menu(text):
        down()
        color(User.color)
        begin_fill()
        Mov.right(802)
        Mov.down(21)
        Mov.left(401)
        color(User.bg)
        write(text, align="center", font=("Verdana", User.fontsize, "bold")) 
        color(User.color)
        Mov.left(401)
        Mov.up(21)
        end_fill()
        up()
        Mov.down(21)

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
        write("  " + text, align="left", font=("Verdana", User.fontsize, "normal"))
        Mov.left(19)
        Mov.up(19)
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



User.name = textinput("Classix Setup", "Your name:")
User.color = textinput("Classix Setup", "Interface color:")
User.bg = textinput("Classix Setup", "Background color:")
User.speed = int(textinput("Classix Setup", "Interface rendering speed: (0 - fastest)"))
User.fontsize = int(textinput("Classix Setup", "System font size: (standard = 10)"))

title(User.name + "'s session")
color(User.color)
bgcolor(User.bg)
speed(User.speed)

while True:
    clear()

    Pig.borders()
    Pig.menu("Classix Desktop")

    Pig.indent(19, 19)
    Pig.icon("exit")

    Pig.indent(0, 19)
    Pig.icon("settings")

    Pig.indent(0, 19)
    Pig.icon("help")

    Pig.indent(0, 34)
    write("Enter command into the opened console", align="left", font=("Verdana", User.fontsize, "bold"))

    Pig.indent(0,19)

    console = textinput("Console", "Enter a command:")

    if console == "exit":
        break

    elif console == "settings":
        while True:
            Pig.window(400, 320, "settings")

            Pig.indent(19, 39)
            write("Settings", align="left", font=("Verdana", User.fontsize, "bold"))

            Pig.indent(0, 19)
            Pig.icon("exit")

            Pig.indent(0, 19)
            Pig.icon("1. change user name")

            Pig.indent(0, 19)
            Pig.icon("2. change interface color")

            Pig.indent(0, 19)
            Pig.icon("3. change background color")

            Pig.indent(0, 19)
            Pig.icon("4. change interface rendering speed")

            Pig.indent(0, 19)
            Pig.icon("5. change font size")

            console = textinput("Console", "Enter a command:")

            if console == "exit":
                break
            
            elif console == "1":
                User.name = textinput("Classix Setup", "Your name:")
                title(User.name + "'s session")

            elif console == "2":
                User.color = textinput("Classix Setup", "Interface color:")
                color(User.color)

            elif console == "3":
                User.bg = textinput("Classix Setup", "Background color:")
                bgcolor(User.bg)

            elif console == "4":
                User.speed = int(textinput("Classix Setup", "Interface rendering speed: (0 - fastest)"))
                speed(User.speed)

            elif console == "5":
                User.fontsize = int(textinput("Classix Setup", "System font size: (standard = 10)"))

            else:
                Pig.window(400, 120, "error")

                Pig.indent(19, 39)
                write("Error!", align="left", font=("Verdana", User.fontsize, "bold"))

                Pig.indent(0, 39)
                write(str(console) + " isn't a command or application", align="left", font=("Verdana", User.fontsize, "normal"))
                
                textinput("", "Press OK or CANCEL to continue")

    elif console == "help":
        while True:
            Pig.window(400, 320, "help")

            Pig.indent(19, 39)
            write("Help", align="left", font=("Verdana", User.fontsize, "bold"))

            Pig.indent(0, 29)
            write("Welcome to Classix!", align="left", font=("Verdana", User.fontsize, "normal"))

            Pig.indent(0, 19)
            write("Author: Yaroslaw Kotov", align="left", font=("Verdana", User.fontsize, "normal"))

            Pig.indent(0, 19)
            write("Version: 2.0", align="left", font=("Verdana", User.fontsize, "normal"))

            Pig.indent(0,19)
            Pig.icon("exit")

            console = textinput("Console", "Enter a command:")

            if console == "exit":
                break

            else:
                Pig.window(400, 120, "error")

                Pig.indent(19, 39)
                write("Error!", align="left", font=("Verdana", User.fontsize, "bold"))

                Pig.indent(0, 39)
                write(str(console) + " isn't a command or application", align="left", font=("Verdana", User.fontsize, "normal"))
                
                textinput("", "Press OK or CANCEL to continue")

    else:
        Pig.window(400, 120, "error")

        Pig.indent(19, 39)
        write("Error!", align="left", font=("Verdana", User.fontsize, "bold"))

        Pig.indent(0, 39)
        write(str(console) + " isn't a command or application", align="left", font=("Verdana", User.fontsize, "normal"))
                
        textinput("", "Press OK or CANCEL to continue")