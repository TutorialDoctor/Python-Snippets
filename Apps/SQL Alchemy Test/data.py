import sqlite3
con = sqlite3.connect("Search.db")
cur = con.cursor()
#stmnt = cur.execute("SELECT * from Jobs")
one = cur.fetchone()
lla = cur.fetchall()

for x in lla:
  print(x)

#con.close()