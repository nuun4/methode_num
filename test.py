import math

def app():
    from trapezoidal import trapezoidal

    x = lambda u: math.log(u)

    print trapezoidal(x,2,5,3)

def nice():
    print math.erf(5)

if __name__ == '__main__':
    nice()