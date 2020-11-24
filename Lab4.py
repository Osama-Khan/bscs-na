from random import randint

'''
#Exercise 1
for i in range(50):
    print(randint(3,6))

#Exercise 2
x = randint(1, 50)
y = randint(2, 5)
print (x**y)

#Exercise 3
r = randint(1, 10)
print("Osama"*r)

#Exercise 4
r = randint(1, 1000)
print (r/100)

#Exercise 5
for i in range(1, 50):
    r = randint(1, i+1)
    print(r)

#Exercise 6
x = eval(input("Enter Number 1: "))
y = eval(input("Enter Number 2: "))
print(abs(x-y)/(x+y))

#Exercise 7
x = eval(input("Enter angle bw -180 to 180: "))
print(x+180)

#Exercise 8
x = eval(input("Enter seconds: "))
mins = (x // 60)
secs = (x % 60)
print(f'{mins} Minutes and {secs} Seconds.')

#Exercise 9
x = eval(input("Enter hour bw 1 to 12: "))
y = eval(input("How many hours ahead: "))
out = (x + y) % 12
print (f'{y} hours from {x} would be {out}\'o Clock')

#Exercise 10 
x = int(input("Write power: "))
#a
print(f'Last digit of 2^{x} = {(2**x)%10}')
#b
print(f'Last 2 digits of 2^{x} = {(2**x)%100}')
#c
y = int(input("Number of Last digits: "))
print(f'Last {y} digits of 2^{x} = {(2**x)%(10**y)}')

#Exercise 11
x = eval(input("Enter kilograms: "))
print(f'{x}kg in pounds is {x*2.20462}')
'''