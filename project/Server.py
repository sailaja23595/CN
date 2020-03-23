# first of all import the socket library 
import socket		

users = {}
game_started = False

def handle_request(from_client):
   global users
   global game_started
   print("from client :"+from_client)
   resp = "not a valid input \n\nMenu : \n1. login \n2. register \n3.close \nEnter a value (1/2/3) :"
   if(from_client=="1"):
      resp = "enter login username"
      #if from_client in users:
      #   resp =  "Welcome to Game"
   else if(from_client=="2"):
      resp = "enter register username"
   else if(from_client.find("register") != -1):
      user = from_client.split()
      user = user[1]  
      if user in users:
         resp =  "user already exists \n\nMenu : \n1. login \n2. register \n3.close \nEnter a value (1/2/3) :"
      else:
         users[user] = 0
         print(users)
         resp =  "user Added successfully \n\nMenu : \n1. login \n2. register \n3.close \nEnter a value (1/2/3) :"
   
   else if(from_client.find("login") != -1):
      user = from_client.split()
      user = user[1]    
      if user in users:
         game_started = True
         resp =  "\n ****Welcome to Game ******\n"
      else :
         resp =  "user does not exists \n\nMenu : \n1. login \n2. register \n3.close \nEnter a value (1/2/3) :"

   else if(game_started):
      resp =  "\n ****Welcome to Game ******\n"      

   return resp

# next create a socket object 
s = socket.socket()		 
print "Socket successfully created"

# reserve a port on your computer in our 
# case it is 12345 but it can be anything 
port = 12345				
s.bind(('', port))		 
print "socket binded to %s" %(port) 

# put the socket into listening mode 
s.listen(5)	 
print "socket is listening"			

while True: 
   c, addr = s.accept()	 
   print ('Got connection from', addr) 
   c.send("Menu : \n1. login \n2. register \n3.close \nEnter a value (1/2/3) :")
   while True:       
      from_client = c.recv(1024)
      if(from_client=="3"):
         break
      response = handle_request(from_client)
      c.send(response) 
   c.close() 


