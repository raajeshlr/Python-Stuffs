class father:
    def method(self):
        print("father method")

class mother(father):
    def method(self):
        print("mother method")

motherinstance = mother()
print(motherinstance.method())
"""class child(father,mother):
    #def method(self,father):
        #father.method()
    print("chuyma")

fatherinstance = father()
motherinstance = mother()
childinstance = child()
print(childinstance.method())
#print(childinstance.method(motherinstance))"""