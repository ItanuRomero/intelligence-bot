import requests
from decouple import config

def main():
    API_TOKEN = config('API_TOKEN')
    bot_url = f'https://api.telegram.org/bot{API_TOKEN}/getUpdates'
    result = requests.get(bot_url)
    print(result.json())

if __name__ == "__main__":
    main()