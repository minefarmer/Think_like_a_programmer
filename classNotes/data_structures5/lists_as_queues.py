'''     Queues

A queue is a linear list of elements in which deletions can take place  only at one end, called the front.
Insertions in the Quwuw can only take place at the other end called rear.
Queues are also called FIFO (first in first out), since the first element in a queue will be the first element that can go out of tIn other words, the order in which elemente enter a qqueue, is the order in which they leave
dEFINATION TAKEN FROM: sCHAUM'S OUTLINES dATA sTRUCTURES BY sEYMOUR lIPSCHUTZ

    How to implement?
To implement a queue, use "collections.deque" which was designed to have fast appends and pops from both ends
from collections import deque
Use popleft() to remove element from front
Use append() to insert new element at the end.




'''
from collections import deque

queue = deque([10, 20, 30])

while True:
    print("1. Insert Element in the queue")
    print("2. Remove element from queue")
    print("3. Display elements in queue")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        if len(queue) == 5:
            print("Sorry, queue is already full")
        else:
            element = int(input("Please enter element: "))
            queue.append(element)
            print(element, " inserted successfully")
    elif choice == 2:
        if len(queue) == 0:
            print("Sorry, queue is already empty")
        else:
            element = queue.popleft()
            print(element, " was removed successfully")
    elif choice == 3:
        for i in queue:
            print(i, end = ' ')
        print()
    elif choice == 4:
        print("Thank You. See you later")
        break
    else:
        print("Invalid option")
        
    more = input("Do you want to continue?(y/n) : ")
            
    if more == 'Y' or more == 'y':
        continue
    else:
        print("Thank You. See you later")
        break



'''

1. Insert Element in the queue
2. Remove element from queue
3. Display elements in queue
4. Exit
Enter your choice: 3
10 20 30 
Do you want to continue?(y/n) : y
1. Insert Element in the queue
2. Remove element from queue
3. Display elements in queue
4. Exit
Enter your choice: 1
Please enter element: 40
40  inserted successfully
Do you want to continue?(y/n) : y
1. Insert Element in the queue
2. Remove element from queue
3. Display elements in queue
4. Exit
Enter your choice: 3
10 20 30 40 
Do you want to continue?(y/n) : y
1. Insert Element in the queue
2. Remove element from queue
3. Display elements in queue
4. Exit
Enter your choice: 2
10  was removed successfully
Do you want to continue?(y/n) : y
1. Insert Element in the queue
2. Remove element from queue
3. Display elements in queue
4. Exit
Enter your choice: 3
20 30 40 
Do you want to continue?(y/n) : n
Thank You. See you later

'''