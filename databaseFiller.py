import sqlite3
from sqlite3 import Error
class DatabaseFiller:
    def __init__(self) -> None:
        self.db_filename="game_stats.db"
        self.create_connection()
        self.create__map_name_table()
        self.create_table()
        pass
    def create_connection(self):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(self.db_filename)
            print(sqlite3.version)
        except Error as e:
            print(e)
        finally:
            if conn:
                conn.close()
    def create__map_name_table(self):
        conn = sqlite3.connect(self.db_filename)
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS map_name (
                                                        id integer PRIMARY KEY,
                                                        map_name text NOT NULL,
                                                        original_console text NOT NULL,
                                                        )""")
        # if the table map_name is empty, insert the data from the Mario_kart8deluxe_maps_with_dlcs_map.csv file
        if c.execute("""SELECT COUNT(*) FROM map_name""").fetchone()[0] == 0:
            # read a csv file and insert the data in the table map_name
            with open('Mario_kart8deluxe_maps_with_dlcs_map.csv','r') as file:
                for line in file:
                    line=line.split(',')
                    c.execute("INSERT INTO map_name (map_name,original_console) VALUES (?,?)",(line[0],line[1]))
                    
        conn.commit()
        conn.close()
    def create_table(self):
        conn = sqlite3.connect(self.db_filename)
        c = conn.cursor()
        # create a table with the data from the Mario_kart8deluxe_maps_with_dlcs_map.csv file
        
        
        c.execute("""CREATE TABLE IF NOT EXISTS game_stats (
                                                        id integer PRIMARY KEY,
                                                        map_name text NOT NULL,
                                                        date DATE NOT NULL
                                                        )""")
        # create a table that store the result of the game (players, scores, date) and link it to the table game_stats

        c.execute("""CREATE TABLE IF NOT EXISTS game_stats_result ( 
                                                        id integer PRIMARY KEY,
                                                        players text NOT NULL,
                                                        scores INTEGER NOT NULL,
                                                        FOREIGN KEY (id) REFERENCES game_stats(id)
                                                        )""")
        conn.commit()
        conn.close()
    def insert_data(self,map_name,players,scores,date):
        conn = sqlite3.connect(self.db_filename)
        c = conn.cursor()
        for i in range(len(map_name)):
            c.execute("INSERT INTO game_stats (map_name,date) VALUES (?,?)",(map_name[i],date))
        # insert the data of the score of each player in the table game_stats_result
        for i in range(len(players)):
            c.execute("INSERT INTO game_stats_result (players,scores) VALUES (?,?)",(players[i],scores[i]))
        conn.commit()
        conn.close()
if __name__ == '__main__':
    db=DatabaseFiller()
    
