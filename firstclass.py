# naming format T=ticket S=staff 
# all the functions with get are for getting the variable named after get
# all the functions with set are for changing the variable named after set

class Ticket:  # this is the class for making and changing the tickets infomation
    Tnum=2000  # this is the static counter that is the same across all tickets created
    TID=0  # this is to store the static counter at each ticket so that there IDs can be found
    Tcreated=0  # counter for tickets created
    Topen=0  # counter for tickets open/unresolved
    Tresolved=0  # counter for tickets resolved
    Tresponse="Not Yet Provided"  # this makes it that all tickets that are made will default as not yet provided
    Tstatus="Open"  # like the one above but defaults them to open
    Tlist=[]  # this is to store the tickets so we can call upon older tickets later

    def __init__(self,SID,Tcreator,Email,desc):  # used to store the base details needed
        Ticket.Tnum+=1
        self.TID=Ticket.Tnum
        Ticket.Tcreated+=1
        Ticket.Topen+=1
        self.SID=SID
        self.Tcreator=Tcreator
        self.Email=Email
        self.desc=desc
        Ticket.Tlist.append(self)  # this will make all tickets be stored in Tlist
        self.changePassword()  # this will make it always check if it is a password change problem 

    def getSID(self):  # infomation at line 2
        return self.SID
    
    def setSID(self,SID):  # infomation at line 3
        self.SID=SID

    def getTcreator(self):  # infomation at line 2
        return self.Tcreator
    
    def setTcreator(self,Tcreator):  # infomation at line 3
        self.Tcreator=Tcreator 

    def getEmail(self):  # infomation at line 2
        return self.Email
    
    def setEmail(self,Email):  # infomation at line 3
        self.Email=Email

    def getdesc(self):  # infomation at line 2
        return self.desc
    
    def setdesc(self,desc):  # infomation at line 3
        self.desc=desc 

    def getTresponse(self):  # infomation at line 2
        return self.Tresponse
    
    def setTresponse(self,Tresponse):  # this will change the response and if the ticket isn't already closed it will close it
        self.Tresponse=Tresponse
        if self.Tstatus.lower()!="closed":
            self.resolve()

    def getTstatus(self):  # infomation at line 2
        return self.Tstatus
    
    def setTstatus(self,Tstatus):  # this will change the status to Tstatus and will plus or minus Topen and Tresolved depending on Tstatus
        self.Tstatus=Tstatus
        if self.Tstatus.lower()=="closed":
            Ticket.Topen-=1
            Ticket.Tresolved+=1
        elif self.Tstatus.lower()=="reopened":
            Ticket.Topen+=1
            Ticket.Tresolved-=1
        else:  # this should never be reached and if it is something is very wrong
            print("something very wrong is happening here")

    def changePassword(self):  # will check if the desc is password change and if is will make a new password
        if self.desc.lower()=="password change" or self.desc.lower()=="change password":
            password="New password generated: "+self.SID[0:2]+self.Tcreator[0:3]  # makes a new password out of there id and name
            self.setTresponse(password)

    def resolve(self):  # it closes the ticket
        self.setTstatus("Closed")

    def reopen(self):  # it reopens the ticket
        self.setTstatus("Reopened")

    def TStats():  # the stats of all tickets also formated for display
        stats=f"Tickets Created: {Ticket.Tcreated}\n"
        stats+=f"Tickets Resolved: {Ticket.Tresolved}\n"
        stats+=f"Tickets To Solve: {Ticket.Topen}"
        return stats
    
    def Tinfo(self):  # gets all the present ticket stats and formats it for display
        info=f"Ticket Number: {self.TID}\n"
        info+=f"Ticket Creator: {self.getTcreator()}\n"
        info+=f"Staff ID: {self.getSID()}\n"
        info+=f"Email Address: {self.getEmail()}\n"
        info+=f"Description: {self.getdesc()}\n"
        info+=f"Response: {self.getTresponse()}\n"
        info+=f"Ticket Status: {self.getTstatus()}"
        return info
    
    def AllTinfo():  # will use Tinfo but on all tickets one by one
        ATI=""
        for ticket in range(len(Ticket.Tlist)):
            ATI += f"{Ticket.Tlist[ticket].Tinfo()}\n\n\n"
        return ATI
    
    def Allinfo():  # will use AllTinfo and Tstats to get all tickets and stats
        everything=f"Displaying Ticket Statistics \n{Ticket.TStats()}\n\n"
        everything+=f"Printing Tickets \n{Ticket.AllTinfo()}\n\n"
        return everything

        

class Main:  # this is the class that is where everything is used

    def __init__(self):        
        command=0
        while command !=6:
            print("\n-----------------------------------------------------------------------------------")
            print("1:create a ticket")
            print("2:interact with a specific ticket")
            print("3:show all tickets")
            print("4:show all stats")
            print("5:show all infomation")
            print("6:end program")
            command=int(input("your command\n"))
            if command==1:      
                ID=input("your ID")
                name=input("your name")
                email=input("your email")
                problem=input("your problem")
                TT=Ticket(ID,name,email,problem)  # used to make tickets with the inputs
            elif command==2:
                Tcommand=0
                while Tcommand!=6:
                    Tcommand=0
                    TID=int(input("The ticket's ID"))-2001  # I minus 2001 because that will be the index of the ticket in the list
                    if TID>=0 and TID<len(Ticket.Tlist):  # confirms that they put a vaild ticket ID
                        while Tcommand !=5 and Tcommand !=6:  # this one has !=5 in it so that they can change the ticket ID if they want
                            print("\n-----------------------------------------------------------------------------------")
                            print("1:see ticket infomation")
                            print("2:respond to ticket")
                            print("3:close ticket")
                            print("4:reopen ticket")
                            print("5:change ticket")
                            print("6:exit ticket menu")
                            Tcommand=int(input("your command\n"))
                            if Tcommand==1:
                                print(Ticket.Tlist[TID].Tinfo())
                            elif Tcommand==2:
                                respond=input("The response")
                                Ticket.Tlist[TID].setTresponse(respond)
                                print("response updated")
                            elif Tcommand==3:
                                if Ticket.Tlist[TID].getTstatus().lower()!="closed":  # this is so that if it is already closed it won't close it again and mess with the static counters
                                    Ticket.Tlist[TID].resolve()
                                print("ticket closed")
                            elif Tcommand==4:
                                if Ticket.Tlist[TID].getTstatus().lower()!="reopened":  # this is so that if it is already reopened it won't close it again and mess with the static counters
                                    Ticket.Tlist[TID].reopen()
                                print("ticket reopened")
                            elif Tcommand==5:
                                print("changing ticket")
                            elif Tcommand==6:
                                print("exiting ticket menu")
                            else:
                                print("put a vaild command number")
                    else:
                        print("give an existing ticket ID please")
            elif command==3:
                print(Ticket.AllTinfo())
            elif command==4:
                print(Ticket.TStats())
            elif command==5:
                print(Ticket.Allinfo())
            elif command==6:
                print("thank you for using the ticket system farewell")
            else:
                print("put a vaild command number")



Main()  # so that class Main is used