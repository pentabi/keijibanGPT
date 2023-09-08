from flask import Flask, request, render_template
import myproject.chatgpt_response

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    message = request.form['message']
    response = myproject.chatgpt_response.Chatgpt_response(message)
    return response

if __name__ == '__main__':
    app.run()
