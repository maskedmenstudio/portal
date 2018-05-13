import socket
from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

def game(player):
  #assign a random play to the computer
 computer = t[randint(0,2)]
 if player == computer:
    return "Tie!"
 elif player == "Rock":
   if computer == "Paper":
     return "You lose! "+ computer + " covers "+player
   else:
     return "You win! "+player+" smashes "+ computer
 elif player == "Paper":
         if computer == "Scissors":
           return "You lose! "+computer+" cut "+player
         else:
            return "You win! "+player+" covers "+computer
 elif player == "Scissors":
          if computer == "Rock":
              return "You lose... "+computer+" smashes "+ player
          else:
              return "You win! "+player+" cut "+computer
 
def Main():
    host = "localhost"
    port = 5001
     
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))
             
            data = str(game(str(data)))
            print ("sending: " + data)
            conn.send(data.encode())
             
    conn.close()
     
if __name__ == '__main__':
    Main()
