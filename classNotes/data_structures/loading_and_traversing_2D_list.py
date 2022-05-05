'''     Loading and Traversing 2D list   Part 1
        Loading and Traversing 2D list   Part 2   line 40

    Loading and Traversing 2D List
Create a 3 x 3 list, initialize it with some values and then display the list using nested for loop

>>> # Create a 2D list of demension 5x3
>>> twoDList = [[0]*3 for i in range(5)]
>>> twoDList
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> 

'''

# List = [[0]*3 for i in range(3)]

# List[0][0] = 10
# List[0][1] = 20
# List[0][2] = 30
# List[1][0] = 11
# List[1][1] = 12
# List[1][2] = 13
# List[2][0] = 6
# List[2][1] = 7
# List[2][2] = 4

# for row in List:
#     for j in row:
#         print (j, end = " ")
#     print()  # 10 20 30 
            # 11 12 13 
            # 6 7 4 







'''      Loading and Traversing 2D list   Part 2  *************************

Write a program that takes matrix of size 3x3 from user and then displays the matrix.

'''
List = [[0]*3 for i in range(3)]

for i in range(len(List[0])):
    for j in range(len(List)):
        List[i][j] = int(input("Please Enter the Value: "))

for row in List:
    for j in row:
        print (j, end = " ")
    print()  # Please Enter the Value: 12
            # Please Enter the Value: 32
            # Please Enter the Value: 54
            # Please Enter the Value: 43
            # Please Enter the Value: 65
            # Please Enter the Value: 43
            # Please Enter the Value: 65
            # Please Enter the Value: 43
            # Please Enter the Value: 32
            # 12 32 54 
            # 43 65 43 
            # 65 43 32 

