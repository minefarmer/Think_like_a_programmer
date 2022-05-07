'''         String Basics Part 2
Concatenation
Indexing and Slicing
in and not in
upper(), lower(), isupper(), and isLower()


>>> firstName = "Carl"
>>> lastName = "Matson"
>>> print(firstName + lastName)
CarlMatson
>>> print("Carl" + str(10))
Carl10
>>> print("Carl" + " " + str(10))
Carl 10
>>> 
>>> # indexing
>>> name = "Carl"
>>> name[0]
'C'
>>> name[2]
'r'
>>> len (name)
4
>>> for i in name:
...     print(i)
...     
...     
... 
C
a
r
l
>>> 
>>> # Slicing
>>> venue = "Mirpur University"
>>> venue[0:6]
'Mirpur'
>>> venue[7:]
'University'
>>> "Mirpur" in venue
True
>>> "CAT".lower
<built-in method lower of str object at 0x7fa52aceea70>
>>> "CAT".lower()
'cat'
>>> "cat".upper()
'CAT'
>>> "Carl".lower
<built-in method lower of str object at 0x7fa52ba63070>
>>> "Carl".lower()
'carl'
>>> "cat".islower()
True
>>> "CAT".isupper
<built-in method isupper of str object at 0x7fa52ad5f9f0>
>>> "CAT".isupper()
True
>>> 



'''