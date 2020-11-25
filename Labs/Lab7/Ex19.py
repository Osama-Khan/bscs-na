'''
Write a program that asks the user for a large integer and inserts
commas into it accordingto the standard American convention for 
commas in large numbers. For instance, if the user enters 1000000,
the output should be1,000,000
'''
inp = input("Enter number: ")[::-1]
out = ""
for i in range(0, len(inp)):
    if(i % 3 == 0 and i != 0):
        out += ","
        out += inp[i]
    else:
        out += inp[i]
print(out[::-1])
