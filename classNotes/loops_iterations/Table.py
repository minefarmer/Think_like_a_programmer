'''         While Loop

N = 2
print(N, " x ", 1, " = ", N*1)
print(N, " x ", 2, " = ", N*1)
print(N, " x ", 3, " = ", N*1)
print(N, " x ", 4, " = ", N*1)
print(N, " x ", 5, " = ", N*1)  # 2  x  1  =  2
                                # 2  x  2  =  2
                                # 2  x  3  =  2
                                # 2  x  4  =  2
                                # 2  x  5  =  2
'''

N = int(input("Please enter the number: "))
for i in range(1, 11):
    print(N, " x ", 1, " = ", N*i)
'''  Please enter the number: 2
                                2  x  1  =  2
                                2  x  1  =  4
                                2  x  1  =  6
                                2  x  1  =  8
                                2  x  1  =  10
                                2  x  1  =  12
                                2  x  1  =  14
                                2  x  1  =  16
                                2  x  1  =  18
                                2  x  1  =  20
'''