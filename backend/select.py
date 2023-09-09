import sqlite3

while True:
    con = sqlite3.connect('./sample.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS TEST(id INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    sql = 'INSERT INTO TEST(name) values (?)'
    name = str(input("名前を入力:"))
    cur.execute(sql, name)
    cur.execute("SELECT * FROM TEST")
    con.commit()
    for row in cur:
        print(str(row[0]) + "," + str(row[1]))
    con.close()


