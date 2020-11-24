'''
A simple way of encrypting a message is to rearrange its characters. 
One way to rearrange the characters is to pick out the characters at 
even indices, put them first in the encrypted string,and follow them 
by the odd characters.  For example, the stringmessagewould be encrypted
as msaeesg because the even characters are m,s,a,e (at indices 0, 2, 4,
and 6) and the odd characters are e,s,g (at indices 1, 3, and 5).
(a)  Write a program that asks the user for a string and uses this method
to encrypt the string.
(b)  Write a program that decrypts a string that was encrypted with this 
method.
'''
msg = input("Enter message: ")
enc = ""
for i in range(0, len(msg), 2):
    enc += msg[i]
for i in range(1, len(msg), 2):
    enc += msg[i]
print(f"Encrypted: {enc}")
l = len(enc)
enc1 = enc[0:int(l/2 + 1)]
enc1_index = 0
enc2 = enc[int(l/2 + 1): l]
enc2_index = 0
dec = ""
swapper = True
for i in range(0, l):
    if swapper:
        dec += enc1[enc1_index]
        enc1_index += 1
    else:
        dec += enc2[enc2_index]
        enc2_index += 1
    swapper = not swapper
print(f"Decrypted: {dec}")
