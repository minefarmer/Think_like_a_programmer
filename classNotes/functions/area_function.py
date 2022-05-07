'''         Area() function
write a program that inputs base and height of a triangle in main program and passes them to a function called area(b, h).
        b = base,  h = height.
The function finds the area of triangle and returns it to main program. The area should be displayed on the screen.
        Area = 1/2*base*height




'''
def area(b, h):
    return 1 / 2 * b * h

base = int(input("Enter base: "))
height = int(input("enter height: "))

print("area is", area(base, height))  # Enter base: 12
                                    # enter height: 5
                                    # area is 30.0
