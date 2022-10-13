#!/usr/bin/env python3

from math import pi
from sign_frac import *

def tau_periode_to_fun():
    try:
        tau   = -float(input("tau:"))
        per   = eval(input("periode:"))
    except:
        quit()
    if per+tau <= per/2:
        tau += per
    per = floatToFrac(per)
    freq  = (per[1], per[0])
    omega = mult_frac((2,1),freq)
    phi   = mult_frac(omega, floatToFrac(tau))

    if phi[0]/phi[1] > 1:
        phi = add_frac((2,1), (-phi[0], phi[1]))
    elif phi[0]/phi[1] <= -1:
        phi = add_frac((2,1), phi)

    phi_sin = add_frac(phi, (1,2))

    if phi_sin[0]/phi_sin[1] > 1:
        phi_sin = add_frac((2,1), (-phi_sin[0], phi_sin[1]))
    elif phi_sin[0]/phi_sin[1] <= -1:
        phi_sin = add_frac((2,1), phi_sin)

    print("========= cos =========")
    print("Acos("+print_frac(omega)+"pi*t + "+print_frac(phi)+"pi)")
    print("Acos("+str(round(pi*omega[0]/omega[1], 2))+"*t + "+str(round(pi*phi[0]/phi[1], 2))+")")
    print("========= sin =========")
    print("Asin("+print_frac(omega)+"pi*t + "+print_frac(phi_sin)+"pi)")
    print("Asin("+str(round(pi*omega[0]/omega[1], 2))+"*t + "+str(round(pi*phi_sin[0]/phi_sin[1], 2))+")")

def dephasage():
    print("1: calcul déphasage")
    print("2: calcul différence temporelle")
    try:
        r = int(input(">>"))
    except:
        quit()
    if r == 1:
        tau  = floatToFrac(float(input("tau:")))
        per  = floatToFrac(float(input("periode:")))
        freq = (per[1], per[0])
        print(print_frac(mult_frac(mult_frac(freq, (2, 1)), tau))+"pi rad"+" ou "+str(round(freq[0]/freq[1]*tau[0]/tau[1]*2*pi, 2))+" rad voire "+str(round(freq[0]/freq[1]*tau[0]/tau[1]*2*180, 2))+" deg")



print("1: calcul de la sinusoide avec la période et tau")
print("2: calcul déphasage / temps")

while True:
    try:
        r = int(input(">"))
    except:
        quit()
    if r == 2:
        dephasage()
    else:
        tau_periode_to_fun()
