import socket
import sys
import time

#end of imports

#init

s=socket.socket()
host=socket.gethostname()
print("Server will start at host:",host)
port=8080
s.bind((host,port))
print("")
print("Server done binding to host and port successfully")
print("")
print("Server is waiting for incoming connections....")
print("")
s.listen(1)
conn, addr = s.accept()
print(addr, "Has connected to the server and is now online...")
print("")
while 1:
     message = input(str(">> "))
     message = message.encode()
     conn.send(message)
     print("message has been sent...")
     print("")
     incoming_message = conn.recv(1024)
     incoming_message = incoming_message.decode()
     print("Client:",incoming_message)
     print("")

     
