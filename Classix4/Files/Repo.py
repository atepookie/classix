from turtle import textinput, write
from . import User
from . import Mov
from . import Pig

while True:
    Pig.window(User.resx, User.resy, "Магазин приложений для Classix!")

    console = textinput("Repo", "Enter a command:")

    if console == "exit" or str(console) == "None":
        break

    else:
        Pig.window(400, 120, "error")

        Pig.indent(19, 39)
        write("Error!", align="left", font=("Verdana", User.fontsize, "bold"))

        Pig.indent(0, 39)
        write(str(console) + " isn't a command or application", align="left", font=("Verdana", User.fontsize, "normal"))
                
        textinput("", "Press OK or CANCEL to continue")