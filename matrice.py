#!/usr/bin/env python3
def multM(m1,m2):
    if len(m1) != len(m2[0]):
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
    print(inv(m3))
