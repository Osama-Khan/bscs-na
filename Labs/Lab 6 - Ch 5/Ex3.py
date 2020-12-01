# Write a program that asks the user to enter a value n,
# and then computes (1 + 1/2 + 1/3 + ... + 1/n) - ln(n).
# The ln function is log in the math module

from math import log

n = int(input("Enter value of n: "))
seq = 1.0
for i in range(2, n + 1):
    seq += 1/i
print(f"Result: {seq - log(n)}")
