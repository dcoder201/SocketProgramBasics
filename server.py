# importing socket module
import socket as sc

# creating an object for calling socket method
con = sc.socket()
print('Socket Created...')
# binding server connection with localhost and a random port number for connection
con.bind(('localhost', 9999))
print('Binding Completed...')
# setting buffer limit for connection
con.listen(4)
print('Ready to listen...')

# server response to incoming and outgoing messages
while True :
    # getting address of client
    c, addr = con.accept()
    # getting name of client from client side
    name = c.recv(1024).decode()
    # printing client name with port and socket details in server
    print('connected with ', addr, name)
    # sending connection confirmation message to client
    c.send(bytes('{} have successfully established the connection'.format(name), 'utf-8'))
    # closing the connection
    c.close()



