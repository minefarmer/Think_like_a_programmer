'''     Control Structures

A statement used to control the flow of execution in a program is called a control structure.


    Types of control structures
    
1. Sequence     ******************************************************

In a sequential structure the statements are executed in the same order in which they are specified in the program, the control flows from one statement to the other in a logical sequence, all sequences are executed exactly as run.
It means that no statement is kept and no statement is executed more than once.

    Statement # 1
    Statement # 2
    Statement # 3
    Statement # 4

        An example
        Start
          |
        input base
          |
        input height
          |
        input height
          |
        calculate area
        Area = 1/2 * base * height
          |
        Display Area
          |
        End
        



2. Selection        ******************************************************

A selection structure selects a statement or set of statements to execute on the basis of a condition.
In this structure, a statement or set of statements is executed when the condition is True. And ignored when the condition is False.

        An example
    Suppose a program that imputs the temperature and then displays the message on the screen.
    
    If the temperature is greater than 35, the it displays the message "Hot day".
    
    When the temperature is between 25 and 35 the it displays the message "Pleasant day".
    
    If it is less than 25, then it displays the message "cool day".

        
            Flowchart of simple selection.
                    Condition
                      T or F
                T               F
            (if True)        (if False)
            Statement #1    Statement #2
    


3. Repetition

A repetition structure executes a statement or set of statements repeadadly.

It is also known as iterations or loops.


        An example.
    Suspose we want to display a message to the screen "Hello World" one thousand times!
    
    It takes huge time to write that code and it takes more space as well. (lenghty awkward looking code)
    
    It is very easy to perform this task usig loops or repetition structure.
    
                Flowchart of Repetition
                     _______
                    |       |
                    |       |
                    |   Condition   =   F    
                    |     T or F        |
                    |       | T         |
                    |       |           |
                    |   Statement       |
                    |_______|           |
                                        |
                                    End of loop




4. Relational or Comparision Operators.

Less than, greater than or equal to.
Sometime we need to do a lot of comparisions in order to see whether a specific command should be executed.
    The conditional statements are used to specify conditions in programs.
    
    A relatinal operator compares two values. It produces a result as True or False.
    
    The relation operators are sometimes called the conditional operators as they test conditions that are tru or false.

        RELATIONAL OR COMPARISION OPERATORS
>       Greater than returns true if the value on the left side of > is greater than the value on the righr side. Otherwise, it returns false.
>>> # greator than operator  (>)
>>> 10 > 3
True
>>> 10 > 13
False

<       Less than operator returns true if the value on the left side < is less than the value on the rught side. Otherwise it returns false.
>>> # Less Than operator (<)
>>> 3 < 7
True
>>> 10 < 7
False

==      Equals operator returns true if the value on both sides of == are equal. Otherwise returns false.  == The assignment operator is used to assign the value on the right hand side of any expression to the variable on the left hand side while the equal equal operator which is Gradley comparision operator is used to compare the two to values on the left and right hand side of this operator.
>>> 10 == 10
True
>>> 10 == 11
False


>=      Greater that or equal to operator returns true if the value on the left side of >= us greator than or equal to the value on the right hand side. Otherwise returns false.
>>> # Greater that or equal to operator (>=)
>>> 10 >= 9
True
>>> 10 >= 10
True
>>> 10 >= 11
False

<=      Less that or equal to operator returns true if the value on the left of <= is less than or equal to value on right side. Otherwise returns false.
>>> # Lesser than or equal to operator
>>> 10 <= 10
True
>>> 10 <= 11
True
>>> 10 <= 9
False

!= The not equal to operator. Returns true if the value on the left side of != is not equal to the value on the right. Otherwise returns false.
>>> # not equal to operator
>>> 10 != 10
False
>>> 10 == 10
True
>>> 3 != 5
True


'''

