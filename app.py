from flask import Flask
from flask_socketio import SocketIO
import eventlet

app = Flask(__name__)
socket_app = SocketIO(app, async_mode="eventlet")


if __name__ == "__main__":
    socket_app.run(
        host="0.0.0.0",
        port=8080,
        debug=True,
    )