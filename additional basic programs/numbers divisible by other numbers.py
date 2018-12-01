nterms = int(input("enter the total number of terms"))

for i in range(0,nterms+1):
    if (i<=1):
        print(i)
    else:
        for dividingnumber in range(2,i):
            if(i%dividingnumber==0):
                print(i,"is divisible by" ,dividingnumber)
                break
            else:
                if((dividingnumber+1) ==i):
                    print("this number is not divisible", i)
                else:
                    pass

