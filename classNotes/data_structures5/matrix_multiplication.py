'''             Multiplication of Matrices
Rule: We can only multiply matrices if the number of columns in the first matrix is the same as the number of rows in the second matrix.
a) Multiplying a 2 x 3 matrix by a 3 x 4 matrix and it gives a 2 x 4 matrix as the answer.






'''

r1 = r2 = c1 = c2 = 0
while True:
    print("Order of First Matrix")
    r1 = int(input("Please enter rows for first matrix: "))
    c1 = int(input("Please enter columns for second matrix: "))
    
    print("Order of Second Matrix")
    r2 = int(input("Please enter rows for Second matrix: "))
    c2 = int(input("Please enter columns for Second matrix: "))
    
    if c1 !=r2:
        print('_'*50)
        print("Sorry, matrices cannot be multiplied. Re-enter correct order")
        continue
    else:
        break
    
# create first empty matrix
arr1 = [[0]*c1 for x in range (r1)]
    
# create second empty matrix
arr2 = [[0]*c2 for y in range (r2)]
    
# create third empty matrix
arr3 = [[0]*c2 for z in range (r1)]

print("Enter element for first Matrix here: ")
for i in range(r1):
    for j in range(c1):
        arr1[i][j] = int(input(">>> "))


print("Enter element for first Matrix here: ")
for i in range(r2):
    for j in range(c2):
        arr2[i][j] = int(input(">>> "))

print("Matrix 1: ")
for i in range(c1):
    for j in range(c1):
        print(arr1[i][j], end= ' ')
    print()

print("Matrix 2: ")
for i in range(r2):
    for j in range(c2):
        print(arr2[i][j], end= ' ')
    print()

# add code for matrix multiplication

for i in range(r1):
    for j in range(c2):
        for k in range(r2):
            arr3[i][j] += arr1[i][k] * arr2[k][j]

# print the resultant code
for row in arr3:
    print(row)
    
