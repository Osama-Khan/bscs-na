# Ask the user to enter a list containing numbers between 1 and 12.
# Then replace all of the entries in the list that are greater than
# 10 with 10.

print("Enter numbers between 1 to 12: ")
lst = [eval(input()) for i in range(5)]
lst = [l if l < 10 else 10 for l in lst]
