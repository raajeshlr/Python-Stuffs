def print_func (par):
    print("hello :" , par)
    return

def fibonacci(n):
    if (n<=1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

nterms = int(input("enter the number ?"))

if (nterms <= 0):
    print("enter correct number")
else:
    print("here you go the fibonacci series are")
    for i in range(nterms):
        print(fibonacci(i))
