from config import FORMAT, IP_ADD, PORT, HEADER, client


class Client:
    def __init__(self) -> None:
        pass
    
    def connect_to_server(self):
        #make the connection 
        client.connect((IP_ADD, PORT))


    def send(self, msg):
        '''
        send a message to the server 

        '''
        #encode the message 
        message = msg.encode(FORMAT)
        msg_len = len(message)
        send_len = str(msg_len).encode(FORMAT)
        
        #padding to make sure it follows the headers size in bytes 
        send_len += b' ' * (HEADER - len(send_len))
        
        client.send(send_len)
        client.send(message)

    def recieve_msg_from_server(self):
        '''
        recieve mmsg from the server 

        '''
        r_msg = client.recv(HEADER).decode()
        return r_msg


# client instance 
c_0 = Client()

c_0.connect_to_server()

c_0.send('hello')

c_0.recieve_msg_from_server()










