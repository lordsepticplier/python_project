def hello():  # used to print hello world
    print("hello world")
def add_numbers():  # used to print 5+5
    print(5+5)
def sub_numbers():  # used to print 10-5
    print(10-5)
def name(first,last):  # used to print the strings given in the paramaters with a space between them
    print(first," ",last)
def spam(x,y):  # used to print the string given for y, x amount of times
    while x>0:
        print(y,end=" ")
        x-=1
def sum(list):  # used to find the total result of all the numbers in a list being added together
    total=0
    for I in list:
        total+=I
    return total
def tim(lister):  # used to find the total result of all the numbers in a list being timed together
    result=1
    for z in lister:
        result*=z
    return result
def charge():  # used to activate all the other functions and get inputs   
    first=input("first name ")
    last=input("last name ")   
    num=int(input("number"))
    word=input("pain")
    hello()
    add_numbers()
    sub_numbers()
    name(first,last)
    spam(num,word)
    lists=[100,2,3,4,5]
    summary=sum(lists)
    lis=[1,2,3,4,5]
    times=tim(lis)
    print(summary,"and",times)
charge()