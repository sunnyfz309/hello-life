from random import randint
import sys

"""create play board"""
board = []

def create_board():
  for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print ("Battleship Game")
create_board()
print_board(board)

"""generate a list of ships with non-duplicate locations"""
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

def generate_one():
  ship_row = random_row(board)
  ship_col = random_col(board)
  return [ship_row, ship_col]

ship_set = []

def generate_ships():
  ship_num = randint(1, 6)
  for i in range(ship_num):
    ship_loc = generate_one()
    while ship_loc in ship_set:
      ship_loc = generate_one()
    ship_set.append(ship_loc)

def print_ships(ship_set):
  for ship in ship_set:
    print (ship)

print ("ships")
generate_ships()
print_ships(ship_set)

"""game logic"""
turns = len(ship_set) + 5
count = 0
for turn in range(turns):
  print ("Turn", turn + 1)
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))
  guess = [guess_row, guess_col]
  
  if guess in ship_set:
    board[guess_row][guess_col] = "X"
    count += 1
    ship_set.remove(guess)
    print ("You sunk my battleships: " + str(count) + "/" + str(turns - 5))
    if len(ship_set) == 0:
      print ("Congratulations! Yon won!")
      break
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print ("Oops, that's not even in the ocean.")
    elif (board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "*"):
      print ("You guessed that one already.")
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col] = "*"
  if turn == turns - 1:
    print ("Game Over")
    break
  print_board(board)