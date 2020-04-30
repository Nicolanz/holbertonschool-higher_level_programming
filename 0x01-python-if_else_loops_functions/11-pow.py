#!/usr/bin/python3
def pow(a, b):
    power = 1
    for i in range(b, 0, -1):
        power *= a
    return power
