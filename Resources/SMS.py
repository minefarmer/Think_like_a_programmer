

while True:
    print('-' * 25)
    print("STUDENT MANAGEMENT SYSTEM")
    print('-' * 25)
    print("1. add a student\n2. delete a student\n3. Search a student \n4. Exit")

    option = int(input("Please enter the option: "))

    if option == 1:
        print("Student added Successfully")
    elif option == 2:
        print("Student deleted Successfully")
    elif option == 3:
        print("Student record was found Successfully")
    elif option == 4:
        break
    else:
        print("Invalid option")

    choice = input("do you want to continue(y/n)?")

    if choice == 'Y' or choice == 'y':
        continue
    else:
        break

print("Thank you. See you later")













































# while True:
#     print('-'*25)
#     print("STUDENT MANAGEMENT SYSTEM")
#     print('-'*25)
#     print("1. Add a Student")
#     print("2. Delete a Student")
#     print("3. Search a Student")
#     print("4. Exit/Quit")
#
#     option = int(input("Please enter your option: "))
#
#     if option == 1:
#         print("Student added successfully")
#     elif option == 2:
#         print("Student deleted successfully")
#     elif option == 3:
#         print("Student record was found successfully")
#     elif option == 4:
#         break
#     else:
#         print("Sorry, Invalid Option")
#
#     choice = input("Do you want to continue? (y/n)")
#     if choice == 'y' or choice == 'Y':
#         continue
#     else:
#         break
# print("Thank You. See you later")


