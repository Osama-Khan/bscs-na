'''
Write a program that generates the 26-line block of letters 
partially shown below. Use a loop containing one or two 
print statements
abcdefghijklmnopqrstuvwxyz
bcdefghijklmnopqrstuvwxyza
cdefghijklmnopqrstuvwxyzab
...
zabcdefghijklmnopqrstuvwxy

'''
s = "abcdefghijklmnopqrstuvwxyz"
for i in range(0, len(s)):
    print(s[i:], end="")
    print(s[:i])
