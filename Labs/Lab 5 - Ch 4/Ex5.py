# Generate a random number between 1 and 10. Ask the user to
# guess the number and print a message based on whether they
# get it right or not.

from random import randint
num = randint(1, 10)
userNum = int(input("Guess number 1-10: "))
if num == userNum:
    print("You got it right!")
else:
    print("Wrong guess, Better luck next time.")
