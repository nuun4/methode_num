
import numpy as np

def f(x):
    return 4*x**2+1

def point_slope():
    N = 100
    c = 10*np.random.rand()-5
    P = np.empty(N)
    for i in range(N):
        x = 10*np.random.rand()-5
        p = (f(x) - f(c))/(x - c)
        P[i] = p
    return np.var(P) < 1e-10


test = point_slope()
if test:
    print 'SUCCESS'
else:
    print 'FAILURE'