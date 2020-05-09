from IPython.display import clear_output

def display_board(board):
 
    clear_output()
        
    print(f"{board[0]}  | {board[1]}  | {board[2]}")
    print(f"___|____|____")
    print(f"{board[3]}  | {board[4]}  | {board[5]}")
    print(f"___|____|____")
    print(f"{board[6]}  | {board[7]}  | {board[8]}")
    print(f"   |    |")
    return board
    
def player_input(): 
   
    marker = input("Player 1, Please pick a marker 'X' or 'O'").upper()
    while marker not in ["X","O"]:
        marker = input("Invalid input. Please enter only X or O").upper()
    player1=marker
    if player1=="X":
        player2="O"
    else:
        player2="X"
    return (player1,player2)
    
 def place_marker(board, marker, position):
    board[position-1]=marker
    
 def win_check(board, mark):
    if board[0]==mark and board [1]==mark and board [2]==mark:
        return True
    elif board[3]==mark and board [4]==mark and board [5]==mark:
        return True
    elif board[6]==mark and board [7]==mark and board [8]==mark:
        return True
    elif board[0]==mark and board [4]==mark and board [8]==mark:
        return True
    elif board[2]==mark and board [4]==mark and board [6]==mark:
        return True
    else:
        return False
        
import random

def choose_first():
    first_play=random.randint(1,2)
    print (f"Player {first_play} goes first")
    return first_play
    
def space_check(board, position):
    if board[position-1]!="X" and board[position-1]!="O":
        return True
    else:
        return False
        

def full_board_check(board):
    x=True
    for n in range(0,9):
        if board[n]!="X" and board[n]!="O":
            x=False
    return x 
    
    
def player_choice(board, turn):   
    position=0
    while position not in range(1,10) or board[position-1] in ["X","O"]:
        try:
            position=int(input(f"Player {turn} Please make your move by selecting available slot between numbers 1 to 9"))
        except:
            print("I'm sorry, please try again")
    return position
    
def replay():
    playagain=""
    while playagain not in ["Y","N"]:
        playagain=input("Do you want to play again? Enter Y or N").upper()
    if playagain=="Y":
        the_game()
        

def the_game():
    print('Welcome to Tic Tac Toe!')

    the_board=[1,2,3,4,5,6,7,8,9]
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    game_on=True
    
    
    while game_on:   
        if turn==1:
            display_board(the_board)
            position=player_choice(the_board,turn)
            place_marker(the_board,player1_marker,position)
            
            if win_check(the_board,player1_marker)==True:
                display_board(the_board)
                print(f"Player {turn} has won")
                game_on=False
                replay()
            elif full_board_check(the_board)==True:
                display_board(the_board)
                print("TIE GAME!")
                game_on=False
                replay()
            else: 
                turn=2
            
        
        else:
            display_board(the_board)
            position=player_choice(the_board,turn)
            place_marker(the_board,player2_marker,position)
            
            if win_check(the_board,player2_marker)==True:
                display_board(the_board)
                print(f"Player {turn} has won")
                game_on=False
                replay()
            elif full_board_check(the_board)==True:
                display_board(the_board)
                print("TIE GAME!")
                game_on=False
                replay()
            else:
                turn=1