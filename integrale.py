#!/usr/bin/env python3

def integrale_rectangle(f, a, b, n=100000):
    delta = b-a
    largeur = delta/n
    integrale = 0
    for i in range(n):
        integrale += f(a+largeur*i)*largeur
    return integrale

def integrale_trapeze(f, a, b, n=100000):
    delta = b-a
    largeur = delta/n
    integrale = 0
    for i in range(1, n+1):
        integrale += largeur*(f(a+largeur*i)+f(a+largeur*(i-1)))/2
    return integrale

if __name__ == "__main__":
    def f(x):
        return x**2
    print(integrale_rectangle(f, 0, 3))
    print(integrale_trapeze(f, 0, 3))

