
"""num=34
while(num>=1):
    print(num%2 ,end=' ')
    num = num//2"""

def conversion(n):
    if n>1:
        conversion(n//2)
    print(n%2 , end='')

dec = 34

conversion(dec)


