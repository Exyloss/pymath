#!/usr/bin/env python3
from math import pi, sin, cos, sqrt, e, radians
from pascal import pascal
from arithmetique import *
from solve import *
from matrice import *
from integrale import *
from proba import *
r = "h"
ans = "0"
while r != "q":
    if r == "h":
        print("1: calcul linéaire")
        print("2: calcul matriciel")
        print("3: résolveur équation 2nd degrès")
        print("4: résolveur diophantienne")
        print("5: calcul d'intégrales")
        print("6: probabilités")
        print("q: quitter")
        print("h: afficher cette aide")
    elif r == "1":
        while r != "q":
            r = input(">")
            r = r.replace("^", "**")
            if r != "q" and r != "h":
                try:
                    ans = eval(r)
                    print(ans)
                except:
                    print("erreur de syntaxe")
                    pass
            elif r == "h":
                print("\033[4mvariables:\033[0;0m")
                print("ans: valeur précédemment calculée")
                print("e: valeur de e")
                print("pi: valeur de pi")
                print("\033[4mfonctions:\033[0;0m")
                print("sqrt(x): racine carré de x")
                print("cos(x), sin(x): cos/sin de x en radians")
                print("radians(x): convertir x degrès en radians")
                print("pascal(n, k): k parmis n")
                print("pgcd(a, b), ppcm(a, b): pgcd et ppcm de a et b")
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
                signe1 = "+"
                b_str  = str(b)+"x"
                signe2 = "+"
                c_str  = str(c)
                if b < 0:
                    signe1 = "-"
                    b_str  = str(abs(b))+"x"
                elif b == 0:
                    signe1 = ""
                    b_str  = ""
                if c < 0:
                    signe2 = "-"
                    c_str  = str(abs(c))
                elif c == 0:
                    signe2 = ""
                    c_str  = ""

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
                solve_diophantienne(a, b, c)
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
    elif r == "6":
        print("1: loi binomiale")
        print("2: loi normale")
        print("3: dénombrement")
        while r not in "123q":
            r = input(":")
        if r == "1":
            print("B(n; p)")
            while r != "q":
                try:
                    n = int(input("n:"))
                    p = float(input("p:"))
                    assert 0 <= p <= 1
                    print("P(X [oper] k)")
                    oper = input("oper:")
                    assert oper in ["=", "<=", ">="]
                    k = int(input("k:"))
                    print(binomial(n, p, oper, k))
                except:
                    print("erreur")
                    pass
                r = input("quitter = q:")
        elif r == "2":
            print("N(esp; et)")
            while r != "q":
                try:
                    esp = float(input("espérance:"))
                    et = float(input("écart-type:"))
                    print("P(a <= X <= b)")
                    a = float(input("a:"))
                    b = float(input("b:"))
                    print(normal(esp, et, a, b))
                except:
                    print("erreur")
                    pass
                r = input("quitter = q:")
        elif r == "3":
            while r != "q":
                try:
                    printM([["[X]"],["k"]])
                    n = int(input(":"))
                    printM([[n],["[X]"]])
                    k = int(input(":"))
                    print(pascal(n, k))
                except:
                    pass
                r = input("quitter = q:")




    r = input("menu:")
