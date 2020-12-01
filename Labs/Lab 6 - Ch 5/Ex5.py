# Write a program that asks the user to enter a number
# and prints the sum of the divisors of that number. The
# sum of the divisors of a number is an important
# function in number theory.

sum = 1
inp = int(input("Enter number: "))
for i in range(2, int(inp/2 + 2)):
    sum += i if inp % i == 0 else 0
sum += inp
print(sum)
