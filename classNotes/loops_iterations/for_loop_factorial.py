'''         Print the series (Horizontally
Write a program that prints the series 1 4 5 10 13 16 19 22 25 28 horizontally on the screen using the for loop

Example:
1
1 + 3 = 4
4 + 3 = 7

25 + 3 = 28


Sum of first N Numbers  line 40

'''

# for i in range(1, 29, 3):
#     print(i)  # 1
#                 # 4
#                 # 7
#                 # 10
#                 # 13
#                 # 16
#                 # 19
#                 # 22
#                 # 25
#                 # 28



# Way to get horizontial output.
for i in range(1, 29, 3):
    print(i,end =",")  # 1,4,7,10,13,16,19,22,25,28,(venv)







'''             Sum of first N Numbers

Write a program that takes an interger number N from user. It nthen calculates an displays the sum of numbers from 1 to N.


    For example:
    Please enter a number: 5
    Sum of first 5 numbers is 15
        1+2+3+4+5 = 15
        

Pseudocode

1. Start
2. Set SUM = 0
3. Take an integer N from user
4. Repeat counter = 1 to N
    1. SUM = SUM + counter
5. Display SUM

'''


# Take the value from user
N = int(input("Please enter the number: "))

#  Set SUM = 0
SUM = 0

#  Loop from 1 to N
for i in range(1, N+1):
    SUM += i
    
# display the SUM
print("Sum is ", SUM)  # Please enter the number: 5
                       # Sum is  15
