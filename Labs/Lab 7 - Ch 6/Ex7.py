'''
Write a program that asks the user to enter
a word and determines whether the word is a 
palindrome or not. A palindrome is a word 
that reads the same backwards as forwards
'''
a = input("Enter word: ")
print("Palindrome" if a.lower() == a[::-1].lower() else "Not palindrome")
