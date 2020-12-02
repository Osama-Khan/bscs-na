# Write a program to count how many integers from 1
# to 1000 are not perfect squares, perfect cubes,
# or perfect fifth powers.

from math import sqrt
count = 0
count2 = 0
count3 = 0
for i in range(1, 1001):
    if (round(sqrt(i))**2 == i) or (round(i**(1./3.))**3 == i) or (round(i**(1./5.))**5 == i):
        continue
    count += 1

print(f"Numbers of such Integers: {count} {count2} {count3}")
