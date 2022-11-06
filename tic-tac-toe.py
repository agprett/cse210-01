import math

wins3x3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

class Board:
  def __init__(self, board_size, num_rows, wins):
    self.board_size = board_size
    self.num_rows = num_rows
    self.x = []
    self.o = []
    self.wins = wins
    self.rows = []

  def build_rows(self):
    while len(self.rows) < self.num_rows:
      row = ''
      for i in range(1, self.board_size + 1):
        if len(self.rows) % 2 != 0:
          if i != 1:
            row += '+ '
          row += ' - '
        else:
          if i != 1:
            row += '| '
          row += f' {i + (self.board_size * math.floor(len(self.rows) / 2))} '
        i += 1
      
      self.rows.append(row)
  
  def show_board(self):
    for row in self.rows:
      print(row)

  def make_move(self, turn, position):
    if turn == 'x':
      if position in self.o or position > self.board_size * self.board_size or position < 1:
        return False
      else:
        self.x.append(position)

    if turn == 'o':
      if position in self.x or position > self.board_size * self.board_size or position < 1:
        return False
      else:
        self.o.append(position)

    self.rows[math.floor((position - 1) / self.board_size) * 2] = self.rows[math.floor((position - 1) / self.board_size) * 2].replace(f'{position}', turn)

    return True

  def check_win(self, turn):
    win = False
    for possibles in self.wins:
      if turn == 'x' and set(possibles).issubset(set(self.x)):
        win = True
      elif turn == 'o' and set(possibles).issubset(set(self.o)):
        win = True

    return win

  def check_tie(self):
    return self.board_size * self.board_size == len(self.x) + len(self.o)

def build_board(size):
  board_size = 0
  num_rows = 0
  wins = 0

  if size == '3x3':
    board_size = 3
    num_rows = 5
    wins = wins3x3
  else:
    return 'Not a valid board size, please try again'

  board = Board(board_size, num_rows, wins)

  board.build_rows()

  return board

def main():
  game = build_board('3x3')

  print('Welcome to tic-tac-toe!')
  print('To play, just type in the number of the position you want to take.')

  turn = 'x'

  print('\n')
  game.show_board()
  print('\n')

  while True:
    selected = int(input(f"{turn}'s turn to select a space(1-{game.board_size * game.board_size}): "))

    move = game.make_move(turn, selected)

    if move:
      print('\n')
      game.show_board()
      print('\n')

      if game.check_win(turn):
        print(f'The winner is {turn}!')
        break
      elif game.check_tie():
        print('The game is a tie!')
        break
      
      if turn == 'x':
        turn = 'o'

      elif turn == 'o':
        turn = 'x'


    else:
      print('That move was not allowed. Please try again.')

if __name__ == '__main__':
  main()