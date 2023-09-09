from flask import Flask, request, render_template
import myproject.chatgpt_response
from datetime import datetime
from flask_sqlalchemy import flask_sqlalchemy
import sqlite3

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    message = request.form['message']
    response = myproject.chatgpt_response.Chatgpt_response(message)
    return render_template("form.html", response=response)

if __name__ == '__main__':
    app.run()
