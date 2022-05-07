'''     Stack
A stack is a list of elements in whicn an element may be inserted or deleted only at one end
This means that elements are removed in reverse order of that in which they were inserted
It is also called LIFO (last-In_first_Out).  Because the last element that you insert in the stack is he one that can be removed first.

        Applications of the stack
Parsing
Recursive Function
Calling Function
Expression Evaluation
Expression conversion
Towers of hanoi

        Implementation of Stack
Implement Stack data structure in python. Restrict the user to enter only 5 elements in the stack. If user try to enter 6th element then show an error message "Stack is all ready full". If user try to remove element from empty stack then display a message "Sorry, stack is already empty". Display the following menu in the start of program.

    Hint: Use append() and pop() functions.

    Menu
1. Insert element in Stack
2. Remove element from stack
3. Display stack.
4. Exit


'''





stack = []

while True:
    print("1. Insert Element in a stack")
    print("2. Remove element from stack")
    print("3. Display elements in stack")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        if len(stack) ==5:
            print("Sorry, stack is already full")
        else:
            element = int(input("Please enter the element: "))
            stack.append(element)
            print(element, " inserted successfully")
    elif choice == 2:
        if len(stack) == 0:
            print("Sorry, stack is already empty")
        else:
            element = stack.pop()
            print(element, " was removed successfully")
    elif choice == 3:
        for i in range(len(stack)-1, -1, -1):
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
