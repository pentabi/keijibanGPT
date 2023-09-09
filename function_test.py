from create_function import thread_insert, comment_insert

thread_insert("スレッド新規作成テスト")

comment_insert(
    # 現在のスレッドナンバーを変数に入れて保持しておく
    1,
    # chatGPTが投稿した時にユーザー名をどうするか
    "kai",
    #messageはDBから選ばれた最新５件のうちの一つ又は、人間が打ち込んだ投稿
    Chatgpt_response(message),
    # 人間が投稿した場合はformボタンを押した時にfalseを返す仕組みをフロント側にお願い
    #false又はtrueを返す関数を定義する
    False 
)
comment_insert(
    1,
    "tabito",
    "僕もテストです。",
    False
)