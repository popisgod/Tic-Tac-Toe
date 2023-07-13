from tabulate import tabulate
from game import *
from sql import *

'''
Runs the game in player vs player mode, stores the game in the db for later retrieval. 
'''
def GamePvP() -> None:
    # Get the players names
    playerX = input('Enter the name of player X: ')
    playerO = input('Enter the name of player O: ')
    print()
    # Running the game
    game = player_vs_player(playerX, playerO)
    if game['winner'] != 'Draw':
        print(f'The winner is {game["winner"]}!!!\n')
    else:
        print('Draw!!!\n')

    # Storing the game
    store_game(game,conn)

'''
Runs the game in Bot vs Bot mode, stores the game in the db for later retrieval. 
'''
def gameCvC() -> None: 
    # Running the game
    game = bot_vs_bot()
    if game['winner'] != 'Draw':
        print(f'The winner is {game["winner"]}!!!\n')
    else:
        print('Draw!!!\n')

    # Storing the game
    store_game(game,conn)

'''
Runs the game in Player vs Bot mode, stores the game in the db for later retrieval. 
'''
def gamePvC() -> None: 
    # Get the player name and side
    while True:
        player_side = input('Enter the side you want to play X or O: ')
        if player_side in ['O','X']:
            break
    player = input('Enter the name of the player: ')
    print()

    # Running the game
    game = bot_vs_player(player, player_side)
    if game['winner'] != 'Draw':
        print(f'The winner is {game["winner"]}!!!\n')
    else:
        print('Draw!!!\n')

    # Storing the game
    store_game(game,conn)

'''
a function that returns history of games, shows information about past games.
'''
def history() -> None: 
    while True:
        # Name of requested information
        request = input('\nEnter ALL to see all games, a NAME of a player to see their games, QUIT to leave history, DELETE to delete history: ')
        if request == 'QUIT': return 
        if request == 'DELETE': 
            delete_table(conn)
            create_table(conn)
            print('history deleted, returning to menu...')
            return
        # Requested information
        info = pull_game(request,conn)
        info = list(map((lambda x: (x[0]+1,*x[1])), enumerate(info)))

        if info: 
            print(tabulate.tabulate(map(lambda x: (x[0],x[1],x[2],x[3],x[6],x[7]),info), 
                headers=['ID', 'PlayerX','PlayerO', 'Winner', 'Date','Time'],tablefmt="fancy_grid"))
            while True:
                while True:
                    request = input('\nTo see the game and board of a specific game enter its ID, to go back enter BACK: ')
                    if (request.isdigit() and (0 < (request := int(request)) <= len(info))) or request == 'BACK':
                        break
                    print('ID doesn\'t exist in the database or invalid input')
                if request != 'BACK':
                    print(f'\nDate {info[request-1][6]} | Time: {info[request-1][7]} | Winner: {info[request-1][2]} | PlayerX: {info[request-1][1]} | PlayerO: {info[request-1][2]}  ')
                    print('Moves:'," -> ".join(map(lambda x: 'X: ' + x[1] if not x[0] % 2 else 'O: ' + x[1] ,enumerate(info[request-1][4].split(', ')))))
                    print_table(dict(map(lambda x: (x[0],int(x[1])),map(lambda x: x.split('.'),info[request-1][5].split(',')))))
                else: break
        elif request == 'ALL':
            print('History is empty.')
        else: 
            print('Name doesn\'t exist in the database or invalid input')

'''
Main function, connects all of the main game functions,
'''
def main() -> None:
    global conn
    conn = lite.connect('database.db')
    create_table(conn)


    print(
'_______           _____               _____          \n\
|_   __|         |_   _|             |_   _|         \n\
 | |  _  ___ ______| | __ _  ___ ______| | ___   ___  \n\
 | | | |/ __|______| |/ _` |/ __|______| |/ _ \ / _ \ \n\
 | | | | |__       | | |_| | |__       | | |_| |  __/ \n\
 \_/ |_|\___|      \_/\__,_|\___|      \_/\___/ \___| \n' )

    # Menu with all of the game options.
    menu = '\n\nGame Options \n','1. Player vs Player\n','2. Player vs Bot\n','3. Bot vs Bot\n','4. History\n','5. Quit\n'
    
    # list containing possible game modes functions.
    game_modes = [GamePvP,gamePvC,gameCvC,history,lambda : [print('\nThank you for playing my Tic-Tac-Toe game!!!\n'),conn.close(),quit()]] # TODO: mb add ascii art for the quit message

    # The game runs untill the user enters the Quit option. 
    while True:
        print(*menu)

        # Input option
        while True:
            option = input('Enter option: ')
            if  option.isdigit() and 1 <= (option := int(option)) <= 5:
                break 
        # Running the option
        game_modes[option-1]()
        if option != 4:
            input('Press Enter to continue...')

if __name__=='__main__':
   main()



