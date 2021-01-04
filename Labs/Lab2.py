# Exercise 1
chars = 19
lines = 4
print(("*" * chars + "\n") * lines)

# Exercise 2
print("*" * chars)
print("*" + " "*(chars-2) + "*")
print("*" + " "*(chars-2) + "*")
print("*" * chars)

# Exercise 3 (HW)
i = 1
print("*"*i)
i += 1
print("*"*i)
i += 1
print("*"*i)
i += 1
print("*"*i)

# Exercise 4
print((512-282)/(47 * 48 + 5.0))

# Exercise 5
n = int(input("Enter a number: "))
print("The square of 5 is", n**2, sep=" ")

# Exercise 6
n = int(input("Enter a number: "))
print(n, n*2, n*3, n*4, n*5, sep="---")

# Exercise 7
kg = float(input("Enter weight in kilos: "))
print("Weight in pounds: ", kg*2.2)

# Exercise 8
n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
n3 = float(input("Enter number 3: "))
total = n1+n2+n3
average = total/3
print(total, average)

# Exercise 9
n = float(input("Enter price of meal: "))
tip = n * (int(input("Enter tip percent: "))/100.)
print("Tip: ", tip)
print("Bill: ", tip + n)
