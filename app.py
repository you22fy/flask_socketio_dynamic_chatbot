from flask import Flask, render_template
from flask_socketio import SocketIO
from chat import random_response


app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_message(data):
    response_message = random_response()
    socketio.emit('receive_message', {'message': response_message})

if __name__ == '__main__':
    socketio.run(app, port=3000)
