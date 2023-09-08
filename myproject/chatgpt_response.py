from flask import Flask
import openai
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def Chatgpt_response():
    openai.api_key = "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"

    chat = input("質問を入力: ")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "斜に構えた態度で話して"},
            {"role": "system", "content": "ひねくれた態度で話して"},
            {"role": "user", "content": chat},
        ],
    )

    print(response['choices'][0]['message']['content'])

while True:
    Chatgpt_response()