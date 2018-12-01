class person:
    def __init__(self,id):
        print("our class is crated" ,id)
        self.id=id
    def __del__(self):
        classname = person.__name__
        myclassname = self.__class__.__name__
        print("our class is destroyed",classname,myclassname)
    def setfullname(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def printfullname(self):
        print(self.firstname," ",self.lastname)

personname = person(5)

prefix = input("enterfirstname")
suffix = input("enterlastaname")

personname.setfullname(prefix,suffix)
personname.printfullname()

personname.setfullname(prefix,suffix)
personname.printfullname()
personname.__del__()

personname.setfullname(prefix,suffix)
personname.printfullname()
personname.setfullname(prefix,suffix)
personname.printfullname()