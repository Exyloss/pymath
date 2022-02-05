# importing the required module
import matplotlib.pyplot as plt
from random import randint

def f1(x,y):
    x1=0
    y1=0.16*y
    return (x1,y1)

def f2(x,y):
    x1=0.85*x+0.04*y
    y1=-0.04*x+0.85*y+1.6
    return (x1,y1)

def f3(x,y):
    x1=0.2*x-0.26*y
    y1=0.23*x+0.22*y+1.6
    return (x1,y1)

def f4(x,y):
    x1=-0.15*x+0.28*y
    y1=0.26*x+0.24*y+0.44
    return (x1,y1)

# x axis values
x = [0]
# corresponding y axis values
y = [0]


def fougere(n):
    for i in range(n):
        r=randint(1,100)
        if r == 1:
            v=f1(x[-1],y[-1])
            x.append(v[0])
            y.append(v[1])
        if 2 <= r <= 86:
            v=f2(x[-1],y[-1])
            x.append(v[0])
            y.append(v[1])
        if 87 <= r <= 93:
            v=f3(x[-1],y[-1])
            x.append(v[0])
            y.append(v[1])
        if 94 <= r <= 100:
            v=f4(x[-1],y[-1])
            x.append(v[0])
            y.append(v[1])

fougere(500000)
# plotting the points
plt.scatter(x, y, s=0.2, c='g')


# giving a title to my graph
plt.title('Fougère')

# function to show the plot
plt.show()
