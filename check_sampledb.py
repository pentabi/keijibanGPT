import sqlite3
print('comments:')
con = sqlite3.connect('sample.db')
cur = con.cursor()

cur.execute("SELECT * FROM test")
rows = cur.fetchall()

for row in rows:
    print(row)

con.close()