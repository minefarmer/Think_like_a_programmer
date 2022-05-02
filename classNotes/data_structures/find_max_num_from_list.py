'''     Find max number from list

>>> a = [10, 4, 76, 98, 43, 100]
>>> max(a)
100
>>> min(a)
4
>>> 

'''
import random
intList = []
for i in range(10):
    intList. append(random.randint(1, 100))
    
max = intList[0]

print(intList)  #[76, 30, 31, 60, 46, 30, 6, 36, 88, 72] 

for j in range(1, 10):
    if intList[j] > max:
        max = intList[j]
print("maximum value is ", max)  # maximum value is  88

# second run
# [39, 88, 95, 56, 21, 64, 41, 60, 22, 1]
# maximum value is  95
