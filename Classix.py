import turtle
from turtle import *
ink = Turtle()

import datetime

import os

import time

class system:
    time = datetime.datetime.now().strftime("%H:%M")
    name = "Classix"
    version = "1.0"
    author = "Kotov Yaroslaw"
    font = "Manrope"
    fontsize = 8
    speed = 0 # ОСТАВЬТЕ 0 ДЛЯ МАКСИМАЛЬНОЙ СКОРОСТИ
    
    def title(name):
        if os.name == "nt":
            os.system("title " + name)
            
        else:
            0
            
    def clear():
        if os.name == "nt":
            os.system("cls")
            
        else:
            os.system("clear")
    
class r:
    def setstd():
        turtle.title(system.name)
        turtle.setup(660, 500)
        ink.speed(system.speed)
        ink.ht()
        
    def stdpos():
        ink.up()
        ink.setpos(-320, 240)
        ink.down()
        ink.setpos(-320, -240)
        ink.setpos(320, -240)
        ink.setpos(320, 240)
        ink.setpos(-320, 240)
        
    def left(number):
        ink.left(180)
        ink.forward(int(number))
        ink.left(180)
        
    def right(number):
        ink.forward(int(number))
        
    def up(number):
        ink.left(90)
        ink.forward(int(number))
        ink.right(90)
        
    def down(number):
        ink.right(90)
        ink.forward(int(number))
        ink.left(90)
        
    def indent(number):
        ink.up()
        ink.forward(int(number))
        ink.right(90)
        ink.forward(int(number))
        ink.left(90)
        ink.down()
        
    def enter(number):
        ink.up()
        ink.right(90)
        ink.forward(int(number))
        ink.left(90)
        
class icon:
    def file(text):
        ink.down()
        r.right(24)
        for i in range(8):
            r.down(1)
            r.right(1)
        r.down(24)
        r.left(32)
        r.up(32)
        ink.up()
        r.right(24)
        ink.down()
        r.down(8)
        r.right(8)
        ink.up()
        r.down(24)
        r.left(32)
        ink.up()
        
        r.down(10)
        r.down(system.fontsize * 2)
        ink.write(str(text), align="left", font=(system.font , system.fontsize, "bold"))
        
    def trash(text):
        ink.up()
        r.down(7)
        ink.down()
        r.right(11)
        r.up(2)
        r.right(9)
        r.down(2)
        r.right(12)
        ink.up()
        r.down(2)
        r.left(3)
        ink.down()
        for i in range(4):
            r.down(6)
            r.left(1)
        r.left(20)
        for i in range(4):
            r.up(6)
            r.left(1)
        ink.up()
        r.down(24)
        
        r.down(10)
        r.down(system.fontsize * 2)
        ink.write(str(text), align="left", font=(system.font , system.fontsize, "bold"))
        
class gui:
    def topbar(text):
        r.stdpos()
        ink.begin_fill()
        r.right(640)
        r.down(20)
        r.left(20)
        ink.write(system.time, align="right", font=(system.font , int(system.fontsize)))
        r.left(300)
        ink.write(text, align="center", font=(system.font , int(system.fontsize)))
        r.left(300)
        ink.write(system.name, align="left", font=(system.font , int(system.fontsize), "bold"))
        r.left(20)
        r.up(20)
        ink.color("white")
        ink.end_fill()
        ink.color("black")
        ink.up()
        r.down(20)
        ink.down()
    
    def title(text):
        ink.up()
        r.down(system.fontsize * 1.5 * 2)
        ink.write(str(text), align="left", font=(system.font , int(system.fontsize * 1.5), "bold"))
        
    def text(text):
        ink.up()
        r.down(system.fontsize * 2)
        ink.write(str(text), align="left", font=(system.font , system.fontsize))
        
    def bold(text):
        ink.up()
        r.down(system.fontsize * 2)
        ink.write(str(text), align="left", font=(system.font , system.fontsize, "bold"))
        
    def button(text):
        width = len(text) * system.fontsize + 10
        ink.down()
        
        r.down(20)
        r.right(width / 2)
        ink.write(str(text), align="center", font=(system.font , int(system.fontsize), "bold"))
        r.right(width / 2)
        r.up(20)
        r.left(width)
        
        ink.up()
        r.down(20)
        ink.down()
        
    def window(title):
        ink.up()
        ink.setpos(-160, 120)
        ink.down()
        ink.begin_fill()
        ink.setpos(-160, -120)
        ink.setpos(160, -120)
        ink.setpos(160, 120)
        ink.setpos(-160, 120)
        ink.color("white")
        ink.end_fill()
        ink.color("black")
        
        ink.begin_fill()
        r.down(20)
        r.right(160)
        ink.color("white")
        ink.write(str(title), align="center", font=(system.font , system.fontsize, "bold"))
        ink.color("black")
        r.right(160)
        r.up(20)
        r.left(320)
        ink.end_fill()
        
        ink.up()
        r.down(20)
        
    def menu(text):
        ink.down()
        r.right(320)
        r.down(20)
        r.left(310)
        ink.write(text, align="left", font=(system.font , int(system.fontsize)))
        r.left(10)
        r.up(20)
        ink.up()
        r.down(20)
        ink.down()
    
r.setstd()
r.stdpos()

gui.topbar("Предупреждение: не закрывайте консоль!")
r.indent(20)

gui.title("Добро пожаловать в " + system.name + "!")
r.enter(10)

gui.text("Давайте приступим к первоначальной настройке системы!")
r.enter(20)

gui.bold("1. введите шрифт системы, который хотите использовать (рекомендуем: Manrope)")

gui.bold("2. введите размер шрифта системы (рекомендуем: 8)")

gui.bold("3. введите скорость отрисовки интерфейса системы (самое быстрое значение: 0)")
r.enter(20)

gui.button("Примечание: для ввода значений используйте открывшуюся консоль.")

system.title("Сделайте выбор!")
system.font = input("1. введите шрифт системы, который хотите использовать (рекомендуем: Manrope): ")
system.fontsize = int(input("2. введите размер шрифта системы (рекомендуем: 8): "))
system.speed = int(input("3. введите скорость отрисовки интерфейса системы (самое быстрое значение: 0): "))

system.clear()
system.title("Вернитесь в " + system.name)
print("Теперь вы можете вернуться в интерфейс " + system.name)

while True: 
    ink.clear()
    r.setstd()
    r.stdpos()
    
    gui.topbar("Workspace")
    r.indent(20)
    
    gui.button("введите название файла в консоль, чтобы его открыть")
    r.enter(20)
    
    icon.file("help.txt")
    r.enter(20)
    
    icon.trash("корзина")
    r.enter(20)
    
    system.title("Сделайте выбор!")
    console = input("введите название файла: ")
    
    system.clear()
    gui.topbar(console)
    
    if console == "help.txt":
        system.title("Вернитесь в " + system.name)
        gui.window(console)
        gui.menu("Количество слов: 8")
        r.indent(20)
        
        gui.title("Добро пожаловать!")
        r.enter(10)
        
        gui.text("Спасибо, за то что используете Classix!")
        r.enter(10)
        
        gui.text("Скоро здесь появятся подсказки.")
        gui.text("Свои идеи пишите на t.me/skibidiwc")
        
    elif console == "корзина":
        system.title("Вернитесь в " + system.name)
        gui.window(console)
        gui.menu("Количество объектов в корзине: 0")
        r.indent(20)
        
        gui.text("В корзине ничего нет.")
        
    input()