# In algebraic expressions, the symbol for multiplication is often left out.
# Computers prefer those expressions to include the multiplication symbol.
# Write a program that asks the user for an algebraic expression and then
# inserts multiplication symbols where appropriate.

from string import ascii_letters as c

inp = input("Enter algebraic expression:")
out = ""
for i in range(len(inp)):
    if inp[i] == "x":
        if num:
            out += "*"
        out += "x"
        num = False
    elif inp[i] == "(":
        out += "*("
        num = False
    elif inp[i] == ")":
        out += ")"
        if i != len(inp) - 1:
            out += "*"
        num = False
    else:
        out += inp[i]
        num = True
print(out)
