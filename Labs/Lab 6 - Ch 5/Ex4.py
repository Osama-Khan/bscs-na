# Write a program to compute the sum 1−2+3−4+···+1999−2000.

sum = 1
for i in range(2, 2001):
    sum += (-i) if i % 2 == 0 else i
print(sum)
