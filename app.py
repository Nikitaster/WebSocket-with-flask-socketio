import logging
import os
import json
import time

from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_socketio import send, emit

logging.basicConfig(format='[%(asctime)-15s] %(message)s', filename='{}/logfile.log'.format(os.getcwd()), level=logging.INFO)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('message')
def handle_message(message):
    try:
        emit('received', message)
        logging.info('message has been received: {}'.format(message))

        data = json.loads(message)
        text = data['text'].lower().replace(',', ' ').replace('.', ' ').replace('!', ' ').replace('?', ' ').split()
        for word in text:
            if word in ['привет', 'hi', 'hello']: 
                response = {'text': 'Привет! {}'.format(chr(128526)), 'time': int(time.time())}
                logging.info('message has been sent: {}'.format(response))
                emit('response', json.dumps(response))
            elif word in ['инфо', 'info']:
                response = {'text': 'Это учебный бот. Написан на flask-socketio.\nАвтор: Гудков Никита', 'time': int(time.time())}
                logging.info('message has been sent: {}'.format(response))
                emit('response', json.dumps(response))
            else:
                response = {'text': 'Мне нечего ответить', 'time': int(time.time())}
                logging.info('message has been sent: {}'.format(response))
                emit('response', json.dumps(response))
        
    except Exception as e:
        logging.error('{}'.format(e.args))


# @socketio.on('connect')
# def test_connect(auth):
#     emit('my response', {'data': 'Connected'})

# @socketio.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')


@socketio.on_error()        # Handles the default namespace
def error_handler(e):
    print(e)

@socketio.on_error('/chat') # handles the '/chat' namespace
def error_handler_chat(e):
    print(e)

@socketio.on_error_default  # handles all namespaces without an explicit error $
def default_error_handler(e):
    print(e)

if __name__ == '__main__':
    socketio = SocketIO(logger=True, engineio_logger=True)
    socketio.run(app, debug=True)
