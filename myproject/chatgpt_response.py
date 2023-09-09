from flask import Flask
import openai
import os


def Chatgpt_response(message):
    openai.api_key = "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" #自分のAPI KEYを入力

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "斜に構えた態度で話して"},
            {"role": "system", "content": "ひねくれた態度で話して"},
            {"role": "user", "content": message},
        ],
    )

    return response['choices'][0]['message']['content']

