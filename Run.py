from turtle import *
from time import sleep
from random import randint
t1 = Turtle()
t2 = Turtle()
t3 = Turtle()
w = 200
h = 200
t1.color('green')
t2.color('red')
t3.color('blue')
t1.shape('turtle')
t2.shape('turtle')
t3.shape('turtle')
t1.width(5)
t2.width(5)
t3.width(5)
t2.left(120)
t3.left(-120)
def tangkap1(x, y):
    t1.penup()
    t1.goto(randint(-100,100),randint(-100,100))
    t1.pendown()
    t1.left(randint(0, 180))
def tangkap2(x, y):
    t2.penup()
    t2.goto(randint(-100,100),randint(-100,100))
    t2.pendown()
    t2.left(randint(0, 180))
def tangkap3(x, y):
    t3.penup()
    t3.goto(randint(-100,100),randint(-100,100))
    t3.pendown()
    t3.left(randint(0, 180))
t1.onclick(tangkap1)
t2.onclick(tangkap2)
t3.onclick(tangkap3)
def GameSelesai(t1, t2, t3):
    t1_luar = abs(t1.xcor()) > w or abs(t1.ycor()) > h
    t2_luar = abs(t2.xcor()) > w or abs(t2.ycor()) > h
    t3_luar = abs(t3.xcor()) > w or abs(t3.ycor()) > h
    diluar = t1_luar or t2_luar or t3_luar
    return diluar
while GameSelesai(t1, t2, t3) != True:
    t1.forward(7)
    t2.forward(7)
    t3.forward(7)
    sleep(0.1)
t1.clear()
t2.clear()
t3.clear()
t1.penup()
t1.goto(-30, 0)
t1.write('Goodbye!',font=('Arial', 16,'bold'))
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
exitonclick()