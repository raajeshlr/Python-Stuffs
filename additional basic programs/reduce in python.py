from functools import reduce
nterms = int(input("enter the number of terms"))

for i in range(nterms):
    output = reduce((lambda x,y : x*y),range(1,nterms+1))
    print(output)
