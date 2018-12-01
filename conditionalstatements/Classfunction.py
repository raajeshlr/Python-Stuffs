class Animal:
    name = ""
    height = 0
    weight = 0
    sound = 0
    chuma = "am here"

    def __init__(self,name,height,weight,sound):
        self.name = name
        self.height = height
        self.weight = weight
        self.sound = sound

    def setname(self,name):
        self.name= name
    def getname(self,name):
        print(Animal.chuma)
        return self.name
    def setheight(self,height):
        self.height= height
    def getheight(self,height):
        return self.height
    def setweight(self,weight):
        self.weight= weight
    def getweight(self,weight):
        return self.weight
    def setsound(self,sound):
        self.sound= sound
    def getsound(self,sound):
        return self.sound
    def gettype(self):
        print("animal")
    def multiplesounds(self, howmany = None):
        if howmany is None:
            print(self.getsound(""))
        else:
            print(self.getsound("") * howmany)
    def chumma(self):
        print("check")
    def tostring(self):
        return "{} is {} cm tall and {} kilograms and say {}".format(self.name,self.height,self.weight,self.sound)

cat = Animal("whiskers",33,10,"meow")
print(cat.tostring())

class dog(Animal):
    ownername = ""

    def __init__(self,name,height,weight,sound,ownername): #super class constructor overwrite
        self.ownername=ownername
        super(dog,self).__init__(name,height,weight,sound)

    def setownername(self,ownername):
        self.ownername = ownername
    def getownername(self,ownername):
        return self.ownername
    def gettype(self):
        print("dog")

    def tostring(self):           #overwrite functions on our superclass
        return "{} is {} cm tall and {} kilograms and say {} and his owner name is {}".format(self.name, self.height, self.weight, self.sound,self.ownername)

    def multiplesounds(self, howmany = None):
        if howmany is None:
            print(self.getsound(""))
        else:
            print(self.getsound("") * howmany)


german = dog("sport",53,20,"ruff","mohan")
print(german.tostring())
print(german.getownername("raaj"))
print(german.multiplesounds(5))
print(cat.multiplesounds(5))
print(cat.chumma())
cat.getname("f")
class Animaltesting():
    def gettype(self,Animal): #its receiving animal objects
        Animal.gettype() #going to refer animal gettype


testanimal = Animaltesting()

testanimal.gettype(cat)
testanimal.gettype(german)

