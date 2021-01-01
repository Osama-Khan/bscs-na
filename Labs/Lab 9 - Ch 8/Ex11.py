# Section 8.3 described how to use the shuffle method to create a random anagram
# of a string.Use the choice method to create a random anagram of a string.
from random import choice
from string import ascii_lowercase as letters

x = [choice(letters) for i in range(100)]
print(''.join(x))
