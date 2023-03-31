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
        self.changePassword()

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
        self.resolve()

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
            self.resolve()

    def resolve(self):
        self.setTstatus("Closed")

    def reopen(self):
        self.setTstatus("Reopened")

    def TStats():
        stats=f"Tickets Created: {Ticket.Tcreated}/n"
        stats+=f"Tickets Resolved: {Ticket.Tresolved}/n"
        stats+=f"Tickets To Solve: {Ticket.Topen}"
        return stats
    def Tinfo(self):
        info=f"Ticket Number: {Ticket.TID}/n"
        info+=f"Ticket Creator: {self.getTcreator()}/n"
        info+=f"Staff ID: {self.getSID()}/n"
        info+=f"Email Address: {self.getEmail()}/n"
        info+=f"Description: {self.getdesc()}/n"
        info+=f"Response: {self.getTresponse()}/n"
        info+=f"Ticket Status: {self.getTstatus()}"
        return info
    def AllTinfo():
        for ticket in Ticket.Tlist:
            ATI += f"{Ticket.Tlist[ticket].Tinfo()}/n/n/n"
        return ATI
    def Allinfo():
        everything=f"Displaying Ticket Statistics /n{Ticket.Tstats()}/n/n"
        everything+=f"Printing Tickets /n{Ticket.AllTinfo()}/n/n"
        return everything

        





tkt=Ticket()
#when using the tickets use the list and do list[desired ticket].desiredfunction