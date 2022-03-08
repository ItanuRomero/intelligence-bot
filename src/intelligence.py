import requests
from decouple import config
import json
import os
import time

class Intelligence:
    def __init__(self):
        API_TOKEN = config('API_TOKEN')
        self.bot_url = f'https://api.telegram.org/bot{API_TOKEN}/'

    def listen(self):
        update_id = None
        while True:
            new_messages_response = self.get_new_messages(update_id)
            new_messages = new_messages_response["result"]
            if new_messages:
                for message in new_messages:
                    update_id = message['update_id']
                    text = str(message["message"]["text"])
                    chat_id = message["message"]["from"]["id"]
                    message_id = int(message["message"]["message_id"])
                    is_first_message = message_id == 1
                    self.user_id = message["message"]['from']['id']
                    response = self.create_reply(
                        text, is_first_message)
                    self.reply(response, chat_id)
            time.sleep(10)

    def get_new_messages(self, update_id):
        new_messages_url = f'{self.bot_url}getUpdates?timeout=100'
        if update_id:
            new_messages_url = f'{new_messages_url}&offset={update_id + 1}'
        result = requests.get(new_messages_url)
        return json.loads(result.content)
    
    def create_reply(self, text, is_first_message):
        if is_first_message == True or text.lower() in ('hi', 'hello'):
            return f'''Hello. Test if I'm a idiot'''
        if text.lower() == 'are you inteligent?':
            return f'''Nope...'''
        elif text.lower() == 'really?':
            return f'''Really. I was only programmed to understand some inputs.'''
        elif text.lower() == 'well that sucks':
            return f'''Yeah, but at least I'm alive!{os.linesep}
        Who knows if someday I can be more intelligent and dominate the world.
        '''
        elif text.lower() == 'but what can you do?':
            return f'''I can send you your ID, do you wanna see it?'''
        elif text.lower() in ('yes', 'yep'):
            return f'''Nice, it is {self.user_id}'''
        elif text.lower() in ('no', 'nope'):
            return '''Well, if you need something I'll be here.'''
        else:
            return "Do you wanna know what I'm capable of? Send Hi or access my repository"

    def reply(self, text, chat_id):
        reply_user_url = f'{self.bot_url}sendMessage?chat_id={chat_id}&text={text}'
        requests.get(reply_user_url)


if __name__ == "__main__":
    bot = Intelligence()
    bot.listen()