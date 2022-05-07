'''     Nested Loops  # lesson 65, 66 = 40, 67 = 60

A loop within a loop is called a nested loop.
The inner loop is executed completely with each new value in the counter of outer variable
Any loop can be used as inner loop of any outer loop.
While loop can be nested in a for loop and visa versa
Same loops can also be nested. For example for loop within for loop or while loop within while loop.


       Main
        |
Interger outer
        |
Interger inner
        |
Outer = 1 to 5 _Next___
        |   |           |
        |   |       inner = 1 to 5 __Next___
        |   |           |                   |
        |   |           |   ^        Output "outer = "&outer&" inner is "&outer         
        |   |      Done |   |______________|
        |   |___________|
      End  


'''

from turtle import clear


for outer in range(1, 6):
    for inner in range (1, 6):
        print (outer, inner,end=",")  # 1 1,1 2,1 3,1 4,1 5,2 1,2 2,2 3,2 4,2 5,3 1,3 2,3 3,3 4,3 5,4 1,4 2,4 3,4 4,4 5,5 1,5 2,5 3,5 4,5 5,






# lesson 66 Display pattern numbers **************************

for i in range(1,10):
    for j in range(1, i+1):
        print(j, end = " ")
    print()  # 1 2 
            # 1 2 3 
            # 1 2 3 4 
            # 1 2 3 4 5 
            # 1 2 3 4 5 6 
            # 1 2 3 4 5 6 7 
            # 1 2 3 4 5 6 7 8 
            # 1 2 3 4 5 6 7 8 9 







# Display inverted pattern of numbers  ***************************

for i in range(1, 7):
    print(" " * (7 - (8 - i)))
    for j in range(1, 8-i):
        print(j, end = " ")
    print() # 1 2 3 4 5 6 
        
           # 1 2 3 4 5 
        
           # 1 2 3 4 
        
           # 1 2 3 
            
           # 1 2 
            
           # 1

for i in range(1, 7):
    print(" " * (7 - (8 - i)), end = '')
    for j in range(1, 8-i):
        print(j, end = " ")
    print() # 1 2 3 4 5 6
             # 1 2 3 4 5
              # 1 2 3 4
               # 1 2 3
                # 1 2
                 # 1

for i in range(1, 7):
    print(" " * (7 - (8 - i)), end = '')
    for j in range(1, 8-i):
        print(j, end = "")  # removed this space (" ")
    print()  # 123456
             # 12345
             # 1234
             # 123
             # 12
             # 1
