#!/usr/bin/env python3

from math import sqrt

def prod_scalaire(vec1: list, vec2: list) -> int:
    return vec1[0]*vec2[0] + vec1[1]*vec2[1]

def length(pt1, pt2=None):
    if pt2 == None:
        return sqrt(pt1[0]**2+pt1[1]**2)
    else:
        return sqrt((pt2[0]-pt1[0])**2+(pt2[1]-pt1[1])**2)

