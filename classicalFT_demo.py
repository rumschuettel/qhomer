from classicalFT import *
from pngTools import *
from pprint import pprint

"""
Get gray vector
"""
filename        = 'Resources/homer_low_quality.png'
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
