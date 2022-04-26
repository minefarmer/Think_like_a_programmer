'''         Student management system
Write a program that can display the following menu to the user
1. Add student
2. Delete student
3. Search a student
4. Exit/Quit
The program should take the option from 1 to 4 from user if user enters the correct option then display the option. The ptogram should keep going until user presses option 4 (Exit/Quit)


        Main
          |
        Interger option
          |
        String choice
          |
        True _______________________________________________________________________________________
          |                                                                                         |
          |     ^                                                                               Output"1.add a student"
          |     |                                                                                   |
          |     |                                                                               Output"2.Delete a student"
          |     |                                                                                   |
          |     |                                                                               Output"3.Search a student"
          |     |                                                                                   |
          |     |                                                                               Output"exit/Quit
          |     |                                                                                   |
          |     |                                                                               Output"Enter your option "
          |     |                                                                                   |
          |     |                                                                                 Input option
          |     |                                                                                   |
          |     |                                                              _________False___option == 1__True_______
          |     |                                                              |                                        |
          |     |                                               _____False__option == 2 __true______              Output "StUdent added successfuly
          |     |                                               |                                   |                   |
          |     |                      ___________False_____output ==3___True____          Output "Student deleted      |
          |     |                      |                                         |              Successfully"           |
          |     |          ___False_option # 4_True__                      Output "Student Record   |                   |
          |     |          |                         |                      Found Successfully"     |                   |
          |     |     Output "Invalid Option"        | (add break command)       |                  |                   |
          |     |          |___________0_____________|                           |                  |                   |
          |     |                      |                                         |                  |                   |
          |     |                      |_____________________0___________________|                  |                   |
          |     |                                            |______________________0_______________|                   |
          |     |                                                                   |___________________0_______________|
          |     |                                                                                       |
          |     |                                                                                 Output "Do you want to continue (y/n)?"
          |     |                                                                                       |
          |     |                                                                                   Input choice
          |     |                                                                                       |
          |     |                                                                 _False__(choice = 'n' or choice = 'y'__True_
          |     |                                                                 |                                           |
          |     |                                                          add 'break' here                             add 'continue' here
          |     |                                                                 |_____________________0_____________________|
          |     |_______________________________________________________________________________________|
          |
Output "Thankyou, see you later"
          |
        Exit                         
          
'''


while True:
    print('-' * 25)
    print("STUDENT MANAGEMENT SYSTEM")
    print('-' * 25)
    print("1. add a student\n 2. delete a student\n 3. Search a student \n 4. Exit")
            # -------------------------
            # STUDENT MANAGEMENT SYSTEM
            # -------------------------
            # 1. add a student
            # 2. delete a student
            # 3. Search a student 
            # 4. Exit

    option = int(input("Please enter the option: "))
    
    if option == 1:
        print("Student added Successfully")
    elif option == 2:
        print("Student deleted Successfully")
    elif option == 3:
        print("Student record found successfully")
    elif option == 4:
        break
    else:
        print("Invalid option")
    
    choice = input("do you want to continue (y/n? ")
    
    if choice == 'Y' or choice == 'y':
        continue
    else:
        break
    
print("Thank you. See you later.")  # STUDENT MANAGEMENT SYSTEM
                                    # -------------------------
                                    # 1. add a student
                                    # 2. delete a student
                                    # 3. Search a student 
                                    # 4. Exit
                                    # Please enter the option: 1
                                    # Student added Successfully
                                    # do you want to continue (y/n? y
                                    # -------------------------
                                    # STUDENT MANAGEMENT SYSTEM
                                    # -------------------------
                                    # 1. add a student
                                    # 2. delete a student
                                    # 3. Search a student 
                                    # 4. Exit
                                    # Please enter the option: 4
                                    # Thank you. See you later.
            