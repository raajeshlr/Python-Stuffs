"""num = int(input("enter the number"))
initial = 1
if num<=0:
    print("enter correct number")
else:
    for i in range(1,num+1):
        initial = initial*i
print(initial)"""

num = int(input("enter the number"))

def recursive(n):
    if(n<=1):
        return n
    else:
        return n * recursive(n-1)

print("output is" , recursive(num))