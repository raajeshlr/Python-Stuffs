number = int(input("enter number ?"))
if (number < 0):
    print("are u mad ? enter positive number pls")
else:
    sum = 0
    while(number>0):
        sum+=number
        number-=1
    print(sum)

