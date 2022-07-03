# user (0) vs. computer (1)
import random
board = [[-1, -1, -1],
         [-1, -1, -1],
         [-1, -1, -1]]

player = 0

def numToString(num):
  if num == 0:
    return "O"
  elif num == 1:
    return "X"
  else:
    return "."

def printBoard():
  for a in board: 
    print("{0:^5} {1:^5} {2:^5}".format(numToString(a[0]), numToString(a[1]), numToString(a[2])))
  return 0

# returns winner
def get_winner():
  winner = -1
  emptyCount = 0
  for a in board:
    if a[0] == a[1] and a[1] == a[2]:
      winner = a[0]
      return winner
  for a in range(0, 3):
    if board[0][a] == board[1][a] and board[1][a] == board[2][a]:
      winner = board[0][a]
      return winner
  if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
    winner = board[0][0]
    return winner
  if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
    winner = board[2][0]
    return winner
  for i in range (0, 3):
    for j in range (0, 3):
      if board[i][j] == -1:
        emptyCount = 1;
  if emptyCount == 0:
    return -15
  else:
    return -1

  


def makeMove():
    for i in range (0,3):
      #print (i)
      compStones=0
      manStones=0
      
      for b in board[i]:
        #print("b: {0}".format(b))
        if b == 0:
          manStones = manStones + 1
        elif b == 1:
          compStones = compStones + 1
        #print("compStones {0}, manStones   {1}".format(compStones, manStones))
      if compStones == 2 and manStones == 0:
        for j in range(0,3):
          if board[i][j] == -1:
            board[i][j] = 1
            return 0
  ###############################
    for i in range (0, 3):
      
      compStones=0
      manStones=0
        
      for b in range (0, 3):
        #print("b: {0}".format(board[b][i]))
        if board[b][i] == 0:
          manStones = manStones + 1
        elif board[b][i] == 1:
          compStones = compStones + 1
      if compStones == 2 and manStones == 0:
        for j in range(0,3):
          if board[j][i] == -1:
            board[j][i] = 1
            return 0
      
    #print("compStones {0}, manStones {1}".format(compStones, manStones))
######################
    compStones=0
    manStones=0
    for i in range (0, 3):
      #print("i: {0}".format(i))
      #print(board[i][i])
      if board[i][i] == 0:
        manStones = manStones + 1
      elif board[i][i] == 1:
        compStones = compStones + 1
      #print("compStones {0}, manStones {1}".format(compStones, manStones))
      if compStones == 2 and manStones == 0:
        for j in range(0,3):
          if board[j][j] == -1:
            board[j][j] = 1
            return 0

##########################
    compStones=0
    manStones=0
    for i in range (0, 3):
      #print("i: {0}".format(i))
      #print(board[i][i])
      if board[i][2-i] == 0:
        manStones = manStones + 1
      elif board[i][i] == 1:
        compStones = compStones + 1
      #print("compStones {0}, manStones {1}".format(compStones, manStones))
      if compStones == 2 and manStones == 0:
        for j in range(0,3):
          if board[j][2-j] == -1:
            board[j][2-j] = 1
            return 0
  
    #&&&&&&&&&&&&&&DEFENSE&&&&&&&&&&&&&

    for i in range (0,3):
    
      compStones=0
      manStones=0
      
      for b in board[i]:
        #print("b: {0}".format(b))
        if b == 0:
          manStones = manStones + 1
        elif b == 1:
          compStones = compStones + 1
      if compStones == 0 and manStones == 2:
        for j in range(0,3):
          if board[i][j] == -1:
            board[i][j] = 1
            return 0
###############################
    for i in range (0, 3):
      
      compStones=0
      manStones=0
        
      for b in range (0, 3):
        #print("b: {0}".format(board[b][i]))
        if board[b][i] == 0:
          manStones = manStones + 1
        elif board[b][i] == 1:
          compStones = compStones + 1
      if compStones == 0 and manStones == 2:
        for j in range(0,3):
          if board[j][i] == -1:
            board[j][i] = 1
            return 0
      
    #print("compStones {0}, manStones {1}".format(compStones, manStones))
######################
    compStones=0
    manStones=0
    for i in range (0, 3):
      #print("i: {0}".format(i))
      #print(board[i][i])
      if board[i][i] == 0:
        manStones = manStones + 1
      elif board[i][i] == 1:
        compStones = compStones + 1
      #print("compStones {0}, manStones {1}".format(compStones, manStones))
      if compStones == 0 and manStones == 2:
        for j in range(0,3):
          if board[j][j] == -1:
            board[j][j] = 1
            return 0

##########################
    compStones=0
    manStones=0
    for i in range (0, 3):
      #print("i: {0}".format(i))
      #print(board[i][i])
      if board[i][2-i] == 0:
        manStones = manStones + 1
      elif board[i][i] == 1:
        compStones = compStones + 1
      #print("compStones {0}, manStones {1}".format(compStones, manStones))
      if compStones == 0 and manStones == 2:
        for j in range(0,3):
          if board[j][2-j] == -1:
            board[j][2-j] = 1
            return 0
    while True:
      randomX = random.randint(0, 2)
      randomY = random.randint(0, 2)
      if board[randomX][randomY] == -1:
        board[randomX][randomY] = 1
        break
    
    return 0

  

printBoard()

difficulty = input("Type E for Easy Mode and H for Hard Mode. Type R for Really hard mode.")

if difficulty == "H":
  print ("\nHard Mode it is!\n")  
  makeMove()
  print ("\nI made my move\n")  
  printBoard()
elif difficulty == "R":
  print ("\n\"It\'s only hubris if I fail\" - Julius Caesar\n")  
  board[1][1] = 1
  makeMove()
  print ("\nI made my moves, man.\n")  
  printBoard()
elif difficulty == "E":
  print("\nYou don't seem very confident. Did you forget this is a 2-hour coding project?\n")

while True:

  while True:

  
    
    print("\nMake your move, man\n")
    xcoord = input("X coordinate: ")
    xcoord = int(xcoord)-1
    ycoord = input("Y coordinate: ")
    ycoord = int(ycoord)-1
    if board[ycoord][xcoord] == -1:
      board[ycoord][xcoord] = player
      break
  
    
  printBoard()

  winner = get_winner()
  if winner == 0:
    print("Man won!")
    break
  elif winner == 1:
    print("You just lost to a 2 hour coding project!")  
    break
  elif winner == -15:
    print("Its a draw!")
    break
    
  makeMove()
  print ("\nI made my move\n")  
  printBoard()
  
  winner = get_winner()
  if winner == 0:
    print("Man won!")
    break
  elif winner == 1:
    print("You just lost to a 2 hour coding project!")  
    break
  elif winner == -15:
    print("Its a draw!")
    break
    

