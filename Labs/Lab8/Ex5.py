# Ask the user to enter a list of strings. Create a new list that
# consists of those strings with their first characters removed.

print("Enter some strings: ")
lst = [input() for i in range(5)]
lst2 = [l[1:] for l in lst]
