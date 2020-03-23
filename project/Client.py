import socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=5007
soc.connect(('127.0.0.1',port))
while True:
    print("\n Welcome to the game, Hangman!")
    print("-"*50)
    print("Select One Option")
    print("1.New User ")
    print("2.Existing User \n")
    opition = input()
    soc.sendall(opition.encode())
    while True:
        if(opition == "1"):
            userName = input("Enter your Name: ")
            soc.send(userName.encode())

        elif(opition == "2"):
            existingName = input("Enter Your Username : ")
            soc.send(existingName.encode())
        else:
            print("Enter Valid Input.")
            continue
        Status = soc.recv(1024).decode()

        if Status == "start":
            print(soc.recv(1024).decode())
            
            while True:
                message = soc.recv(1024).decode() 
                if message == "you won":
                    print(message,end='')
                    soc.close()
                    break
                elif message[-1] == "1": 
                    print("entered")
                    print(message[:-1], end='')
                    soc.sendall(input().encode())
                else:
                    print(message,end = '')
