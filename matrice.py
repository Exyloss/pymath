#!/usr/bin/env python3
def multM(m1,m2):
    """
    m1: matrice de gauche
    m2: matrice de droite
    """
    if len(m1) != len(m2[0]) or not (estMatrice(m1) and estMatrice(m2)):
        return -1
    n1 = len(m1)
    n2 = len(m1[0])
    n3 = min(n1, n2)
    m3=[[0 for i in range(n3)] for j in range(n3)]
    tmp = 0
    for i in range(n1):
        for k in range(n1):
            for j in range(n2):
                tmp += m1[i][j]*m2[j][k]
            m3[i][k] = tmp
            tmp = 0
    return m3

def estMatrice(m):
    if not isinstance(m, list) or not isinstance(m[0], list):
        return False
    n = len(m)
    for i in range(1, n):
        if len(m[i]) != len(m[i-1]) or not isinstance(m[i], list):
            return False
    return True

def expM(m, e):
    """
    m: matrice de départ
    e: exposant de la matrice
    """
    if not estMatrice(m): return -1
    if e == 0:
        return genId(len(m))
    else:
        m_e = m
        for _ in range(e-1):
            m_e = multM(m, m_e)
        return m_e

def transpoM(m):
    if not estMatrice(m): return -1
    n1 = len(m[0])
    n2 = len(m)
    t = [[0 for i in range(n2)] for _ in range(n1)]
    for i in range(n2):
        for j in range(n1):
            t[j][i] = m[i][j]
    return t

def genId(l,coef=1):
    m=[[0 for j in range(l)] for i in range(l)]
    for i in range(l):
        m[i][i] = coef
    return m

def dim(m):
    if not estMatrice(m): return -1
    return (len(m),len(m[0]))

def inv(m):
    if not estMatrice(m): return -1
    a=m[0][0]
    b=m[0][1]
    c=m[1][0]
    d=m[1][1]
    det=a*d-b*c
    return [[d/det,-b/det],[-c/det,a/det]]

if __name__ == "__main__":
    m1 = [
    [1,2,3],
    [4,5,6]
    ]
    m2=[
    [1,4],
    [2,5],
    [3,6]
    ]
    m3=[
    [3,-2],
    [1,4]
    ]
    print(multM(m3,m3))
    print(expM(m3, 3))
    print(inv(m3))
    print(estMatrice(m1))
    print(m1)
    print(transpoM(m1))
