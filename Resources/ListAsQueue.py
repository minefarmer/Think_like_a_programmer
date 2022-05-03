from collections import deque

queue = deque([10, 20, 30])

while True:
    print("1. Insert Element in the queue")
    print("2. Remove element from queue")
    print("3. Display elements in queue")
    print("4. Exit")

    choice = int(input("Enter your Choice: "))

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

    more = input("Do you want to continue?(y/n): ")

    if more == 'Y' or more == 'y':
        continue
    else:
        print("Thank You. See you later")
        break

