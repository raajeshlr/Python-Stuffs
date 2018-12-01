x = int(input("enter first number"))
y = int(input("enter second number"))


def computehcf(a,b):
    if(a<b):
        smaller = a
    else:
        smaller = b

    for i in range(1,smaller+1):
        if(a%i == 0) and (b%i == 0):
            hcf = i
    return hcf

print("the result is " , computehcf(x,y))