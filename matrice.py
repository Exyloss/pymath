#!/usr/bin/env python3
def multM(m1,m2):
    n1=len(m1)
    n2=len(m2)
    m3=[[0 for i in range(n1)] for j in range(n1)]
    for k in range(n1):
        for i in range(n1):
            res=0
            for j in range(n2):
                res+=m1[i][j]*m2[j][k]
            print(res)
            m3[k][i]=res
    return m3

def genId(l,coef=1):
    m=[[0 for j in range(l)] for i in range(l)]
    for i in range(l):
        m[i][i] = coef
    return m

def dim(m):
    return (len(m),len(m[0]))

def inv(m):
    a=m[0][0]
    b=m[0][1]
    c=m[1][0]
    d=m[1][1]
    det=a*d-b*c
    return [[d/det,-b/det],[-c/det,a/det]]

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
print(multM(m1,m2))
print(inv(m3))
