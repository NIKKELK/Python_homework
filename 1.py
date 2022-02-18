import math


def main(x,y,z):
    a = ((abs(x-1-y**3))**6/43)+(z/55)
    b = 68*(y*y+1)**7+32*(71*z+x*x+27*x**3)**5
    c = 44*x*x-77*(66*x*x-y*y*y-59*z)
    result = a/b-c
    return result

