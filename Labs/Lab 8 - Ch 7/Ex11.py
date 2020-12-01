# Using a for loop, create the list below, which consists of
# ones separated by increasingly many zeroes. The last two ones
# in the list should be separated by ten zeroes.
# [1,1,0,1,0,0,1,0,0,0,1,0,0,0,0,1,....]

lst = []
for i in range(11):
    lst.append(1)
    for j in range(i):
        lst.append(0)
lst.append(1)
print(lst)
