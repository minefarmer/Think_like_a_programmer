""" Return a value
>>> len("hello")
5
>>> max(10, 20)
20
>>> 

carl@carlhptiny:~/Desktop/MatsHub/Think_like_a_programmer$ /usr/bin/python /home/carl/Desktop/MatsHub/Think_like_a_programmer/classNotes/functions/return_a_value.py
Traceback (most recent call last):
  File "/home/carl/Desktop/MatsHub/Think_like_a_programmer/classNotes/functions/return_a_value.py", line 19, in <module>
    x = Max(a, b)
NameError: name 'a' is not defined
carl@carlhptiny:~/Desktop/MatsHub/Think_like_a_programmer$ /usr/bin/python /home/carl/Desktop/MatsHub/Think_like_a_programmer/classNotes/functions/return_a_value.py
Traceback (most recent call last):
  File "/home/carl/Desktop/MatsHub/Think_like_a_programmer/classNotes/functions/return_a_value.py", line 19, in <module>
    print("Maximum value is", Max(num1, num2))
NameError: name 'num1' is not defined
carl@carlhptiny:~/Desktop/MatsHub/Think_like_a_programmer$ 



"""


def Max(a, b):
    if a > b:
        return a
    else:
        return b

print("Maximum value is", Max(num1, num2))

