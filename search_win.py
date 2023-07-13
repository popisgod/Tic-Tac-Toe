
# Checks if win condition is met on one of the cols. 
def search_vertical_win(game_board : dict, player : int) -> bool: 
    cols = [list(game_board.values())[i::3] for i in range(3)]
    return any(all(spot == player for spot in col) for col in cols)

# Checks if win condition is met on one of the rows. 
def search_horizontal_win(game_board : dict, player : int) -> bool: 
    rows = [list(game_board.values())[i*3:i*3+3] for i in range(3)]
    return any(all(spot == player for spot in row) for row in rows)

# Checks if win condition is met on one of the diagonals. 
def search_diagonal_win(game_board : dict, player : int) -> bool: 
    return all(list(game_board.values())[i] == player for i in [0, 4, 8]) or all(list(game_board.values())[i] == player for i in [2, 4, 6])

'''
Searches for a win, combines the 3 function above, to check for horizontal, vertical, and diagonal win.
If the win condition is met, 3 spots in a row are takeb by the same player, the function returns true. 
'''
def search_win(game_board : dict, player : int) -> bool:
    return search_diagonal_win(game_board,player) or search_horizontal_win(game_board
    ,player) or search_vertical_win(game_board,player)