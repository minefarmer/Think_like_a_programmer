'''         Exception Handling: Part 1
            Exception Handling: Part 2   line 40
            Raising my own exception     line 68
    Common types of exceptions
Division by zero
Key error
Value error
Type error
Many others...


>>> try:
...     print(10 / 0)
... except:
...     print("Error: Division by Zero")
...
Error: Division by Zero
>>>
>>> try:
...     print(10 + 'Carl')
... except:
...     print("Error: Division by Zero")
...
Error: Division by Zero




'''
# Division by zero.
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Division by Zero")  # Division by Zero
except ValueError:
    print("Can't convert from 'sdg' to int")



'''         Part 2

>>> # Using Exception Class
>>> try:
...     a = [10, 20, 30, 40]
...     print(a[4])
... except Exception as e:
...     print("Error Type: {}, Error Message: {}".format(type(e), e.args))
...
Error Type: <class 'IndexError'>, Error Message: ('list index out of range',)

>>>
>>> try:
...     a = {1: 'a', 2: 'b'}
...     print(a[4])
... except Exception as e:
...     print("Error Type: {} Error Message: {}".format(type(e), e.args))
...
Error Type: <class 'KeyError'> Error Message: (4,)
>>> try:
...     print(10 + '')
... except Exception as e:
...     print("Error Type: {}, Error Message: {}".format(type(e), e.args))
... finally:
...     print("Lets wind up things here..")
...
...

>>> # Raising my own exception  **************************************************************
>>> try:
...     raise Exception("This is my own generated exception...")
... except Exception as e:
...     print(e.args)
...('This is my own generated exception...',)



'''
