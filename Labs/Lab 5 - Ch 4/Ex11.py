# Write a program that asks the user for an hour between 1 and 12,
# asks them to enter am or pm, and asks them how many hours into
# the future they want to go. Print out what the hour will be that
# many hours into the future, printing am or pm as appropriate.

userHour = int(input("Enter hour between 1 and 12: "))
am = True if int(
    input("Enter 1 for am, any other number for pm: ")) == 1 else False
addition = int(input("How many hours ahead do you want to go: "))
curHour = userHour + addition
if (curHour / 12) % 2 != 0:
    am = not am
curHour %= 12
print(f"The current time is: {curHour} {'am' if am else 'pm'}")
