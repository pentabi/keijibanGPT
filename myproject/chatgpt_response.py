from flask import Flask
import openai
import os


def Chatgpt_response(message):
    openai.api_key = "" #API KEYを入力

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "斜に構えた態度で話して"},
            {"role": "system", "content": "ひねくれた態度で話して"},
            {"role": "user", "content": message},
        ],
    )

    return response['choices'][0]['message']['content']

