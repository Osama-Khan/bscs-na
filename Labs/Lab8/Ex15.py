# There is a provably unbreakable cipher called a one-time pad.
# The way it works is you shift each character of the message by
# a random amount between 1 and 26 characters, wrapping around
# the alphabet if necessary. The program should generate a
# random shift between 1 and 26 for each character.
# a) Encrypt a string
# b) Decrypt a string

from random import randint
characters = "abcdefghijklmnopqrstuvwxyz"
inp = input("Enter string: ")
rands = [randint(0, 25) for i in inp]

enc = ""
for i in range(0, len(inp)):
    if inp[i] in characters:
        inputIndex = characters.index(inp[i])
        encryptedIndex = (inputIndex + rands[i]) % 26
        enc += characters[encryptedIndex]
    else:
        enc += inp[i]
print("Encrypted = " + enc)

dec = ""
for i in range(0, len(enc)):
    if enc[i] in characters:
        encryptedIndex = characters.index(enc[i])
        decryptedIndex = (encryptedIndex - rands[i]) % 26
        dec += characters[decryptedIndex]
    else:
        dec += enc[i]
print("Decrypted = " + dec)
