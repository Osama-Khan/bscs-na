from math import factorial, sin, cos, tan, radians, floor
from random import randint

# Exercise 1
for i in range(50):
    print(randint(3, 6), end=" ")
print()

# Exercise 2
x = randint(1, 50)
y = randint(2, 5)
print(x**y)

# Exercise 3
r = randint(1, 10)
print("Osama"*r)

# Exercise 4
r = randint(1, 1000)
print(r/100)

# Exercise 5
for i in range(1, 50):
    r = randint(1, i+1)
    print(r, end=" ")
print()

# Exercise 6
x = eval(input("Enter Number 1: "))
y = eval(input("Enter Number 2: "))
print(abs(x-y)/(x+y))

# Exercise 7
x = eval(input("Enter angle bw -180 to 180: "))
print(x+180)

# Exercise 8
x = eval(input("Enter seconds: "))
mins = (x // 60)
secs = (x % 60)
print(f'{mins} Minutes and {secs} Seconds.')

# Exercise 9
x = eval(input("Enter hour bw 1 to 12: "))
y = eval(input("How many hours ahead: "))
out = (x + y) % 12
print(f'{y} hours from {x} would be {out}\'o Clock')

# Exercise 10
x = int(input("Write power: "))
# a
print(f'Last digit of 2^{x} = {(2**x)%10}')
# b
print(f'Last 2 digits of 2^{x} = {(2**x)%100}')
# c
y = int(input("Number of Last digits: "))
print(f'Last {y} digits of 2^{x} = {(2**x)%(10**y)}')

# Exercise 11
x = eval(input("Enter kilograms: "))
print(f'{x}kg in pounds is {x*2.20462}')

# Exercise 12
x = int(input("Enter number: "))
print(factorial(x))

# Exercise 13
x = int(input("Enter number: "))
print("sin: ", sin(x), ", cos: ", cos(x), ", tan: ", tan(x))

# Exercise 14
x = int(input("Enter angle in degrees: "))
print("sin: ", sin(radians(x)))

# Exercise 15
for i in range(0, 346, 15):
    print(i, " --- ", round(sin(radians(i)), 4),
          " ", round(cos(radians(i)), 4))

# Exercise 16
# y = int(input("Enter year: "))
# c = y/100
# m = (15 + c - floor(c/4.) - floor((8*c + 13)/25)) % 30
# n = (4 + c - floor(c/4.)) % 7
# a = y % 4
# b = y % 7
# c = y % 19
# d = (19*c + m) % 30
# e = (2*a + 4*b + 6*d + n) % 7

# Exercise 17
year = int(input("Enter year: "))
years = 0
for i in range(1600, year + 1):
    if (i % 4 == 0 and (i % 100 != 0 or i % 400 == 0)):
        years += 1
print("Years: ", years)

# Exercise 18
coins = float(input("Enter amount: "))
dec = (coins * 100) % 100
coins = int(coins)
quarters = int(dec // 25)
dec = dec % 25
dimes = int(dec // 10)
dec = dec % 10
nickels = int(dec // 5)
pennies = int(dec % 5)
print(pennies, " Pennies, ", dimes, " Dimes, ", nickels,
      " Nickels, ", quarters, " Quarters, and ", coins, " Dollars")

# Exercise 19
w = int(input("Enter width: "))
h = int(input("Enter height: "))
c = 0
for i in range(h):
    for j in range(w):
        print(c % 10, end="")
        j += 1
        c += 1
    print()
