import sqlite3

def select_data():
    con = sqlite3.connect('./sample.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS TEST(id integer,name text)")
    cur.execute("SELECT * FROM TEST")
    for row in cur:
        print(str(row[0]) + "," + str(row[1]))
    con.close()


def insert_data():
    con = sqlite3.connect('./sample.db')
    cur = con.cursor()
    sql = 'INSERT INTO TEST (id, name) values (?,?)'
    data = [1, '猫']
    cur.execute(sql, data)
    con.commit()
    con.close()

