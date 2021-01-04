# Write a program that asks the user to enter two strings of the same length.
# The program should then check to see if the strings are of the same length.
# If they are not, the program should print an appropriate message and exit.
# If they are of the same length, the program should alternate the characters
# of the two strings.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if len(s1) == len(s2):
    for i in range(len(s1)):
        print(s2[i] + s1[i], end="")
else:
    print("Strings must be same length!")
