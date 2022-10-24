function load_bot() {
    var botui = new BotUI('essnine-sitebot');
    botui.message.add({
        content: 'Hello There!'
    }).then(function () { // wait till its shown
        botui.message.add({ // show next message
            content: 'How are you?'
        });
    });
}