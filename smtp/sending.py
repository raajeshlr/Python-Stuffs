import smtplib

content = "hi raajesh"

mail = smtplib.SMTP('smtp.office365.com',587)

mail.ehlo()
mail.starttls()
mail.login('raajesh.laguduvarameshbabu@openreach.co.uk','DadMom@123')
mail.sendmail('raajesh.laguduvarameshbabu@openreach.co.uk','raajeshlr2@gmail.com',content)
mail.close()