'''     Find first N prime numbers

Write a program that can find the first N prime number.
The program should display all first N Prime numbers and should also display the count of all prime numbers.

'''
N = int(input("Please enter the number up to which you want to find prime numbers: "))

count = 0
if N > 1:
    for i in range(2, N + 1):
        isPrime = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                isPrime = False
                break
    if isPrime:
        print(i, " is a prime number")
        count +- 1
        
else:
    print("Prime number should be greater than 1")
print(count, " prime numbers are found")

