import math


def main(m, a, b, p):
    result = 0
    for k in range (1, b+1):
        mult = 0
        for j in range (1, a+1):
            temp = 1
            for i in range (1, m+1):
                temp = temp * ((66*(k**2-69-p)**6 + (j**2/79) + i**5))
            mult = mult + temp
        result = result + mult
    return result
