import socket 

HEADER = 64 
PORT = 5050
FORMAT = 'utf-8'
DISCONECT_MSG = 'd'
IP_ADD =  '192.168.8.6'
ADDR = (IP_ADD, PORT)

#create a socket 
client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

#make the connection 
client.connect((IP_ADD, PORT))


def send(msg):
    '''
    send a message to the server 

    '''
    #en code the message 
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    
    #padding 
    send_len += b' ' * (HEADER - len(send_len))
    
    client.send(send_len)
    client.send(message)
def recieve_msg_from_server():
    '''
    recieve mmsg from the server 

    '''
    r_msg = client.recv(HEADER).decode()
    return r_msg

send(DISCONECT_MSG)

r = recieve_msg_from_server()
print(r)











