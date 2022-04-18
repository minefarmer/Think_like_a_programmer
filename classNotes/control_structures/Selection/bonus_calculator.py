'''   Problem # 3

Write a program that takes the salary and grade from user.
It then adds 50% bonus if the grade is greater tha 15. 
It adds 25% bonus if the grade is 15 or less and then it should display the salary


Pseudocode

1. Start
2. Take the salary and grade from the user
3. If the grade is greater than 15
then
    1. Calculate the bonus using the formula 50 / 100 * salary  #  can also use 1.5
4. Otherwise do the following
    1. Caculate the bonus using the formula 25 / 100 * salary  # can also use 1.25
5. Calculate the total salary using salary = salary + bonus.
6. Display the total salary
7. End

# I need to create three variables: 
#   1. Salary needs to be a floating point number
#   2. grade needs to be a interger
#   3. bonus should be a floating point number


        Main
         |
    Real Salary
         |
    Real bonus
         |
    Interger grade
         |
    Input Salary
         |
    Input bonus
         |
 False   |      True
____if grade > 15__________________________
|                                       |     
Bonus = 25/100 * salary       bonus = 50/100 * salary
|_______________________ 0 _____________|
                        |
                salary = salary + bonus
                        |
                Output"Your total salary is"salary and bonus
                        |
                       End 


'''

salary = float(input("please enter the salary: "))

grade = int(input("please enter your grade: "))

if grade > 15:
    bonus = 50 / 100 * salary

else:
    bonus = 25 / 100 * salary

salary += bonus  # salary = salary + bonus

print("Your total salary is", salary)  # please enter the salary: 50000
                                        # please enter your grade: 18
                                        # Your total salary is 75000.0
