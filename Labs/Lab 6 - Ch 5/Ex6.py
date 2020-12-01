# Write a program that finds all four of the perfect numbersthat are less than 10000.
perfectNums = []
for i in range(2, 10001):
    divSum = 0
    for j in range(1, int(i/2 + 2)):
        divSum += j if i % j == 0 else 0
    if divSum == i:
        perfectNums.append(i)
print(f"The perfect numbers are: {perfectNums}")
