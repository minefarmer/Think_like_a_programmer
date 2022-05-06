'''         String Basic        New format function

>>> name = 'Maxwell'
>>> gender = "male"
>>> age = 30
>>> print("My name is {}, my gender is {} and my age is {}".format(name, gender, age))
My name is Maxwell, my gender is male and my age is 30
>>> 
>>> print("{0} is better than {1}".format("Maria", "John"))
Maria is better than John
>>> 
>>> print("{0} is better than {1}".format("Maria", "John"))
Maria is better than John
>>> print("{1} is better than {0}".format("Maria", "John"))
John is better than Maria


>>> # 3.3415926
>>> print("{;.2f}".format(3.1415926))
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    print("{;.2f}".format(3.1415926))
KeyError: ';'
>>> print("{:.2f}".format(3.1415926))
3.14
>>> print("{:+.2f}".format(3.1415926))
+3.14
>>> print("{:+.2f}".format(-3.1415926))
-3.14
>>> print("{:.2f}".format(3.1415926))
3.14
>>> print("{:.0f}".format(3.1415926))
3
>>> #MM/DD/YY
>>> print("{:0>2d}/{:0>2D}/".format(3, 9, 16))
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    print("{:0>2d}/{:0>2D}/".format(3, 9, 16))
ValueError: Unknown format code 'D' for object of type 'int'
>>> print("{:0>2d}/{:0>2d}/".format(3, 9, 16))
03/09/
>>> print("{:x<4d}".format(30))
30xx
>>> print("{:x<4d}".format(3000))
3000
>>> # 1000000 => 1,000,000
>>> print("{:,}".format(1000000)))
  File "<input>", line 1
    print("{:,}".format(1000000)))
                                 ^
SyntaxError: unmatched ')'
>>> print("{:,}".format(1000000))
1,000,000
>>> # .35 to 35%
>>> print("{:,0%}".format(.35))
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    print("{:,0%}".format(.35))
ValueError: Invalid format specifier
>>> print("{:.0%}".format(.35))
35%
>>> print("{:.0%}".format(.35))
35%
>>> print("{:.2%}".format(.35))
35.00%
>>> print("{:>0e}".format(1000000000)
... print("{:>0e}".format(1000000000))
  File "<input>", line 2
    print("{:>0e}".format(1000000000))
    ^
SyntaxError: invalid syntax
>>> print("{:>0e}".format(1000000000))
1.000000e+09
>>> # right hand aligned
>>> print("{:10d}".format(13))
        13
>>> # left aligned
>>> print("{:<10d}".format(13))
13        
>>> # center alighned
>>> print ("{:^10d}".format(137545))
  137545  
>>> # center aligned
>>> print ("{:^10d}".format(137545))
  137545  
>>> 
>>> 
>>> print ("{:^10d}".format(1376))
   1376   
>>> 


'''