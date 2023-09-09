import sqlite3
import json

from backend.create_db import comment_db_cur, comment_db_conn

# 指定したスレッドIDに関連するコメントを取得し、リストのJSON形式で返す関数
def get_comments_by_thread_id(thread_id):
    # コメントデータを取得
    comment_db_cur.execute("SELECT * FROM comment WHERE thread_id=?", (thread_id,))
    comments = comment_db_cur.fetchall()

    # コメントデータをリストに変換
    comment_list = []
    for comment in comments:
        comment_dict = {
            "comment_id": comment[0],
            "thread_id": comment[1],
            "name": comment[2],
            "content": comment[3],
            "chatGpt": bool(comment[4])  # 0をFalse、1をTrueに変換
        }
        comment_list.append({"comment": comment_dict})

    # リストをJSON形式に変換して返す
    return json.dumps({"comment_list": comment_list}, indent=3, ensure_ascii=False)

# Usage example:
if __name__ == "__main__":
    thread_id = 2  # 取得したいコメントのスレッドIDを指定
    comments_json = get_comments_by_thread_id(thread_id)
    print(comments_json)
