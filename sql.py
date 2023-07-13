import sqlite3 as lite 
from datetime import date,datetime

'''
function that pulls information from the database, returns raw data.
'''
def pull_game(name : str, conn : lite) -> dict: 
    try: 
        cur = conn.cursor()
        if name == 'ALL':
            cur.execute("SELECT * FROM games")
        else:
            cur.execute("SELECT * FROM games WHERE PlayerX = ? OR PlayerO = ?", (name,name))
        return cur
    except lite.Error as e:
        print(e)

'''
function receives information and the database conn, inserts the information to the DB.
'''
def store_game(information : dict, conn : lite) -> None: 
    try: 
        # adjusting and editing information to enter it to the DB. 
        board = tuple(information['game_board'].items())
        insert = """INSERT INTO Games (PlayerO, PlayerX , Winner, MoveList, GameBoard, Date, Time) VALUES (?,?,?,?,?,?,?)"""
        values = (information['playerO'],information['playerX'],information['winner'],
            ", ".join(information['move_list']),",".join(map(lambda x: ".".join(map(str,x)),board)),
                date.today().strftime("%d/%m/%Y"), datetime.now().strftime("%H:%M:%S"))
    
        cur = conn.cursor()
        cur.execute(insert,values)
        conn.commit() 

    except lite.Error as e:
        print(e)

'''
Creats the DB table.
'''
def create_table(conn : lite) -> None: 
    
    try:
        create_str='''CREATE TABLE Games (
                PlayerX TEXT NOT NULL,
                PlayerO TEXT NOT NULL,
                Winner TEXT NOT NULL,
                MoveList TEXT NOT NULL,
                GameBoard TEXT NOT NULL,
                Date TEXT NOT NULL,
                Time TEXT NOT NULL
            );'''
           
        cur = conn.cursor()
        cur.execute(create_str)
        conn.commit()
    except lite.Error as e:
        print(e)

'''
Deletes the DB table.
'''
def delete_table(conn : lite) -> None:
    try: 
        cur = conn.cursor()
        cur.execute("DROP TABLE Games")
        conn.commit()

    except lite.Error as e:
        print(e)

if __name__=='__main__':
    pass