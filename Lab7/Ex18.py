'''
(a)  Without using the in operator, write a program that asks the user for a string
and a letter and prints out whether or not the letter appears in the string.
(b)  Without using the count method, write a program that asks the user for a string
and a letter and counts how many occurrences there are of the letter in the string.
(c)  Without using the index method, write a program that asks the user for a string
and a letter and prints out the index of the first occurrence of the letter in the string.
'''
# a
inp = input("Enter string: ")
letter = input("Enter letter: ")[0]
appears = False
i = 0
while (i < len(inp)):
    if (inp[i] == letter):
        appears = True
        break
    i += 1
print("Appears" if appears else "Doesn't appear")

# b
inp = input("Enter string: ")
letter = input("Enter letter: ")[0]
appearances = 0
for l in inp:
    if l == letter:
        appearances += 1
print(f"Appears {appearances} times.")

# c
inp = input("Enter string: ")
letter = input("Enter letter: ")[0]
index = 0
appears = False
for l in inp:
    if l == letter:
        appears = True
        break
    index += 1
print(f"Appears at index {index}." if appears else "Doesn't appear")
