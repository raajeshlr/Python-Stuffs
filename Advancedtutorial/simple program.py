class Employee:
    empcount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empcount+=1

    def displaycount(self):
        print("total employee count is",Employee.empcount)

    def displayemployee(self):
        print("name is",self.name,"salary is",self.salary)

emp1 = Employee("kishore",50000)
emp2 = Employee("pandi",50000)

emp1.displaycount()
print(Employee.empcount)
print(emp1.empcount)
print(hasattr(emp1,'age'))
print(getattr(emp1,'salary'))
setattr(emp1,'age',25)
emp1.displayemployee()
print(getattr(emp1,'age'))



print(Employee.__dict__)
print(Employee.__class__)
print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)

print(id(emp1))







