import sqlite3

def select():
    con = sqlite3.connect('../sample.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS TEST(id INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    cur.execute("SELECT * FROM TEST")
    