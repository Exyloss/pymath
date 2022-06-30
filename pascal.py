#!/usr/bin/env python3
def factorielle(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def pascal(n, k):
    return factorielle(n)//(factorielle(k)*factorielle(n-k))

def pascal_array(n):
    assert isinstance(n, int) == True
    tab = [[1], [1,1]]
    if n == 0:
        return [[1]]
    elif n == 1:
        return tab
    elif n >= 2:
        for _ in range(n-1):
            new_line = [1]
            for k in range(1, len(tab[-1])):
                new_line.append(tab[-1][k-1]+tab[-1][k])
            new_line.append(1)
            tab.append(new_line)
        return tab
    else:
        return -1

if __name__ == "__main__":
    assert pascal(9, 6) == 84
    print(pascal_array(4))
