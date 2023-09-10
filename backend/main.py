from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
import json
from db import get_comment, get_thread, add_comment, add_thread

app = Flask(__name__)

CORS(app)

@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        data = get_thread()
        return data
    elif request.method == "POST" :
        add_thread(request.get_json())
        return jsonify("success")

@app.route("/thread/<id>", methods=["GET", "POST"])
def thread(id):
    print("/thread")
    if request.method == "GET":
        data = get_comment(id)
        return data
    elif request.method == "POST":
        add_comment(request.get_json())
        return jsonify("success")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
