from numpy import array
import matplotlib.pyplot as plt

def f(t,a,b):
    return a*t + b

def find_error(a, b):
    E = 0
    for i in range(len(time)):
        E += (f(time[i],a,b) - data[i])**2
    return E

def interactive_line_fit():
    one_more = True
    while one_more:
        a = input('Give a: ')
        b = input('Give b: ')
        print ('The error is: %g' % find_error(a, b))
        y = f(time, a, b)
        plt.plot(time, y, time, data, '*') 
        plt.xlabel('Time (s)')
        plt.ylabel('y (stars) and straight line f(t)')
        plt.show()
        answer = raw_input('Do you want another fit (y/n)? ')
        if answer == "n":
            one_more = False

data = array([0.5, 2.0, 1.0, 1.5, 7.5])
time = array([0, 1, 2, 3, 4])

interactive_line_fit()