from flask import Flask, request, jsonify
from intelligence_api import reply

app = Flask(__name__)


@app.route('/')
def base():
    return 'you accessed the base route'


@app.route('/bot', methods=['Post'])
def new_messages_listener():
    message = request.args.get('message')
    text = str(message['text'])
    chat_id = message['from']['id']
    reply(text, chat_id)
    return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
