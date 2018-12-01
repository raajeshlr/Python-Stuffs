

names_file = open("names.txt","w+")
body_file = open("body.txt","w+")

names_file.write("raajesh \n swati \n sowmya \n nikila ")
body_file.write("This project is about to close")

namesinfile = names_file.read()
print(namesinfile)
bodyinfile = body_file.read()
print(bodyinfile)
namesinfile = names_file.seek(0,0)
namesinfile = names_file.read()
bodyinfile = body_file.seek(0,0)
bodyinfile = body_file.read()
print(namesinfile)
print(bodyinfile)
