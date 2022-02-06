#!/usr/bin/env python3
from random import randint
import matplotlib.pyplot as plt
def f1(x,y):
    return ((x-y)/2,(x+y)/2)

def f2(x,y):
    return ((x+y)/2+1/2,-(x-y)/2+1/2)

x=[0]
y=[0]
for i in range(100000):
    r = randint(1,2)
    if r == 1:
        c = f1(x[-1],y[-1])
        x.append(c[0])
        y.append(c[1])
    else:
        c = f2(x[-1],y[-1])
        x.append(c[0])
        y.append(c[1])
# plotting the points
plt.scatter(x, y, s=0.2, c='g')


# giving a title to my graph
plt.title('Lévy')

# function to show the plot
plt.show()
