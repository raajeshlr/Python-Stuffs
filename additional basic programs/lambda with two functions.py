def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

functions = [multiply,add]
for i in range(5):
    #value = list(map(lambda x : x(i) , multiply()))
    value = map(multiply(i),i)
    print(value)
