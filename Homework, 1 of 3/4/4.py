import math


def main(n):
    if n == 0:
        return -0.85
    else:
        return ((math.sin(main(n-1)))**2) - (main(n-1))
    
