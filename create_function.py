import sqlite3
from create_db import thread_db_cur, comment_db_cur, thread_db_conn, comment_db_conn

# スレッドに新しいスレッドを追加する関数
def thread_insert(thread_now_name):
    thread_db_cur.execute("INSERT INTO thread(thread_name) VALUES(?)", (thread_now_name,))
    thread_db_conn.commit()



# 内容は{スレッド番号(ID), ユーザーID, ユーザの名前, 投稿内容, 時刻, 人物フラグ(false=人間, true=chatGPT)}
def comment_insert(
        # user_id,
        thread_now_id,
        user_name,
        now_content,
        now_flag
    ):
    # comment_db_cur.execute('INSERT INTO comment (id) values(user_id)')
    comment_db_cur.execute("INSERT INTO comment(thread_id) VALUES(?)",(thread_now_id,))
    comment_db_cur.execute("INSERT INTO comment(name) VALUES(?)",(user_name,))
    comment_db_cur.execute("INSERT INTO comment(content) VALUES(?)",(now_content,))
    comment_db_cur.execute("INSERT INTO comment(flag) VALUES(?)",(now_flag,))
    comment_db_conn.commit()



# テスト
# thread_insert("スレッド新規作成テスト")
# comment_insert(1, "テスト君", "コメント追加テストです。", True)

# Don't close cursors and connections here, as they should be closed after all operations are done.
