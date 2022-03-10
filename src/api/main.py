from flask import Flask, request, jsonify
import requests
from decouple import config

app = Flask(__name__)


@app.route('/')
def base():
    return 'you accessed the base route'


@app.route('/bot', methods=['Post'])
def new_messages_listener():
    message = request.get_json()
    text = str(message['text'])
    chat_id = message['from']['id']
    reply(text, chat_id)
    return jsonify(message)


def reply(text, chat_id):
    api_token = config('API_TOKEN')
    bot_url = f'https://api.telegram.org/bot{api_token}/'
    reply_user_url = f'{bot_url}sendMessage?chat_id={chat_id}&text={text}'
    requests.get(reply_user_url)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
