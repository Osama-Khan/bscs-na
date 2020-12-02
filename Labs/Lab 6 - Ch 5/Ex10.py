# Ask the user to enter 10 test scores. Write a program
# to do the following:
# (a)  Print out the highest and lowest scores.
# (b)  Print out the average of the scores.
# (c)  Print out the second largest score.
# (d)  If any of the scores is greater than 100, then
# after all the scores have been entered, print a message
# warning the user that a value over 100 has been entered
# (e)  Drop the two lowest scores and print out the
# average of the rest of them.

greaterThan100 = False
inps = []
for i in range(0, 10):
    num = int(input(f"Number {i + 1}: "))
    if num > 100:
        greaterThan100 = True
    inps.append(num)

inps.sort()
print(f"Highest: {inps[-1]}, Lowest: {inps[0]}")
print(f"Average: {sum(inps)/len(inps)}")
print(f"Second highest: {inps[-2]}")
if greaterThan100:
    print("Score greater than 100 has been entered!")
inps.pop(0)
inps.pop(0)
print(f"Average after dropping lowest: {sum(inps)/len(inps)}")
