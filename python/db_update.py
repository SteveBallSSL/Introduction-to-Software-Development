import sqlite3 as s

con = s.connect('store.db')
cur = con.cursor()

sql = 'INSERT INTO USER (name, age) values(?, ?)'
data = ['Ruthy', 25]

cur.execute(sql, data)

con.commit()
con.close()