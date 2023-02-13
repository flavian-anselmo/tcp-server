import socket 

PORT = 5050
IP_ADD =  'localhost'
MAX_NO_CLIENTS = 3 
FORMAT = 'utf-8'
HEADER = 64
DISCONNECT_MSG = 'd'
ADDR = (IP_ADD, PORT)





# create a server socket 
server = socket.socket(
    socket.AF_INET,   
    socket.SOCK_STREAM, 
)