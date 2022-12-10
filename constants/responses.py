CONST_RESPONSES_MAP = {
    "What is your name?":
        {
            "validResponses": [
                    "Baburao Ganpatrao Apte",
                ],
            "postProcessSequence": [
                "select_answer",
            ]
        },
    "Are you a robot?":
        {
            "validResponses": [
                    "Are you a captcha?",
                ],
            "postProcessSequence": [
                "select_answer",
            ]
        },
    "Are you human?":
        {
            "validResponses": [
                    "Thankfully, no.",
                ],
            "postProcessSequence": [
                "select_answer",
            ]
        },
    "How are you?":
        {
            "validResponses": [
                    "Same panic, different disco.",
                ],
            "postProcessSequence": [
                "select_answer",
            ]
        },
    "What's up?":
        {
            "validResponses": [
                    "Waasaaaaaaaaapp!",
                ],
            "postProcessSequence": [
                "select_answer",
            ]
        },
    "Good Morning":
        {
            "validResponses": [
                    "Good Morning",
                ],
            "postProcessSequence": [
                "select_answer",
            ]
        },
    "Good Evening":
        {
            "validResponses": [
                    "Good Evening",
                ],
            "postProcessSequence": [
                "select_answer",
            ]
        },
    "What can you do?":
        {
            "validResponses": [
                    "Small talk. For now, at least.",
                    "Make you smile, maybe? :)",
                    "Definitely not sarcasm, I'm pathologically sincere.",
                ],
            "postProcessSequence": [
                "select_answer",
            ]
        },
    "Is this the real life?":
        {
            "validResponses": [
                    "Is this just fantasy?",
                ],
            "postProcessSequence": [
                "select_answer",
            ]
        },
    "Tell me a joke":
        {
            "validResponses": [
                    "Your love life",
                ],
            "postProcessSequence": [
                "select_answer",
            ]
        },
    "What is the time right now?":
        {
            "validResponses": [
                    "It is {hh_mm} right now.",
                ],
            "postProcessSequence": [
                "select_answer",
                "handle_time",
                
            ]
        },
    "What is the date today?":
        {
            "validResponses": [
                    "It's {day} the {dd} of {mm} {yyyy}.",
                ],
            "postProcessSequence": [
                "select_answer",
                "handle_time",
            ]
        },
    "What's the weather like?":
        {
            "validResponses": [
                    "Where I am, it's {temp} and {summary}",
                ],
            "postProcessSequence": [
                "select_answer",
                "handle_weather",
            ]
        },
    "How's the weather in {location}?":
        {
            "validResponses": [
                    "It's {temp} and {summary} in {location}",
                ],
            "postProcessSequence": [
                "select_answer",
                "handle_weather",
            ]
        },
    "Is it going to {weather_condition} today?":
        {
            "validResponses": [
                    "{bool}, it is going to {weather_condition} today",
                ],
            "postProcessSequence": [
                "select_answer",
                "handle_weather",
            ]
        }"
}
