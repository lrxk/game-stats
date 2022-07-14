import sqlite3
from sqlite3 import Error


class DatabaseFiller:
    def __init__(self) -> None:
        self.db_filename = "game_stats.db"
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
                                                        original_console text NOT NULL
                                                        )""")
        # if the table map_name is empty, insert the data from the Mario_kart8deluxe_maps_with_dlcs_map.csv file
        if c.execute("""SELECT COUNT(*) FROM map_name""").fetchone()[0] == 0:
            # read a csv file and insert the data in the table map_name
            with open('Mario_kart8deluxe_maps_with_dlcs_map.csv', 'r') as file:
                for line in file:
                    line = line.split(',')
                    c.execute(
                        "INSERT INTO map_name (map_name,original_console) VALUES (?,?)", (line[0], line[1]))

        conn.commit()
        conn.close()

    def create_table(self):
        conn = sqlite3.connect(self.db_filename)
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS game (
                                                        id integer PRIMARY KEY,
                                                        date text NOT NULL
                                                        )""")
        c.execute("""CREATE TABLE IF NOT EXISTS leaderboard (
                                                id integer PRIMARY KEY,
                                                game_id integer NOT NULL,
                                                player_name text NOT NULL,
                                                player_score integer NOT NULL,
                                                FOREIGN KEY (game_id) REFERENCES game(id)
                                                )""")
        c.execute("""CREATE TABLE IF NOT EXISTS maps_played (
                                                id integer PRIMARY KEY,
                                                game_id integer NOT NULL,
                                                map_name text NOT NULL,
                                                FOREIGN KEY (game_id) REFERENCES game(id)
                                                )""")
        conn.commit()
        conn.close()


    def insert_data(self, map_name, players, scores, date):
        conn = sqlite3.connect(self.db_filename)
        c = conn.cursor()
        # insert the data in the table game
        c.execute("INSERT INTO game (date) VALUES (?)", (date,))
        game_id = c.lastrowid
        for player, score in zip(players, scores):
            c.execute("INSERT INTO leaderboard (game_id, player_name, player_score) VALUES (?,?,?)", (game_id, player, score))
        for map in map_name:
            c.execute("INSERT INTO maps_played (game_id, map_name) VALUES (?,?)", (game_id, map))
        conn.commit()
        conn.close()

if __name__ == '__main__':
    db = DatabaseFiller()
