# Write a program that asks the user to enter a length in centimeters.
# If the user enters a negative length, the program should tell the
# user that the entry is invalid. Otherwise, the program should convert
# the length to inches and print out the result

cm = float(input("Enter length in cm: "))
if (cm < 0):
    print("Invalid input")
else:
    inches = cm/2.54
    print(f"There are {inches} inches in {cm} cm.")
