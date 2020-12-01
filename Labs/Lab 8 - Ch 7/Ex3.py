# Start with the list[8,9,10]. Do the following:
# (a)  Set the second entry (index 1) to 17
# (b)  Add 4, 5, and 6 to the end of the list
# (c)  Remove the first entry from the list
# (d)  Sort the list
# (e)  Double the list
# (f)  Insert 25 at index 3

lst = [8, 9, 10]

lst[1] = 17

lst.extend([4, 5, 6])

lst.pop(0)

lst.sort()

lst.extend(lst)

lst.insert(3, 25)
