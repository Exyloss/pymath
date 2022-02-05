#!/usr/bin/env python3
from math import sin,cos
import matplotlib.pyplot as plt
def ikeda(x,y,u):
    t=0.4-6/(1+x**2+y**2)
    x1=1+u*(x*cos(t)-y*sin(t))
    y1=u*(x*sin(t)+y*cos(t))
    return (x1,y1)
x=[0]
y=[0]
u=float(input("u = "))
for i in range(50000):
    n=ikeda(x[-1],y[-1],u)
    x.append(n[0])
    y.append(n[1])
plt.scatter(x, y, s=0.2, c='g')

# giving a title to my graph
plt.title('Ikéda')

# function to show the plot
plt.show()
