"""num = int(input("enter the number"))
sum = 0
for i in range(0,num+1):
    sum = sum + i

print(sum)"""

num = int(input("enter number"))

def recursive(n):
    if(n<=1):
        return n
    else:
        return n + recursive(n-1)

print("output is" , recursive(num))