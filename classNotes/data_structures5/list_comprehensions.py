'''     List Comprehensions    
List comprehensions provide a concise and easy way to create lists.
List comprehensions are a tool for transforming one list into another list. Durning this operation transformation, elements can be conditionally included in the new list and each element can be transformed as needed
    Defination taken from: http://treyhunner.com/2015/12/python-list-comprhensions-now-in-color


    Syntax
'new list' = [ *output expression*  *iteration*  *filter(optional)* ]

>>> # create a list that contains numbers from 0-9
>>> x = [i for i in range(10)]
>>> x
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> 
>>> y = [i for i in range(21) if i%2 == 0]
>>> y
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> 
>>> y = [i for i in range(21) if i%2 == 1]
>>> y
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> 


>>> # create a list that contains the squares of numbers from 0 to 10
>>> squares = [x ** 2 for x in range(11)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> 
>>> # Create a list that multiplies each number from 1to 10 with 2
>>> N = [x * 2 for x in range(1, 11)]
>>> N
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> 
>>> 
>>> # Create a 2D list using list comparehensions
>>> List = [[0]*3 for i in range(3)]
>>> List
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> 
'''