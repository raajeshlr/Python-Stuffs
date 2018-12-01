"""givenum = int(input("enter the number"))
givennum = givenum
sum = 0
while (givenum>0):
    remainder = (givenum % 10)
    sum = (sum * 10) + remainder
    givenum = (givenum // 10)


if (sum == givennum):
    print(givennum,"is palindrome")
else:
    print(givennum,"its not palindrome")"""

string = input("enter string")
string = string.casefold()
reverestring = reversed(string)

if list(string) == list(reverestring):
    print("its palindrome")
else:
    print("its not")
