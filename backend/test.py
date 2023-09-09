import sqlite3

def insert(response):
    con = sqlite3.connect('./sample.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS TEST(id INTEGER PRIMARY KEY AUTOINCREMENT,value json)")
    cur.execute("INSERT INTO TEST(name) VALUES(?)", (response,))
    cur.execute("SELECT * FROM TEST")
    con.commit()
    for row in cur:
        print(str(row[0]) + "," + str(row[1]))
    con.close()

