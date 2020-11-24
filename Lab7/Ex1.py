'''
Write  a  program  that  asks  the  user  to  enter  a  string.   
The  program  should  then  print  the following:
(a)  The total number of characters in the string
(b)  The string repeated 10 times
(c)  The first character of the string (remember that string indices start at 0)
(d)  The first three characters of the string
(e)  The last three characters of the string
(f)  The string backwards
(g)  The seventh character of the string if the string is long enough and a message otherwise
(h)  The string with its first and last characters removed
(i)  The string in all caps
(j)  The string with every a replaced with an e
(k)  The string with every letter replaced by a space
'''
inp = input("Enter a string: ")
print(f"Total number of characters = {len(inp)}")
print(f"The string repeated 10 times: \n{inp*10}")
print(f"The first character of string: {inp[0]}")
print(f"The first three characters of string: {inp[:3]}")
print(f"The last three characters of string: {inp[-3:]}")
print(f"The string backwards: {inp[::-1]}")
print(
    f"The seventh character of the string: {inp[6] if len(inp) >= 6 else 'String too small'}")
print(
    f"String with it's first and last character removed: {inp[1:len(inp)-1]}")
print(f"The string in all caps: {inp.upper()}")
print(f"The string with every a replaced with e: {inp.replace('a', 'e')}")
print(f"The string with every letter replaced with a space: {' '*len(inp)}")
