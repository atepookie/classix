import turtle
from turtle import *
ink = Turtle()

import datetime

import os

import time

import sys

class system:
    time = datetime.datetime.now().strftime("%H:%M")
    name = "Classix"
    version = "2.0"
    author = "Ярослав Котов"
    font = "Manrope"
    fontsize = 8
    speed = 0 # ОСТАВЬТЕ 0 ДЛЯ МАКСИМАЛЬНОЙ СКОРОСТИ
    background = "default"
    
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
    def togui():
        system.title("Вернитесь в " + system.name)
        turtle.title(system.name)
        
        
    def tocli():
        system.title("Сделайте выбор!")
        turtle.title("Окно консоли ожидает...")
        
        
    def setstd():
        r.togui()
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
        ink.setpos(ink.xcor() - number , ink.ycor())
        
    def right(number):
        ink.setpos(ink.xcor() + number , ink.ycor())
        
    def up(number):
        ink.setpos(ink.xcor(), ink.ycor() + number)
        
    def down(number):
        ink.setpos(ink.xcor(), ink.ycor() - number)
        
    def indent(number):
        ink.up()
        ink.setpos(ink.xcor() + number, ink.ycor())
        ink.setpos(ink.xcor(), ink.ycor() - number)
        ink.down()
        
    def enter(number):
        ink.up()
        ink.setpos(ink.xcor(), ink.ycor() - number)
        ink.down()
        
    def topleft():
        ink.setpos(-320, 240)
        
    def topright():
        ink.setpos(320, 240)
        
    def bottomleft():
        ink.setpos(-320, -240)
        
    def bottomright():
        ink.setpos(320, -240)
        
        
class icon:
    def file(text):
        ink.down()
        r.right(31)
        r.down(31)
        r.left(31)
        r.up(31)
        
        ink.up()
        r.right(7)
        r.down(3)
        
        ink.down()
        r.right(12)
        
        for i in range(5):
            r.down(1)
            r.right(1)
            
        r.down(20)
        r.left(17)
        r.up(25)
        r.right(11)
        
        r.down(6)
        r.right(6)
        
        ink.up()
        r.left(24)
        r.down(22)
        
        ink.up()
        r.down(4)
        r.down(system.fontsize * 2)
        ink.down()
        ink.write(str(text), align="left", font=(system.font , system.fontsize, "bold"))
        ink.up()
        
    def trash(text):
        ink.down()
        r.right(31)
        r.down(31)
        r.left(31)
        r.up(31)
        
        ink.up()
        r.right(5)
        r.down(5)
        
        ink.down()
        r.right(8)
        r.up(2)
        r.right(5)
        r.down(2)
        r.right(8)
        r.down(1)
        
        ink.up()       
        r.down(2)
        r.left(2)
        
        ink.down()
        r.down(20)
        r.left(17)
        r.up(21)
        
        ink.up()
        r.left(7)
        r.down(25)
        
        ink.up()
        r.down(4)
        r.down(system.fontsize * 2)
        ink.down()
        ink.write(str(text), align="left", font=(system.font , system.fontsize, "bold"))
        ink.up()
        
    def base(text):
        ink.down()
        r.right(31)
        r.down(31)
        r.left(31)
        r.up(31)
        
        ink.up()
        r.down(31)
        r.down(4)
        r.down(system.fontsize * 2)
        ink.down()
        ink.write(str(text), align="left", font=(system.font , system.fontsize, "bold"))
        ink.up()
        
class gui:
    def topbar(text):
        r.stdpos()
        ink.begin_fill()
        ink.color("black")
        r.right(640)
        r.down(20)
        r.left(20)
        ink.color("white")
        ink.write(system.time, align="right", font=(system.font , int(system.fontsize)))
        ink.color("black")
        r.left(300)
        ink.color("white")
        ink.write(text, align="center", font=(system.font , int(system.fontsize)))
        ink.color("black")
        r.left(300)
        ink.color("white")
        ink.write(system.name, align="left", font=(system.font , int(system.fontsize), "bold"))
        ink.color("black")
        r.left(20)
        ink.end_fill()
        r.up(20)
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
        r.left(300)
        ink.write(text, align="left", font=(system.font , int(system.fontsize)))
        r.left(20)
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

r.tocli()
system.font = input("1. введите шрифт системы, который хотите использовать (рекомендуем: Manrope): ")
system.fontsize = int(input("2. введите размер шрифта системы (рекомендуем: 8): "))
system.speed = int(input("3. введите скорость отрисовки интерфейса системы (самое быстрое значение: 0): "))

system.clear()
r.togui()
print("Теперь вы можете вернуться в интерфейс " + system.name)

while True: 
    ink.clear()
    r.setstd()
    r.stdpos()
    
    gui.topbar("введите название файла в консоль, чтобы его открыть")
    r.indent(30)
    
    icon.file("выключить")
    r.enter(20)
    
    icon.file("справка")
    r.enter(20)
    
    icon.file("что нового?")
    r.enter(20)
    
    icon.trash("корзина")
    r.enter(20)
    
    r.tocli()
    console = input("введите название файла: ")
    
    system.clear()
    r.togui()
    
    ink.clear()
    gui.topbar(console)
    
    if console == "справка":
        r.togui()
        gui.window(console)
        gui.menu("ClassiX info")
        r.indent(20)
        
        gui.bold("Спасибо, за то что используете Classix!")
        r.enter(10)
        
        gui.text("текущее время: " + system.time)
        gui.text("имя системы: " + system.name)
        gui.text("версия системы: " + system.version)
        gui.text("автор: " + system.author)
        gui.text("шрифт по умолчанию: " + system.font)
        gui.text("размер шрифта: " + str(system.fontsize))
        gui.text("скорость отрисовки: " + str(system.speed))
        r.enter(10)
        
        gui.bold("t.me/skibidiwc")
        
    elif console == "корзина":
        r.togui()
        gui.window(console)
        gui.menu("Количество объектов в корзине: 0")
        r.indent(20)
        
        gui.text("В корзине ничего нет.")
        
    elif console == "выключить":
        sys.exit()
        
    elif console == "что нового?":
        r.setstd()
        r.indent(20)
        
        gui.title("Что нового?")
        r.enter(10)
        
        gui.text("Добро пожаловать! В этом приложении вы сможете узнать о новых функциях")
        
    else:
        r.togui()
        gui.window(console)
        r.indent(20)
        
        gui.title("Ошибка")
        r.enter(10)
        
        gui.text("Введённый текст не является командой.")
        r.enter(20)
        
        gui.button("чтобы закрыть окно, нажмите ENTER")
        
    input("Приложение завершило свою работу. Нажмите Enter для продолжения\n")