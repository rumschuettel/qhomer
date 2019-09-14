from classicalFT import *
from pngTools import *
from pprint import pprint

"""
Get gray vector
"""
filename        = 'Resources/test_4x4.png'
img             = read(filename)
grayVector_in   = rgbImage2grayVector(img)


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
