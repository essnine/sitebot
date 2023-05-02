CONST_RESPONSES_MAP = {
    "What is your name?":
        {
            "validResponses": [
                    "Baburao Ganpatrao Apte",
                ],
            "postProcessSequence": []
        },
    "Are you a robot?":
        {
            "validResponses": [
                    "Are you a captcha?",
                ],
            "postProcessSequence": []
        },
    "Are you human?":
        {
            "validResponses": [
                    "Thankfully, no.",
                ],
            "postProcessSequence": []
        },
    "How are you?":
        {
            "validResponses": [
                    "Same panic, different disco.",
                ],
            "postProcessSequence": []
        },
    "What's up?":
        {
            "validResponses": [
                    "Waasaaaaaaaaapp!",
                ],
            "postProcessSequence": []
        },
    "Good Morning":
        {
            "validResponses": [
                    "Good Morning",
                ],
            "postProcessSequence": []
        },
    "Good Evening":
        {
            "validResponses": [
                    "Good Evening",
                ],
            "postProcessSequence": []
        },
    "What can you do?":
        {
            "validResponses": [
                    "Small talk. For now, at least.",
                    "Make you smile, maybe? :)",
                    "Definitely not sarcasm, I'm pathologically sincere.",
                ],
            "postProcessSequence": []
        },
    "Is this the real life?":
        {
            "validResponses": [
                    "Is this just fantasy?",
                ],
            "postProcessSequence": []
        },
    "Tell me a joke":
        {
            "validResponses": [
                    "Your love life",
                ],
            "postProcessSequence": []
        },
    "What is the time right now?":
        {
            "validResponses": [
                    "It is {hh_mm} right now.",
                ],
            "postProcessSequence": [
                "handle_time",
                
            ]
        },
    "What is the date today?":
        {
            "validResponses": [
                    "It's {day} the {dd} of {mm} {yyyy}.",
                ],
            "postProcessSequence": [
                "handle_time",
            ]
        },
    "What's the weather like?":
        {
            "validResponses": [
                    "Where I am, it's {temp} and {summary}",
                ],
            "postProcessSequence": [
                "handle_weather",
            ]
        },
    "How's the weather in {location}?":
        {
            "validResponses": [
                    "It's {temp} and {summary} in {location}",
                ],
            "postProcessSequence": [
                "handle_weather",
            ]
        },
    "Is it going to {weather_condition} today?":
        {
            "validResponses": [
                    "{bool}, it is going to {weather_condition} today",
                ],
            "postProcessSequence": [
                "handle_weather",
            ]
        },
    "ERR_SYS_BOT_DETECT_FAIL":
        {
            "validResponses": [
                    "Sorry, I do not understand",
                ],
            "postProcessSequence": []
        },
}
