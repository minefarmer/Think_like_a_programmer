'''         Matrix Addition
Write a program to add two matrices. First input the order of matrices. The matrices must be of same size to be added. Get the input for each element of first matrix and then for second matrix. Add two matrices and then store the values in third matrix.

'''
r1 = int(input("Please enter the rows for first matrix: "))
c1 = int(input("Please enter the columns for first matrix: "))

r2 = int(input("Please enter the rows for second matrix: "))
c2 = int(input("Please enter the columns for second matrix: "))

matrix1 = [[0]*c1 for i in range(r1)]
matrix2 = [[0]*c2 for i in range(r2)]
resultant = [[0]*c2 for i in range(c2)]

if r1 == r2 and c1 == c2:
    
    for i in range(r1):
        for j in range(c1):
            matrix1[i][j] = int(input("Please enter the element for the first matrix: "))
            matrix2[i][j] = int(input("Please enter the element for the second matrix: "))
    
    for i in range(r1):
        for j in range(c1):
            resultant[i][j] = matrix1[i][j] + matrix2[i][j]
    
    for i in matrix1:
        print(i)
    print("Matrix 2: ")
    for j in matrix2:
        print(j)
    print("Resultant matrix")
    for j in range(r1):
        for j in range(c1):
            print(resultant[i][j], end = ' ')
        print()
else:
    print("Matrix addition can't be done. ")

                # data_structures/matrix_addition.py
                # Please enter the rows for first matrix: 2
                # Please enter the columns for first matrix: 2
                # Please enter the rows for second matrix: 2
                # Please enter the columns for second matrix: 2
                # Please enter the element for the first matrix: 12
                # Please enter the element for the second matrix: 32
                # Please enter the element for the first matrix: 43
                # Please enter the element for the second matrix: 54
                # Please enter the element for the first matrix: 65
                # Please enter the element for the second matrix: 54
                # Please enter the element for the first matrix: 65
                # Please enter the element for the second matrix: 34
                # 44 97 119 99 



# second run  ********************************************************
# Please enter the rows for first matrix: 2
# Please enter the columns for first matrix: 2
# Please enter the rows for second matrix: 2
# Please enter the columns for second matrix: 2
# Please enter the element for the first matrix: 12
# Please enter the element for the second matrix: 33
# Please enter the element for the first matrix: 43
# Please enter the element for the second matrix: 54
# Please enter the element for the first matrix: 65
# Please enter the element for the second matrix: 54
# Please enter the element for the first matrix: 43
# Please enter the element for the second matrix: 65
# [12, 43]
# [65, 43]
# Matrix 2: 
# [33, 54]
# [54, 65]
    