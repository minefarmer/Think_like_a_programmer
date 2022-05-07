'''         Dictionaries

>>> student = {'name': "Carl', 'rollno':10, 'cgpa:3.1}
  File "<input>", line 1
    student = {'name': "Carl', 'rollno':10, 'cgpa:3.1}
                                                      ^
SyntaxError: EOL while scanning string literal

>>> student = {'name': 'Carl', 'rollno':10, 'cgpa':3.}
>>> student
{'name': 'Carl', 'rollno': 10, 'cgpa': 3.0}
>>> student['name']
'Carl'

>>> Week = {1:'Monday', 2:'Tuesday', 3:'Wednesday'}
>>> Week[1]
'Monday'

>>> x1 = [10, 20, 30]
>>> x2 = [20, 10, 30]
>>> x1 == x2
 
>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
>>> egg = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
>>> ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
>>> egg == ham
True



>>> student = {'name':'John', 'rollno':10, 'cgpa': 3.17}
>>> student['gender'] = 'male'
>>> student
{'name': 'John', 'rollno': 10, 'cgpa': 3.17, 'gender': 'male'}
>>> 'name' in student
True
>>> del student['gender']
>>> student
{'name': 'John', 'rollno': 10, 'cgpa': 3.17}
>>> 

'''