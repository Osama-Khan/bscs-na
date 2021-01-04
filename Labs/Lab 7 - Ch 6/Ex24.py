# Write a program that asks the user for input like x^3 or x^25 and prints the derivative.

inp = input("Enter expression for power rule: ").split("^")
n = int(inp[1])
print(f"{n}{inp[0]}^{n-1}")
