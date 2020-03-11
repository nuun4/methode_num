from numpy import linspace
def f(x):
    return x

def g(x):
    return x*x


N = input("N InPUT: ")
epsilon = input("EPSILON InPUT (a small number): ")
interval = linspace(-4,4,N)

for i in range(N):
    if abs((f(interval[i]) - g(interval[i])) < epsilon):
        print(interval[i])

