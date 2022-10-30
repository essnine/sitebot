var botui = new BotUI('sitebot');
var hostURL = window.location.host;
const socket = io(
    hostURL+"/botMessage",
    {
        reconnectionDelayMax: 10000,
    }
); // imported in bot.html

socket.connect();

const responses = {
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

function load_bot() {
    botui.message.add({
        content: 'Hello There!'
    }).then(function () { // wait till its shown
        botui.message.add({ // show next message
            content: 'How are you?'
        });
    }).then(function () { // wait till its shown
        botui.action.text({ // show next message
            action: {
                placeholder: 'Say something',
            }
        }).then(function (res) {
            checkResponse(res);
        });
    });
}

function setResponseAndAddAction(res) {
    botui.message.add({
        content: res
    }).then(function () { // wait till its shown
        botui.action.text({ // show next message
            action: {
                placeholder: 'Say something',
            }
        }).then(function (res) {
            checkResponse(res);
            socket.emit(
                "userMessage",
                {
                    "message": res
                }
            )
        });
    });
}

function checkResponse(res) {
    var resp = responses[res.value];
    console.log(resp);
    if (resp == null) {
        resp = "Unknown value"
    }
    setResponseAndAddAction(resp);
}


socket.on("botResponse", (data) => {
    setResponseAndAddAction(data.message)
    }
);


function toggleButton() {
    chatWin = document.getElementById("chatWindow");
    toggleMap = {
        "block": "none",
        "none": "block"
    }
    chatWin.style.display = toggleMap[chatWin.style.display];
}


function detectmob() {
    if (
        navigator.userAgent.match(/Android/i)
        || navigator.userAgent.match(/webOS/i)
        || navigator.userAgent.match(/iPhone/i)
        || navigator.userAgent.match(/iPad/i)
        || navigator.userAgent.match(/iPod/i)
        || navigator.userAgent.match(/BlackBerry/i)
        || navigator.userAgent.match(/Windows Phone/i)
    ) {
        chatWin.style.display = "none";
    } else {
        chatWin.style.display = "block";
    }
}


function onStart() {
    load_bot();
    detectmob();
}
