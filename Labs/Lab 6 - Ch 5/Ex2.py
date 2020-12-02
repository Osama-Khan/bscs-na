# Write a program that counts how many of the squares of the
# numbers from 1 to 100 end in a 4 and how many end in a 9.

nums4 = 0
nums9 = 0
for i in range(1, 101):
    power = i*i
    if str(power).endswith("4"):
        nums4 += 1
    if str(power).endswith("9"):
        nums9 += 1
print(f"Squares from 1 to 100 ending in 4: {nums4}")
print(f"Squares from 1 to 100 ending in 9: {nums9}")
