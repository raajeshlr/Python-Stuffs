names_file = open("names.txt","r+")
body_file = open("body.txt","r+")

namesinfile = names_file.read()
bodyinfile = body_file.read()
#print(namesinfile)
#print(bodyinfile)

for name in namesinfile:
    mail = "hello" + name +bodyinfile
    mail_file = open("suresh.txt",'w+')
    mail_file.write(mail)
    mailinfile = mail_file.read()

print(mailinfile)




