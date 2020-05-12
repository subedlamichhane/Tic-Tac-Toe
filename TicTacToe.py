
import random


def draw_board(board):
    #print the board to the user

    print(' \t| \t| ')
    print(board[7]+'\t| '+board[8]+'\t| ' +board[9])
    print(' \t| \t| ')
    print('--------------')

    print(' \t| \t| ')
    print(board[4] + '\t| ' + board[5] + '\t| ' + board[6])
    print(' \t| \t| ')
    print('--------------')

    print(' \t| \t| ')
    print(board[1] + '\t| ' + board[2] + '\t| ' + board[3])
    print(' \t| \t| ')



def player_letter():
    #ask player to select his letter
    letter=''
    while not (letter=='X' or letter=='O'):
        print('Do you want to be X or 0')
        letter= input().upper()

        if letter == 'X': #if user chose X assign O to computer and vice-versa
            return[ 'X','O']
        else:
            return['O','X']


def first_player():
    #randomly selecting the first player
    if random.randint(0,1)==0:
        return 'computer'
    else:
        return 'player'


def freespace_check(board, move): #check if selected move is available
    return board[move] ==''


def player_move(board):
    #take move from user limiting it to 1-9
    move=''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not freespace_check(board,int(move)):
        print('enter your next move (1-9): ')
        move=input()
    return int(move)


def make_move(board,letter,move):
    #assign the players choice to board
    board[move]=letter

def is_winner(board, letter):
    #check if the letters match for a win
    return ((board[7]==letter and board[8]==letter and board[9]==letter)or #check top row
            (board[6] == letter and board[5] == letter and board[4] == letter) or # check medium row
            (board[1] == letter and board[2] == letter and board[3] == letter) or # check bottom row
            (board[7] == letter and board[4] == letter and board[1] == letter) or # check left column
            (board[8] == letter and board[5] == letter and board[2] == letter) or # check middle column
            (board[9] == letter and board[6] == letter and board[3] == letter) or # check right column
            (board[1] == letter and board[5] == letter and board[9] == letter) or # check diagonal
            (board[3] == letter and board[5] == letter and board[7] == letter) ) # check another diagonal

def board_copy(board):
    #to generate intermidiate boards
    temp_board=[] #duplicate board initialization
    for i in board:
        temp_board.append(i)
    return temp_board


def random_move(board,move_list):
    #random move generation for computer
    possible_moves=[]
    for i in move_list:
        if freespace_check(board,i):
            possible_moves.append(i)

    if len(possible_moves)!=0:
        return random.choice(possible_moves) #randomly select the board position
    else:
        return None

def computer_move(board,computerletter):
    #determine move for computer
    if computerletter=='X':
        playerletter='O'
    else:
        playerletter='X'

    #checking if the move can make computer winner , a Simple AI
    for i in range(1,10):
        copy=board_copy(board)
        if freespace_check(copy,i):
            make_move(copy,computerletter,i)
            if is_winner(copy,computerletter):
                return i
    # checking if move can make player winner and blocking that move
    for i in range(1,10):
        copy=board_copy(board)
        if freespace_check(copy,i):
            make_move(copy,playerletter,i)
            if is_winner(copy,playerletter):
                return i
    move = random_move(board,[1,3,7,9]) # making moves at the corners
    if move != None:
        return move

    if freespace_check(board,5): #placing the letter at the center
        return 5

    return random_move(board,[2,4,6,8]) # making move to other empty spaces

def is_full(board):
    #checking if the board is full
    for i in range(1,10):
        if freespace_check(board,i): #checking if the particular space of board is taken
            return False
    return True


def restart():
    #restart the program upon user request
    print('Play again??(yes/no)')
    return input().lower().startswith('y')
print('-------TIC TAC TOE!!!----------')


while True:

    board=['']*10 # board initialization

    playerletter,computerletter=player_letter() # ask user which letter he wants to choose
    turn=first_player() # randomly deciding who plays first
    print(turn+' !!! is  playing  first.')
    game_on = True

    while game_on:
        if turn=='player':
            #for players moves
            draw_board(board) # draw the board
            move=player_move(board) #assign players move to the board
            make_move(board, playerletter,move)

            if is_winner(board,playerletter):
                #checking if player wins with the recent move
                draw_board(board)
                print('!!!Congratulations!!You won this game')
                game_on=False
            else:
                if is_full(board):
                    # If no one is winning and the board is full , The game is draw
                    draw_board(board)
                    print('!!!!Game is draw!!!')
                    break
                else:
                    #if no one is winning and the board is not full, pass the turn to computer
                    turn='computer'
        else:
            #computers move
            move= computer_move(board,computerletter)
            make_move(board,computerletter,move)

            if is_winner(board,computerletter):
                #check if computer wins
                draw_board(board)
                print('!!Sorry !!!Computer won this game')
                game_on=False
            else:
                #if computer has not won and the board is full the game is draw
                if is_full(board):
                    draw_board(board)
                    print('!!!Game is draw!!!')
                    break
                else:
                    #if no one has own and board still has some space left pass the turn to player
                    turn= 'player'

    if not restart():
        #If user doesnot wants to replay quit the game
        break


