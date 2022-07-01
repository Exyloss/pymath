#!/usr/bin/env python3
# Calculatrice en cours de développement...
from math import exp, pi, sin, cos, sqrt
from arithmetique import solve_diophantienne
r = "h"
while r != "q":
    if r == "h":
        print("1: calcul linéaire")
        print("2: calcul matriciel")
        print("3: résolveur équation 2nd degrès")
        print("4: résolveur diophantienne")
        print("q: quitter")
        print("h: afficher cette aide")
    elif r == "1":
        while r != "q":
            r = input(">")
            r.replace("^", "**")
            if r != "q":
                try:
                    res = eval(r)
                    print(r)
                except:
                    print("erreur de syntaxe")
                    pass
    elif r == "4":
        while r != "q":
            try:
                a = int(input("a:"))
                b = int(input("b:"))
                c = int(input("c:"))
                signe = "+"
                if b < 0:
                    signe = "-"
                print("équation : "+str(a)+"x"+" "+signe+" "+str(abs(b))+"y = "+str(c))
                print(solve_diophantienne(a, b, c))
            except:
                print("erreur")
                pass
            r = input("quitter = q:")

    r = input("menu:")
