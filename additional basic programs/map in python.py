"""items = [1,2,3,4,5]
squared = []
for x in items:
    squared.append(x**2)

print(squared)"""

squared = []
items = [2,3,4,5]
def sqr(x):
    values = x**2
    squared.append(values)
list(map(sqr,items))
print(squared)

