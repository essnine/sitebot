# creating this file to help maintain database abstractions
from datetime import datetime
from typing import Union


class UserMessage:
    message_id: str
    message_text: str
    message_time: Union[datetime,str]


class User:
    user_id: int
    user_name: str
    user_last_message: dict
