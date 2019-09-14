from classicalFT import *
from pngTools import *
from pprint import pprint
import numpy as np
import json, glob, math

def normalized(arr):
    """l2-normalization"""
    return arr / np.linalg.norm(arr, 2)

"""
Get complex numbers
"""
with open("./Resources/elephant.9.json") as f:
   data = json.load(f)[:-1]
   data = normalized(np.array([complex(a, b) for a, b in data]))



"""
Fourier transform
"""
grayVector_ft       = ft(grayVector_in)
grayVector_ft_abs   = [abs(element) for element in grayVector_ft]


"""
Inverse Fourier transform
"""
grayVector_ft_ift   = ift(grayVector_ft)
grayVector_out      = [abs(element) for element in grayVector_ft_ift]

"""
Show difference in floating point values and images
"""
pprint(grayVector_in)
divider()
pprint(grayVector_ft)
divider()
pprint(grayVector_ft_ift)

exit()
show(grayVector2rgbImage(grayVector_in))
show(grayVector2rgbImage(grayVector_ft_abs))
show(grayVector2rgbImage(grayVector_out))
