
import sqlite3 as s

con = s.connect('store.db')

query = "DROP TABLE USER;"

data = con.execute(query)


con.commit()
con.close()

