from math import sqrt,pi
from matplotlib.pyplot import *

l1 = []
l2 = []

N = input("TYPE N HERE: ")

# leibniz
res = 0.0
for i in range(N):
    res += (1.0/((4*i+1)*(4*i+3)))
    l1.append(pi - res*8)

# euler
res = 0.0
for i in range(1,N+1):
    res += 1.0/(i**2)
    l2.append(pi - sqrt(6*res))

# processing

plot(range(N), l1, 'b-',\
         range(N), l2, 'r-')
xlabel('No of terms')
ylabel('Error with Leibniz (blue) and Euler (red)')
show()


