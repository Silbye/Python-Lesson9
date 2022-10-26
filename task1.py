import os
import emoji

os.system('cls')

print("*" * 10, " 2P Tic-tac-toe ", "*" * 10)

board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Place " + player_token+": ")
      try:
         player_answer = int(player_answer)
      except:
         print("Invalid input, enter a number: ")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) in '123456789'):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("This spot is already taken!")
      else:
        print("Invalid input, enter a number between 1 and 9")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    a = ''
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            a = emoji.emojize(':thumbs_up:')
            take_input(a)
        else:
            a = emoji.emojize(':thumbs_down:')
            take_input(a)
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "won!")
              win = True
              break
        if counter == 9:
            print("A tie!")
            break
    draw_board(board)
main(board)

