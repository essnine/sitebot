
function load_bot() {
    var botui = new BotUI('sitebot');
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
        });
    });
}


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
