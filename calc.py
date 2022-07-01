#!/usr/bin/env python3
from math import exp, pi, sin, cos, sqrt, e
from arithmetique import *
from solve import *
from matrice import *
from integrale import *
r = "h"
while r != "q":
    if r == "h":
        print("1: calcul linéaire")
        print("2: calcul matriciel")
        print("3: résolveur équation 2nd degrès")
        print("4: résolveur diophantienne")
        print("5: calcul d'intégrales")
        print("q: quitter")
        print("h: afficher cette aide")
    elif r == "1":
        while r != "q":
            r = input(">")
            r = r.replace("^", "**")
            if r != "q":
                try:
                    res = eval(r)
                    print(res)
                except:
                    print("erreur de syntaxe")
                    pass
    elif r == "2":
        try:
            tab = []
            while r != "s":
                i = int(input("nombre de lignes:"))
                j = int(input("nombre de colonnes:"))
                m = [[0 for _ in range(j)] for _ in range(i)]
                for k in range(i):
                    for l in range(j):
                        m[k][l] = "[X]"
                        printM(m)
                        val = int(input("("+str(k)+", "+str(l)+"):"))
                        m[k][l] = val
                printM(m)
                tab.append(m)
                index = len(tab)
                r = input("s = phase de calcul:")
            while r != "q":
                print("1: produit")
                print("2: transposée")
                print("3: exposant")
                print("4: historique")
                r = input(":")
                if r == "1":
                    for i in range(len(tab)):
                        print(str(i)+":")
                        printM(tab[i])
                    m1 = int(input("première matrice:"))
                    m2 = int(input("seconde matrice:"))
                    printM(tab[m1])
                    print("X")
                    printM(tab[m2])
                    print("=")
                    m = multM(tab[m1], tab[m2])
                    printM(m)
                    if len(tab) > 5:
                        tab.pop(0)
                    tab.append(m)
                elif r == "2":
                    for i in range(len(tab)):
                        print(str(i)+":")
                        printM(tab[i])
                    m1 = int(input("matrice:"))
                    m = transpoM(tab[m1])
                    printM(m)
                    if len(tab) > 5:
                        tab.pop(0)
                    tab.append(m)
        except:
            print("erreur")
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
    elif r == "5":
        r = input("f(x):")
        a = int(input("debut:"))
        b = int(input("fin:"))
        def f(x):
            return eval(r)
        print("intégrale (trapezes): "+str(integrale_trapeze(f, a, b, n=100000)))

    r = input("menu:")
