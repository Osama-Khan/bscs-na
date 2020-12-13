
# Ex1
print("Osama"*100)

# Ex2
print("Osama"*1000, end="")

# Ex3
for i in range(100):
    print(f"{i + 1} Osama")

# Ex4
for i in range(1, 21):
    print(f'{i} --- {i*i}')

# Ex5
for i in range(8, 90, 3):
    if (i == 89):
        print(f'{i}.')
        break
    print(i, end=", ")

# Ex6
for i in range(100, 0, -2):
    if (i == 2):
        print(f'{i}.')
        break
    print(i, end=", ")

# Ex7
for i in range(10):
    print("A", end="")
for i in range(7):
    print("B", end="")
for i in range(4):
    print("CD", end="")
print("E", end="")
for i in range(6):
    print("F", end="")
print("G", end="")

# Ex8
name = input("Enter Name: ")
times = int(input("Enter times to print: "))
print(name*times)

# Ex9
amount = int(input("How many numbers: "))
fib = [1, 1]
for i in range(amount):
    ind = i + 2
    prev = fib[ind-2]
    prev2 = fib[ind-1]
    fib.append(prev+prev2)
print(fib[0:amount])

# Ex10
height = int(input("Box Height: "))
width = int(input("Box Width: "))
for i in range(height):
    print("*" * width)

# Ex11
height = int(input("Box Height: "))
width = int(input("Box Width: "))
print("*"*width)
for i in range(height - 2):
    print("*" + (" " * (width - 2)) + "*")
print("*"*width)

# Ex12
height = int(input("Triangle Height: "))
for i in range(1, height + 1):
    print("*"*i)

# Ex13
height = int(input("Triangle Height: "))
for i in range(height, 0, -1):
    print("*"*i)

# Ex14
height = int(input("Diamond Height: "))
stars = 1
for i in range(height, int(height/2), -1):
    print((" " * (i - 2)) + "*"*stars)
    stars = stars + 2
for i in range(int(height/2), height + 1):
    print((" " * (i - 2)) + "*"*stars)
    stars = stars - 2

# Ex15
size = int(input("Enter size:"))
gap = -1
for i in range(size, 0, -1):
    print(" " * int(i - 1), "*", end="")
    if i == int((size+1)/2):
        print("*"*gap, end="")
    else:
        print(" "*gap, end="")
    if(i != size):
        print("*")
    else:
        print("")
    gap = gap + 2
