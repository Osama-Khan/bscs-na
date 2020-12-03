# Write a program that asks the user how many credits they have taken.
# If they have taken 23 or less, print that the student is a freshman.
# If they have taken between 24 and 53, print that they are a sophomore.
# The range for juniors is 54 to 83, and for seniors it is 84 and over.
creds = int(input("Enter credits: "))
msg = "Senior"
if creds <= 23:
    msg = "Freshman"
elif creds <= 53:
    msg = "Sophomore"
elif creds <= 83:
    msg = "Junior"
print(f"The student is a {msg}")
