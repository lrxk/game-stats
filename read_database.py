import sqlite3
from sqlite3 import Error
# create a database connection to a SQLite database
conn=sqlite3.connect("game_stats.db")
# create a cursor
c=conn.cursor()
# read the data from the database
c.execute("SELECT * FROM maps_played")

print(c.fetchall())

conn.close()
