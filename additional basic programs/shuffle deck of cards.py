import itertools ,random

deck = list(itertools.product(range(1,14),['spade','Heart','Diamond','Club']))

random.shuffle(deck)


print("you got")
for i in range(5):
    print(deck[i][0],"of",deck[i][1])
"""
00 01
10 11
20 21
30 31
40 41

(1,2,3,4,5,6,7,8,9,10,11,12,13) , ['spade','Heart','Diamond','Club'}
"""

