# Write a program that removes any repeated items from a
# list so that each item appears at mostonce. For instance,
# the list [1,1,2,3,4,3,0,0] would become [1,2,3,4,0].
lst = [1, 1, 2, 3, 4, 3, 0, 0]

# outlst = list(set(lst)) # alternate solution
outlst = []
for el in lst:
    if el not in outlst:
        outlst.append(el)
