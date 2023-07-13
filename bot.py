import random
from search_win import *

'''
This function goes over every possible move and return if it's possible 
'''
def next_move_win(game_board : dict, player : int) -> str:
    
    # List of possible moves
    possible_moves = list(map(lambda x: x[0] ,filter(lambda x: x[1] == 0, game_board.items())))

    # Checks if any move wins 
    for move in possible_moves:
        spot_value, game_board[move] = game_board[move], player
        if search_win(game_board, player):
            game_board[move] = spot_value 
            return move
        game_board[move] = spot_value 
    return None

'''
checks if there multiple possible wins for one move and returns the number of possible wins and the moves for them.
'''
def multiple_wins(game_board : dict, player : int) -> str:
    
    # List of possible moves
    possible_moves = list(map(lambda x: x[0] ,filter(lambda x: x[1] == 0, game_board.items())))
    counter = 0 
    winning_moves = []

    # Checks if any move wins 
    for move in possible_moves:
        spot_value, game_board[move] = game_board[move], player
        if search_win(game_board, player):
            game_board[move] = spot_value 
            counter += 1 
            winning_moves.append(move)
        game_board[move] = spot_value 
    return (counter,winning_moves)

'''
Return the best move for the player at any situation, player is decided based on player.
players: 1 - X player, 2 - O player.
'''
def bot_move(game_board : dict, player : int) -> str: 
    # List of possible moves
    possible_moves = list(map(lambda x: x[0] ,filter(lambda x: x[1] == 0, game_board.items())))
    # Corners of the board
    corners = ['top-L','top-R','low-L','low-R']
    # opponent int
    opponent = player % 2 + 1 

    # Checks if there's a possible next move that wins for our player.
    our_player_win = next_move_win(game_board,player)
    if our_player_win: return our_player_win

    # Checks if there's a possible next move that wins for our opponent, in order to block him.
    opponent_win = next_move_win(game_board,opponent)
    if opponent_win: return opponent_win

    # Checks for any forks that I can make  
    for move in possible_moves:
        spot_value, game_board[move]  = game_board[move], player
        fork_check = multiple_wins(game_board,player)
        if fork_check[0] > 1 and move in possible_moves: 
            game_board[move] = spot_value 
            return move
        game_board[move] = spot_value     

    # Checks for any forks from the opponent 
    spot_value, game_board['mid-M'] = game_board['mid-M'], opponent
    # If possible play any move that's not one of the corners 
    if search_win(game_board, opponent):
        game_board['mid-M'] = spot_value 
        return random.choice(list(filter(lambda x: x not in corners, possible_moves)))
    game_board['mid-M'] = spot_value 



    # If the middle is empty play in the middle
    if not game_board['mid-M']:
        return 'mid-M'
    # if the middle is not empty play one of the corners 
    corners_possible = list(filter(lambda x: x in possible_moves,['top-L','top-R','low-L','low-R']))
    if corners_possible: return random.choice(corners_possible)
    # if the corners are not empty play a random possible move
    return random.choice(possible_moves)

if __name__=='__main__': pass
