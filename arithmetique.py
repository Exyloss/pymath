#!/usr/bin/env python3
def pgcd(d,n):
    """
    Renvoie le pgcd de d et n
    """
    assert (isinstance(n, int) and isinstance(d, int)) == True, "Erreur, vous devez renseigner des entiers."
    while d != n:
       if d > n:
           d-=n
       elif d < n:
           n-=d
    return d

def ppcm(a,b):
    """
    renvoie le ppcm de a et b
    """
    assert (isinstance(n, int) and isinstance(d, int)) == True, "Erreur, vous devez renseigner des entiers."
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

if __name__ == "__main__":
    assert pgcd(1010101, 365) == 73
    assert pgcd_prod(1234, 5678) == (704, -153)
