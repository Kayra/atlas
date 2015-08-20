from datetime import time


class Progress:

    def completionRate(self, tasks):

        totalCompleted = 0
        totalListed = 0

        for task in tasks:
            totalCompleted += task.times_completed
            totalListed += task.times_listed

        try:
            return (totalCompleted/totalListed) * 100

        except ZeroDivisionError:
            return 0

    def totalTime(self, tasks):

        totalTime = 0

        for task in tasks:
            print type(task.completion_time)
            totalTime += time(seconds=task.times_completed * task.completion_time.total_seconds())

        return totalTime

    def mostCompleted(self, tasks):

        highest = tasks[0]

        for task in tasks:
            if highest.times_completed < ((task.times_completed/task.times_listed) * 100):
                highest = task

        return highest.name

    def leastCompleted(self, tasks):

        lowest = tasks[0]

        for task in tasks:
            if lowest.times_completed > ((task.times_completed/task.times_listed) * 100):
                lowest = task

        return lowest.name

    def __init__(self, tasks):
        self.completionRate = self.completionRate(tasks)
        self.totalTime = self.totalTime(tasks)
        self.mostCompleted = self.mostCompleted(tasks)
        self.leastCompleted = self.leastCompleted(tasks)
        self.skill = tasks[0].skill
