'''         Validate User Input
Write a program that can take the user ID (alphanumeric) and password (numeric with maximum 10 length) from user. If user provide credentials in the wrong format then re-prompt the user until user enters correct creditionals.


'''
while True:
    userID = input("Please enter userID: ")
    
    if userID.isalnum():
        break
    else:
        print("Please enter user ID in alha numeric format")


while True:
    password = input("Please enter password: ")

    if password.isdecimal() and len(password) <= 10:
        break
    else:
        print("Please enter the password in correct format")

            # Please enter userID: minefarmer
            # Please enter password: su356RM9
            # Please enter the password in correct format
            # Please enter password: 357905605
