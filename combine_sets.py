import string

cards = ''

digits = range(9)
letters = string.ascii_uppercase

# a)
for nb in ['A','2','3','4','5','6','7','8','9','10','J','Q','K']:
    for cl in ['C','D','H','S']:
        cards += nb+cl+' '

print("All combinations of cards: "+cards)

cars = ''
# b)
for l1 in letters:
    for l2 in letters:
        for c1 in digits:
            for c2 in digits:
                for c3 in digits:
                    cars += l1+l2+("{}{}{} ".format(c1,c2,c3))

print("All combinations of registration numbers: "+cars)

# c)
dice = range(6)
nb_sum_7 = 0
for d1 in dice:
    for d2 in dice:
        if d1 + d2 == 7:
            nb_sum_7 += 1

print("Number of sums equal to 7: {}".format(+nb_sum_7))