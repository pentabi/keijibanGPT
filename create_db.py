# DB/tableを作成するファイル

import sqlite3

# スレッド番号(ID)・スレッドネームを管理するデータベース
# 内容は{スレッド番号(ID), スレッドネーム}
thread_db = 'thread.db'

# 全スレッドの全コメント管理するデータベース
# 内容は{スレッド番号(ID), ユーザーID, ユーザの名前, 投稿内容, 時刻, 人物フラグ(false=人間, true=chatGPT)}
comment_db = "comment.db"

thread_db_conn = sqlite3.connect(thread_db)
comment_db_conn = sqlite3.connect(comment_db)

# # sqliteを操作するカーソルオブジェクトを作成
thread_db_cur = thread_db_conn.cursor()
comment_db_cur = comment_db_conn.cursor()

# Create the thread table if it does not exist
thread_db_cur.execute(
    "CREATE TABLE IF NOT EXISTS thread(thread_id INTEGER PRIMARY KEY AUTOINCREMENT, thread_name STRING)"
)

# Create the comment table if it does not exist
comment_db_cur.execute(
    "CREATE TABLE IF NOT EXISTS comment(id INTEGER PRIMARY KEY AUTOINCREMENT, thread_id NUMBER, name STRING, content STRING, flag BOOLEAN)"
)




# thread_db_conn.close()
# comment_db_conn.close()
