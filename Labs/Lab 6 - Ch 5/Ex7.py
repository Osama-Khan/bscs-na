# An integer is called squarefree if it is not divisible by
# any perfect squares other than 1. Write a program that
# asks the user for an integer and tells them if it is
# squarefree or not.

from math import sqrt
inp = int(input("Enter a number: "))
squareFree = True
for i in range(2, int(inp/2 + 2)):
    if inp % i == 0:
        s = sqrt(i)
        if int(s) == s:
            squareFree = False
            break
if squareFree:
    s = sqrt(inp)
    if int(s) == s:
        squareFree = False
    else:
        print("The number is square free")
if not squareFree:
    print("The number is not square free")
