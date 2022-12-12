var botui = new BotUI('sitebot');
var hostURL = window.location.host;
const chatWin = document.getElementById("chatWindow");
const socket = io(
    hostURL+"/botMessage",
    {
        reconnectionDelayMax: 10000,
    }
); // imported in bot.html

socket.connect();


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
            // checkResponse(res);
            socket.emit(
                "userMessage",
                {
                    "message": res
                }
            )
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
            // checkResponse(res);
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
        setResponseAndAddAction(data.message);
    }
);


function toggleButton() {
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
