from flask import Flask
from flask import request
from flask_cors import CORS
import json
from db.db import get_comment, get_thread, add_comment, add_thread

app = Flask(__name__)

CORS(app)

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        data = get_thread()
        print("home: GET")
        print(data)
        return data
    elif request.method == "POST" :
        print("home: POST")

@app.route("/thread/<id>", methods=["GET", "POST"])
def thread(id):
    if request.method == "GET":
        data = json.load(open("comment_list.json", "r"))
        print("thread: GET")
        print(data)
        print(id)
        return data
    else:
        print("home: POST")

if __name__ == '__main__':
    app.run(debug=True)
