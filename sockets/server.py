import socket

s = socket.socket()

host = socket.gethostname()
port = 12003
s.bind((host,port))


s.listen(10)

while True:
    c , addr = s.accept()
    print("got connection" , addr)
    c.send('thank you for connecting')
    c.close()