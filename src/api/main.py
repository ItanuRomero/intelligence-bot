from flask import Flask, request, jsonify
from decouple import config

app = Flask(__name__)


@app.route('/')
def base():
    return 'you accessed the base route'


@app.route('/bot', methods=['GET', 'Post'])
def new_messages_listener():
    message = request.args.get('message')
    message = {'text': message}
    return jsonify(message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
