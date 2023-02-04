import socket 

c = socket.socket()

#conect to a server 
c.connect(
    ('localhost', 9998)
)

name = input('Enter name: ')

#send data to the server 
c.send(bytes(name, 'utf-8'))

# recieve data from the server 
r = c.recv(1024).decode()
print(r)