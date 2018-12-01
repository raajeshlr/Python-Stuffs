"""name = input("name?")
if name=="mark":
    print("name is",name)
elif name=="raajesh":
    print("name is",name)
else:
    print("get out")

name = input("name?")
if name=="raajesh":
    familyname = input("familyname?")
    if familyname == "laguduva":
        print("u are in family group")
    elif not familyname == "laguduva":
        print("you are not in family group")
else:
    print("you doesn belong here")

first = int(input("enterfirstnum:"))
second = int(input("entersecondnum:"))
third = int(input("enterthirdnum:"))
if first>second and first>third:
    print("first num is big")
elif second>third and second>third:
    print("second is big")
else:
    print("third is big")


string = input("enter")
if '___ ' in string:
    print("its there")
a = [1,2,3]
b = [1,2,3]
if a==b:
    print("equal")

a=1
s=0
while a!=0:
    print("current sum",s)
    a=float(input("number?"))

    s=s+a
print("total",s)

b=[1,2,3]

for num in b:
    print(num)

a=input("enter?")
for num in a:
    print(a)"""

"""for x in range (0,10):
    print (x,' ', end = '')"""

"""print("first line " , end="secondline")
print("second line")
print("i dont \" like to print it in the second lien" , end=" ")
print("thats why i used end keyword above")

print('\n' *5)"""

grocerylist = ['tomatoes','potatoes','bananas','juice']
print(grocerylist[0])
todolist = ['wash car','pick up kids','watch movie']
totallist = (grocerylist,todolist)
print(totallist)
grocerylist.append('onemoregrocery')
print(grocerylist)
grocerylist.remove('potatoes')
print(grocerylist)

print(totallist)
print((totallist[0][1]))
grocerylist.insert(1,"secondgrocery")
print(grocerylist)

grocerylist.sort()
grocerylist.reverse()
print(grocerylist)

playerslist = ['aasachintendulkar','sehwag','rahuldravid','anilkumble']
finallist = grocerylist + todolist + playerslist
print(len(finallist))
print(min(playerslist))
print(max(playerslist)) 


tuple = ('b','c','a','z','x')
print(tuple)
convertedtolist = list(tuple)
print(convertedtolist)

print(len(tuple))
print(min(tuple))
print(max(tuple))













