# A store charges $12 per item if you buy less than 10 items.
# If you buy between 10 and 99 items, the cost is $10 per
# item. If you buy 100 or more items, the cost is $7 per item.
# Write a program that asks the user how many items they are
# buying and prints the total cost.

items = int(input("How many items are you buying? "))
cost = 7
if items < 10:
    cost = 12
elif items < 100:
    cost = 10
print(f"Your purchase cost will be: {items*cost}")
