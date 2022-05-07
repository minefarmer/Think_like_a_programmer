'''             Break statement
Break statement is used to exit from a loop.


                Continue State4ment
Continue statement will move the control to the next iteration and skip all statements that comes after the continue statement.

    Examp0le:
Let's say we want to print the firsr 100 nubers that are not a multiple of 3
During the iteration of the loop, we want to skip those numbers that are multiples of three.

If N % 3 == 0:
    continue
    


Prime numbers line 53 ***********************************************************


# Break and continue (Practice) line 120  ****************************************

'''

# for i in range(5):
#     if i == 3:
#         continue
#     print(i, end =",")  # 0,1,2,4,  ## only with numbers


# for i in range(5):
#     if i == 3:
#         break
#     print(i)  # 1
#               # 2
              
# for i in range(5):
#     if i == 3:
#         continue
#     print("Hello World!")
#     print("Bye") # Hello World!
#                 # Bye
#                 # Hello World!
#                 # Bye
#                 # Hello World!
#                 # Bye
#                 # Hello World!
#                 # Bye





'''Prime numbers  *************************************************

A prime number (or prime) is a natural number greater than 1 tha has no positive divisers other that 1 and itself

A naturl number greater than 1 that is not a prime number is called a composite number

For example, 5 is a prime number because 1 and 5 are its only positive interger factors, whereas 6 is composite because it has the devisors 2 and 3 in addition to 1 and 6



Find Prime numbers

Write a p[rogram that inputs an interger and prints if it is prime or composite. (Use break command)


# procedure 1: if N is number then divide N from 2 to N - 1
#  if at any statge, remainder is ZERO then it's not a prime number
# if N is not divisible by any number from 2 to N - 1, then it is a prime number

>>> 5 % 2 == 0
False
>>> 5 % 3 == 0
False
>>> 5 % 4 == 0
False
>>> 5 % 5 == 0
True

# Find whether 11 is prime or not. Only need to go half way

>>> 11 % 2 == 0
False
>>> 11 % 3 == 0
False
>>> 11 % 4 == 0
False
>>> 11 % 5 == 0
False

# procedure 2: If N is Number then divide the number from 2 to N / 2(Interger)
# for example if N = 17, then you should divide it from 2 to 8 (17/2 = 8)

'''

# Take the number from user
# N = int(input("Please enter the number: "))

# isPrime = True
# #  check whether it is prime or not:
# for i in range(2, N // 2 + 1):
#     if N % i == 0:
#         isPrime = False
#         break
# if isPrime == True:
#     print(N, " is a prime number")  # Please enter the number: 5
#                                     # 5  is a prime number
# else:
#     print(N, " is a composite number")  # Please enter the number: 12
#                                         # 12  is a composite number








'''     Break and continue (Practice)  **********************************************************

Write a program that can display the numbers from 1 to 100 which are not multiples of 3 and 5


'''

# for i in range(1, 101):
#     if i % 3 == 0 or i % 5 == 0:
#         continue
#     else:
#         print(i,end=',')  # 1,2,4,7,8,11,13,14,16,17,19,22,23,26,28,29,31,32,34,37,38,41,43,44,46, 47,49,52,53,56,58,59,61,62,64,67,68,71,73,74,76,77,79,82,83,86,88,89,91,92,94,97,98,



for i in range(1, 101):  # the teacher got a differient result
    if i % 3 == 0 and i % 5 == 0:
        continue
    else:
        print(i)  # 1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,40,41,42,43,44,46,47,48,49,50,51,52,53,54,55,56,57,58,59,61,62,63,64,65,66,67,68,69,70,71,72,73,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,93,94,95,96,97,98,99,100,
        


