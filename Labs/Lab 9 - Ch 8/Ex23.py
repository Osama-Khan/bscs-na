# This exercise is useful in creating a Memory game. Randomly generate
# a 6×6 list of assorted characters such that there are exactly two of
# each character
from random import randint
charsList = []
for i in range(18):
    while True:
        c = chr(randint(33, 127))
        if c not in charsList:
            charsList.append(c)
            charsList.append(c)
            break

lst = []
while len(lst) < 6:
    current = []
    while len(current) < 6:
        r = randint(0, len(charsList) - 1)
        current.append(charsList[r])
        charsList.pop(r)
    print(' '.join(current))
    lst.append(current)
# lst holds the 6x6 list
