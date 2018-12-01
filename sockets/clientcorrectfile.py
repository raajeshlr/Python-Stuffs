import socket

host = socket.gethostname()
port = 6003

s=socket.socket()
s.connect((host,port))

message = input("->")
while message != 'q':
    s.send(message.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    print("received from server:" + data)
    message = input("->")
s.close()
