import socket

s = socket.socket()
host = socket.gethostname()
port = 5005

s.connect((host,port))

output = s.recv(1024).decode('utf-8')
print(output)

s.close()