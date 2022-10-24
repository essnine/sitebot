from datetime import datetime as dt


def populate_time(resp_str: str):
    """adds a time value in HH:MM to input string,/
    which has to be formattable

    Args:
        resp_str (str): response to an FAQ usually

    Returns:
        str: same as resp_str but with current time
    """    
    current_time = dt.now()
    time_val = current_time.strftime("%H:%M")
    return resp_str.format(time_val)
