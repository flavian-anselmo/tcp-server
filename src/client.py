from config import FORMAT, IP_ADD_CLIENT, PORT, HEADER, client, DISCONNECT_MSG
import time


class Client:
    def __init__(self) -> None:
        pass
    
    def connect_to_server(self):
        #make the connection 
        client.connect((IP_ADD_CLIENT, PORT))


    def send(self, msg):
        '''
        send a message to the server 

        '''
        connected = True
        while connected:
            #encode the message 
            message = msg.encode(FORMAT)
            msg_len = len(message)
            send_len = str(msg_len).encode(FORMAT)

            
            
            #padding to make sure it follows the headers size in bytes 
            send_len += b' ' * (HEADER - len(send_len))
            
            client.send(send_len)
            client.send(message)

            '''
            create a cli 

            '''
            reciver_rank = input('Enter target-rank: ')

            if reciver_rank == DISCONNECT_MSG:
                break

          
            rank = reciver_rank.encode(FORMAT)
            client.send(rank)
            connected = False
            if connected == False:
                print('waiting for msg...')
                rcv = self.recieve_msg_from_server()
                print(rcv)
            connected = True
                
            

    def recieve_msg_from_server(self):
        '''
        - recieve mmsg from other clients 
        - these messages are distributed by the server 

        '''
        
        r_msg = client.recv(HEADER).decode()
        return r_msg


 


    
# client instance 
c_0 = Client()

#connect to server
c_0.connect_to_server()

#recieve data 
# rcv = c_0.recieve_msg_from_server()
# print(rcv)


#send 

message_intro = input('Say hello to Server-> type d to disconnect: ')
c_0.send(message_intro)











