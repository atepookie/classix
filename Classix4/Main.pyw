from turtle import *
from subprocess import getoutput
import os
import sys
from url_downloader import save_file

from Files import User
from Files import Mov
from Files import Pig

ht()

User.resx = int(textinput("Classix Setup", "Enter screen width:"))
User.resy = int(textinput("Classix Setup", "Enter screen height:"))
User.name = textinput("Classix Setup", "Your name:")
User.color = textinput("Classix Setup", "Interface color:")
User.bg = textinput("Classix Setup", "Background color:")
User.bgtext = ""
User.speed = int(textinput("Classix Setup", "Interface rendering speed: (0 - fastest)"))
User.fontsize = int(textinput("Classix Setup", "System font size: (standard = 10)"))

while True:
    setup(width = User.resx + 20, height = User.resy + 20)
    title(User.name + "'s session")
    color(User.color)
    bgcolor(User.bg)
    speed(User.speed)

    clear()

    Pig.window(User.resx, User.resy, "Classix")

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

    up()
    temp_position143 = position()
    goto(User.resx / 2 - 9, -User.resy / 2 + 9)
    down()
    write("Enter a command into the opened console", align="right", font=("Verdana", User.fontsize, "bold"))
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

            Pig.indent(0, 39)
            write("Put the required file to the 'Files\\' folder", align="left", font=("Verdana", User.fontsize, "normal"))

            Pig.indent(0,19)
            Pig.icon("exit")

            console = textinput("Console", "Enter a command:")

            if console == "exit" or str(console) == "None" or console == "":
                break

            else:
                clear()
                __import__("Files." + console)
                del sys.modules["Files." + console]

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
        Pig.window(500, 320, "files in the 'Files\\' folder")
        goto(-500 / 2 + 19, -320 / 2 + 19)

        if os.system == "nt":
            write(os.path.dirname(os.path.abspath(__file__)) + "\\Files\\\n\n" + getoutput("dir '" + os.path.dirname(os.path.abspath(__file__)) + "\\Files\\' /B"), align="left", font=("Verdana", User.fontsize, "normal"))
        
        else:
            write(os.path.dirname(os.path.abspath(__file__)) + "/Files/\n\n" + getoutput("ls '" + os.path.dirname(os.path.abspath(__file__)) + "/Files/'"), align="left", font=("Verdana", User.fontsize, "normal"))
        
        textinput("", "Press OK or CANCEL to exit")

    elif console == "urlget":
        if os.system == "nt":
            save_file(url=str(textinput("URL File Downloader", "Enter file URL to download it:")), file_path=os.path.dirname(os.path.abspath(__file__)) + "\\Files\\", file_name=str(textinput("URL File Downloader", "Enter file name:")))
        
        else:
            save_file(url=str(textinput("URL File Downloader", "Enter file URL to download it:")), file_path=os.path.dirname(os.path.abspath(__file__)) + "/Files/", file_name=str(textinput("URL File Downloader", "Enter file name:")))

        textinput("Success!", "File download complete!")

    else:
        Pig.window(400, 120, "error")

        Pig.indent(19, 39)
        write("Error!", align="left", font=("Verdana", User.fontsize, "bold"))

        Pig.indent(0, 39)
        write(str(console) + " isn't a command or application", align="left", font=("Verdana", User.fontsize, "normal"))
                
        textinput("", "Press OK or CANCEL to continue")