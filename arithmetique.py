#!/usr/bin/env python3
def pgcd(d,n):
    while d != n:
       if d > n:
           d-=n
       elif d < n:
           n-=d
    return d

def ppcm(a,b):
    return a*b//pgcd(a,b)

if __name__ == "__main__":
    print(pgcd(1010101, 365))
