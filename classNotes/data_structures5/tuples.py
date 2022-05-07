'''         Tuples
>>> x = (10, 20, 30)
>>> x
(10, 20, 30)
>>> x[0]
10
>>> x[1] = 100
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    x[1] = 100
TypeError: 'tuple' object does not support item assignment
>>> x = (10,)
>>> type(x)
<class 'tuple'>
>>> y = (20)
>>> type(y)
<class 'int'>
>>> #tuple() and list()
>>> tuple([10, 20, 30, 40])
(10, 20, 30, 40)
>>> list((10, 20, 30))
[10, 20, 30]
>>> 


'''