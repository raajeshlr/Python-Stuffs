import re

line = "2004-959-5959  This is ab  phone number ab fsafsf"

output = re.sub(r'ab.*',"",line)
print(output)