'''             String basics # 4
    Agenda (Part 4)

startwith() and endwith()
join() and split()
rjust(), ljust(), and center()
strip(), rstrip(), and lstrip()

>>> "rich".startswith("r")
True
>>> "rich".endswith("h")
True
>>> # join()
>>> names = ["John", "Ali", "Rich"]
>>> names1 = " "
>>> names1 .join(names)
'John Ali Rich'
>>> names1 = ""
>>> names1.join(names)
'JohnAliRich'
>>> names1 = ","
>>> names1.join(names)
'John,Ali,Rich'
>>> # split()
>>> text = "My name is rich"
>>> text.split(" ")
['My', 'name', 'is', 'rich']
>>> p = input("Please enter three numbers with spaces: ")
Please enter three numbers with spaces: 12 54 87
>>> p.split(" ")
['12', '54', '87']
>>> numbers = p.split(" ")
>>> x1 = int(numbers[0])
>>> x1
12
>>> x2 = int(numbers[1])
>>> x2
54
>>> # Justifying Text
>>> 'hello'.rjust(10)
'     hello'
>>> 'hello'.ljust(10)
'hello     '
>>> 'hello'.center(10)
'  hello   '
>>> # removing white spaces
>>> '   hello world'.strip
<built-in method strip of str object at 0x7fa72c252bb0>
>>> '   hello world'.strip()
'hello world'
>>> '   hello world'.ltrip()
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    '   hello world'.ltrip()
AttributeError: 'str' object has no attribute 'ltrip'
>>> '   hello world'.lstrip()
'hello world'
>>> '   hello world     '.lstrip()
'hello world     '
>>> '   hello world     '.rstrip()
'   hello world'
>>> 

'''