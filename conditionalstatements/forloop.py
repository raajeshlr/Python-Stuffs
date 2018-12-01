"""import sys
b = [1,2,3,4]
for num in b:
    print(num,' ', end = " ")

for x in range(0,10):
    print(x  ,end = "")

numlist = [[0,1,2],[10,20,30],[100,200,300]]

for x in range(0,3):
    for y in range(0,3):
        print(numlist[x][y] ,' ', end = "")"""

"""print("enter ur name")
name = sys.stdin.readline()
print(name[0:3])

longstring = "I'll catch you if you fall - The floor"
print(longstring[0:4])
print(longstring[:-5])
print("%s%s%s"%("raajesh","is working in","tcs"))

print("%s is my %s and i watched %d series" % ("sherlock holmes" ,"favorite",4))

longstring = "raajesh is working in tcs"
print(longstring.capitalize())
print(longstring.find("in"))
print(longstring.isalpha())
print(longstring.isalnum())
print(longstring.replace("tcs","Google"))
print(longstring.strip())
convertingtolist = longstring.split(" ")
print(convertingtolist)
print(convertingtolist[0:3])

numlist = [[0,1,2],[10,20,30],[100,200,300]]
fruits = ["banana","apple","orange"]
print(len(fruits))
print(range(len(fruits)))
for index in range(len(fruits)):
    print(fruits[index])"""

for num in range(10,20):
    for i in range(2,num):
        if num%i ==0:
            j=num/i
            print("%d equals to %d *%d" % (num ,j,i))
            break
        else:
            print("its odd number")
            break
