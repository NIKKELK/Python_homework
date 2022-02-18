import math


def main(z):
    if (z < 73):
        result = 7*(62*z**3+80*z)**5
    elif (z >= 95):
        result = 85*(log2(1-z-z**3))**3+(52*z**3+17*z*z)**4
    else:
        result = 1+(5+z**3+5*z**2)**4
    return result
