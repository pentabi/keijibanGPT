from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    message = request.form['message']
    return message

if __name__ == '__main__':
    app.run()
