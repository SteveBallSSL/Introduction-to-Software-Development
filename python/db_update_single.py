import sqlite3 as s

con = s.connect('store.db')
cur = con.cursor()

sql = 'UPDATE USER SET name=?, age=? WHERE id =?'
data = ['Bobby', 3, 2]

cur.execute(sql, data)

con.commit()
con.close()