from matplotlib import pyplot as plt

def f(a,b,t):
    print(t)
    return a*t+b

# a)
def find_error(a,b):
    e = 0.0
    for i in range(1,5):
        e += (f(a,b,y[i]) - x[i])**2
    return e

# b)
def display(a,b):
    end = False
    while not end:
        print('%d' % find_error(a,b))
        plt.plot(y,f(a,b,y), y, x, '*')
        plt.xlabel('Some Y')
        plt.ylabel('f(x)')
        plt.show()
        res = input("do you wanna continue ?")
        if(res == "no"):
            end = False

x = [0.5,0.2,1.0,1.5,7.5]
y = [0,1,2,3,4]
display(1.0,0.0)
