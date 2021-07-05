from stackapi import StackAPI
from datetime import datetime, timedelta

def get_dates():
    today = datetime.now()
    day_before_yesterday = today - timedelta(days=2)
    today = round(today.timestamp())
    day_before_yesterday = round(day_before_yesterday.timestamp())
    return today, day_before_yesterday


def stack_q():
    SITE = StackAPI('stackoverflow')
    questions = SITE.fetch(
        'questions',
        fromdate=get_dates()[1],
        todate=get_dates()[0],
        tagged='python',
        sort='creation')
    return questions