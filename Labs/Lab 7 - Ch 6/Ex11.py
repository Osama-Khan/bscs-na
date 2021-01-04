# Write a program that asks the user to enter a word that contains the letter a.
# The program should then print the following two lines: On the first line should
# be the part of the string upto and including the the first a, and on the second
# line should be the rest of the string.

inp = input("Enter a string with a: ").split("a")
print(inp[0] + "a")
print(inp[1])
