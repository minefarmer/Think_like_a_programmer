



r1 = int(input("Please enter the rows for first matrix: "))
c1 = int(input("Please enter the columns for first matrix: "))

r2 = int(input("Please enter the rows for second matrix: "))
c2 = int(input("Please enter the columns for second matrix: "))

matrix1 = [[0]*c1 for i in range(r1)]
matrix2 = [[0]*c2 for i in range(r2)]
resultant = [[0]*c2 for i in range(r2)]

if r1 == r2 and c1 == c2:

    for i in range(r1):
        for j in range(c1):
            matrix1[i][j] = int(input("Please Enter the element for first matrix: "))
            matrix2[i][j] = int(input("Please Enter the element for second matrix: "))

    for i in range(r1):
        for j in range(c1):
            resultant[i][j] = matrix1[i][j] + matrix2[i][j]

    for i in matrix1:
        print(i)
    print("Matrix 2: ")
    for j in matrix2:
        print(j)
    print("Resultant matrix")
    for i in range(r1):
        for j in range(c1):
            print(resultant[i][j], end = ' ')
        print()
else:
    print("Matrix addition can't be done. order must be same")
