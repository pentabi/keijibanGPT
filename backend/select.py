import sqlite3

while True:
    con = sqlite3.connect('./sample.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS TEST(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
    name = input("名前を入力:")  # Removed unnecessary str() conversion
    cur.execute("INSERT INTO TEST(name) VALUES (?)", (name,))
    con.commit()

    # Retrieve the last row from the table
    cur.execute("SELECT * FROM TEST ORDER BY id DESC LIMIT 1")
    last_row = cur.fetchone()

    if last_row:
        print("Last Row:")
        print("ID:", last_row[0])
        print("Name:", last_row[1])
    else:
        print("No rows in the table yet.")

    con.close()