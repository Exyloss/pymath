#!/usr/bin/env python3
def solve_snd_deg(a, b, c):
    from math import sqrt
    delta = b**2-4*a*c
    if delta > 0:
        return ((-b+sqrt(delta))/(2*a),(-b-sqrt(delta))/(2*a))
    elif delta == 0:
        return -b/(2*a)
    else:
        return False

if __name__ == "__main__":
    print(solve_snd_deg(3, 2, -1))

