from plot_tools import *
from VectorQraphics import *

file = "Resources/vector_line.svg"

lines = get_points(file) 
for line in lines:
    plot('',map(lambda x: real(x)),map(lambda y:imag(y)  ))