#!/usr/bin/env python3
def binomial(n, p, oper, k, cs=5):
    """
    n: nombre de tirages
    p: probabilité de réussite
    oper: P(X [oper] k) oper peut prendre comme valeurs: =, <=, >=
    k: P(X [oper] k)
    cs: chiffres significatifs, 5 par défaut
    """
    from pascal import pascal
    if oper == "=":
        return round(pascal(n, k)*p**k*(1-p)**(n-k), cs)
    elif oper == "<=":
        somme = 0
        for i in range(k+1):
            somme += pascal(n, i)*p**i*(1-p)**(n-i)
        return round(somme, cs)
    elif oper == ">=":
        somme = 0
        for i in range(n, k-1, -1):
            somme += pascal(n, i)*p**i*(1-p)**(n-i)
        return round(somme, cs)
    else:
        return -1

def normal(esp, et, a, b):
    """
    esp: espérence
    et: écart-type
    a: début de l'intervalle
    b: fin de l'intervalle
    """
    from math import e, pi, sqrt
    from integrale import integrale_trapeze
    def f(x):
        return 1/(et*sqrt(2*pi))*e**(-1/2*((x-esp)/et)**2)
    return round(integrale_trapeze(f, a, b), 5)

if __name__ == "__main__":
    print(binomial(20, 0.3, ">=", 5))
    print(normal(10, 1, 10, 12))
