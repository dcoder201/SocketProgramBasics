# SocketProgramBasics
Simple-Server-client-model-Socket

socket Programming
-----------------------------------

Socket programming is a way of connecting two nodes on a network to communicate with each other. 
One socket(node) listens on a particular port at an IP, while the other socket reaches out to the other to form a connection.
The server forms the listener socket while the client reaches out to the server. 


Setting up a server
-----------------------------------
1. import socket module

2. create an object to access socket method functionalities

3. Bind server with an IP address and a port number (It's better to try with 2 or more different machines on same network)

4. Set buffer limit for listeners

5. Now it's ready to process client data and to send messages to client.





Setting up a client 
-----------------------------------
1. import socket module

2. create an object to access socket method functionalities

3. connect client with an IP address of server and a port number 

4. Now client can send or recieve messages to and from server.

