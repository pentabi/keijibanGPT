from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
import json
from db import get_comment, get_thread, add_comment, add_thread

app = Flask(__name__)

CORS(app)

@app.route("/home", methods=["GET", "POST"])
def home():
    print("/home")
    if request.method == "GET":
        data = get_thread()
        print("home: GET")
        print(data)
        return data
    elif request.method == "POST" :
        print("home: POST")
        add_thread(request.get_json())
        return jsonify("ok")

@app.route("/thread/<id>", methods=["GET", "POST"])
def thread(id):
    print("/thread")
    if request.method == "GET":
        data = json.load(open("comment_list.json", "r"))
        print("thread: GET")
        print(data)
        return data
    else:
        data = request.get_json()
        print("thread: POST")
        print(data)
        return jsonify("ok")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
