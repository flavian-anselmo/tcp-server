#create a socket 
import socket

IP_ADD_CLIENT =  'localhost'

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
