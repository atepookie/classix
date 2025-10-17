from turtle import *
from datetime import datetime

ht() # СКРЫТЬ ЧЕРЕПАШКУ
tracer(False) # FALSE = МГНОВЕННАЯ ОТРИСОВКА

class System: # СИСТЕМНЫЕ ПЕРЕМЕННЫЕ
    time = datetime.now().strftime("%H:%M")
    name = "Classix"
    version = "5.0b"
    font = "Arial"
    fontSize = 8
    drawSpeed = 0
    accentColor = (0, 0, 0)
    backgroundColor = "white"

class Render: # ОТРИСОВКА
    def moveLeft(pixels): # ДВИЖЕНИЕ ВЛЕВО
        setx( xcor() - pixels )
    
    def moveRight(pixels): # ДВИЖЕНИЕ ВПРАВО
        setx( xcor() + pixels )
    
    def moveDown(pixels): # ДВИЖЕНИЕ ВНИЗ
        sety( ycor() - pixels )
    
    def moveUp(pixels): # ДВИЖЕНИЕ ВВЕРХ
        sety( ycor() + pixels )

    # home() - ПЕРЕМЕЩЕНИЕ В ЦЕНТР

    def moveBottomLeft(pixels): # ДВИЖЕНИЕ ВЛЕВО-ВНИЗ
        goto(
            xcor() - pixels,
            ycor() - pixels
        )

    def moveBottomRight(pixels): # ДВИЖЕНИЕ ВПРАВО-ВНИЗ
        goto(
            xcor() + pixels,
            ycor() - pixels
        )

    def moveTopLeft(pixels): # ДВИЖЕНИЕ ВЛЕВО-ВВЕРХ
        goto(
            xcor() - pixels,
            ycor() + pixels
        )

    def moveTopRight(pixels): # ДВИЖЕНИЕ ВПРАВО-ВВЕРХ
        goto(
            xcor() + pixels,
            ycor() + pixels
        )

class GUI: # ЭЛЕМЕНТЫ ГРАФИЧЕСКОГО ИНТЕРФЕЙСА
    def blank(selectedColor = None):
        if selectedColor == None:
            selectedColor = "white"

        up()
        bgcolor("black")
        previousColor = pencolor() # ПОЛУЧАЕМ ТЕКУЩИЙ ЦВЕТ
        pencolor(selectedColor)
        fillcolor(selectedColor)
        x, y = screensize() # ПОЛУЧАЕМ РАЗМЕР ОКНА (ЭКРАНА)
        goto( # ВЕРХНИЙ ЛЕВЫЙ УГОЛ ЭКРАНА
            -x / 2,
            y / 2
        )
        down()
        begin_fill() # НАЧАЛЬНАЯ ПОЗИЦИЯ ФОРМЫ ЗАЛИВКИ
        goto( # ВЕРХНИЙ ПРАВЫЙ УГОЛ ЭКРАНА
            x / 2,
            y / 2
        )
        goto( # НИЖНИЙ ПРАВЫЙ УГОЛ ЭКРАНА
            x / 2,
            -y / 2
        )
        goto( # НИЖНИЙ ПРАВЫЙ УГОЛ МЕНЮ
            -x / 2,
            -y / 2
        )
        goto( # ВЕРХНИЙ ЛЕВЫЙ УГОЛ ЭКРАНА
            -x / 2,
            y / 2
        )
        end_fill() # ЗАКОНЧИТЬ ЗАЛИВКУ
        color(previousColor) # ВОЗВРАЩАЕМ ПРЕЖНИЙ ЦВЕТ КУРСОРУ
        
    def menu(text, bgColor, textColor): # ОТРИСОВКА ВЕРХНЕГО МЕНЮ
        up()
        bgcolor("black")
        previousColor = pencolor() # ПОЛУЧАЕМ ТЕКУЩИЙ ЦВЕТ
        pencolor(bgColor) # ЦВЕТ ПЕРА
        fillcolor(bgColor) # ЦВЕТ ЗАЛИВКИ

        x, y = screensize() # ПОЛУЧАЕМ РАЗМЕР ОКНА (ЭКРАНА)
        goto( # ВЕРХНИЙ ЛЕВЫЙ УГОЛ МЕНЮ
            -x / 2,
            y / 2
        )
        down()
        begin_fill()
        goto( # ВЕРХНИЙ ПРАВЫЙ УГОЛ МЕНЮ
            x / 2,
            y / 2
        )
        goto( # НИЖНИЙ ПРАВЫЙ УГОЛ МЕНЮ
            x / 2,
            y / 2 -16 # ОТСТУП ДЛЯ ВЫСОТЫ МЕНЮ (16)
        )
        goto( # НИЖНИЙ ПРАВЫЙ УГОЛ МЕНЮ
            x / 2 -8, # ОТСТУП ДЛЯ ЧАСОВ (8)
            y / 2 -16 # ОТСТУП ДЛЯ ВЫСОТЫ МЕНЮ (16)
        )
        write( # ОТРИСОВКА ЧАСОВ МЕНЮ
            datetime.now().strftime("%H:%M"), # ТЕКСТ: ЧАСЫ
            align = "Right",
            font = (
                System.font,
                System.fontSize,
                "normal",
            )
        )
        goto( # НИЖНИЙ ЛЕВЫЙ УГОЛ МЕНЮ С ОТСТУПОМ ДЛЯ ТЕКСТА
            -x / 2 +8, # ОТСТУП ДЛЯ ТЕКСТА (8)
            y / 2 -16 # ОТСТУП ДЛЯ ВЫСОТЫ МЕНЮ (16)
        )
        write( # ОТРИСОВКА ТЕКСТА МЕНЮ
            text,
            align = "Left",
            font = (
                System.font,
                System.fontSize,
                "bold",
            )
        )
        goto( # НИЖНИЙ ЛЕВЫЙ УГОЛ МЕНЮ
            -x / 2,
            y / 2 -16 # ОТСТУП ДЛЯ ВЫСОТЫ МЕНЮ (16)
        )
        goto( # ВЕРХНИЙ ЛЕВЫЙ УГОЛ МЕНЮ
            -x / 2,
            y / 2
        )

class Windows: # РАБОТА С ОТКРЫТЫМИ ОКНАМИ
    list = {}
    active = ""

setup(810, 610) # РЕГУЛИРУЕТ РАЗМЕР ОКНА
screensize(800, 600) # РЕГУЛИРУЕТ РАЗМЕР ХОЛСТА
title("") # ЗАГОЛОВОК ОКНА
colormode(255) # ЦВЕТОВОЙ РЕЖИМ ОТ 0 ДО 255

Render.moveUp(100)
Render.moveTopRight(100)
Render.moveRight(100)
Render.moveBottomRight(100)
Render.moveDown(100)
Render.moveBottomLeft(100)
Render.moveLeft(100)
Render.moveTopLeft(100)

GUI.blank()
GUI.menu("Добро пожаловать!")

update() # ОБНОВЛЕНИЕ КАДРА
done() # ПОЗВОЛЯЕТ НЕ ЗАКРЫВАТЬ ОКНО