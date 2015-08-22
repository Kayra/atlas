from datetime import datetime, date


def timeToSeconds(time):

    timeZero = datetime.now().time().replace(hour=0, minute=0, second=0, microsecond=0)

    seconds = datetime.combine(date.today(), time) - datetime.combine(date.today(), timeZero)

    return seconds.seconds
