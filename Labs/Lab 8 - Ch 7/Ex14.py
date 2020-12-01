# Write a program that asks the user to enter a length in feet.
# The program should then give the user the option to convert
# from feet into inches, yards, miles, millimeters, centimeters,
# meters, or kilometers. Say if the user enters a1, then the
# program converts to inches, if they enter a2, then the program
# converts to yards, etc. While this can be done with if
# statements it is much shorter with lists and it is also easier
# to add new conversions if you use lists.

l = input("Enter length in feet: ")
multList = [12, 0.33333, 0.00081, 304.8, 30.48, 0.3048, 0.0003048]
choices = "abcdefg"
choice = input(
    "Convert to:\na) inches\nb) yards\nc) miles\nd) mm\ne) cm\nf) meters\ng) km")
if choice not in choices:
    print("Invalid choice")
else:
    print(f"{l} feet = {float(l) * multList[choices.index(choice)]}")
