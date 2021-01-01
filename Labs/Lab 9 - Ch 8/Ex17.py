# Write a program that finds the average of all of the entries in a 4×4 list of integers.

lst = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
s = 0
for i in lst:
    s += sum(i)
print(s/16)
