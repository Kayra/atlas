

def completionRate(tasks):

    totalCompleted = 0
    totalListed = 0

    for task in tasks:
        totalCompleted += task.times_completed
        totalListed += task.times_listed

    try:
        return (totalCompleted/totalListed) * 100

    except ZeroDivisionError:
        return 0


def totalTime(tasks):

    totalTime = 0

    for task in tasks:
        totalTime += task.times_completed * tasks.completion_time

    return totalTime


def mostCompleted(tasks):

    highest = tasks[0]

    for task in tasks:
        if highest.times_completed < ((task.times_completed/task.times_listed) * 100):
            highest = task

    return highest.name


def leastCompleted(tasks):

    lowest = tasks[0]

    for task in tasks:
        if lowest.times_completed > ((task.times_completed/task.times_listed) * 100):
            lowest = task

    return lowest.name
