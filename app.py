from flask import Flask, request, render_template
import myproject.chatgpt_response
from backend import insert

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    message = request.form['message']
    response = myproject.chatgpt_response.Chatgpt_response(message)
    insert.insert(response)
    return render_template("form.html", response=response)

if __name__ == '__main__':
    app.run()