from turtle import *

def up(number):
    sety(ycor() + int(number))

def down(number):
    sety(ycor() - int(number))

def left(number):
    setx(xcor() - int(number))

def right(number):
    setx(xcor() + int(number))