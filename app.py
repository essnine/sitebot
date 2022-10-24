from flask import Flask, render_template
from flask_socketio import SocketIO
import logging
import eventlet
eventlet.monkey_patch()


app = Flask(
    import_name=__name__,
    template_folder="static/html",
)
socket_app = SocketIO(app, async_mode="eventlet")


@socket_app.on("connect")
def handle_connect(sid):
    logging.info("Socket connected: {}".format(sid))


@app.get("/<path_name>")
def bot_page(path_name):
    return render_template("/{}.html".format(path_name))
    # except Exception as exc:
    #     logging.exception("Could not load template: {}".format(
    #         str(exc)
    #     ))
    #     return "Not found", 404


@app.get("/")
def return_root_path():
    return "Hello World"


@app.get("/healthz")
def check_healthz():
    return "OK"


if __name__ == "__main__":
    socket_app.run(
        app,
        host="0.0.0.0",
        port=8080,
        debug=True,
    )
