import sqlite3 as s
# Creates the db in the current folder
con = s.connect('store.db')
cur = con.cursor()

user = ("""
    CREATE TABLE USER (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER
    );
""")

cur.execute(user)

con.commit()
con.close()