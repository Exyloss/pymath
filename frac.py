#!/usr/bin/env python3
class Fraction:
    def __init__(self,d,n):
        if n == 0:
            raise ZeroDivisionError
        self.denom=d
        self.num=n
        if d > 0:
            self.pgcd=pgcd(d,n)
        else:
            self.pgcd=pgcd(-d,n)
        if self.pgcd > 1:
            self.denom//=self.pgcd
            self.num//=self.pgcd

    def __str__(self):
        if self.num != 1 and self.num != -1:
            return str(self.denom)+"/"+str(self.num)
        elif self.num == 1:
            return str(self.denom)
        else:
            return str(self.denom)

def pgcd(d,n):
    while d != n:
       if d > n:
           d-=n
       elif d < n:
           n-=d
    return d

def ppcm(d,n):
    return d*n//pgcd(d,n)

def floatToFrac(f):
    if f > 0:
        i=1
        j=1
        while i/j != f:
            if i/j > f:
                j+=1
            else:
                i+=1
        return Fraction(i,j)
    elif f < 0:
        i=-1
        j=1
        while i/j != f:
            if i/j < f:
                j+=1
            else:
                i-=1
        return Fraction(i,j)
    return None

print(Fraction(4,6))
print(floatToFrac(-5.2222))
