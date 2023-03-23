class Ticket:
    def __init__(self,staffID,Tname,contact,desc):
        self.staffID=staffID
        self.Tname=Tname
        self.contact=contact
        self.desc=desc
    def getstaffID(self):
        return self.staffID
    def setstaffid(self,staffID):
        self.staffID=staffID
    def getTname(self):
        return self.Tname
    def setTname(self,Tname):
        self.Tname=Tname   
    def getcontact(self):
        return self.contact
    def setcontact(self,contact):
        self.contact=contact
    def getdesc(self):
        return self.desc
    def setdesc(self,desc):
        self.desc=desc 

tkt=Ticket()