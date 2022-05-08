'''         Exception Handling: Part 1
            Exception Handling: Part 2

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
    

