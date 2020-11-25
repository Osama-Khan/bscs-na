'''
A simple way to estimate the number of words in a string
is to count the number of spaces in the string.  Write a
program that asks the user for a string and returns an
estimate of howmany words are in the string.
'''
inp = input("Enter a string: ")
print(f"Estimated number of words: {inp.count(' ') + 1}")
