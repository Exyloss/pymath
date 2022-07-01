#!/usr/bin/env python3
# Calculatrice en cours de développement...
from math import exp, pi, sin, cos, sqrt, e
from arithmetique import solve_diophantienne
from solve import *
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
    elif r == "3":
            try:
                a = int(input("a:"))
                b = int(input("b:"))
                c = int(input("c:"))
                signe = "+"
                b_str = str(b)+"x"
                signe2 = "+"
                c_str = str(c)
                if b < 0:
                    signe1 = "-"
                    b_str = str(abs(b))+"x"
                elif b == 0:
                    signe1 = ""
                    b_str = ""
                if c < 0:
                    signe2 = "-"
                    c_str = str(abs(c))
                elif c == 0:
                    signe2 = ""
                    c_str = ""

                print("équation : "+str(a)+"x^2"+" "+signe1+" "+b_str+" "+signe2+" "+c_str+" = 0")
                print(solve_snd_deg(a, b, c))
            except:
                print("erreur")
                pass
            r = input("quitter = q:")

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
