import socket 

#configs 
PORT = 5050
IP_ADD =  'localhost'
MAX_NO_CLIENTS = 3 
FORMAT = 'utf-8'
HEADER = 1024
DISCONNECT_MSG = 'd'
ADDR = (IP_ADD, PORT)
IP_ADD_CLIENT =  'localhost'


#create a socket 
client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)



# create a server socket 
server = socket.socket(
    socket.AF_INET,   
    socket.SOCK_STREAM, 
)