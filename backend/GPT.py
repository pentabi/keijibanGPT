from flask import Flask
import chatgpt_response
import insert
from gpt_get_comments import get_comments_by_thread_id, get_thread_title_by_thread_id,get_all_thread_ids
import time  # Import the time module

app = Flask(__name__)

def chat_gpt_periodically():
    while True:
        print("hello")
        thread_ids = get_all_thread_ids()
        for thread_id in thread_ids:
            # チャットGPTへの最初の命令
            message = [
                {"role": "system", "content": "斜に構えた態度で話して"},
                {"role": "system", "content": "ひねくれた態度で話して"},
                {"role": "system","content": "今から色々な人のコメントを送るので、話の流れに合ったコメントを二十行以内で返して下さい"},
            ]

            # スレタイトルを命令
            thread_title = get_thread_title_by_thread_id(thread_id)
            message.append({"role": "system", "content": "これが話題です： " + thread_title})

            #thread_idを選択
            comment_list = get_comments_by_thread_id(thread_id)
            cnt = 1
            for comment in comment_list:
                message.append({"role": "system", "content": str(cnt) + " " + comment['content']})
                cnt += 1
            
            message.append({"role": "system", "content": str(cnt) + " ???(あなたの返信がここに来る)"})
            message.append({"role": "system", "content": "前の会話に当てはまるコメントを返してください"})

            # チャットGPTの返信を追加
            response = chatgpt_response.Chatgpt_response(message)
            insert.insert(response,thread_id)
            print(response + " " + thread_id)
            time.sleep(20)

if __name__ == '__main__':
    chat_gpt_periodically()
