import os
testfile = open("raajesh.txt","w+")
print(testfile.name)
print(testfile.mode)
print(testfile.closed)

#print(testfile.write(bytes("write me to the file raajesh" , 'UTF-8'))) if you put wb+ mode
print(testfile.write("write me to the file raajesh"))
testfile.close()
print(testfile.name)
testfile = open("raajesh.txt","r+")
print(testfile)
textinfile = testfile.read(10) #put 10 here will move cursor to the 10th position
print(textinfile)
textinfile = testfile.read(5)
print(textinfile)
textinfile = testfile.seek(0,0)
textinfile = testfile.read(10)
print(textinfile)
position = testfile.tell()
print(position)
#os.rename("raajesh.txt","raajeshlr2.txt")
#print(testfile.name)

currentdir = os.getcwd()
print(currentdir)

def onefunction():
    print("its one function")
