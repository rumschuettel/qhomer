import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import random
import math

RED     = '#f44242'
ORANGE  = '#f48641'
YELLOW  = '#f4be41'
GREEN   = '#41f470'
LBLUE   = '#41f4eb'
BLUE    = '#4197f4'
DBLUE   = '#4155f4'
PURPLE  = '#9741f4'
PINK    = '#f141f4'
GREY    = '#5b5f66'
BLACK   = '#000000'

font = {
'weight': 'normal',
'size': 13,
}

def plot(title, x, y, x_err=None, y_err=None,
        colour = DBLUE, marker = '.', markersize = 4, linestyle = '',
        show = True):

    plt.errorbar(x, y, xerr=x_err, yerr=y_err, color = colour, marker = marker, markersize = markersize, linestyle = linestyle, linewidth = 1)

    plt.title(title, fontdict = font)
    plt.grid(True)
    plt.xticks([])
    plt.yticks([])

    if (show):
        plt.show()

def complex_to_cartesian(input):
    xx = list(map(lambda x: np.real(x), input))
    yy = list(map(lambda y: np.imag(y), input))
    return xx, yy

def plot_complex_vector(cVector):
    [x, y] = complex_to_cartesian(cVector)
    plot('', x, y)


# x = np.array([0, 1, 2, 3, 4, 5])
# y = np.array([i**2 + random.random() for i in x])

# plot('Test', x, y)
def matrix_mid_value(mats):
    #return np.average(np.array([mats]), axis=0,weights=[0.5])
    # res = np.mean(np.array([mats]), axis=0)
    res = sum(np.array(mat) for mat in mats)
    return res/len(mats)

def matrix_weighted_avg(mats, w=[2,2]):
    res = np.average(np.array(mats), axis=0,weights=w)
    return res

