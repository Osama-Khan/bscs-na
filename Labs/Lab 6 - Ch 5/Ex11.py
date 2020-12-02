# Write a program that computes the factorial of a number.
# The factorial n! of a number n is the product of all the
# integers between 1 and n, including n.

inp = int(input("Enter number: ")) - 1
fact = inp + 1
while inp > 1:
    fact *= inp
    inp -= 1
print(fact)
