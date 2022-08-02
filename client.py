import socket as sc

# Object creation for socket functionality
con = sc.socket()

# connecting to server with port
con.connect(('localhost', 9999))

# prompting client to input name
client_name = input("Enter name: ")

# sending name of client as bytecode to server
con.send(bytes(client_name, 'utf-8'))

# Gathering processed data from server to client side
print(con.recv(1024).decode())

