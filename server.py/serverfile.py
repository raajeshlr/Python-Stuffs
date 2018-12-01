import socket

s = socket.socket()

host = socket.gethostname()
port = 5005
s.bind((host,port))


s.listen(10)

while True:
    c , addr = s.accept()
    print("got connection" , addr)
    data = "thanks"
    c.send(data.encode('utf-8'))
    c.close()