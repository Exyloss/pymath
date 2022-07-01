#!/usr/bin/env python3
from pascal import pascal
def binomial(n, p, oper, k, cs=5):
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

if __name__ == "__main__":
    print(binomial(20, 0.3, ">=", 5))
