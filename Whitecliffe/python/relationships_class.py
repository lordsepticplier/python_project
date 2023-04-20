class Address:

    def __init__(self,street,city,state,postalcode,country):
        self.street=street
        self.city=city
        self.state=state
        self.postalcode=postalcode
        self.country=country
    def validate():
        return True
    
    def outputAsLabel(self):
        label=self.street
        label+=self.city
        label+=self.postalcode
        label+=self.country
        return label

    


class Person:
    
    def __init__(self,name,phonenum,email,address):
        self.name=name
        self.phonenum=phonenum
        self.email=email
        self.address=address

    def PPP():
        pass

class Student(Person):

    def __init__(self,studentnum,avmark):
        self.studentnum=studentnum
        self.avmark=avmark
    
    def isEligibleToEnroll(able):
        return True
    
    def getSeminarsTaken():
        return 10



class Professor(Person):

    def __init__(self,salary,staffnum,yearsofserv,numofclass):
        self.salary=salary
        self.staffnum=staffnum
        self.yearsofserv=yearsofserv
        self.numofclass=numofclass