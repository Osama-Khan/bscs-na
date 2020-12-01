# Write a program that rotates the elements of a list so that the
# element at the first index movesto the second index, the element
# in the second index moves to the third index, etc., and the
# element in the last index moves to the first index.

lst = [1, 2, 3, 4, 5]
tmp = lst[len(lst) - 1]
for i in range(0, len(lst)):
    tmp, lst[i] = lst[i], tmp
