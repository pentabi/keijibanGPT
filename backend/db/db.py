import json
from create import thread_db_cur, comment_db_cur, thread_db_conn, comment_db_conn
import sqlite3

# Function to add a new thread based on JSON data
def add_thread(json_data):
    data = json.loads(json_data)

    if "thread_add" in data:
        thread_name = data["thread_add"]["thread_name"]
        thread_db_cur.execute("INSERT INTO thread(thread_name) VALUES(?)", (thread_name,))
        thread_db_conn.commit()
        print("Thread added:", thread_name) #追加したスレッドを表示
    else:
        print("Invalid JSON format. Provide 'thread_add' data.")

# Function to add a new comment based on JSON data
def add_comment(json_data):
    data = json.loads(json_data)

    if "comment_add" in data:
        comment_data = data["comment_add"]
        thread_id = comment_data["thread_id"]
        user_name = comment_data["name"]
        content = comment_data["content"]
        chatGpt = False #フロントの投稿はいつも人間なので常にFalse
        comment_db_cur.execute("INSERT INTO comment(thread_id, name, content, flag) VALUES(?, ?, ?, ?)",
                                (thread_id, user_name, content, chatGpt))
        comment_db_conn.commit()
        print("Comment added to thread_id", thread_id, "by", user_name, "with content:", content) #追加したコメントを表示
    else:
        print("Invalid JSON format. Provide 'comment_add' data.")

def get_thread():
    comcon = sqlite3.connect('comment.db')  # Replace with your database path
    comcur = comcon.cursor()

    # Fetch data from the comments table
    comcur.execute("SELECT * FROM comment")
    comments_data = comcur.fetchall()

    thrcon = sqlite3.connect('thread.db')  # Replace with your database path
    thrcur = thrcon.cursor()

    # Fetch data from the thread table
    thrcur.execute("SELECT * FROM thread")
    thread_data = thrcur.fetchall()

    # Create a JSON structure based on the provided format
    json_data = {
        "thread_list": []
    }

    for thread_row in thread_data:
        thread_id, thread_name = thread_row
        thread_dict = {
            "thread": {
                "thread_id": thread_id,
                "thread_name": thread_name,
                "comment_list": []
            }
        }

        # Fetch comments associated with the current thread_id
        comcur.execute("SELECT * FROM comment WHERE thread_id=?", (thread_id,))
        comments_data = comcur.fetchall()

        for comment_row in comments_data:
            comment_id, _, name, content, flag = comment_row
            comment_dict = {
                "comment": {
                    "comment_id": comment_id,
                    "name": name,
                    "content": content,
                    "chatGpt": bool(flag)
                }
            }
            thread_dict["thread"]["comment_list"].append(comment_dict)

        json_data["thread_list"].append(thread_dict)

    comcon.close()
    thrcon.close()

    return json.dumps(json_data, indent=3, ensure_ascii=False)  # Ensure_ascii set to False

# 指定したスレッドIDに関連するコメントを取得し、リストのJSON形式で返す関数
def get_comment(thread_id):
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
