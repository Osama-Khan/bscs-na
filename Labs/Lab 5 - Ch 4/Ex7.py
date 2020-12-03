# Write a program that asks the user for two numbers and prints
# Close if the numbers are within .001 of each other and Not close
# otherwise.

num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
diff = abs(num1 - num2)
if diff <= .001:
    print("Close")
else:
    print("Not close")
