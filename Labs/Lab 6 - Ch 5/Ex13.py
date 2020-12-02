# In the last chapter there was an exercise that asked you to create a
# multiplication game for kids. Improve your program from that exercise
# to keep track of the number of right and wrong answers. At the end of
# the program, print a message that varies depending on how many
# questions the player got right.

from random import randint

score, right = 0, 0
for i in range(0, 5):
    rand = randint(1, 10)
    guess = int(input("Guess number: "))
    if guess is rand:
        print("Correct Guess +10")
        score += 10
        right += 1
    else:
        print("Incorrect Guess -1")
        score -= 1
print(
    f"You scored {score} after {right} correct and {5 - right} incorrect answers")
