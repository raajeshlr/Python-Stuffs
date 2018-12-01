"""def main():
    print(sorted([1,5,2,9,6]))
    print(sorted(['a','g','z','r']))
    items = ["bread","cheese","egg","agrapes"]
    output = items.sort()
    correctoutput = sorted(items)
    print(output)
    print(correctoutput)
    oneworditems = ["z","a","f"]
    outputoneword = sorted(oneworditems)
    print(outputoneword)
    a = [5,1,3]
    b = a.sort()
    print(b)
    c = sorted(a)
    print(c)
main()

mylist = {4:'d',1:'s',3:'t',5:'a'}
print(mylist)
x=sorted(mylist)
print(x)"""

from operator import itemgetter,attrgetter
books = [('book5','rs.100',1),('book2','rs.101',5),('book3','rs.99',2)]
output = sorted(books , key = itemgetter(2))
print(output)
"""output1 = sorted(books,key=lamda books: books[2])"""
output1=sorted(books ,key=itemgetter(2),reverse = True)
print(output1)


newbooks = {}