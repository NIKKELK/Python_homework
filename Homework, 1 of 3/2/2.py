import math


def main(z):
    if (z < 56):
        result = (math.sin(z))**2+26*(math.cos(z))**3
    elif (z >145):
        result = 47*z**5+z**4
    elif ((z>=56)&(z<89)):
        result = z**7-z**3
    else:
        result = (z**3+z**2+60)**6
    return result
