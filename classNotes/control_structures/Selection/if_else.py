''' Pseudocode

1. Start
2. Take an interger number from user
3. Calculate whether the number is even or odd.
4. If the number is even
    1. Display the message "Number is even"
5. Otherwise
    1. Display the message "Number is odd"


>>> 13 % 2  # % is called modulus
1  

>>> 4 % 2
0   

**********************************
        Main
         |
    Integer number
         |
    Interger result
         |
     Input number   # taken from user
         |
    result = number % 2
         |
  False  |  True
         |    
____result == 0 ____________    # 0 is even, 1 is odd
|                           |
Output "Number is Odd"      Output "Number is even"
|___________________________|
           |
          End


'''

number = int(input("Please enter the number: "))

result = number % 2

if result == 0:
    print("Number is even") # Please enter the number: 13
                            # Number is odd
else:
    print("Number is odd")  # Please enter the number: 4
                            # Number is even

