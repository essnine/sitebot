from flask import Flask, render_template
from flask_socketio import SocketIO
from os import getcwd
import logging
import eventlet
eventlet.monkey_patch()


app = Flask(
    import_name=__name__,
    static_folder="static/",
)
socket_app = SocketIO(app, async_mode="eventlet")


@socket_app.on("connect")
def handle_connect(sid):
    logging.info("Socket connected: {}".format(sid))


@app.get("/bot")
def bot_page():
    return render_template(
        "{}/static/html/bot.html".format(getcwd())
    )


@app.get("/")
def root_path():
    return "Hello World"


if __name__ == "__main__":
    socket_app.run(
        app,
        host="0.0.0.0",
        port=8080,
        debug=True,
    )
