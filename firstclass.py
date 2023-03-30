class Ticket:
    TID=2000
    Tcreated=0
    Topen=0
    Tresolved=0
    Tresponse="Not Yet Provided"
    Tstatus="Open"
    TList=[]
    def __init__(self,SID,Tcreator,Email,desc):
        Ticket.TID+=1
        Ticket.Tcreated+=1
        Ticket.Topen+=1
        self.SID=SID
        self.Tcreator=Tcreator
        self.Email=Email
        self.desc=desc
        Ticket.Tlist.append(self)
    def getSID(self):
        return self.SID
    def setSID(self,SID):
        self.SID=SID
    def getTcreator(self):
        return self.Tcreator
    def setTcreator(self,Tcreator):
        self.Tcreator=Tcreator   
    def getEmail(self):
        return self.Email
    def setEmail(self,Email):
        self.Email=Email
    def getdesc(self):
        return self.desc
    def setdesc(self,desc):
        self.desc=desc 
    def getTresponse(self):
        return self.Tresponse
    def setTresponse(self,Tresponse):
        self.Tresponse=Tresponse
        self.setTstatus("Closed")
    def getTstatus(self):
        return self.Tstatus
    def setTstatus(self,Tstatus):
        self.Tstatus=Tstatus
        if self.Tstatus.lower()=="closed":
            Ticket.Topen-=1
            Ticket.Tresolved+=1
        elif self.Tstatus.lower()=="reopened":
            Ticket.Topen+=1
            Ticket.Tresolved-=1
        else:
            print("something very wrong is happening here")
    def changePassword(self):
        if self.desc.lower()=="password change":
            password="New password generated: "+self.SID[0:2]+self.Tcreator[0:3]
            self.setTresponse(password)
            self.setTstatus("Closed")
    def resolve(self):
        self.setTstatus("Closed")
    def reopen(self):
        self.setTstatus("Reopened")


tkt=Ticket()