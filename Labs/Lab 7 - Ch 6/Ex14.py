# Write a program that asks the user to enter their name in lowercase and then
# capitalizes the first letter of each word of their name.

name = input("Enter name: ").split()
for i in range(len(name)):
    name[i] = name[i][0].capitalize() + name[i][1:]
for i in range(len(name)):
    print(name[i], end=" ")
