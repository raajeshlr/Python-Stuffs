def changeme (ownlist):
    print(ownlist)
    #ownlist.append([7,8,9])
    ownlist.sort()
    print(ownlist)
    return
ownlist = [78,68,98]
print(ownlist)
changeme(ownlist)
print(ownlist)

def namechanges(myname):
    print(myname)
    #myname = "suresh"
    myname = myname + "laguduva rameshbabu"
    print(myname)
    return
myname = input("enter ur name")
print(myname)
namechanges(myname)
print(myname)

def changeme(ownlist):
    print(ownlist)
    ownlist = [1,2,3,4] #am assigning new referenc to mylist so it wont reflect until i return ownlist and returned ownlist
    #must have some equal to name in calling function
    print(ownlist)
    return()
ownlist = [10,20,30,40]
print(ownlist)
changeme(ownlist)
print(ownlist)