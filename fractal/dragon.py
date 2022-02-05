#!/usr/bin/env python3
from turtle import *
droite="d"
gauche="g"
p=droite
def inv(p):
    new_p=""
    for i in p:
        if i == droite:
            new_p=gauche+new_p
        else:
            new_p=droite+new_p
    return new_p
def pliage(p):
    new_p=p+droite+inv(p)
    return new_p

for i in range(10):
    p=pliage(p)

bgcolor("black")
penup()
turtlesize(0.01)
goto(0,100)
color("red")
pendown()
speed(0)
width(1)

for j in p:
    forward(5)
    if j == "d":
        right(90)
    else:
        left(90)

done()
