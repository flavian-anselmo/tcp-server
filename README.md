# tcp-server (pesapal developer challenge) 🚀

## Problem 3: A distributed system. 📌
Build a TCP server that can accept and hold a maximum of N clients (where N is configurable).
These clients are assigned ranks based on first-come-first-serve, i.e whoever connects first receives the next available high rank. Ranks are from 0–N, 0 being the highest rank.

Clients can send to the server commands that the server distributes among the clients. Only a client with a lower rank can execute a command of a higher rank client. Higher rank clients cannot execute commands by lower rank clients, so these commands are rejected. The command execution can be as simple as the client printing to console that command has been executed.

If a client disconnects the server should re-adjust the ranks and promote any client that needs to be promoted not to leave any gaps in the ranks.

## Thought Process 🤹
I was able to identify 3 sub problems in the problem statement as shown below. I did this to be able to understand the problem more and also solve the problem a sub problem at a time. This will also help the person viewing the problem to see my commits and at every subproblem solved. 

- Build a TCP server that can accept and hold a **maximum of N clients** (where N is **configurable**) These clients are assigned ranks based on **first-come-first-serve**, i.e whoever connects first receives the next available high rank. Ranks are from 0–N, 0 being the highest rank.


- Clients can **send to the server commands** that the server **distributes among the clients**. Only a client with a **lower rank can execute a command** of a higher rank client. **Higher rank clients cannot execute commands** by lower rank clients, so these commands are rejected. The command execution can be as simple as the client printing to console that command has been executed.

- If a client disconnects the server should **re-adjust the ranks and promote any client** that needs to be promoted **not to leave any gaps in the ranks**.



## Sub Problem #1 ✅
In this first sub problem #1, I was able to disect it into 2 subproblems as listed and explained below:

**1. The program should accept and hold a maximum of N-Clients**
    
This means that we can only have  **N** clients to the server. If the server is full, we have to close the socket and reject all the incoming connection. 

**2. Assign ranks based on first come first served basis**

This means the first client to connect to the server will have the **highest** rank which is **0(zero)** and the last client to connect to the server will have the **lowest** rank **N**. This will depend on the datastructure used to store the clients who are connected to the server. For my first solution iam using a list datastructure where the ranks will be the indices. 

Therefore the client with the highest rank will be stored at the index zero and the client with the lowest rank will have an index N 

## Sub Problem #2 ✅
In this second sub problem #2, I was able to disect it into other 5 subproblems as listed below:

**1. Allow Clients To Send Commands**

Allow clients that are connected to send commands to the server. 

**2. Distribute The Commands Amoung Clinets** 

For this one I first enabled all the clients to be able to communicate since thats the simplest problem I was able to solve  first. 

**3. Lower Rank**

For this one, since the server was now able to distribute these commands, I was now able to enable Clients with a lower rank  execute commands from  higher ranked clients. 

**4. Higher Rank** 

Any commands trying to reach clients with high rank were rejected by simply printing on console 'REJECTED COMMAND' 

**5. Command Execution**

For the command execution I was able to state from which client the command was coming from using the ranks since they can be used to identify the clients stored in the list. 



## Sub Problem #3 (Rank Promotion) ✅ 

In the solution to the problem where a list data structure is used, clients are assigned ranks based on their index positions in the list. The promotion of clients is automatically handled when a client is disconnected, as the highest rank starts from 0 and the lowest rank is N. Therefore, if a client at index 0 is disconnected, the client at index 1 takes its place, effectively promoting the client to a higher rank.