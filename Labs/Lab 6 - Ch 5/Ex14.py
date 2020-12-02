# This exercise is about the well-known Monty Hall problem. In
# the problem, you are a contestant on a game show. The host,
# Monty Hall, shows you three doors. Behind one of those...
# (a) Write a program that simulates playing this game 10000
# times and calculates what percentage of the time you would win
# if you switch and what percentage of the time you would win by
# not switching.
# (b) Try the above but with four doors instead of three.
# There is still only one prize, and Monty still opens up one
# door and then gives you the opportunity to switch.

from random import randint
doorWithPrize = randint(1, 2)
switchWins, keepWins = 0, 0
for i in range(0, 10000):
    choice = randint(1, 2)
    if choice is doorWithPrize:
        keepWins += 1
    else:
        switchWins += 1
print("With 3 doors: ")
print(f"Switch win chance: {switchWins / 100}%")
print(f"Keep win chance: {keepWins / 100}%")

doorWithPrize = randint(1, 3)
switchWins, keepWins = 0, 0
for i in range(0, 10000):
    choice = randint(1, 3)
    if choice is doorWithPrize:
        keepWins += 1
    else:
        switchWins += 1

print("With 4 doors: ")
print(f"Switch win chance: {switchWins / 100}%")
print(f"Keep win chance: {keepWins / 100}%")
