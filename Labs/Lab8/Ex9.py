# When playing games where you have to roll two dice, it is nice
# to know the odds of each roll. For instance, the odds of rolling
# a 12 are about 3%, and the odds of rolling a 7 are about 17%.
# You can compute these mathematically, but if you don’t know the
# math, you can write a program to do it. To do this, your program
# should simulate rolling two dice about 10,000 times and compute
# and print out the percentage of rolls that come out to be 2, 3,
# 4, . . . , 12.

from random import randint
countMsg = ["2: ", "3: ", "4: ", "5: ", "6: ",
            "7: ", "8: ", "9: ", "10: ", "11: ", "12: "]
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(10000):
    roll1 = randint(1, 6)
    roll2 = randint(1, 6)
    count[(roll1+roll2) - 2] += 1
[print(f"{msg} {i/100}") for msg, i in zip(countMsg, count)]
