import tabulate
from bot import bot_move 
from search_win import *

'''
Receives a dictionary with the values of the game and prints out the board. 
'''
def print_table(game_board : dict) -> None:
    # The special characters are invisible characters, so that it will look more symmetrical 
    X_O = ['\n\u2800','\n\u2800 X','\n\u2800 O']
    table_tabulate = []

    # Split the dictionary to three different lists, then add them to table_tabulate  
    for line in [list(game_board.items())[i*3:i*3+3:] for i in range(3)]:
        table_tabulate.append([spot_key +  X_O[spot_value] for spot_key,spot_value in line ])

    # Print the board using tabulate 
    print(tabulate.tabulate(table_tabulate,tablefmt='rounded_grid'))

'''
The function runs the tic tac toe game in player vs player mode.
The fucntion returns information about the game moves done by the players, who won, the game board, name of the players.
All of the other parameters are general information about the game.
The function returns only when winning conditions are met, the rules are of a regular tic-tac-toe game. 
'''
def player_vs_player(playerX : str = None, playerO : str = None) -> dict:
    '''
    Intiating the game board, default value is 0 because the board is empty. 
    0 - default value, the spot is not taken, 1 - the spot was taken by X, 2 - the spot was taken by O. 
    '''
    game_board = dict.fromkeys(['top-L','top-M','top-R','mid-L','mid-M','mid-R','low-L','low-M','low-R'],0)

    # Intiate Move_list, stores all the moves the players make, the order signifies the number of the turn.
    move_list = []

    # Making a list of all of the unused spots on the board
    unused_spots = list(game_board.keys())

    # The game only ends when winning condition is met. 
    while True:


        # Printing the board for X move. 
        print('X move')
        print_table(game_board)

        # Get input from the user, and check it. 
        while True:
            playerX_move = input('Player X enter your move: ')
            print()
            if playerX_move in unused_spots: 
                break
        # Make the move and store it. 
        game_board[playerX_move] = 1
        move_list.append(playerX_move)
        unused_spots.remove(playerX_move)

        # If won return info.
        if search_win(game_board,1):
            print_table(game_board)
            return {'move_list':move_list,'winner':'X','playerX':playerX,
    'playerO':playerO, 'game_board' : game_board}

        # Printing the board for O move. 
        print('O move')
        print_table(game_board)

        # Check if it's a draw
        if not unused_spots:
            return {'move_list':move_list,'winner':'Draw','playerX':playerX,
    'playerO':playerO, 'game_board' : game_board}
        


        # Get input from the user, and check it. 
        while True:
            playerO_move = input('Player O enter your move: ')
            print()
            if playerO_move in unused_spots: 
                break
        # Make the move and store it. 
        game_board[playerO_move] = 2
        move_list.append(playerO_move)
        unused_spots.remove(playerO_move)

        # If won return info.
        if search_win(game_board,2):
            print_table(game_board)
            return {'move_list':move_list,'winner':'O','playerX':playerX,
    'playerO':playerO, 'game_board' : game_board}

        # Check if it's a draw
        if not unused_spots:
            return {'move_list':move_list,'winner':'Draw','playerX':playerX,
    'playerO':playerO, 'game_board' : game_board}

'''
The function runs the tic tac toe game in player vs bot mode.
The parameters required are player name, and the player side as the bot can play either side.
'''  
def bot_vs_player(player : str, player_side : str) -> dict:
    '''
    Intiating the game board, default value is 0 because the board is empty. 
    0 - default value, the spot is not taken, 1 - the spot was taken by X, 2 - the spot was taken by O. 
    '''
    game_board = dict.fromkeys(['top-L','top-M','top-R','mid-L','mid-M','mid-R','low-L','low-M','low-R'],0)

    # Intiate Move_list, stores all the moves the players make, the order signifies the number of the turn.
    move_list = []

    # Making a list of all of the unused spots on the board
    unused_spots = list(game_board.keys())

    # The game only ends when winning condition is met. 
    while True:

        # Printing the board for X move. 
        if player_side == 'X': 
            print('\nX move')
            print_table(game_board)

        # Get input from the user, and check it. 
        if player_side == 'X': 
            while True:
                playerX_move = input('Player X enter your move: ')
                if playerX_move in unused_spots: 
                    break
        else: 
            playerX_move = bot_move(game_board, 1)

        # Make the move and store it. 
        game_board[playerX_move] = 1
        move_list.append(playerX_move)
        unused_spots.remove(playerX_move)

        # If won return info.
        if search_win(game_board,1):
            print_table(game_board)
            return {'move_list':move_list,'winner':'X','playerX':(lambda : player if player_side == 'X' else 'Bot')(),
    'playerO':(lambda : player if player_side == 'O' else 'Bot')(), 'game_board' : game_board}

        # Printing the board for O move. 
        if player_side == 'O':  
            print('\nO move')
            print_table(game_board)

        # Check if it's a draw
        if not unused_spots:
            return {'move_list':move_list,'winner':'Draw','playerX':(lambda : player if player_side == 'X' else 'Bot')(),
    'playerO':(lambda : player if player_side == 'O' else 'Bot')(), 'game_board' : game_board}
        


        # Get input from the user, and check it. 
        if player_side == 'O':
            while True:
                playerO_move = input('Player O enter your move: ')
                if playerO_move in unused_spots: 
                    break
        else: 
            playerO_move = bot_move(game_board, 2)
        # Make the move and store it. 
        game_board[playerO_move] = 2
        move_list.append(playerO_move)
        unused_spots.remove(playerO_move)

        # If won return info.
        if search_win(game_board,2):
            print_table(game_board)
            return {'move_list':move_list,'winner':'O','playerX':(lambda : player if player_side == 'X' else 'Bot')(),
    'playerO':(lambda : player if player_side == 'O' else 'Bot')(), 'game_board' : game_board}

        # Check if it's a draw
        if not unused_spots:
            return {'move_list':move_list,'winner':'Draw','playerX':(lambda : player if player_side == 'X' else 'Bot')(),
    'playerO':(lambda : player if player_side == 'O' else 'Bot')(), 'game_board' : game_board}

'''
Runs a game between two bots and returns the results. 
'''
def bot_vs_bot() -> dict: 
    '''
    Intiating the game board, default value is 0 because the board is empty. 
    0 - default value, the spot is not taken, 1 - the spot was taken by X, 2 - the spot was taken by O. 
    '''
    game_board = dict.fromkeys(['top-L','top-M','top-R','mid-L','mid-M','mid-R','low-L','low-M','low-R'],0)

    # Intiate Move_list, stores all the moves the players make, the order signifies the number of the turn.
    move_list = []

    # Making a list of all of the unused spots on the board
    unused_spots = list(game_board.keys())

    # The game only ends when winning condition is met. 
    while True:
        # Make the move and store it. 
        playerX_move = bot_move(game_board,1)
        game_board[playerX_move] = 1
        move_list.append(playerX_move)
        unused_spots.remove(playerX_move)

        # If won return info.
        if search_win(game_board,1):
            print_table(game_board)
            return {'move_list':move_list,'winner':'X','playerX':'Bot',
    'playerO':'Bot', 'game_board' : game_board}

        # Check if it's a draw
        if not unused_spots:
            print_table(game_board)
            return {'move_list':move_list,'winner':'Draw','playerX':'Bot',
    'playerO':'Bot', 'game_board' : game_board}
        
        # Make the move and store it. 
        playerO_move = bot_move(game_board,2)
        game_board[playerO_move] = 2
        move_list.append(playerO_move)
        unused_spots.remove(playerO_move)

        # If won return info.
        if search_win(game_board,2):
            print_table(game_board)
            return {'move_list':move_list,'winner':'O','playerX':'Bot',
    'playerO':'Bot', 'game_board' : game_board}

        # Check if it's a draw
        if not unused_spots:
            print_table(game_board)
            return {'move_list':move_list,'winner':'Draw','playerX':'Bot',
    'playerO':'Bot', 'game_board' : game_board}

if __name__=='__main__':
    pass