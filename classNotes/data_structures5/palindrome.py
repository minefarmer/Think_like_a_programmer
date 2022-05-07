'''         Find a Palindrome
Write a program that can find whether a string is palidrome or not. A palindrome is something that reads the same forward as it does backwards.
Examples: Adinida, deified, Hagigah, murdrum, Nauruan, peeweep






'''
String = input("Enter a String: ")

String.lower

L = len(String)

flag = True

for i in range(L//2):
    if String[i] == String[(L-1) - i]:
        pass
    else:
        flag = False
        break


if flag:
    print(String, " is a palindrome")
else:
    print(String, " is a palindrome")
