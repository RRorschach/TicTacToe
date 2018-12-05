##Tic Tac Toe Draw

print ("")
print ("-------------------------")
print ("Welcome to TIC TAC TOE :)")
print ("-------------------------")
print ("Game Rules: It is a 2 player game. Its player must enter the desired coordinates, 'row, column'.")
print ("Player 1 is marked with 'X' and player 2 is marked with 'O'.")
print ("example: 1,2")
print ("Have Fun!!!")
print ("-------------------------")
print ("")

def player_moves(player):
    stop = False
    while not stop:
        try:
            print("Players' " + player + " turn...")
            player_input = input("")
            coord_2 = player_input.replace(' ', '').split(',')
            row = int(coord_2[0])
            col = int(coord_2[1])                                  
            if row > 2 or row < 0:
                print("Wrong row input...")
            elif col > 2 or col < 0:
                print("Wrong column input...")
            elif board[row][col] != ' . ':
                print("Tile already played. Play another tile...")
            else:
                if player == 'one':
                    board[row][col] = ' X '
                    stop = True
                elif player == 'two':
                    board[row][col] = ' O '
                    stop = True
        except IndexError:
            print ("Invalid format imput. Please enter two coordinates separated with comma (example for first square: 0,0).")
        except ValueError:
            print ("Invalid format imput. Please enter two coordinates separated with comma (example for first square: 0,0).")
    return board[row][col]


def check_game_status(board, X):
        end_game = False
        if board[0] == [X,X,X] or board[1] == [X,X,X] or board[2] == [X,X,X]:
            end_game = True
        elif board[0][0] == X and board[1][0] == X and board[2][0] == X:
            end_game = True
        elif board[0][1] == X and board[1][1] == X and board[2][1] == X:
            end_game = True
        elif board[0][2] == X and board[1][2] == X and board[2][2] == X:
            end_game = True
        elif board[0][0] == X and board[1][1] == X and board[2][2] == X:
            end_game = True
        elif board[0][2] == X and board[1][1] == X and board[2][0] == X:
            end_game = True
        return end_game

board = [[' . ', ' . ', ' . '], [' . ', ' . ', ' . '], [' . ', ' . ', ' . ']]
turns = 0
not_another_game = False
stop = False
player = "one"

while not not_another_game:
    new_game = input ("Start a new game (y or n): ").lower()
    if new_game == 'y':
        while not stop:
            player_moves(player)
            print ("")
            print ('\n'.join(' '.join(map(str,row)) for row in board))
            print ("")
            print ("-------------------------")
            print ("")

            if player == 'one':
                if check_game_status(board, ' X ') == True:
                    print ("Game Over!")
                    print ("Player one won the game!!!")
                    stop = True
                player = 'two'
            else:
                if check_game_status(board, ' O ') == True:
                    print ("Game Over!")
                    print ("Player two won the game!!!")
                    stop = True
                player = 'one'

            if turns == 8:
                print ("Game Over!")
                print ("No more Moves...The game is tie!!!")
                stop = True
            turns += 1
    else:
        print ("Next time!")
        not_another_game = True
