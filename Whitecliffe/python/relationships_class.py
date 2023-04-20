class Address:  # class that stores their address

    def __init__(self,street,city,state,postalcode,country):  # creates all of the storage boxes for the address
        self.street=street
        self.city=city
        self.state=state
        self.postalcode=postalcode
        self.country=country
    def validate():  # returns true
        return True
    
    def outputAsLabel(self):  # formats the address and returns it
        label=self.street
        label+=self.city
        label+=self.postalcode
        label+=self.country
        return label

    


class Person:  # class that stores the person infomation
    
    def __init__(self,name,phonenum,email,address):  # creates all the storage boxes for person
        self.name=name
        self.phonenum=phonenum
        self.email=email
        self.address=address

    def PPP():
        pass

class Student(Person):  # this class has inhereted class person so it has all of persons functions and varables

    def __init__(self,studentnum,avmark):  # creates all storage boxes for student
        self.studentnum=studentnum
        self.avmark=avmark
    
    def isEligibleToEnroll(able):  # return true
        return True
    
    def getSeminarsTaken():  # returns 10
        return 10



class Professor(Person):  # this class has inhereted class person so it has all of persons functions and varables

    def __init__(self,salary,staffnum,yearsofserv,numofclass):  # creates all storage boxes for professor
        self.salary=salary
        self.staffnum=staffnum
        self.yearsofserv=yearsofserv
        self.numofclass=numofclass