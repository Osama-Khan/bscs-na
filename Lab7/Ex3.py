'''
People often forget closing parentheses when
entering formulas. Write a program that asks
the user to enter a formula and prints out 
whether the formula has the same number of
open-ing and closing parentheses.
'''
f = input("Enter formula: ")
print("Seems correct" if f.count(")") == f.count("(") else "Formula is wrong.")
