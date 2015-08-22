from .models import Task, Skill


def allTasks(user):

    skills = Skill.objects.filter(user=user)

    tasks = []
    for skill in skills:
        skillTasks = Task.objects.filter(skill=skill)
        for task in skillTasks:
            tasks.append(task)

    return tasks
