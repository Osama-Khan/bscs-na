# Write a program that asks the user to enter a list of integers. Do the following:
# (a) Print the total number of items in the list.
# (b) Print the last item in the list.
# (c) Print the list in reverse order.
# (d) Print Yes if the list contains a 5 and No otherwise.
# (e) Print the number of fives in the list.
# (f) Remove the first and last items from the list, sort the remaining items, and print the result.

print("Enter a list of integers: ")
lst = [int(input()) for i in range(5)]

print(f"Length: {len(lst)}")
print(f"Last item: {lst[-1]}")
print(f"Reversed: {lst[::-1]}")
contains5 = lst.index(5) > -1
print("List contains 5: " + ("Yes" if contains5 else "No"))
print("Number of 5s: " + (str(lst.count(5)) if contains5 else "0"))
lst.pop(0)
lst.pop()
lst.sort()
print("f: " + str(lst))
