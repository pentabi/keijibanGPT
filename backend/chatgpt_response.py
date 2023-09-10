from flask import Flask
import openai
import os


def Chatgpt_response(message):
    openai.api_key = "" #API KEYを入力

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = message,
    )

    return response['choices'][0]['message']['content']

