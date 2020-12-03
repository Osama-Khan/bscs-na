# Write a program that lets the user play Rock-Paper-Scissors
# against the computer. There should be five rounds, and after
# those five rounds, your program should print out who won and
# lost or that there is a tie.

from random import randint
score = 0
print("Choose 0 for Rock, 1 for Paper, 2 for Scissors")
choices = ["Rock", "Paper", "Scissor"]
for i in range(0, 5):
    user = int(input(f"Round {i+1}:\nChoice: "))
    ai = randint(0, 2)
    print(f"You chose {choices[user]}\nAI Chose {choices[ai]}")
    if user - ai == 1 or user - ai == -2:
        score += 1
    elif user == ai:
        score += 0
    else:
        score -= 1

if score > 0:
    print("You win")
elif score < 0:
    print("You lose")
else:
    print("Tie")
