nterms = int(input("enter the count"))

result = list(filter(lambda x : 2**x , range(nterms+1)))


for i in range(0,nterms+1):
    print("2 raised to the power {} is {}".format(i,result[i]))

