def f(x): return x ** 3 + 4 * (x*x) - 10
def fd(x): return 3*(x*x) + 8*x


xn = 1
xn1 = 0
print("n\txn")
n = 0
while True:
    xn1 = round(xn - (f(xn)/fd(xn)), 10)
    if xn == xn1:
        print("Final value: " + str(xn))
        break
    print(n, xn, sep="\t")
    xn = xn1
    n += 1
