import socket
import random




# conn.sendall(ALPHA.encode())



def getAvailableletter(LETTERGUESSED,TURN):
  '''
  letterguessed :list,what letters have been guessed untill now
    returns:string,comprised of letters that represents what letters have been guessed untill now
  '''

  # TURN = TURN
  '''global Turn means calling the turn which is in global into a function'''

  global ALPHA
  '''global alpha means calling the alpha i.e alphabets list into the function'''
  for i in LETTERGUESSED:
    if i in SECRETWORD:
      '''If the letterguessed is in secretWord then remove the letter '''
      conn.sendall("good guess.\n".encode())
      ALPHA.remove(i)




    else:
      '''If the letterguessed not in secretword then remove the letter'''
      TURN=TURN-1
      ALPHA.remove(i)
      conn.sendall("wrong guess.\n".encode())
  return "".join(ALPHA),TURN

'''If the letterguessed is not in the secretword then then we are replacing with "_"'''

def getguessword(SECRETWORD,lettersGuessed):
    '''
    secretWord: string , the word is user guessing
    lettersGuessed:list,what letters have been guessed so far
    returns:string,comprised of letters and underscores that represents that represents what letters in secretWord have been guessed so far
    '''
    a=SECRETWORD

    for d in SECRETWORD:
      if d not in lettersGuessed :
         a=a.replace(d," _")
    if a==SECRETWORD:
      conn.sendall("\nyou won! ".encode())
      #conn.sendall(SECRETWOR.encode(D)
      return
    else:
      return(a)


def isWordguessed(SECRETWORD,LETTERGUESSED,l):
  '''secretWord :string,the word is user guessing
  letterguessed:list,what letters have been guessed so far
  '''
  TURN = 8
  length = l
  #conn.sendall(SECRETWORD)
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


players = {'Reetu' : 100}
score = 0
lst = ""
LETTERGUESSED=[]
lettersGuessed=[]
'''To import a word from words.txt into secretWord'''
SECRETWORD=random.choice(open('words.txt').read().split())
# print("Hello  Welcome to Hangman")
l=len(SECRETWORD)
'''Here turn are the guesses '''

'''Alphabets are considered into a list as alpha'''
ALPHA=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

try:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

except socket.error() as msg:
    print('Socket creation failed!')

while True:
    soc.bind(('127.0.0.1',5000))
    soc.listen(5)
    while True:
        conn,addr = soc.accept()
        option = conn.recv(1024).decode() #option 1 or 2
        if option == '1':  #newusr
            newUser = conn.recv(1024).decode()
            players[newUser] = 0
            conn.sendall("start".encode())
            hangman(SECRETWORD,LETTERGUESSED,l)
            players[newUser] = score
        else: #existing users
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
