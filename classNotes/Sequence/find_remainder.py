'''  Pseudocode 

1. Start
2. Take dividend from the user
3. Take divisor from user
4. Calculate the quotient
5. Calculate the remainder
6. Disdlays quotient and remainder
7. End

'''

# Take the value of dividend
dividend = int(input('Enter the value of dividend: '))

#  Take the value of the divisor
divisor = int(input('Enter the value of divisor: '))

#  The quotient can be calculated be Interger Division (//)
Q = dividend // divisor

#  The Remainder can be calculated by Modulus Operator (%)
R = dividend % divisor

print('Quotient is', Q, 'Remainder is', R)  # Enter the value of dividend: 13
                                        # Enter the value of divisor: 2
                                        # Quotient is 6 Remainder is 1
