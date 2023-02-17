import threading
from config import PORT, IP_ADD, MAX_NO_CLIENTS, FORMAT, DISCONNECT_MSG, HEADER, server

addr =  (
    IP_ADD,
    PORT,
)

print('socket created...')

class Server:
    # store the clients
    CLIENTS_CONNECTED = []

    def __init__(self) -> None:
        pass
    def bind_server_port(self): 
        #bind a socket with a port number 
        server.bind(addr)



    def handle_clients(self, conn, addr, sender_rank):
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
                # print(msg_len)
                msg = conn.recv(msg_len).decode(FORMAT)
                print(msg)

                # disconnection from the server 
                if msg == DISCONNECT_MSG:
                    # close the current connection 
                    conn.send(
                        bytes(f'disconnected client {addr}', FORMAT)
                    )

                    c_socket = self.CLIENTS_CONNECTED[int(sender_rank)]


                    promote_rank = sender_rank
                    self.CLIENTS_CONNECTED.pop(sender_rank) 

                    # disconnnect the client from the socket 

                    
                    # close the socket 
                    c_socket.close()
                    

                    # the current number of clients 
                    print(self.CLIENTS_CONNECTED)


                    # since indices are the ranks, 
                    conn.send(
                        bytes(f'Hey your new rank is {promote_rank}',FORMAT)
                    )



                    
                else:
                    conn.send(
                        bytes(f'Welcome your rank is {sender_rank }  ', FORMAT)
                    )
                    #send cmd 

                    print(f'[{addr}]: {msg}')
                    # recieve the target rank here 
                    reciver_rank = conn.recv(HEADER).decode(FORMAT)
                
                    #send to target client 
                    self.send_to_target_client(reciver_rank, sender_rank) 

                    print(f'[{addr}]: {msg}')
                    # recieve the target rank here 
                    reciver_rank = conn.recv(HEADER).decode(FORMAT)
                    # self.distribute_commnads_to_clients(reciver_rank, sender_rank)



        #close the connection 
        conn.close()



 

    def send_to_target_client(self, target, sender):
        '''
        send the message to target client 

        '''
        client_socket = self.CLIENTS_CONNECTED[int(target)]

        if int(sender) > int(target):
            # sender has a lower rank 


            client_socket.send(
                bytes(f'hey 😂 TARGET_RANK: {target} from SENDER_RANK: {sender} 🚀',FORMAT)
            )
            
        else:
            # reject the command -> printed on the server 
            print('REJECTED COMMAND')





    def start_server(self):
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
        while True:
            # continnous connection 
            c_socket, addr = server.accept()

            #set the client rank 
            client_rank = len(self.CLIENTS_CONNECTED)
            if client_rank == MAX_NO_CLIENTS:
                '''
                - This means the server is full: -> no thread created 

                '''
                c_socket.send('Server is full, try again later'.encode())
                
            else:
                '''
                Update the connected users 

                '''
                # update the list of conected users 
                self.CLIENTS_CONNECTED.append(c_socket)



                # create a thread
                client_thread = threading.Thread(target = self.handle_clients, args = (c_socket, addr, client_rank)) 
                
                #start the thread 
                client_thread.start()

                #print the active threads in this python process 
                print(f'[ACTIVE CONNECTIONS MADE] {threading.active_count()-1}')
                print(self.CLIENTS_CONNECTED)

#START_THE_SERVER 
sv = Server()

#bind 
sv.bind_server_port()

#start the server 
sv.start_server()

