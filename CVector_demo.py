from classicalFT import *
from plotTools import *
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

data = np.array(data).tolist()


"""
Fourier transform
"""
data_ft = ft(data)


"""
Inverse Fourier transform
"""
data_ft_ift   = ift(data_ft)


"""
Show difference in floating point values and images
"""
# pprint(data)
# divider()
# pprint(data_ft)
# divider()
# pprint(data_ft_ift)


plot_complex_vector(data)
plot_complex_vector(data_ft)
plot_complex_vector(data_ft_ift)
