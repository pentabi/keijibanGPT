import sqlite3
from create import thread_db_cur, comment_db_cur, thread_db_conn, comment_db_conn

# 内容は{スレッド番号(ID), ユーザーID, ユーザの名前, 投稿内容, 時刻, 人物フラグ(false=人間, true=chatGPT)}
# この場合はCHATGPTなので一旦thread_idは常に１、名前CHATGPT、返答、TRUE
def insert(response,thread_id):
    comment_db_cur.execute("INSERT INTO comment(thread_id, name, content, flag) VALUES(?, ?, ?, ?)",
                            (thread_id, 'CHATGPT',response, True))
    comment_db_conn.commit()
