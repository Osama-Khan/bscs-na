# Write a python program that will print the numbers in a square shape matrix according to user defined number of rows. The numbers start from 1 and end on rows^2.
size = int(input("Enter number of rows: "))
m = size**2 + 1
for i in range(size):
  for j in range(size):
    a = min(i, j)
    b = min(size - 1 - i, size - 1 - j)
    x = min(a, b)
    s_2x = size - 2 * x
    if i <= j:
      print(abs(s_2x * s_2x - (i - x) - (j - x) - m), end='')
    else:
      print( abs((s_2x - 2) * (s_2x - 2) + (i - x) + (j - x) - m), end='')
    print('\t', end='')
  print()