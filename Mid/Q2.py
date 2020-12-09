# Write python code to find the solution of given set of equations using
# Seidel Method with initial conditions x, y, z = 1, 1, 1 [for 10 iterations only]

def f1(y, z): return (-4*y + z + 32)/28
def f2(x, z): return (-2*x - 4*z + 35)/17
def f3(x, y): return (-x - 3*y + 24)/10


x, y, z = 1, 1, 1

print("k", "x", "y", "z", sep="\t")
for k in range(0, 10):
    x = round(f1(y, z), 4)
    y = round(f2(x, z), 4)
    z = round(f3(x, y), 4)
    print(k, x, y, z, sep="\t")
