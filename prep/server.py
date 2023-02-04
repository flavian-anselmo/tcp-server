import socket

PORT = 9998
IP_ADD = 'localhost'
N = 3 

sk = socket.socket(
    socket.AF_INET,   
    socket.SOCK_STREAM, 
)

print('socket created...')


# bid a socket with a port number 
sk.bind(
    (
        IP_ADD,
        PORT,
    )
)


#listen to a client 
sk.listen(
    N
)
print('waiting for connections...')


while True:
    # continnous connection 
    c_socket, addr = sk.accept()
    name = c_socket.recv(1024).decode()
    print('connected with', addr, name)
    
    c_socket.send(
        bytes(f'welcome', 'utf-8')
    )
    c_socket.close()

