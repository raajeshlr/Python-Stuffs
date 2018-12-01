name = "raajesh\a"
print(name)
name = "raajesh\b"
print(name)
lastname = " l r"
print(name)
fullname = name + lastname
print(fullname)
multipliedname =  name * 2
print(multipliedname)
print(name[1])
print(name[0:3])
for num in name:
    if  (num == 'r'):
        print("there")

strings = ["raaajesh" , "laguduva" , "rameshbabu"]
suffix = 'esh'
myname = "raajesh"
for num in strings:
    print(num)
    print(num.upper(),num.lower(),num.__len__())
    print(num.capitalize())
    print(num.center(20,'z'))
    print(num.count("a",0,15))

    print(myname.endswith(suffix))

project = "british\ttelecommunication"
print(project.expandtabs(10))