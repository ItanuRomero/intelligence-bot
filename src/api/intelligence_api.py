import requests
from decouple import config


def reply(text, chat_id):
    api_token = config('API_TOKEN')
    bot_url = f'https://api.telegram.org/bot{api_token}/'
    reply_user_url = f'{bot_url}sendMessage?chat_id={chat_id}&text={text}'
    requests.get(reply_user_url)