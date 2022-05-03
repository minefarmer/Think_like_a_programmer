
stack = []

while True:
    print("1. Insert Element in the stack")
    print("2. Remove element from stack")
    print("3. Display elements in stack")
    print("4. Exit")

    choice = int(input("Enter your Choice: "))

    if choice == 1:
        if len(stack) == 5:
            print("Sorry, stack is already full")
        else:
            element = int(input("Please enter element: "))
            stack.append(element)
            print(element, " inserted successfully")
    elif choice == 2:
        if len(stack) == 0:
            print("Sorry, stack is already empty")
        else:
            element = stack.pop()
            print(element, " was removed successfully")
    elif choice == 3:
        for i in range(len(stack)- 1, -1, -1):
            print(stack[i])
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




