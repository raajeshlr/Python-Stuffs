mylist = [12,13,26,33,39]
result = list(filter(lambda x : (x%13 == 0) ,mylist))

print("numbers divisible by 13",result)