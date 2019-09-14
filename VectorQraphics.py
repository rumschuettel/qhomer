import svgpathtools
import math
from numpy import real, imag
import json

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
        if len(pathpoints) > 0:
            res.append(pathpoints)

    def f(x): return x.start
    starts = list(map(lambda i: f(i), paths[0]))
    return res, starts


def flip_x(input):
    """flips the real values of all of the points"""
    # DOES NOT WORK DO NOT TOUCH STAY AWAY FROM THIS ONE CAUSE IT BITES
    res = []
    for line in input:
        max_x = real(max(line, key=(lambda x: (real(x)))))
        res.append(list(map(lambda x: complex(max_x-real(x), imag(x)), line)))
    return res


def flip_y(inp):
    """flips the imaginary values of all of the points, do THAT for good results"""
    res = []
    for line in inp:
        #max_y = imag(max(line , key=(lambda y: (imag(y)))))
        res.append(list(map(lambda y: complex(real(y), -imag(y)), line)))
    return res


def offset(line, dx, dy):
    return list(map(lambda p: complex(real(p)+dx, imag(p)+dy), line))


def jsonify(lines):
    res = []
    for line in lines:
        tmp = []
        for point in line:
            pt = []
            pt.append(str(real(point)))
            pt.append(str(imag(point)))
            tmp.append(pt)
        if len(tmp) > 0:
            res.append(tmp)

    return json.dumps(res)
def eww(file,target):
    density = 10
    for i in range(density):
        lines, starts = get_points(file,density -i)
        count = 0
        for line in lines:
            count+=len(line)
        if count>target:
            return get_points(file,density-i+1)
    return None