# Write a program that generates a list of 20 random numbers between 1 and 100.
# (a)  Print the list.
# (b)  Print the average of the elements in the list.
# (c)  Print the largest and smallest values in the list.
# (d)  Print the second largest and second smallest entries in the list
# (e)  Print how many even numbers are in the list.

from random import randint

lst = [randint(1, 100) for i in range(20)]

print(lst)

print(f"Average: {sum(lst)/len(lst)}")

print(f"Largest: {max(lst)}, Smallest: {min(lst)}")

sortedlist = sorted(lst)
print(f"Second Largest: {sortedlist[-2]}, Second Smallest: {sortedlist[1]}")

print(f"Even numbers = {len([i for i in lst if i % 2 == 0])}")
