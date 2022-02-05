#!/usr/bin/env python3
import matplotlib.pyplot as plt
from random import randint
def f1(x,y):
    return (x/2,y/2)
def f2(x,y):
    return ((x+1)/2,y/2)
def f3(x,y):
    return (x/2,(y+1)/2)
x=[0,1,0]
y=[0,0,1]
for i in range(10000):
    r=randint(1,3)
    if r == 1:
        c=f1(x[-1],y[-1])
        x.append(c[0])
        y.append(c[1])
    elif r == 2:
        c=f2(x[-1],y[-1])
        x.append(c[0])
        y.append(c[1])
    elif r == 3:
        c=f3(x[-1],y[-1])
        x.append(c[0])
        y.append(c[1])

# plotting the points
plt.scatter(x, y, s=0.2, c='g')


# giving a title to my graph
plt.title('Triangle de Sierpinski')

# function to show the plot
plt.show()
