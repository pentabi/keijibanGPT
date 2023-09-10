from flask import Flask
import openai
import os
import get_api_key


def Chatgpt_response(message):
    openai.api_key = get_api_key.get_api_key()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = message,
    )

    return response['choices'][0]['message']['content']

