
from pngTools import *
import math
import cmath
from pprint import pprint

def ft(x):
    N = len(x)
    y = []
    for k in range(0, N):
        yk = 0
        for i in range(0, N):
            yk += x[i] * cmath.exp(-(2j*i*k*math.pi/N))
        yk = (1/math.sqrt(N)) * yk

        y.append(yk)
    return y

def ift(y):
    N = len(y)
    x = []
    for k in range(0, N):
        xk = 0
        for i in range(0, N):
            xk += y[i] * cmath.exp((2j*i*k*math.pi/N))
        xk = (1/math.sqrt(N)) * xk
        x.append(xk)
    return x


"""
Get gray vector
"""

filename        = 'Resources/test.png'
img             = read(filename)
grayVector_in   = rgbImage2grayVector(img)


"""
Fourier transform
"""
grayVector_ft       = ft(grayVector_in)


"""
Inverse Fourier transform
"""
grayVector_ft_ift   = ift(grayVector_ft)
grayVector_out      = [abs(element) for element in grayVector_ft_ift]

"""
Show difference in floating point values and images
"""
pprint(grayVector_in)
pprint(grayVector_out)

show(grayVector2rgbImage(grayVector_in))
show(grayVector2rgbImage(grayVector_out))
