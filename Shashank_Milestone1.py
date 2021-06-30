import random

#Step 1: Tic Tac Toe Board
def display_board(board):
    
    #clear_output()
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    #print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    #print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    #print('   |   |')


#Step 2: which player goes first 

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'player 1'
    else: return 'player 2'


# Step 3: Player Marker assign

def player_marker(player):
    marker = ''
    
    #asking player to choose x or o
    while not (marker == 'x' or marker == 'o'):
        marker = input("\nDo you want to be X or O, {}? ".format(player)).lower()

    #assigning opposite to other player
    if marker == 'x':
        return ('x','o')
    else:
        return ('o', 'x')



#step 4: input position and checking its validity
def player_input(board):

    #initial value
    choice = "Invalid"
    board_size = 9
    #acceptable = range(1,board_size*board_size+1)
    acceptable = range(1,board_size+1)
    within_range = False

    # DIGIT or WITHIN_RANGE == False
    while choice.isdigit()==False or within_range == False:
        
        choice = input("Choose your next position in range (1-{}):".format(board_size))

        # Digit check
        if choice.isdigit()==False:
            print("Not a valid integer, try again!")
        
        # Range check and position not already occupied
        else:
            if int(choice) in acceptable:
                if board[int(choice)] != ' ':
                    print("this position already filled, try again!")

                else:
                    within_range = True
                      
            else:
                #print("Please enter an integer within range (1-{})!".format(board_size*board_size))   
                print("Please enter an integer within range (1-{})!".format(board_size))   
    
    return int(choice)  


#Step 5: insert that marker in the board

def insert(board, marker, position):
    board[position] = marker


#Step 6: check winner

def winner(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# Step 7: play again?
def gameon_choice():
    choice = 'wrong'
    choice = input('Play Again? Enter Yes or No.')
    
    if choice.lower()[0] == 'y':
        return True
    elif choice.lower()[0] == 'n':
        return False
    else:
        print("invalid choice,try again!")
        return gameon_choice()






# Final Code:

print('Welcome to Tic Tac Toe!')

player1 = input("Player-1 name: ")
player2 = input("Player-2 name: ")

score_card = {player1:0, player2:0}

game_on = True

while game_on:

    print("\nScoreCard: {} ".format(score_card))

    # Reset the board
    theBoard = [' '] * 10

    turn = choose_first()
    if turn == 'player 1':
        print("\n{} will go first".format(player1))
        player1_marker, player2_marker = player_marker(player1)

    else: 
        print("\n{} will go first".format(player2))
        player2_marker, player1_marker = player_marker(player2)

    counter = 1
    win = False
    while counter <= 9:

        if turn == 'player 1':
            # Player1's turn.
            
            display_board(theBoard)
            #position = player_choice(theBoard)
            position = player_input(theBoard)
            insert(theBoard, player1_marker, position)

            if winner(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! {} have won the game!'.format(player1))
                score_card[player1]+=1
                win = True
                break
            else:
                turn = 'player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            #position = player_choice(theBoard)
            position = player_input(theBoard)
            insert(theBoard, player2_marker, position)

            if winner(theBoard, player2_marker):
                display_board(theBoard)
                print('Congratulations! {} have won the game!'.format(player2))
                score_card[player2] += 1
                win = True
                break
            else:
                turn = 'player 1'
            
        counter+=1

    if counter == 9 and win == False:
        display_board(theBoard)
        print('The game is a draw!')

    game_on = gameon_choice()