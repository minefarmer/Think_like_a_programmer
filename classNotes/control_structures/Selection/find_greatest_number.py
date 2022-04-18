'''   Find the greatest number

Write a program that takes three numbers from user and then find the greatest number

'''

A = int(input("Please enter the first number: "))

B = int(input("Please enter the second number: "))

C = int(input("Please enter the third number: "))

if A > B and A > C:
    print(A, " is the greatest number")

elif B > A and B > C:
    print(B, "is the greaest number")
else:
    print(C,"is the greatest number")  # Please enter the first number: 10
                                    # Please enter the second number: 34
                                    # Please enter the third number: 100
                                    # 100 is the greatest number

