import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 3000))

s.send(bytes("DATA", "utf-8"))

data = s.recv(10000)

s.close()

print (str(data , "utf-8"))