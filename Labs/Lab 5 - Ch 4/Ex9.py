# Write a program that asks the user to enter a number and
# prints out all the divisors of that number.

num = int(input("Enter number: "))
print("Divisors List: ", end="")
for i in range(1, int(num/2 + 2)):
    if num % i == 0:
        print(i, end=", ")
print(num)
