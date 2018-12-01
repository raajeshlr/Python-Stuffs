string = input("enter your string")

punctuation = "'''&#@'''"
output = ""

for char in string:
    if char not in punctuation:
        output = output + char

print(output)