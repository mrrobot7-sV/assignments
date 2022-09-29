# Schrijf een functie die een muntje x maal opgooit en de aantal keer kop of munt terug geeft

import random

# def coin(x):
#     c = ["head", "tail"]
#     total = []
#     for x in range(0,x):
#         total.append(random.choice(c))

#     hCount = len([x for x in total if "head" in x])
#     tCount = len([x for x in total if "tail" in x])
#     return {'head': hCount, 'tail': tCount}

# Generate a random binary string and use List Comprehension
# to count the 1's and 0's and return as a Tuple.
# bs = "{0:b}".format(random.getrandbits(c))

# Generate random binary string and use List Comprehension
# to count the 1's and 0's and return as a Tuple.
def coin_flip(c):
    bs = '' 
    for i in range(0, c):
        bs += random.choice(["0","1"])
    return len([x for x in bs if "0" in x]), len([y for y in bs if "1" in y])

cf = coin_flip(5)
print('Heads: {0[0]}, Tails: {0[1]}'.format(cf))
cf = coin_flip(1000)
print('Heads: {0[0]}, Tails: {0[1]}'.format(cf))
