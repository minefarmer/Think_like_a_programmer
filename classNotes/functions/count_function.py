'''         Count() Function
Write a function count() that can take a list and a number as arguments an return the count or frequency of that number in list (number of times that number appears in the list). Call the function count in the main program with differient argument values.







'''
# def Count(LIST, NUM):
    
#     c = 0
#     for i in LIST:
#         if NUM == i:
#             c += 1
#     return c


# print(Count([12, 43, 65, 54, 43, 43], 43))  # 3


def Count(LIST, NUM):
    
    c = 0
    for i in LIST:
        if NUM == i:
            c += 1
    LIST.append(100)        
    return c
LIST_1 = [12, 43, 65, 54, 43, 43]
print(LIST_1)  # [12, 43, 65, 54, 43, 43]
print(Count (LIST_1, 43))  # 3
print(LIST_1)  # [12, 43, 65, 54, 43, 43, 100]
