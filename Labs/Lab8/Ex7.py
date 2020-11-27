# Write a program that takes any two lists L and M of the same
# size and adds their elements together to form a new list N
# whose elements are sums of the corresponding elements in L
# and M.

l = [3, 1, 4]
m = [1, 5, 9]

n = [el + em for el, em in zip(l, m)]
