import socket
import threading

PORT = 5050
IP_ADD =  socket.gethostbyname(socket.gethostname())
MAX_NO_CLIENTS = 3 
FORMAT = 'utf-8'
HEADER = 64
DISCONNECT_MSG = 'd'

server = socket.socket(
    socket.AF_INET,   
    socket.SOCK_STREAM, 
)

addr =  (
    IP_ADD,
    PORT,
)

print('socket created...')


# bid a socket with a port number 
server.bind(addr)



def handle_clients(conn, addr, rank):
    '''
    - handle the cients :thread 
    - handle the inidvitual connection 
    - concurrently for each client 

    '''
    print(f'[NEW CONNCETION] {addr} connected')
    connected = True
    while connected:

        #recieve the message 
        msg_len = conn.recv(HEADER).decode(FORMAT)

        # if the message is not null 
        if msg_len:
            msg_len = int(msg_len)
            print(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            print(msg)

            # disconnection from the server 
            if msg == DISCONNECT_MSG:
                # close the current connection 
                conn.send(
                    bytes(f'diconnected client {addr}', FORMAT)
                )
                connected = False
            else:
                conn.send(
                    bytes(f'Welcome to the server your rank is {rank}', FORMAT)
                )
                print(f'[{addr}]: {msg}')
    #close the connection 
    conn.close()

def start_server():
    '''
    - start the tcp server 
    - create a thread in the python process 
    
    '''
    #listen to a client 
    server.listen(
        MAX_NO_CLIENTS
    )

    print(f'[LISTENING]--> server is listenng on {IP_ADD}')

    # clients connected 
    CLIENTS_CONNECTED = []
    while True:
        # continnous connection 
        c_socket, addr = server.accept()

        #set the client rank 
        client_rank = len(CLIENTS_CONNECTED)
        if client_rank == MAX_NO_CLIENTS:
            '''
            This means the server is full: -> no thread created 

            '''
            c_socket.send('Server is full, try again later'.encode())
        else:
            '''
            Update the connected users 

            '''
            # update the list of conected users 
            CLIENTS_CONNECTED.append(c_socket)



            # create a thread
            client_thread = threading.Thread(target = handle_clients, args = (c_socket, addr, client_rank)) 
            
            #start the thread 
            client_thread.start()

            #print the active threads in this python process 
            print(f'[ACTIVE CONNECTIONS] {threading.active_count()-1}')

#START_THE_SERVER 
start_server()