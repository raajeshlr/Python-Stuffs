"""supervillains = {'raajesh':'tcs','chellaram':'wipro','pandi':'athena','kishore':'zoho'}
print(supervillains)
print(supervillains['raajesh'])
del supervillains['kishore']
print(supervillains)
supervillains['pandi'] = 'zoho'
print(supervillains)
print(supervillains.get('raajesh'))
print(supervillains.keys())
print(supervillains.values())"""

"""
def main():
    choices = dict(raajesh = "tcs", balaji = "lnt" , venkata = "cg")
    print(choices["raajesh"])
main()

def main():
    words = "this is where i want to break"
    for char in words:
        if char=='b':
            print("reached")
            break
        else:
            print("try again")

main()


words = "there are many works in this sentence".split()
print(words[1])

info = [[r.upper(),r.lower(),len(r)] for r in words]
for data in info:
    print(data)


for r in words:
    info = [r.upper(),r.lower(),len(r)]
    print(info)
    for data in info:
        print(data)"""


d = {'one' : 1 , 'two' : 2 , 'three' : 3}
print(d)
print(type(d))

x = dict(four = 4 , five = 5 , six = 6 )
print(x)

"""d = dict(one = 1 , two = 2 ,three = 3 , **x)
print(d)

if 'four' in x:
    print("true")

for a,b in d.items():
    print(a,b)

print(d.get("one"))
print(d.get("seven","not found"))
print(d)
d.pop("six")
print(d)


a= 10
b = hex(a)
print(a)
print(b)
c=5
d=11//2
print(d)"""

print(len(d))
print(type(d))
print(str(d))
print(d.keys())
print(d.values())
print(d.items())
anotherd = d.copy()
print(anotherd)
list = ("raajesh","latha","subiksha")
dictionay = {"ram":1,"sam":2}
dictionay.clear()
dictionay = dictionay.fromkeys(list)

print(dictionay)
dictionay = dictionay.fromkeys(list,20)
print(dictionay)
print(dictionay.get("raajesh"))
print(dictionay.get("suresh","apdi onum ila"))


