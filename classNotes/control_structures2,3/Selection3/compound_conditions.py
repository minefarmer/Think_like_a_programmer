'''     Compound Conditions

Logical Operators

AND Operator
Or operator
Not operator

A type of condition where we combine or connect differient relational expressions using some connectors

Example: if x> 10 and y <= 9
         if p == 5 or q < 10
         


    P       |   Q       |    P and Q    # P and Q is a compound condition
False           False       False
False           True        False
True            False       False
True            True        True


And Operator

In python, we use the keyword and (small letters) to denote AND operator
It evaluates to true if both conditions on either side of AND operator are true, Otherwise it evaluates to false


>>> 10 > 3 and 4 == 4
True
>>> 9 >= 3 and 10 < 3
False
>>>


Or Operator

In python, we use the keyboard or (small letters) to denote OR operator


>>> 11 > 3 or 3 < 1
True
>>> 1 > 3 or 100 < 2
False


NOT Operator

In Python, we use the keyword not (small letters) to denote not operator
It reverse the result of anycondition. If the result is true, it will reverse it to false and so on

    P   |   not P
 False      True
 True       False


>>> not 1 > 3
True


Precedence of Logical Operators

Operator  |  Precedence
  not           High
  and           Medium
  or            Low
  

>>> not 10 > 3 and 7 <= 5 or 5 > 3
True


I know that  10 is greater than 3 is true, But the not will be evaluated first and it will reverse the desired result of this relation expression and hence the result will be far less nasty and will be richer because it has the second presidence. So the result of this expression will be evaluated with the this expression and we already know that 7 is less than 5 is not true. So therefore the conplete result of this compound expression is false. Next the Or operator will be evaluated. So the result of the expression on the left hand side will be evaluated to the expression on the right.

'''
