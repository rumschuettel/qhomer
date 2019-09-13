import svgpathtools
import math

# input: list of svgpathtools.path objects, each containing a list of segments
# output: list of lists of points in 2D space
def get_points(paths):
    res = []
    for path in paths:
        pathpoints = []
        for seg in paths._segments:
            count = math.ceil(seg.length()/2)
            frac = 1.0/count
            if svgpathtools.is_bezier_segment(seg):
                for i in range(1,count):          
                    pathpoints.append(seg.point(frac*i))
        res.append(pathpoints)
    return res
