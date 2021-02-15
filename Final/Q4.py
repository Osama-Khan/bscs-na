# Write python program that takes user defined square matrix from user and delete its diagonal of index entered by user. If index of diagonal is wrong, then print a message 
size = int(input("Enter number of rows: "))
matrix = []
for i in range(size):
  arr = []
  for j in range(size):
    el = int(input(f"Enter value of location({i+1}, {j+1}): "))
    arr.append(el)
  matrix.append(arr)
print(f"Entered Matrix is: \n{matrix}")
diag = int(input(f"Enter a diagonal to make it 0 between {-size+1} and {size-1}: "))
while diag < (-size+1) or diag > (size-1):
  diag = int(input("You entered a wrong diagonal number, try again: "))
else:
  r, c = 0, 0
  if diag < 0:
    r = abs(diag)
  elif diag > 0:
    c = abs(diag)
  while r >= 0 and r < size and c >= 0 and c < size:
    matrix[r][c] = 0
    r += 1
    c += 1
print(matrix)