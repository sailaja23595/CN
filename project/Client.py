# Import socket module 
import socket			 

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 12345				

# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 
while(True):
    print(s.recv(1024))
    from_client = raw_input() 
    s.send(from_client)
    if(from_client=="3") :
        break     
s.close()	 
