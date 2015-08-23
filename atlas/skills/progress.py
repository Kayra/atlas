from __future__ import division


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

            minutes = task.completion_time.seconds / 60

            totalTime += task.times_completed * minutes

        return totalTime

    def mostCompleted(self, tasks):

        highest = tasks[0]

        for task in tasks:

            if self.taskCompletedCheck(task) and highest.times_completed < task.times_completed:
                highest = task

            elif highest.times_completed == 0:
                highest.name = "None"

        return highest.name

    def leastCompleted(self, tasks):

        lowest = tasks[0]

        for task in tasks:

            if self.taskCompletedCheck(task) and lowest.times_completed > task.times_completed:
                lowest = task

            elif lowest.times_completed == 0:
                lowest.name = "None"

        return lowest.name

    def taskCompletedCheck(self, task):
        return task.times_completed > 0

    def __init__(self, tasks):
        self.completionRate = self.completionRate(tasks)
        self.totalTime = self.totalTime(tasks)
        self.mostCompleted = self.mostCompleted(tasks)
        self.leastCompleted = self.leastCompleted(tasks)
        self.skillName = tasks[0].skill
