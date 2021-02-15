def matrixDiagonalZero(num):
    R =int(num)
    C =int(num)
    matrix = []
    print("Enter the entries rowwise:")


    for i in range(R):
        a = []
        for j in range(C):
            a.append((input('Enter element of location('+str(i+1)+','+str(j+1)+')')))
        matrix.append(a);

    print('Your matrix:')
    for i in range(R):
        print('[',end='')
        for j in range(C):
            print(matrix[i][j], end=" ")
        print(']')
    print(']')

    changer=int(input('Enter a diagonal number to make it zero between -' + str(R-1) + ' and ' + str(R-1) + ' = '))
    if (abs(changer) > R-1 ):
      print("[Error] Invalid diagonal number, nothing updated.")
      return
    if(changer < 0):
      for i in range(R):
        for j in range(C):
          if(i+changer==j):
            matrix[i][j] = 0
    elif(changer > 0):
      for i in range(R):
        for j in range(C):
          if(i==j+changer):
            matrix[i][j] = 0
    else:
      for i in range(R):
        for j in range(C):
          if(i==j):
            matrix[i][j] = 0
    print('matrix after update:')
    for i in range(R):
        print('[',end='')
        for j in range(C):
            print(matrix[i][j], end=" ")
        print(']')
    print(']')


num=int (input("Enter the number of rows of a square matrix:"))
matrixDiagonalZero(num)