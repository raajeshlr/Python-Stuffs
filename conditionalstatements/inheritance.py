class parent1:
    def __init__(self,id):
        print("our class is crated" ,id)
        self.id=id
class parent2:
    def __del__(self):
        print("our class is destroyed")

class parent3:
    def setfullname(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname

class child(parent2,parent3):
    def printfullname(self):
        print(self.firstname," ",self.lastname)

parent1ins = parent1(5)
parent2ins = parent2()
parent3ins = parent3()
childins = child()
prefix = input("enterfirstname")
suffix = input("enterlastaname")

childins.setfullname(prefix,suffix)
childins.printfullname()
childins.__del__()