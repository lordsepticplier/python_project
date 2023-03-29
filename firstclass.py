class Ticket:
    TID=2000
    Tresponse="Not Yet Provided"
    Tstatus="Open"
    TList=[]
    def __init__(self,SID,Tcreator,Email,desc):
        Ticket.TID+=1
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
    def getTstatus(self):
        return self.Tstatus
    def setTstatus(self,Tstatus):
        #CODE THE IF STATEMENT HERE PLEASE
        self.Tstatus=Tstatus
    def changePassword(self):
        if self.desc.lower()=="password change":
            password="New password generated: "+self.SID[0:2]+self.Tcreator[0:3]
            self.setTresponse(password)
            self.setTstatus("Closed")
tkt=Ticket()