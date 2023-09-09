from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)

CORS(app)

@app.route("/home", methods=["GET"])
def index():
    data = json.load(open("data.json", "r"))
    print(data)
    print()
    return data

if __name__ == '__main__':
    app.run(debug=True)
