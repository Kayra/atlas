from datetime import datetime
import time
import random

from .models import Skill, Task, Days, List, ListTask

from .utility import allTasks


def createList(user):

    list = List(user=user)
    list.save()
    generateTasks(user, list)


def generateTasks(user, list):

    days = Days.objects.get(user=user)
    today = datetime.now().strftime("%A").lower()

    minutesToday = getattr(days, today).seconds / 60
    minutes = 0

    tasks = allTasks(user)
    shortestTask = tasks[0].completion_time.seconds / 60

    # timeOut = time.time() + 0.1
    # If a task can still be added to today's list
    while shortestTask + minutes < minutesToday:

        random.shuffle(tasks)
        for task in tasks:

            taskMinutes = task.completion_time.seconds / 60

            if taskMinutes < shortestTask:
                shortestTask = taskMinutes

            try:
                listTask = ListTask.objects.get(name=task.name, list__user=user, list__date=datetime.now())
                listTask.multiplier += 1
                listTask.save()

            except ListTask.DoesNotExist:
                listTask = ListTask(name=task.name, completion_time=task.completion_time, list=list)
                listTask.save()

            minutes += taskMinutes

        # if time.time() > timeOut:
        #     break

