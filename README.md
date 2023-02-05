# tcp-server (pesapal developer challenge)

## Problem 3: A distributed system.
Build a TCP server that can accept and hold a maximum of N clients (where N is configurable).
These clients are assigned ranks based on first-come-first-serve, i.e whoever connects first receives the next available high rank. Ranks are from 0–N, 0 being the highest rank.

Clients can send to the server commands that the server distributes among the clients. Only a client with a lower rank can execute a command of a higher rank client. Higher rank clients cannot execute commands by lower rank clients, so these commands are rejected. The command execution can be as simple as the client printing to console that command has been executed.

If a client disconnects the server should re-adjust the ranks and promote any client that needs to be promoted not to leave any gaps in the ranks.

## Thought Process 
Break the main problem statement into sub-problems as shown below:

## Sub Problem #1 

## 1. The program should accept and hold a maximum of N-Clients 
This means that we can only connect **N** clients to the server. If the server is full close we have to close the socket. 

## 2. Assign ranks based on first come first served basis 
This means the first client to connect to the server will have the **highest** rank which is **0(zero)** and the last client to connect to the server will have the **lowest** rank **N** .

#### Sub Problem #2


