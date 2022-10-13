def gcd(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i
    return gcd

def simplify(f):
    d = f[0]
    n = f[1]
    if n == 0:
        raise ZeroDivisionError
    if d > 0:
        p=gcd(d,n)
    else:
        p=gcd(-d,n)
    if p > 1:
        d//=p
        n//=p
    return(d, n)

def add_frac(f1,f2):
    f3 = (f1[0]*f2[1]+f2[0]*f1[1], f1[1]*f2[1])
    return simplify(f3)

def mult_frac(f1,f2):
    if 0 not in f1 and 0 not in f2:
        return simplify((f1[0]*f2[0], f1[1]*f2[1]))
    else:
        return (0,1)

def floatToFrac(f):
    if f > 0:
        i=1
        j=1
        while i/j != f:
            if i/j > f:
                j+=1
            else:
                i+=1
        return (i,j)
    elif f < 0:
        i=-1
        j=1
        while i/j != f:
            if i/j < f:
                j+=1
            else:
                i-=1
        return (i,j)
    else:
        return (0,1)

def print_frac(f):
    if f[1] != 1:
        return str(f[0])+"/"+str(f[1])
    elif f[1] == 1 and f[0] == 1:
        return ""
    else:
        return str(f[0])

if __name__ == "__main__":
    print(simplify((123,96)))
    print(add_frac((2,3),(5,6)))
