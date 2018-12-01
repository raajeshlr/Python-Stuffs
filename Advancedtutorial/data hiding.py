class father:
    __childname = "raajesh"

    def method(self):
        return self.__childname


fatherinstance = father()
print(fatherinstance.method())
print(fatherinstance.__father.__childname)
