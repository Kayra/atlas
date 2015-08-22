from datetime import datetime

from .models import Skill, Task, Days, List, ListTask

from .utility import timeToSeconds

def createList(user):

    list = List(user=user)
    tasks = selectTasks(user)


def selectTasks(user):

    days = Days.objects.get(user=user)
    today = datetime.now().strftime("%A").lower()

    hours = getattr(days, today)

    print type(timeToSeconds(hours))
