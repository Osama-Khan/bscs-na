# The following is useful in implementing computer players in a number
# of different games. Write a program that creates a 5×5 list consisting
# of zeroes and ones. Your program should then pick a random location in
# the list that contains a zero and change it to a one. If all the
# entries are one, the program should say so.
from random import randint

lst = [
    [0, 0, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0],
]

ones = []
for i in range(5):
    for j in range(5):
        if lst[i][j] == 1:
            ones.append((j, i))

while len(ones) < 25:
    r = (randint(0, 4), randint(0, 4))
    if r not in ones:
        lst[r[0]][r[1]] = 1
        ones.append(r)
