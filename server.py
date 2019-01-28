import socket
import datetime

now=datetime.datetime.now()
str(now)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('', 3000))

s.listen(5)

while True:
      c, a=s.accept()
      print ("connesione da" ,a)
      data=c.recv(10000)
      data = str(data, 'utf-8')
      print (data)
      if data == "DATA": 
         #d=now.year,"/",now.month,"/",now.day
         d = str(now)



         c.send(bytes(d, "utf-8"))
         c.close
      