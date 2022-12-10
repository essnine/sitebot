import logging
import re

from ast import literal_eval
from datetime import datetime as dt
from typing import List

from thefuzz.fuzz import ratio

from constants.responses import CONST_RESPONSES_MAP


class UserMessage():
    def __init__(self, user_query: str):
        self.user_query: str = user_query
        self.possible_responses: str = []
        self.raw_response: str = ""
        self.raw_response_score: float = 0.0
        self.raw_response_entities = []
        self.processed_response: str = ""

    def handle_time(self, entities: list):
        """adds a time value in HH:MM to input string,/
        which has to be formattable

        Args:
            resp_str (str): response to an FAQ usually

        Returns:
            str: same as resp_str but with current time
        """
        current_time = dt.now()
        hh_mm = current_time.strftime("%H:%M")
        day = current_time.day
        dd = current_time.strftime("%d")
        mm = current_time.strftime("%m")
        yyyy = current_time.strftime("%yyyy")
        return literal_eval("")
        return resp_str.format(time_val)

    def handle_weather(self, entities: list):
        weather_component = ""
        pass

    @staticmethod
    def fetch_response_entities(response: str) -> List[str]:
        match_list = []
        try:
            match_list = [i[1:-1] for i in re.findall(r"\{.*?\}", response)]
        except Exception as exc:
            logging.exception("Could not process entities: {}".format(str(exc)))
        return match_list

    def select_answer(self, user_query: str):
        try:
            final_response = CONST_RESPONSES_MAP.get(user_query, False)
            if not final_response:
                possible_response_matches = []
                for possible_match in CONST_RESPONSES_MAP:
                    match_ratio = ratio(user_query, possible_match)
                    if match_ratio >= 80:
                        possible_response_matches.append((possible_match, match_ratio))
                
                possible_response_matches.sort(key=lambda x: x[1], reverse=True)
                final_response = CONST_RESPONSES_MAP[possible_response_matches[1]]
        
        except Exception as exc:
            logging.exception("Error detecting response: {}".format(str(exc)))
            return "Sorry, something seems to have gone wrong"
