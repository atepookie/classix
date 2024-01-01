from turtle import textinput

clicked = 0

while True:
    if textinput("CLICKER", "You clicked the 'OK' button " + str(clicked) + " times") == "":
        clicked += 1

    else:
        break