import matplotlib.pyplot as plt
import numpy as np

N = 2
t = []

def sinesum(t,b):
    sum = 0.0
    for n in range(N):
        sum += b[n]*np.sin((n+1)*t)
    return sum

def test_sinesum():
    tt = [(-(np.pi)/2,-4), (np.pi/4, 2*np.sqrt(2)-3)]
    b = [4,-3]
    for t in tt:
        r = sinesum(t[0], b)
        if abs(r - t[1]) < 1e-6:
            print("ok")
        else:
            print("%g" % r)

def plot_compare(f,N,M):
    plt.plot(f(t), y, sinesum(,), , '*') 
    plt.xlabel('Time (s)')
    plt.ylabel('y (stars) and straight line f(t)')
    plt.show()

test_sinesum()