import sqlite3

con = sqlite3.connect('comment.db')
cur = con.cursor()

cur.execute("SELECT * FROM comment")
rows = cur.fetchall()

for row in rows:
    print(row)

con.close()
