
import pprint
studentRecord = {}  # empty dictionary
# define all variables to be used in program
id = ''
firstName = ''
secondName = ''
rollno = ''
cgpa = ''

while True:
    print('-' * 25)
    print("STUDENT MANAGEMENT SYSTEM")
    print('-' * 25)
    print("1. add a student\n2. delete a student\n3. Search a student"
          "\n4. update a student\n5. display all students\n6. Exit")

    option = int(input("Please enter the option: "))

    if option == 1: # add a new student
        while True:
            id = input("Please enter the ID of student: ")
            if id in studentRecord:
                print("Id already exist, please enter unique id")
                continue
            else:
                break

        while True:
            rollno = input("Please enter the roll no. of student: ")
            if rollno.isalnum():
                break
            else:
                print("Please enter alphanumeric roll number..")
        while True:
            firstName = input("Please enter the first name of student: ")
            secondName = input("Please enter the second name of student: ")
            if firstName.isalpha() and secondName.isalpha():
                break
            else:
                print("Please enter name in alphabetic without spaces")
        while True:
            try:
                cgpa = float(input("Enter cgpa of student: "))
                break
            except ValueError:
                print("Please enter integer or floating point numbers")

        studentRecord.update({id: {'name': firstName +" "+ secondName, 'rollno': rollno, 'cgpa': float(cgpa)}})
        print("Student record updated successfully")

    elif option == 2: # delete a student
        id = input("Please enter the id of student: ")
        result = studentRecord.get(id, -1)
        if result == -1:
            print("Sorry, student does not exist in database")
        else:
            del studentRecord[id]
            print("Student deleted successfully")
    elif option == 3:# searching a student
        id = input("Please enter the id of student: ")
        result = studentRecord.get(id, -1)
        if result == -1:
            print("Sorry, no student was found against id ", id)
        else:
            pprint.pprint(studentRecord[id])
    elif option == 4: # update a student
            id = input("Please enter the id of student: ")
            if studentRecord.get(id, -1) == -1:
                print("No Record was found against ", id)
            else:
                print("press 1 to update name")
                print("press 2 to update roll number")
                print("press 3 to update cgpa")

                choice = int(input("Your Choice: "))
                if choice == 1:
                    while True:
                        firstName = input("Please enter the first name of student: ")
                        secondName = input("Please enter the second name of student: ")
                        if firstName.isalpha() and secondName.isalpha():
                            studentRecord[id]['name'] = firstName + " "+secondName
                            pprint.pprint(studentRecord[id])
                            break
                        else:
                            print("Please enter name in alphabetic without spaces")
                elif choice == 2:
                    while True:
                        rollno = input("Please enter the roll no. of student: ")
                        if rollno.isalnum():
                            studentRecord[id]['rollno'] = rollno
                            print(studentRecord[id])
                            break
                        else:
                            print("Please enter name in alphabetic..")
                elif choice == 3:
                    while True:
                        try:
                            cgpa = float(input("Enter cgpa of student: "))
                            studentRecord[id]['cgpa'] = cgpa
                            break
                        except ValueError:
                            print("Please enter integer or floating point numbers")


    elif option == 5:
        print(pprint.pprint(studentRecord))
    elif option == 6:
        break
    else:
        print("Invalid option")

    choice = input("do you want to continue(y/n)?")

    if choice.lower() == 'y':
        continue
    else:
        break

print("Thank you. See you later")
