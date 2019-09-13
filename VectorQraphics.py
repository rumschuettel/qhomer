import svgpathtools
import math
from numpy import real, imag


# input: list of svgpathtools.path objects, each containing a list of segments
# output: list of lists of points in 2D space
def get_points(file, density):
    #TODO: calculate density automatically for target point #
    paths = svgpathtools.svg2paths2(file)
    res = []
    for i, path in enumerate(paths[0]):
        pathpoints = []
        for seg in path._segments:
            count = math.ceil(seg.length()/density)
            frac = 1.0/count
            for i in range(1, count):
                pathpoints.append(seg.point(frac*i))
        res.append(pathpoints)
    f = lambda x: x.start
    starts = list(map(lambda i: f(i),paths[0]))
    return res, starts


def flip_x(input):
    """flips the real values of all of the points"""
    res = []
    for line in input:
        max_x = real(max(line , key=(lambda x: (real(x)))))
        res.append(list(map(lambda x: complex(max_x-real(x),imag(x)),line)))
    return res

def flip_y(input):
    """flips the imaginary values of all of the points, do THAT for good results"""
    res = []
    for line in input:
        #max_y = imag(max(line , key=(lambda y: (imag(y)))))
        res.append(list(map(lambda y: complex(real(y),-imag(y)),line)))
    return res
def offset(line, dx, dy):
    return list(map(lambda p:complex(real(p)+dx,imag(p)+dy),line))
        