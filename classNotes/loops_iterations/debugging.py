N = int(input("Please enter the number: "))

isPrime = True
#  check whether it is prime or not:
if N > 1:
    for i in range(2, N // 2 + 1):
        if N % i == 0:
            isPrime = False
            break
    if isPrime == True:
        print(N, " is a prime number")  # Please enter the number: 1
                                        # 1  is not 
                                        # a prime number
                                        
                                        # Please enter the number: -2
                                        # -2  is not a prime number
    else:
        print(N, " is a composite number")  # Please enter the number: 12
                                            # 12  is a composite number
else:
    print(N, " is not a prime number")
    