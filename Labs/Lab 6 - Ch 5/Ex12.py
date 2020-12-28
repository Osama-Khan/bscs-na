# Write a program that asks the user to guess a random
# number between 1 and 10. If they guess right, they get
# 10 points added to their score, and they lose 1 point
# for an incorrect guess. Give the user five numbers to
# guess and print their score after all the guessing is
# done.

from random import randint
score = 0
for i in range(0, 5):
    rand = randint(1, 10)
    guess = int(input("Guess number: "))
    if guess == rand:
        print("Correct Guess +10")
        score += 10
    else:
        print("Incorrect Guess -1")
        score -= 1
print(f"Final score = {score}")
