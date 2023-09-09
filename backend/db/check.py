import sqlite3
print('comments:')
con = sqlite3.connect('comment.db')
cur = con.cursor()

cur.execute("SELECT * FROM comment")
rows = cur.fetchall()

for row in rows:
    print(row)

print('thread:')
con = sqlite3.connect('thread.db')
cur = con.cursor()

cur.execute("SELECT * FROM thread")
rows = cur.fetchall()

for row in rows:
    print(row)

con.close()
