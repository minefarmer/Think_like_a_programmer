"""     More simple if Statements
    
            Problem # 2
Write a program that inputs two numbers and find whether whether they are equal
"""

# num1 = input("Enter the first number: ")  # 4

# num1 = int(num1)

# num2 = input("Enter the second number: ")  # 4
# num2 = int(num2)

# if num1 == num2:
#     print("both numbers are equal")  # both numbers are equal


# num1 = input("Enter the first number: ")  # 3

# num1 = int(num1)

# num2 = input("Enter the second number: ")  # 7
# num2 = int(num2)

# if num1 == num2:
#     print("both numbers are equal")  # nothing was printed




"""     Problem # 3
Write a program that inputs marks of three subjects. If the average of the three marks is more than 80, it displays two messages "You are above standard!" and "Admission granted!"


    Pseudocode
    1. Start
    2. Take marks from user
    3. If marks are greater than 80
        1. Display the message "Write a program that inputs marks of three subjects. If the average of the three marks is more than 80, it displays two messages "You are above standard!" and "Admission granted!"

    4. End
    
    
"""



# take input from the user
subject1 = input("Please enter the marks of Subject 1: ")
subject1 = float(subject1)

subject2 = input("Please enter the marks of Subject 2: ")
subject2 = float(subject2)

subject3 = input("Please enter the marks of Subject 3: ")
subject3 = float(subject3)

Sum = subject1 + subject2 + subject3
    
avg = Sum / 3

if avg > 80:
    print("You are above standard!")
    print("Admission granted!")  # Please enter the marks of Subject 1: 80
                                # Please enter the marks of Subject 2: 85
                                # Please enter the marks of Subject 3: 78
                                # You are above standard!
                                # Admission granted! 
  

  