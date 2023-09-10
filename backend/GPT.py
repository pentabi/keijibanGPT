from flask import Flask
import chatgpt_response
import insert
from gpt_get_comments import get_comments_by_thread_id, get_thread_title_by_thread_id,get_all_thread_ids
import time  # Import the time module
import get_interval

app = Flask(__name__)

def chat_gpt_periodically():
    while True:
        print("GPT response started")
        thread_ids = get_all_thread_ids()

        #threadがなかった場合
        if len(thread_ids) < 1:
            print("No thread! GPT will wait for 60 seconds")
            time.sleep(60)

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
            if len(comment_list) < 1:
                print("There is no comment on thread " + str(thread_id) + " GPT will not comment on this thread")
                continue
            for comment in comment_list:
                message.append({"role": "system", "content": comment['content']})

            message.append({"role": "system", "content": "前の会話に当てはまるコメントを返してください"})
            message.append({"role": "system", "content": "特に一個前のコメントにひねくれたコメントを返してください"})

            # チャットGPTの返信を追加
            response = chatgpt_response.Chatgpt_response(message)
            insert.insert(response,thread_id)
            print(response + " " + str(thread_id))
            time.sleep(get_interval.get_interval())

if __name__ == '__main__':
    chat_gpt_periodically()
