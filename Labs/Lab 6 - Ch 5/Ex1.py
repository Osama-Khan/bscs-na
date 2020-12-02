# Write a program that counts how many of the
# squares of the numbers from 1 to 100 end in a 1.

nums = 0
for i in range(1, 101):
    power = i*i
    if str(power).endswith("1"):
        nums += 1
print(f"Squares from 1 to 100 ending in 1: {nums}")
