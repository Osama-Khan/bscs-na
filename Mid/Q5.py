# Write python code to implement user defined Triangle with only one loop.
r = int(input("Enter number of rows: "))
for i in range(0, r):
    print(" " * (r - i), end="")
    print("* " * (i + 1))
