# Write a multiplication game program for kids. The program
# should give the player ten randomly generated multiplication
# questions to do. After each, the program should tell them
# whether they got it right or wrong and what the correct answer
# is.
from random import randint

for i in range(1, 11):
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    ans = int(input(f"Question {i}: {num1} x {num2} = "))
    if ans == num1 * num2:
        print("Right!")
    else:
        print("Wrong!")
