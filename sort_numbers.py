from random import *

res = []
for i in range(6):
    tmp = uniform(0,10)
    res.append(tmp)

print("Liste initiale: ")
for elt in res:
    print("%5.3f" % elt)

res = sorted(res)

print("\nListe triee: ")
for elt in res:
    print("%5.3f" % elt)

