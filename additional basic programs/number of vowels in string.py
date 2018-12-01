string = input("enter string")
vowels = ['a','e','i','o','u']
string = string.casefold()

count = 0
for char in string:
    if char in vowels:
        count = count + 1

print(count)