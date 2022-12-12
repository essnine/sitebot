import eventlet
import logging

from flask import Flask, render_template, send_file     # type: ignore
from flask_socketio import SocketIO, emit     # type: ignore
from services.postprocess import UserMessage

eventlet.monkey_patch(socket=True, thread=True)
app = Flask(
    import_name=__name__,
    template_folder="static/html",
)
socket_app = SocketIO(app, async_mode="eventlet", namespace=["/botMessage"])


@socket_app.on("connect")
def handle_connect(sid):
    logging.info("Socket connected: {}".format(sid))


@socket_app.on("userMessage", namespace="/botMessage")
def handle_user_message(user_json):
    # TODO: add handler for socket message to fetch response from chatbot
    print("user message :{}".format(str(user_json)))
    logging.debug(user_json.keys())
    responseObj = UserMessage(user_json.get("message", {}).get("value", ""))
    emit("botResponse", {"message": str(responseObj)})


@app.get("/bot")
def bot_page():
    return render_template("/bot.html")
    # except Exception as exc:
    #     logging.exception("Could not load template: {}".format(
    #         str(exc)
    #     ))
    #     return "Not found", 404


@app.get("/scripts/<script_name>")
def fetch_script_name(script_name):
    return send_file(
        "static/js/{}".format(
                script_name
            )
        )


@app.get("/css/<stylesheet_name>")
def fetch_stylesheet_name(stylesheet_name):
    return send_file(
        "static/css/{}".format(
                stylesheet_name
            )
        )


@app.get("/img/<image_name>")
def fetch_image_name(image_name):
    return send_file(
        "static/img/{}".format(
                image_name
            )
        )


@app.get("/")
def return_root_path():
    return render_template("/home.html")


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
