'''             Defination of a factorial

The result of multiplying a sequence of descending natural number (such as 4 x 3 x 2 x 1)

Examples:
    4! = 4 x 3 x 2 x 1 = 24
    7! = 7 x 6 x 5 x 4 x 3 x 2 x 1 = 5040

    Taken from: http://www.mathsisfun.com/definations/factorial.html

Two ways  *****************************************************************************
    Find factorial of 5
        5 * 4 * 3 * 2 * 1 = 120
                or
        1 * 2 * 3 * 4 * 5 = 120

            Factorial of 5 (Using count-up loop)
            F = F * 1 (F = 1)
            F = F * 2 (F = 2)
            F = F * 3 (F = 6)
            F = F * 4 (F = 24)


Pseudocode

1. Start
2. Take the F = 1
3. Set the F = 1
4. Repeat counter = 1 to N
    1. Calculate F = F * counter
5. Display value on the screen


Main
  |
integer N
  |
input N
  |
integer F
  |
F = 1
  |
integer counter
  |
counter = 1 to N --next---
  |                       |
Done |  ^                 |
  |     |           F = F * counter
  |     |_________________|
  |
Output "Factorial is "&F
  |
End


'''

# Take the value from user
N = int(input("Please enter the number: "))

#  set F = 1
F = 1

# next we will loop from one
for counter in range(1, N+1):
      F = F * counter  # F *= counter

# finally we will print the value of F
print("Factorial is ", F)  # Please enter the number: 5
                           # Factorial is  120
