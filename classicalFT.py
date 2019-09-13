
import math
import cmath

def ft(x):
    N = len(x)
    y = []
    for k in range(0, N):
        yk = 0
        for i in range(0, N):
            yk += x[i] * cmath.exp(-(2j*i*k*math.pi/N))
        yk = (1/math.sqrt(N)) * yk
        y.append(yk)
        print('FT: ' + str(k) + ' out of ' + str(N))

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
        print('IFT: ' + str(k) + ' out of ' + str(N))

    return x


