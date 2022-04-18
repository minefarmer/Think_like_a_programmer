'''     Elif Statement        lesson 34
Elif statement is used to chose one block of statement from many blocks of statements.

It is used when there are many options and only one block of statements

    Test score | Grade
    >= 90       A
    >= 80       B
    >= 70       C
    >= 60       D
    Selow 60    R
    
					     
										    Main
										     |
									  False    |   True
								____________test_score > 90________________
								|                                          |
					     __False__Test score > 80_____True__          Output"grade A"
					    |                                   |                   |
				 _False____Test score > 70_____True__         |                   |
				|                                    |        |                   |    
	   __False__Test score > 60 ___True__                  |     Output "Grade B"       |
	  |                                  |                 |        |                   |
  Output"Grade F"                          |       Output "grade C"   |                   |
	  |                             Output "Grade D        |        |                   |
	  |                                  |                 |        |                   |
	  |____________0_____________________|                 |        |                   |        
			   |________________0______________________|        |                   |
						  |______________0________________|                   |
								     |                                    |
								     |__________________0_________________|
												|
											     End


		Problem # 1   ******************************************************     
'''


# test_score = int(input("Please enter the test score: "))

# if test_score >= 90:
#       print("You are awarded grade A")


# elif test_score >= 80:
#       print("You are awarded grade B")

# elif test_score >= 70:
#       print("You are awarded grade C")

# elif test_score >= 60:
#       print("You are awarded grade D")  # Please enter the test score: 67
#                                     # You are awarded grade D
	
# else:
#       print("You are awarded grade F")  # Please enter the test score: 47
#                                     # You are awarded grade F




'''    Problem # 2 *******************  Weekday name  *********************************

 Write a program that inputs number of week's day and displays the name of the day.
 For example, if user enters 1, it displays "Monday" and so on.

'''

# week_day = int(input("Please enter the week day: "))

# if week_day == 1:
# 	print("Monday")  # Please enter the week day: 1
# 				# Monday

# elif week_day == 2:
# 	print("Tuesday")  # Please enter the week day: 2
# 					# Tuesday

# elif week_day == 3:
# 	print("Wednesday")  # Please enter the week day: 3
# 						# Wednesday

# elif week_day == 4:
# 	print("Thursday")  # Please enter the week day: 4
# 						# Thursday

# elif week_day == 5:
# 	print("Friday")  # Please enter the week day: 5
# 					# Friday

# elif week_day == 6:
# 	print("Saterday")  # Please enter the week day: 6
# 						# Saterday

# elif week_day == 7:
# 	print("Sunday")  # Please enter the week day: 7
# 					# 10

# else:
# 	print('invalid input!')  # Please enter the week day: 10
# 							# invalid input!
       


'''	Problem # 3  *********************** Arithmatic caculator  *****************************

Write a program that takes two floating point numbers and an 'String type' operator. It then performs the operations (addition, subtraction, multiplication etc.) based on the operator and should display the result.

If divisor is equal to zero then it should display the error message. 

If operator is invalid then it should display the error message

Python assumes a string as a connector, if it contains only one item.

Example:
	Gender = 'M'
	Answer = 'Y'


Pseudocode

1. Start
2. Take the two floating point numbers and and operator from the user
3. If operator is equal to '+' then
	1. Perform the addition operation and display the result
4. If operator is equal to '*' then
	1. Perform the multiplication operation and display the result
5. If operator is equal to '/' then
	1. If the divisor is equal to zero than
		1. Display the error message
	2. Otherwise perform division operation and display the result
6. If operator is equal to '-' then
	1. Perform subtraction operation and display the result
7. otherwise, display the message "invalid operator"

'''

n1 = float(input("please enter the first number: "))
n2 = float(input("please enter the second number: "))

op = input('please enter the operator: ')

if op == '+':
    print("result is ", n1 + n2)  # please enter the first number: 10
								# please enter the second number: 10
								# please enter the operator: +
								# result is  20.0
elif op == '-':
    print("result is ", n1 - n2)
elif op == '/':
    if n2 == 0:  # n2 is the divisor here
        print("Error: Diviser can't be zero")  # please enter the first number: 10

    else:
    	print("result is ", n1 / n2)
elif op == '*':
    print("result is", nl * n2)
else:
    print("invalid operator")  # please enter the first number: 4
							# please enter the second number: 7
							# please enter the operator: @
							# invalid operator
