from math import *
from numpy import linspace
import matplotlib.pyplot as ppt

# volume
L = linspace(1,3,3)
print(L)
V = L**3
for elt in V:
    print(elt)

# plotting
ppt.plot(L,V, 'teal')
ppt.show()
