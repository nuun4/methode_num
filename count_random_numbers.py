from numpy.random import randint

M = 0

N = input("TYPE A POSITIVE INTEGER: ")

for i in range(N):
    res = randint(1,7)
    print(res)
    if res == 6 :
        M += 1

print("M = {} ; N = {} ; M/N = {}".format(M,N,float(M)/float(N)))