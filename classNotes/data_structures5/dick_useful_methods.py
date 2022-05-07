'''         Usfull methods for dictionaries
    Agenda
keys()
values()
items()
get()
setdefault()

r/bin/python3
>>> student = {'name':'John', 'roolno':10, 'gpa': 3.17}
>>> for i in student.keys():
...     print(i)
...     
... 
name
roolno
gpa
>>> for i in student.values():
...     print(i)
...     
... 
John
10
3.17
>>> for i in student.items():
...     print(i)
...     
... 
('name', 'John')
('roolno', 10)
('gpa', 3.17)
>>> for i, j in student.items():
...     print("key: ", i, "Value: ", j)
...     
... 
key:  name Value:  John
key:  roolno Value:  10
key:  gpa Value:  3.17
>>> 'name' in student.keys()
True
>>> 
>>> 'John' in student.values()
True
>>> student['name']
'John'
>>> student.get ('name', -1)
'John'
>>> student.get ('gender', -1)
-1
>>> if 'name' not in student:
...     student['name'] = 'John'
...     
... 
>>> student.setdefault('gender', 'Male')
'Male'
>>> student
{'name': 'John', 'roolno': 10, 'gpa': 3.17, 'gender': 'Male'}
>>> student.update({"Grade":"A+"})
>>> student
{'name': 'John', 'roolno': 10, 'gpa': 3.17, 'gender': 'Male', 'Grade': 'A+'}



'''