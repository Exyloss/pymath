#!/usr/bin/env python3
def pgcd(d,n):
    """
    Renvoie le pgcd de d et n
    """
    assert (isinstance(n, int) and isinstance(d, int)) == True, "Erreur, vous devez renseigner des entiers."
    while d != n:
        if abs(d) > abs(n):
            if d > 0:
               d -= abs(n)
            elif d < 0:
                d += abs(n)
            else:
                return -1
        elif abs(d) < abs(n):
            if n > 0:
                n -= abs(d)
            elif n < 0:
                n += abs(d)
            else:
                return -1

    return d

def ppcm(a,b):
    """
    renvoie le ppcm de a et b
    """
    assert (isinstance(a, int) and isinstance(b, int)) == True, "Erreur, vous devez renseigner des entiers."
    return a*b//pgcd(a,b)

def pgcd_prod(a, b):
    """
    Fonction permettant de remonter l'algorithme d'euclide.
    Renvoie le couple (u, v) tel que :
    a*u + b*v = d
    """
    d = pgcd(a, b)
    u = 1
    v = 1
    comb = a+b
    while comb != d:
        if comb < d:
            u += 1
        else:
            v -= 1
        comb = a*u+b*v
    return (u, v)

def solve_diophantienne(a, b, c):
    """
    Résolveur d'équation diophantienne du type :
    ax+by=c
    """
    d = pgcd(a, b)
    s = pgcd_prod(a, b)
    p = ppcm(d, c)
    if p != c:
        print("pas de solution")
        quit()
    else:
        s2 = (s[0]*c//d, s[1]*c//d)
        signe = ["+", "-"]
        if s2[0] < 0:
            signe[0] = "-"
        if a < 0:
            signe[1] = "+"
        print(str(b)+"k"+signe[0]+str(abs(s2[0]))+" ; "+str(s2[1])+signe[1]+str(abs(a))+"k")

if __name__ == "__main__":
    assert pgcd(1010101, 365) == 73
    assert pgcd_prod(1234, 5678) == (704, -153)
    solve_diophantienne(21, 7, 14)
