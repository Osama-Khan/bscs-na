# Ask the user for a number and then print a diagonal counter,
# where the pattern ends at the number that the user enters.

end = int(input("Enter number to end at: "))
for i in range(0, end):
    print(" "*i, i+1, sep="")
