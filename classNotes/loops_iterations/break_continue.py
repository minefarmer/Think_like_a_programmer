'''             Break statement
Break statement is used to exit from a loop.


                Continue State4ment
Continue statement will move the control to the next iteration and skip all statements that comes after the continue statement.

    Examp0le:
Let's say we want to print the firsr 100 nubers that are not a multiple of 3
During the iteration of the loop, we want to skip those numbers that are multiples of three.

If N % 3 == 0:
    continue
    


Prime numbers line 50 ***********************************************************

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
N = int(input("Please enter the number: "))

isPrime = True
#  check whether it is prime or not:
for i in range(2, N // 2 + 1):
    if N % i == 0:
        isPrime = False
        break
if isPrime == True:
    print(N, " is a prime number")  # Please enter the number: 5
                                    # 5  is a prime number
else:
    print(N, " is a composite number")  # Please enter the number: 12
                                        # 12  is a composite number
    
