import sqlite3

def insert_data(response):
    con = sqlite3.connect('./sample.db')
    cur = con.cursor()
    sql = 'INSERT INTO TEST (id, name) values (?,?)'
    data = [1, response]
    cur.execute(sql, data)
    con.commit()
    con.close()
