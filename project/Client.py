import socket
so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=5000
so.connect(('127.0.0.1',port))
while True:
    print("\n Welcome to the game, Hangman!")
    print("-"*50)
    print("Select One Option")
    print("1.New User ")
    print("2.Existing User \n")
    opition = input()
    so.sendall(opition.encode())
    while True:
        if(opition == "1"):
            userName = input("Enter your Name: ")
            so.send(userName.encode())

        elif(opition == "2"):
            existingName = input("Enter Your Username : ")
            so.send(existingName.encode())
        else:
            print("Enter Valid Input.")
            continue
        Status = so.recv(1024).decode()

        if Status == "start":
            print(so.recv(1024).decode())
            # print("-"*50)
            while True:
                msg = so.recv(1024).decode() #SecretWord count
                if msg == "you won":
                    print(msg,end='')
                    so.close()
                    break
                elif msg[-1] == "1": #input from user
                    print("entered")
                    print(msg[:-1], end='')
                    so.sendall(input().encode())
                else:
                    print(msg,end = '')
