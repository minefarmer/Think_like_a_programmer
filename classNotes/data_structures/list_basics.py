'''         List basics

List Basics Part two:   line 60
List Basics Part three:   line 140

        Agenda

Purpose of lists
Creating lists
Empty lists
Adding things to a list
Getting things from a list


>>> mylist = [10, 20, 30, 40]
>>> mylist
[10, 20, 30, 40]
>>> names = ["Tahir", "Rich", "Sis", "Roger"]
>>> names
['Tahir', 'Rich', 'Sis', 'Roger']
>>> # lists can hold anything
>>> mixture = ["tahir", 10, 20.98, 'male']
>>> mixture
['tahir', 10, 20.98, 'male']
>>> # empty list
>>> a = []
>>> a
[]
>>> # using append() function
>>> a = []
>>> a.append(10)
>>> a
[10]
>>> a
[10, 20]
>>> a.append(30)
>>> a
[10, 20, 30]
>>> # getting elements from a list
>>> a = [10, 20, 30]
>>> a[0]
10
>>> # insert() method
>>> a = [10, 20, 30, 40]
>>> a.insert(1, 5)
>>> a
[10, 5, 20, 30, 40]
>>> # extend method
>>> a.extend([60, 70])
>>> a
[10, 5, 20, 30, 40, 60, 70]
>>> x = [100, 200, 300]
>>> a.extend(x)
>>> a
[10, 5, 20, 30, 40, 60, 70, 100, 200, 300]
>>> 



                List basics: Part two **************************************************
        Summary of Insertion Methods

append() -> this will append single element at the end of the list
extend() -> this will append list of elements to the end of the list
insert() -> this will append insert an element at the specific index in the list

        Agenda
        
Modifying items in a list
"Slicing" a list
Deletion from a list (remove(), del, pop())


bpython version 0.21 on top of Python 3.9.2 /usr/bin/python3
>>> mylist = [10, 20, 30, 40,]
>>> mylist[2] = 100
>>> mylist[2]
100
>>> mylist
[10, 20, 100, 40]
>>> # Slicing a list
>>> a = [10
... , 20, 30, 40]
>>> a[0:2]
[10, 20]
>>> p = a[0:2]
>>> p
[10, 20]
>>> a
[10, 20, 30, 40]
>>> b = [10, 20, 30, 40, 50, 60, 70]
>>> b[3:]
[40, 50, 60, 70]
>>> b[:3]
[10, 20, 30]
>>> b[:4]
[10, 20, 30, 40]
>>> b[:]
[10, 20, 30, 40, 50, 60, 70]
>>> b
[10, 20, 30, 40, 50, 60, 70]
>>> a
[10, 20, 30, 40]
>>> b = a
>>> b
[10, 20, 30, 40]
>>> a.append(100)
>>> a
[10, 20, 30, 40, 100]
>>> b
[10, 20, 30, 40, 100]
>>> b = a[:]
>>> b.append(200)
>>> b
[10, 20, 30, 40, 100, 200]
>>> a
[10, 20, 30, 40, 100]
>>> #  deleti>>> myList = ["Tahir", "John", "Ali", "Maria"]
>>> myList
['Tahir', 'John', 'Ali', 'Maria']
>>> myList.remove("John")
>>> myList
['Tahir', 'Ali', 'Maria']
>>> del myList[2]
>>> myList
['Tahir', 'Ali']
>>> myList
['Tahir', 'Ali']
>>> myList.pop()
'Ali'
>>> myList  
['Tahir']
>>> 






# Basics of lists part 3:  **************************************************************

Agenda

Traversing a list
Searching a list (in, index())
Sorting a list
Min and max function
count function


bpython version 0.21 on top of Python 3.9.2 /usr/bin/python3
>>> a = [12, 23, 34, 45, 56, 67]
>>> for i in a:
...     print(i)
...     
... 
12
23
34
45
56
67
>>> for i in [12, 23, 34, 56]:
...     print(i)
...     
... 
12
23
34
56
>>> for i in range(5):
...     print(a[i])
...     
... 
12
23
34
45
56
>>> for i in range(len(a)):
...     print(a[i])
...      
...  
... 
12
23
34
45
56
67

>>> # Searching a list
>>> a = [12, 34, 45, 76, 87]
>>> 34 in a
True
>>> 100 in a
False
>>> a.index(45)
2
>>> a.index(100)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    a.index(100)
ValueError: 100 is not in list
>>> 
>>> 
>>> # sorting a list
>>> a = [90, 76, 87, 54, 32, 12, 34, 100]
>>> a.sort()
>>> a
[12, 32, 34, 54, 76, 87, 90, 100]
>>> names= ['John', 'Ali', 'Maria', 'Tahir']
>>> names.sort()
>>> names
['Ali', 'John', 'Maria', 'Tahir']
>>> a = [12, 65, 54, 100, 90]
>>> p = sorted(a)
>>> p
[12, 54, 65, 90, 100]
>>> a
[12, 65, 54, 100, 90]
>>> a = [10, 20, 30, 40]
>>> a.reverse()
>>> a
[40, 30, 20, 10]
>>> min(a)
10
>>> max(a)
40
>>> b = [12, 43, 65, 12, 54, 76, 54, 12]
>>> b.count(12)
3
>>> a = [10, 4, 76, 98, 43, 100]
>>> max(a)
100
>>> min(a)
4
>>> 



'''