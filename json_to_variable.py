import json

# 仮の辞書データを作成
temp_data = """{
   "thread_list": [
      {
         "thread": {
            "thread_id": 1,
            "thread_name": "スレッド新規作成テスト",
            "comment_list": [
               {
                  "comment": {
                     "comment_id": 1,
                     "name": "kai",
                     "content": "関数のテストです。",
                     "chatGpt": false
                  }
               },
               {
                  "comment": {
                     "comment_id": 2,
                     "name": "tabito",
                     "content": "僕もテストです。",
                     "chatGpt": false
                  }
               },
               {
                  "comment": {
                     "comment_id": 3,
                     "name": "kai",
                     "content": "関数のテストです。",
                     "chatGpt": false
                  }
               },
               {
                  "comment": {
                     "comment_id": 4,
                     "name": "tabito",
                     "content": "僕もテストです。",
                     "chatGpt": false
                  }
               }
            ]
         }
      },
      {
         "thread": {
            "thread_id": 2,
            "thread_name": "スレッド新規作成テスト",
            "comment_list": []
         }
      }
   ]
}"""

# 辞書をJSON文字列に変換
json_data = json.loads(temp_data)

# JSONデータをプリント
# print(type(json_data))
# print(json_data)

# print(json_data["thread_list"][0])
# print(type(json_data["thread_list"]["thread_id"]))
# print(json_data["thread_list"])

for thread in json_data:
    # 全ての'comment'辞書を繰り返し
    for comment in thread["thread"]["comment_list"]:
        # 'content'キーが'僕もテストです。'と等しい場合
        if comment["comment"]["content"] == "僕もテストです。":
            print(comment["comment"]["content"])
