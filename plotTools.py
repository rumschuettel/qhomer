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
        xlabel = '', ylabel = '',
        show = True):

    plt.errorbar(x, y, xerr=x_err, yerr=y_err, color = colour, marker = marker, markersize = markersize, linestyle = linestyle, linewidth = 1)

    plt.title(title, fontdict = font)
    plt.grid(True)
    plt.xlabel(xlabel, fontdict = font)
    plt.ylabel(ylabel, fontdict = font)

    if (show):
        plt.show()
()


# x = np.array([0, 1, 2, 3, 4, 5])
# y = np.array([i**2 + random.random() for i in x])

# plot('Test', x, y)
