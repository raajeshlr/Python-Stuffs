name = "raajesh"
cut = name[0:-4]
print(cut)
nexthalf = name[3:7]
print(nexthalf)
cat = name[:3]
print(cat)

from operator import itemgetter,attrgetter

items = ['cheese','bread','milk']
print(items)
items.append('onemoreitem')
print(items)
items.insert(1,"inbetween")
print(items)
#items.sort()
#print(items)
newlist = sorted(items,key= itemgetter(2))
print(newlist)
newlist1 = sorted(items,key=lambda x: x)
print(newlist1)


"""

values = [("raajesh",24,10),("latha",28,5),("asubiksha",2,0)]
newvalues = sorted(values,key = itemgetter(1))
print(newvalues)
newvalues = sorted(values, key=lambda r:r)
print(newvalues)"""


