from urllib import response
import eventlet
eventlet.monkey_patch(socket=True, thread=True)
from flask import Flask, render_template, send_file
from flask_socketio import SocketIO
import logging


RESPONSES = {
    "What is your name?": "Baburao Ganpatrao Apte",
    "Are you a robot?": "Are you a captcha?",
    "Are you human?": "Thankfully, no.",
    "How are you?": "Same panic, different disco.",
    "What's up?": "Waasaaaaaaaaapp!",
    "Good Morning": "Good Morning",
    "Good Evening": "Good Evening",
    "What can you do?": "Small talk. For now, at least.",
    "Is this the real life?": "Is this just fantasy? ",
    "Tell me a joke": "Your love life",
    "What is the time right now?": "It is {time_val} {am_pm} right now.",
    "What is the date today?": "It's {day} the {dd} of {mm} {yyyy}. ",
    "How's the weather like?": "it's {temp} and {summary}",
    "How's the weather in {location}?": "it's {temp} and {summary} in {location} ",
    "Is it going to {weather condition} today?": "Boolean based on current weather condition of default or given location"
}


app = Flask(
    import_name=__name__,
    template_folder="static/html",
)
socket_app = SocketIO(app, async_mode="eventlet", namespaces=["botMessage"])


@socket_app.on("connect", namespace="botMessage")
def handle_connect(sid):
    logging.info("Socket connected: {}".format(sid))


@socket_app.on("userMessage", namespace="botMessage")
def handle_user_message(sid, data):
    logging.debug(data)
    message = data.get("message")
    response = RESPONSES.get(message, "Sorry, I do not understand")
    socket_app.emit("botResponse", {"message": response})


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
