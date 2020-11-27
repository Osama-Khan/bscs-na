# Create the following lists using a for loop.
# (a) A list consisting of the integers 0 through 49
# (b) A list containing the squares of the integers 1 through 50.
# (c) The list['a','bb','ccc','dddd',. . .] that ends with 26 copies of the letter z.

lst = []
for i in range(50):
    lst.append(i)

lst = []
for i in range(1, 51):
    lst.append(i*i)

lst = []
s = 'abcdefghijklmnopqrstuvwxyz'
for i in range(26):
    lst.append(s[i] * (i + 1))
