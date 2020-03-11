from numpy import zeros

def interpolate(y,t):
    i = int(t)
    return (y[i+1]-y[i])/1 * (t-i) + y[i] 

def find_y(y,N):
    t = input("Type a time between 1 and {}: ".format(N))
    while t > 0:
       print(interpolate(y,t-1)) 
       t = input("Type a time between 1 and {}: ".format(N))
    return

y = zeros(5)
y[0] = 4.4; y[1] = 2.0; y[2] = 11.0
y[3] = 21.5; y[4] = 7.5
find_y(y,len(y))

