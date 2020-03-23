import socket
import random
def getAvailableletter(LETTERGUESSED,TURN):
# Letter guessed: Lists what letters have been guessed until now.
# return: String comprised of letters that represents what letters have been guessed until now.
# TURN means calliing the turn which is in global into a function.
  global ALPHA
# global ALPHA means calling the alpha i.e.. alphabets list into the function.
  
  for i in LETTERGUESSED:
    if i in SECRETWORD:
    # If the letterguessed is in the secret word then remove the letter.
      conn.sendall("good guess.\n".encode())
      ALPHA.remove(i)
    else:
    # If letterguessed not in secretword then remove the letter.
      TURN=TURN-1
      ALPHA.remove(i)
      conn.sendall("wrong guess.\n".encode())
  return "".join(ALPHA),TURN

def getguessword(SECRETWORD,lettersGuessed):
  # Secret word: string,the word is user guessing.
  # Letterguessed:List what letters have been guessed so far.
  # Return: String comprised of letters and underscores that represents what letters in secretword have been guessed so far.
    s=SECRETWORD
    for d in SECRETWORD:
      if d not in lettersGuessed :
         s=s.replace(d," _")
    if s==SECRETWORD:
      conn.sendall("\n you won! ".encode())
      return
    else:
      return(s)
def isWordguessed(SECRETWORD,LETTERGUESSED,l):
  TURN = 8
  length = l
  
  lettersGuessed = []
  num=['1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')',' ?',' ','/']
  conn.sendall(f'\nI am thinking of a word contains letters is {l}\n'.encode())
  while TURN != 0:
    global alpha
    conn.sendall(f'\nYou have {str(TURN)} guesses left\n'.encode())
    G = conn.sendall('\nplease guess a letter:1'.encode())
    G = conn.recv(1024).decode()
    G= G.lower()
    if (G in  ALPHA) and len(G)==1 :
      LETTERGUESSED=[G]
      lettersGuessed = lettersGuessed+[G]
      let,TURN = getAvailableletter(LETTERGUESSED,TURN)
      conn.sendall(f'{let}\n'.encode())
      if getguessword(SECRETWORD,lettersGuessed):
        conn.sendall(f'{getguessword(SECRETWORD,lettersGuessed)}\n'.encode())
      else:
        break
    else:
      if len(G)>1:
        conn.sendall('only one letter\n'.encode())

      elif(G  in num):
        conn.sendall("Invalid input\n".encode())
      else:
        conn.sendall("Oops! letter already guessed\n".encode())


  else:
    conn.sendall("game over\n".encode())
    conn.sendall(f"secretWord is {SECRETWORD}".encode())

def hangman(SECRETWORD,LETTERGUESSED,l):
  isWordguessed(SECRETWORD,LETTERGUESSED,l)


players = {'Sailaja' : 100}
score = 0
lst = ""
LETTERGUESSED=[]
lettersGuessed=[]
# Importing a word randomly from words.txt into secretword.

SECRETWORD=random.choice(open('words.txt').read().split())

l=len(SECRETWORD)

ALPHA=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# Considering list of alphabets.
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error() as message:
    print('Socket creation failed!')

while True:
    sock.bind(('127.0.0.1',5007))
    sock.listen(5)
    while True:
        conn,addr = sock.accept()
        option = conn.recv(1024).decode() 
        # Choosing option 1 or 2
        if option == '1': 
          # Newuser
            newUser = conn.recv(1024).decode()
            players[newUser] = 0
            conn.sendall("start".encode())
            hangman(SECRETWORD,LETTERGUESSED,l)
            players[newUser] = score
        else: 
          # Existing user
            userName = conn.recv(1024).decode()
            if userName in players :
                conn.sendall("start".encode())
                hangman(SECRETWORD,LETTERGUESSED,l)
                players[userName] = score
                conn.sendall("start".encode())

            else:
                players[userName] = 0
                conn.sendall("start".encode())
                hangman(SECRETWORD,LETTERGUESSED,l)
                players[userName] = score
                conn.sendall("start".encode())
