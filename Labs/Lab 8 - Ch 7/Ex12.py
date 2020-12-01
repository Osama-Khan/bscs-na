# Write a program that generates 100 random integers that are either 0 or 1.
# Then find the longest run of zeros, the largest number of zeros in a row.

from random import randint

lst = [randint(0, 1) for i in range(100)]
maxRun = 0
currentRun = 0
for i in lst:
    if i == 1:
        maxRun = currentRun if currentRun > maxRun else maxRun
        currentRun = 0
    elif i == 0:
        currentRun += 1
