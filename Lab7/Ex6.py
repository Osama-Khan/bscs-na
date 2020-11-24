'''
Write a program that asks the user to enter
a string s and then converts s to lowercase, 
removes all the periods and commas from s,
and prints the resulting string.
'''
s = input("Enter string: ").lower()
s = s.replace(".", "")
s = s.replace(",", "")
print(s)
