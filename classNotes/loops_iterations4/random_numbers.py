'''     Two methods for creating random numbers

randint(a,b)
choice(Sequence)

>>> import random
>>> random.randint(1, 5)
3
>>> random.randint(1, 5)
4
>>> random.randint(1, 5)
5
>>> random.randint(1, 5)
2
>>> random.randint(1, 5)
5
>>> 

>>> for i in range(5):
...     random.randint(1, 10)
... 
5
10
6
6
4
>>> 


>>> import random
>>> random.choice([1, 2, 3, 4, 5])
1
>>> random.choice([1, 2, 3, 4, 5])
2




'''
import random

for i in range(5):
    random.randint(1, 10)
