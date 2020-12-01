# Write a program that asks the user for an integer and creates
# a list that consists of the factors of that integer.

inp = int(input("Enter an integer: "))
divisors = [num for num in range(1, int(inp/2 + 1)) if inp % num == 0]
print(divisors)
