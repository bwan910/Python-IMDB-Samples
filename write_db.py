# The code allows it to write the top movies and bottom movies into SQLlite


import imdb
import sqlite3


ia = imdb.IMDb()

conn = sqlite3.connect('IMDB.db')

print("Opened database successfully")


conn.execute('''CREATE TABLE BOTTOM_MOVIES
(ID INTEGER PRIMARY KEY AUTOINCREMENT,
TITLE           TEXT    NULL,
RATING          DOUBLE     NULL
)
''')
print("Table created successfully")


conn.execute('''CREATE TABLE TOP_MOVIES
(ID INTEGER PRIMARY KEY AUTOINCREMENT,
TITLE           TEXT    NULL,
RATING          DOUBLE     NULL
)
''')
print("Table created successfully")


bottom = ia.get_bottom100_movies()
for i in range(100):
    conn.execute("INSERT INTO BOTTOM_MOVIES (TITLE, RATING) \
      VALUES (?,?)", (bottom[i]['title'], bottom[i]['rating']))


top = ia.get_top250_movies()
for x in range(200):
    conn.execute("INSERT INTO TOP_MOVIES (TITLE, RATING) \
      VALUES (?,?)", (top[x]['title'], top[x]['rating']))


conn.commit()
conn.close()
