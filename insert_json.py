import sqlite3
import json

from backend.create_db import thread_db_cur, comment_db_cur, thread_db_conn, comment_db_conn

# Function to add a new thread based on JSON data
def add_thread_from_json(json_data):
    data = json.loads(json_data)
    
    if "thread_add" in data:
        thread_name = data["thread_add"]["thread_name"]
        thread_db_cur.execute("INSERT INTO thread(thread_name) VALUES(?)", (thread_name,))
        thread_db_conn.commit()
        print("Thread added:", thread_name) #追加したスレッドを表示
    else:
        print("Invalid JSON format. Provide 'thread_add' data.")

# Function to add a new comment based on JSON data
def add_comment_from_json(json_data):
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

# Usage example:
if __name__ == "__main__":
    json_data_thread = '''
    {
        "thread_add": {
            "thread_name": "hello"
        }
    }
    '''
    
    add_thread_from_json(json_data_thread)
    
    json_data_comment = '''
    {
        "comment_add": {
            "thread_id": 1,
            "content": "sleepy",
            "name": "dai"
        }
    }
    '''
    
    add_comment_from_json(json_data_comment)
