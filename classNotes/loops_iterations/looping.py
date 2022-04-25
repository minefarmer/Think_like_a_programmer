'''     Looping till Positive numbers

Write a program that can take the positive numbers from user. The loop should be terminated when user enters negative number (i.e. -1)  Line 15

        Enter Numbers in valid range  Solution 1   # Not working
Write a program that can take the numbers from 1 to 10. If user enters number in a valid range (1 to 10) then program should display the message "Congratulations, you entered the number in correct range". Otherwise, yhe program should ask the user to re-enter the number until user enters the correct number.    Line 25

        Enter Numbers in valid range  Solution 2  Line 45
        



'''

# num = int(input('Enter the value of num: '))

# while num > 0:
#     print("You entered ", num)
#     num = int(input('Enter the value of num again: '))  # Enter the value of num: 10
                                                        # You entered  10
                                                        # Enter the value of num again: 11
                                                        # You entered  11
                                                        # Enter the value of num again: -2
   
'''    Pseudocode (Method # 1)  # not working

1. Start
2. Enter the number
3. While number is less than 1 or greater than 10
        1. Keep taking the number from user
4. Print the message
5. End

'''

# num = int(input('Enter the value of num: '))

# while N < 1 or N > 10:
#     N = int(input("Please enter the number in range 1 to 10: "))
# print("Congratulations, You entered the number in correct range")




'''     Pseudocode (Method # 2) 

1. Start
2. Enter the number
3. Start an infinate loop
        1. If number is less than 1 or greater than 10
                1. Reenter the number3
        2. Otherwise do the following
                1. Display the message
                2. Break/exit from the loop
3. End

'''

N  = int(input("Please enter the number: "))

while True:
    if N < 1 or N > 10:
        N = int(input("Please re-enter the number in range 1 to 10: "))
else:
    print("Congratulations, you entered the number in correct range")
    break
