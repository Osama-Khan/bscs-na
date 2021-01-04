# Write a program that asks the user for a string and returns a random
# anagram of the string.

from random import randint

inp = input("Enter a string: ")
rands = []
for i in range(len(inp)):
    r = randint(0, len(inp) - 1)
    while r in rands:
        r = randint(0, len(inp) - 1)
    rands.append(r)
for i in range(len(inp)):
    print(inp[rands[i]], end="")
