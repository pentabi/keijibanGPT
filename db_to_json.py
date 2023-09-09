import sqlite3
import json

# Function to convert SQLite data to JSON format
def convert_to_json():
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

# Usage example:
if __name__ == "__main__":
    json_result = convert_to_json()
    print(json_result)