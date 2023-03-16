def hello():
    print("hello world")
def add_numbers():
    print(5+5)
def sub_numbers():
    print(10-5)
def name(first,last):
    print(first," ",last)
def spam(x,y):
    while x>0:
        print(y,end=" ")
        x-=1
def sum(list):
    total=0
    for I in list:
        total+=I
    print(total)
def tim(lister):
    result=1
    for z in lister:
        result*=z
    print(result)
def charge():   
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
    sum(lists)
    lis=[1,2,3,4,5]
    tim(lis)
charge()