import math


def main(x, y, z):
    f = 0
    n = len(x)
    z.insert(0, 0)
    z.insert(1, 0)
    for i in range(1, n+1):
        f += 2*(71*z[n+1-((i-1)//2)] + y[i-1]**3 + 91*x[(i-1)//4]**2)**5
    return f
