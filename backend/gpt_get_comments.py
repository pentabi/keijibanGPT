import sqlite3

from create import comment_db_cur, comment_db_conn, thread_db_conn,thread_db_cur

# Function to get comments by thread ID and return a list of comment dictionaries
def get_comments_by_thread_id(thread_id):
    # Comment data retrieval
    comment_db_cur.execute("SELECT * FROM comment WHERE thread_id=?", (thread_id,))
    comments = comment_db_cur.fetchall()

    # Convert comment data to a list of dictionaries
    comment_list = []
    for comment in comments:
        comment_dict = {
            "comment_id": comment[0],
            "thread_id": comment[1],
            "name": comment[2],
            "content": comment[3],
            "chatGpt": bool(comment[4])  # Convert 0 to False, 1 to True
        }
        comment_list.append(comment_dict)

    # Return the list of comment dictionaries
    return comment_list

def get_thread_title_by_thread_id(thread_id):
    thread_db_cur.execute("SELECT thread_name FROM thread WHERE thread_id=?", (thread_id,))
    thread_title = thread_db_cur.fetchone()

    if thread_title:
        return thread_title[0]  # Extract the thread title from the result tuple
    else:
        return None  # Handle the case when no thread with the given ID is found

def get_all_thread_ids():
    try:
        thread_db_cur.execute("SELECT thread_id FROM thread")
        thread_ids = [thread[0] for thread in thread_db_cur.fetchall()]
        return thread_ids
    except sqlite3.Error as e:
        print(f"Error retrieving thread IDs: {e}")
        return []

# Usage example:
if __name__ == "__main__":
    thread_id = 1  # Specify the thread ID for the comments you want to retrieve
    comments = get_comments_by_thread_id(thread_id)
    for comment in comments:
        print(comment)
