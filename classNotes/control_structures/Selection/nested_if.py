''' Nested if

When an if statement is present within an if statement, then it is called = nested if statement

The iner if statement is executed, if an outer if statement is true

# a simple example
if operator == '/':
    if divisor == 0:
        display error message
        
Syntax of Nested if

    if condition 1: # If condition one is true, then the control will enter into the inner condition
        if condition 2:  # will do something if true, if false, it will execute the last part
            do something
        else:
            do something
    else:           # then will execute this part
        do something

Flowchart

                                main
                                |
                     ___False___if___True_______
                    |                           |
                    Output          _False______|___True__
                    |           |                        |
        _False______if_        Output                    Output
       |              |         |                        |
    Output          Output      |___________0____________|
       |              |                     |
       |____________0_|                     |
                    |________0______________|
                             |
                            End 



Pseud0code

1. If the year is evenly divisiable by 4, go to step 2. Otherwise, go to step 5
2. If the year is evenly divisiable by 100, go to step 3. Otherwise go to step 4.
3. If the year is evenly divisiable by 400, go to step 4. Otherwise go to step 5.
4. The year is a leap year (it has 366 days).
5. The year is not a leap year (It has 365 days).

'''

# year = int(input('Enter a year: '))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("year is a leap year")
#         else:
#             print(year, "is not a leap year")  # Enter a year: 1997
#                                                 # 1997 is not a leap year
#     else:
#         print(year, "is a leap year")  # Enter a year: 2012
#                                         # 2012 is a leap year
# else:
#     print(year, "is not a leap year")


'''     Find the smallest number  ***********************************************************

Write a program that takes three numbers from user and then find the smallest number using nested if structure.


                                        Integer Number 1
                                            |
                                        Integer Number 2
                                            |
                                        Interger Number 3
                                            |
                                        Input Number 1
                                            |
                                        Input Number 2
                                            |
                                        Input Number 3
                                            |
                        __________False____#1 = #2___True________________
                       |                                                |
        _______False___|___True______                       ___False____|_____True____
       |            #2 = #3          |                     |         #1 = #3         |
Output #1                       Output #2               Output #3               Output #4
& is minimum                    & is minimum            & is minimum            & is minimum
       |______________0______________|                      |______________0_________|
                      |_____________________0______________________________|
                                            |
                                           End  
    
'''


number1 = int(input("Please enter the first number: "))
number2 = int(input("Please enter the second number: "))
number3 = int(input("Please enter the third number: "))

if number1 < number2:
    if number1 < number3:
        print(number1," is the smallest ")
    else:
        print(number3, " is the smallest number")
else:
    if number2 < number3:
        print(number2, " is the smallest number")
    else:
        print(number3, " is the smallest number")  # Please enter the first number: 2
                                                # Please enter the second number: 4
                                                # Please enter the third number: 5
                                                # 2  is the smallest 
    
