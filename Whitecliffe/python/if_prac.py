col=input("put a letter of a chess board cord")
row=int(input("now put the number for the cord"))
if col == "a" or "c" or "e" or "g":  # this will make us know which numbers will be white and which will be black
    if row%2==0:
        print("the squre is white")
    else:
        print("the squre is black")
else:
    if row%2==0:
        print("the squre is black")
    else:
        print("the squre is white")


side1=int(input("put the first side"))
side2=int(input("put the second side"))
side3=int(input("put the last side"))
if side1==side2 and side2==side3:  # this is using the and so all statements need to be true
    print("equilateral triangle")
elif side1==side2 or side2==side3 or side1==side3:  # this is using the and so all statements need to be true
    print("isosceles triangle")
else:
    print("scalene triangle")