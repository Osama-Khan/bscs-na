'''Write a program that asks the user to enter a
word and prints out whether that word contains
any vowels.
'''
word = input("Enter a word: ")
print("Vowel found" if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word else "Vowel not found")
