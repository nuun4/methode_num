from numpy.random import randint

print("Welcome to the Game 21")
g1 = 0
g2 = 0
end = False

while not end:
    print(">>>")
    res1 = randint(0,11)
    print("gamer1 got ",res1)
    if res1 + g1 > 21:
        print("they let it")
        end = True
    else:
        print("they take it")
        g1 += res1

    res2 = randint(0,11)
    print("gamer2 got ",res2)
    if res2 + g2 > 21:
        print("they let it")
        end = True
    else:
        print("they take it")
        g2 += res2

print("> RESULTS : gamer1: {} gamer2: {}".format(g1,g2))
if g1 > g2:
    print("gamer1 is the winner")
elif g1 < g2:
    print("gamer2 is the winner")
else:
    print("draw")