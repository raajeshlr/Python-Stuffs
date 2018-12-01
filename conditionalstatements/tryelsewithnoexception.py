try:
    filename = open("machinelearning.txt","r+")
    textinfile = filename.read()
    print(textinfile)
except IOError:
    print("file not available")
else:
    print("content written")


