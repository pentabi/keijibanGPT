# keijibanGPT
WINCハッカソン夏期２０２３グループ３のアプリ

## Description
これは掲示板アプリです。しかし、ときどきChatGPTがスレッドを盛り上げてくれます。

## Author
佐藤旅人、福永大、藤田開、堀江広晃、矢代琉介

## Date
2023年9月10日

## Getting Started

### Requires
* Windows 10/11, Mac OS 12.6.7
* node v18.17.1
* Python 3.11.5
* pip 23.2.1

### Execute Program
* Run Frontend Server
```bash
cd frontend
npm install
npm start
```

* Run Backend Server
```bash
cd backend
pip install flask flask_cors numpy SQLAlchemy openai
python main.py
```
* Add your API KEY (First time only)
```bash
cd backend
echo "PUT YOUR API KEY for ChatGPT" > api_key.txt
```
*`"PUT YOUR API KEY for ChatGPT"`の部分はあなたのAPI KEYに変更してください。API KEYは[ChatGPT API KEY](https://platform.openai.com/account/api-keys)で入手できます。*

* Run ChatGPT
```bash
cd backend
echo "PUT YOUR API KEY for ChatGPT" > api_key.txt
python GPT.py
```

* Delete Data Base
```bash
cd backend
rm comment.db thread.db
```

## Share your Bulletin Board
1. Change your branch from `main` to `share`
2. Run frontend server and check your Network IP address[^1]
3. Add this IP address to `frontend/src/api/ApiClient.js`

[^1]: Please check below image
![Network IP address](img/description.png)

## Design
このプロジェクトでは、フロントエンドにはReact、バックエンドではFlaskを用いた掲示板アプリを作成しました。ユーザーは自由にスレッド、コメントを追加することが出来ます。データベースにはSQLiteを用いており、FlaskがSQLiteにデータを保存しています。また、20分に一度、ChatGPTがデータベースにアクセスし、コメントをそれぞれのスレッドに追加します。
![Data Flow](img/dataFlow.jpg)

Data Baseでは以下のようなテーブルを作成しています。
![Data Table](img/table.png)
