#!/usr/bin/env python3
from turtle import *

def f1(x,y):
    return ((x-y)/2,(x+y)/2)

def f2(x,y):
    return ((x+y)/2+1/2,-(x-y)/2+1/2)

width(1)
color("red")
x=10
y=20
for i in range(100):
    penup()
    (x,y) = f1(x,y)
    (x,y) = f2(x,y)
    goto(x,y)
    pendown()
    dot()
done()
