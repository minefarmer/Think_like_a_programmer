'''         Liner Search

In liner search, a key that you want to search is compared against each element in the list.

If the key is matched with any element of the list, then loop will stop and current index of list is shown.



    Pseudocode
1. Start
2. Initalize a list mylist
3. Set LOC = -1
4. Take a key from the user
    1. If key is equal to value at current index of mylist
        1. Set LOC = current index
        2. Break
        
'''
myList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

LOC = -1

key = int(input("Please enter the key that you want to search: "))

for i in range(10):   # or for i in range(len(myList))
    if key == myList[i]:
        LOC = i
        break

if LOC == -1:
    print("Sorry, no value was found")
else:Please enter the key that you want to search: 70
            # Value found at  6
            # carl@carlhptiny:~/Desktop/MatsHub/Think_like_a_programmer$ /usr/bin/python /home/carl/Desktop/MatsHub/Think_like_a_programmer/classNotes/data_structures/liner_search.py
            # Please enter the key that you want to search: 101
            # Sorry, no value was found
            #     print("Value found at ", LOC)  # 
    

