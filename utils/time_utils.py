from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import sys


# format : [number][amount time] [1,..][d,w,m] for day, week or month
def check_for_valid_time(str_input_amount_time):
    stripped_str = str_input_amount_time.replace(' ', '')
    amount_time = stripped_str[-1:]
    amount_time_valid = (amount_time == 'h' or amount_time == 'd' or amount_time == 'w' or amount_time == 'm')
    number = stripped_str[0:-1]
    if number.isdigit():
        number = int(number)
        if number < 1:
            return None
        now = datetime.now()
        # create timedelta object with difference of 2 weeks
        if amount_time == 'h':
            delta_time = timedelta(hours=number)
        elif amount_time == 'd':
            delta_time = timedelta(days=number)
        elif amount_time == 'w':
            delta_time = timedelta(weeks=number)
        elif amount_time == 'm':
            delta_time = relativedelta(months=+number)
        else:
            return None
        return now + delta_time

    else:
        return None
