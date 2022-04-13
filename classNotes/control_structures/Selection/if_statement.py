'''     Simple if statement

A Selection structure selects a statement or set of statements is to execute on the basis of a condition.

In this structure, statement or set of statemnts is executed when a particular condition is True and ignored when the condition is false.

        A simple flowchart of simple selection or to see if the condition is true when we execute the statement #1. However, if the condition is false we do nothing.
            Condition
         ---  T or False ---
      T |                   | F
        |                   |
        |                   |
    Statement # 1           |
        |                   |
        |________0__________|


# if is a keyword in python language.
# if statement is a decision making statement.
# it is the simplist form of selection statements.
# it is used to execute or skip a statement or set of statements by checking a condition.
# The condition is given as relational expression
# For example 10 > 4, 2 < 5, 10 != 23
# if the condition is true, the statement is executed.
# if th condition is false, the statement is not executed.



        Syntax of simple if

if relational expresion:
    do something
    
>>> if 10 > 3:
...     print("Hello")
... 
Hello
    

'''

if 10 > 3:
    print("Hello") # Hello


    """Pseudocode
    1. Start
    2. Take marks from user
    3. If marks are greater than 50
        1. Display the message "Congratulations. You have passed"
    4. End
    """


# take input from the user
marks = input('Please enter the marks! ')

marks = int(marks)

if marks > 50:
    print("Congradulations! You have passed. ")  # Please enter the marks! 89
                                                # Congradulations! You have passed.
    
