'''
Write a program that asks the user to enter a word and
then capitalizes every other letter of that word.
'''
word = input("Enter word: ")
cap = False
for i in word:
    print(i.upper() if cap else i, end="")
    cap = not cap
