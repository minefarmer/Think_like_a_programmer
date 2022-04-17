''' Check valid age

Write a program that takes age fro the user and then decide whether the age is between 18 to 24. If so, then it will display the message "You can apply for youth festival program". Otherwise, display the message "Sorry, you cannot apply".

If age >= 18 and age <= 24  # Not correct

If age = 18 and age < 24  # correct solution

'''

age = int(input("Please enter the age: "))

if age >= 18 and age <= 24:
    print("You can apply for Youth Festival program")
else:
    print("Sorry, you cannot apply")  # Please enter the age: 20
                                    # You can apply for Youth Festival program
                                    
                                    # Please enter the age: 30
                                    # Sorry, you cannot apply
