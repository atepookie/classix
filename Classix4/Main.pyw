from turtle import *
from subprocess import getoutput
import os
import sys
import importlib

from url_downloader import save_file

class Mov:
    def up(number):
        sety(ycor() + int(number))

    def down(number):
        sety(ycor() - int(number))

    def left(number):
        setx(xcor() - int(number))

    def right(number):
        setx(xcor() + int(number))

class Pig:
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

ht()

Username = textinput("Auth method", "Enter your name to login or leave the field blank to create an account")

if Username == "" or str(Username) == "None":
    if os.name == "nt":
        textinput("Error", "Your device doesn't support this feature")

    else:        
        with open(os.path.dirname(os.path.abspath(__file__)) + "" + textinput("Create an account", "Enter your name:") + ".py", "w") as file:
            file.write("resx = " + textinput("Create an account", "Set screen width:") + "\nresy = " + textinput("Create an account", "Set screen height:") +"\ncolor = \"" + textinput("Create an account", "Set system color:") + "\"\nbg = \"" + textinput("Create an account", "Set background color:") + "\"\nbgtext = \"" + textinput("Create an account", "Set background text:") + "\"\nfontsize = " + textinput("Create an account", "Set font size:\n\nstandard - 10"))
        textinput("Create an account", "You've successfully created an account!")
    
        
    sys.exit()

else:
    User = importlib.import_module(Username)

while True:
    setup(width = User.resx + 20, height = User.resy + 20)
    title(Username + "'s session")
    color(User.color)
    bgcolor(User.bg)
    speed(0)

    clear()

    Pig.window(User.resx, User.resy, "Development is temporarily stopped!") # Classix

    up()
    goto(0, 0)
    color(User.color)
    down()
    write(User.bgtext, align="center", font=("Verdana", User.fontsize * 3, "normal"))
    up()
    goto(- User.resx / 2 - 1, User.resy / 2 + 1)
    Mov.down(21)
    
    Pig.indent(19, 19)
    Pig.icon("exit")

    Pig.indent(0, 19)
    Pig.icon("settings")

    Pig.indent(0, 19)
    Pig.icon("help")

    Pig.indent(0, 19)
    Pig.icon("background")

    Pig.indent(0, 19)
    Pig.icon("runout")

    Pig.indent(0, 19)
    Pig.icon("console")

    Pig.indent(0, 19)
    Pig.icon("files")

    Pig.indent(0, 19)
    Pig.icon("urlget")

    Pig.indent(0, 19)
    Pig.icon("relogin")

    up()
    temp_position143 = position()
    goto(User.resx / 2 - 9, -User.resy / 2 + 9)
    down()
    write("Enter a command into the opened console\n\nDevelopment is temporarily stopped!", align="right", font=("Verdana", User.fontsize, "bold"))
    up()
    goto(temp_position143)

    Pig.indent(0,19)

    console = textinput("Console", "Enter a command:")

    if console == "exit" or str(console) == "None" or console == "":
        break

    elif console == "settings":
        while True:
            Pig.window(400, 400, "settings")

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

            Pig.indent(0, 19)
            Pig.icon("6. change screen width")

            Pig.indent(0, 19)
            Pig.icon("7. change screen height")

            console = textinput("Console", "Enter a command:")

            if console == "exit" or str(console) == "None" or console == "":
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

            elif console == "6":
                User.resx = int(textinput("Classix Setup", "Enter screen width:"))                

            elif console == "7":
                User.resy = int(textinput("Classix Setup", "Enter screen height:"))
                

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
            write("Version: 4", align="left", font=("Verdana", User.fontsize, "normal"))

            Pig.indent(0,19)
            Pig.icon("exit")

            console = textinput("Console", "Enter a command:")

            if console == "exit" or str(console) == "None" or console == "":
                break

            else:
                Pig.window(400, 120, "error")

                Pig.indent(19, 39)
                write("Error!", align="left", font=("Verdana", User.fontsize, "bold"))

                Pig.indent(0, 39)
                write(str(console) + " isn't a command or application", align="left", font=("Verdana", User.fontsize, "normal"))
                
                textinput("", "Press OK or CANCEL to continue")

    elif console == "background":
        User.bgtext = textinput("background", "Enter text for background:")

    elif console == "runout":
        while True:
            Pig.window(500, 320, "runout")

            Pig.indent(19, 39)
            write("RunOut", align="left", font=("Verdana", User.fontsize, "bold"))

            Pig.indent(0, 39)
            write("This program allows you to run third-party .PY apps!", align="left", font=("Verdana", User.fontsize, "normal"))

            Pig.indent(0, 19)
            write("Put the required file to the Classix folder", align="left", font=("Verdana", User.fontsize, "normal"))

            Pig.indent(0,19)
            Pig.icon("exit")

            console = textinput("Console", "Enter a command:")

            if console == "exit" or str(console) == "None" or console == "":
                break

            else:
                clear()
                __import__(console)
                del sys.modules[console]

    elif console == "console":
        clear()
        Pig.window(User.resx, User.resy, "Native console environment")



        outlog = ""

        while True:
            console = textinput("Native console", "(Press 'Cancel' to exit)\n\nEnter a command:")

            if console == "exit" or str(console) == "None" or console == "":
                break
            
            clear()
            Pig.window(User.resx, User.resy, "Native console environment")
            goto(-User.resx / 2 + 19, -User.resy / 2 + 19)

            if console != "exit" or str(console) != "None":
                write(str(outlog) + "\n\n" + getoutput(console), align="left", font=("Verdana", User.fontsize -2, "normal"))
                outlog += "\n\n" + getoutput(console)

    elif console == "files":
        Pig.window(500, 320, "Files in the Classix folder")
        goto(-500 / 2 + 19, -320 / 2 + 19)

        if os.name == "nt":
            textinput("Error", "Your device doesn't support this feature")

        else:
            write(os.path.dirname(os.path.abspath(__file__)) + "\n\n" + getoutput("ls '" + os.path.dirname(os.path.abspath(__file__)) + "'"), align="left", font=("Verdana", User.fontsize, "normal"))
            textinput("", "Press OK or CANCEL to exit")
            

    elif console == "urlget":
        if os.name == "nt":
            textinput("Error", "Your device doesn't support this feature")

        else:
            save_file(url=str(textinput("URL File Downloader", "Enter file URL to download it:")), file_path=os.path.dirname(os.path.abspath(__file__)) + "", file_name=str(textinput("URL File Downloader", "Enter file name:")))
            textinput("Success!", "File download complete!")

    elif console == "relogin":
        del sys.modules[Username]
        Username = textinput("Relogin", "Enter your new account name:")
        User = importlib.import_module(Username)


    else:
        Pig.window(400, 120, "error")

        Pig.indent(19, 39)
        write("Error!", align="left", font=("Verdana", User.fontsize, "bold"))

        Pig.indent(0, 39)
        write(str(console) + " isn't a command or application", align="left", font=("Verdana", User.fontsize, "normal"))
                
        textinput("", "Press OK or CANCEL to continue")