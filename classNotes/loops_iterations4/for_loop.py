'''     For loop

    main
    :
   For __Next___
    |           |
    |   ^     Output
    |   |_______|
    |
   End 



        Syntax of For Loop
'''
for i in range(5):
    print(i)  # 0
            # 1
            # 2
            # 3
            # 4


# loop from 0 to 10
for i in range(11):
    print(i)
0
1
2
3
4
5
6
7
8
9
10


for i in range(5):
    print('Hello World!')  # Hello World!
                        # Hello World!
                        # Hello World!
                        # Hello World!
                        # Hello World!


for i in range(5):
    print(i, 'Hello World!')  # 0 Hello World!
                            # 1 Hello World!
                            # 2 Hello World!
                            # 3 Hello World!
                            # 4 Hello World!


#  design a loop that loops from one to 10
for i in range(1, 11):
    print(i)  # 1
            # 2
            # 3
            # 4
            # 5
            # 6
            # 7
            # 8
            # 9
            # 10


# print even numbers up to 10 (2, 4, 6, 8, 10)
# 2
# 2+2 = 4
# 4+2 = 6
# 6+2 = 8
# 8+2 = 10
for i in range(2, 11, 2):
    print(i)  # 2
            # 4
            # 6
            # 8
            # 10


# 1, 3, 5, 7, 9
for i in range(1, 10, 2):
    print(i)  # 1
            # 3
            # 5
            # 7
            # 9


# countdown loop
for i in range(10, 0, -1):
    print(i)  # 10
            # 9
            # 8
            # 7
            # 6
            # 5
            # 4
            # 3
            # 2
            # 1
