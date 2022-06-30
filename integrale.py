#!/usr/bin/env python3

def integrale_rectangle(f, a, b, n=100000):
    """
    f: fonction à intégrer
    a: début de d'intégrale
    b: fin de l'intégrale
    n: nombre de rectangles
    """
    delta = b-a
    largeur = delta/n
    integrale = 0
    for i in range(n):
        integrale += f(a+largeur*i)*largeur
    return integrale

def integrale_trapeze(f, a, b, n=100000):
    """
    f: fonction à intégrer
    a: début de d'intégrale
    b: fin de l'intégrale
    n: nombre de rectangles
    """
    delta = b-a
    largeur = delta/n
    integrale = 0
    for i in range(1, n+1):
        integrale += largeur*(f(a+largeur*i)+f(a+largeur*(i-1)))/2
    return integrale

def integrale_montecarlo(f, a, b, h, n=100000):
    """
    f: fonction à intégrer
    a: début de d'intégrale
    b: fin de l'intégrale
    h: hauteur maximale de f
    n: nombre de tirages
    """
    from random import random
    somme = 0
    delta=b-a
    aire_totale = delta*h
    for _ in range(n):
        x = a+delta*random()
        y = random()*h
        if f(x) > y:
            somme += 1
    moyenne = somme/n
    integrale = moyenne * aire_totale
    return integrale

if __name__ == "__main__":
    def f(x):
        return x**2
    print("Méthode des rectangles :", integrale_rectangle(f, 0, 3))
    print("Méthode des trapèzes :", integrale_trapeze(f, 0, 3))
    print("Méthode de Monte-Carlo :", integrale_montecarlo(f, 0, 3, 9))

