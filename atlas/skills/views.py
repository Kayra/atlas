# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.shortcuts import render, redirect

# from .forms import UserForm
from .models import Skill, Task, Days


def skillProgressView(request):

    if request.user.is_authenticated():
        # Pull all tasks for user
        # Pull all skills for user
        # Run progress utility methods
        # Return object and pass it to the template to be displayed
        return render(request, 'skills/skill_progress.html')

    else:
        return redirect('account_login')


def skillOverview(request):

    if request.user.is_authenticated():
        # Pull all tasks for user
        # Pull all skills for user
        # Pass them to the template to be displayed
        return render(request, 'skills/skill_overview.html')

    else:
        return redirect('account_login')


# Save one skill for user
# Save multiple tasks for user
def skillSetupView(request):

    if request.user.is_authenticated():
        currentUser = request.user
        # try:
        #     skill = Skill.objects.get(user_id=currentUser.id)[0]
        #     return redirect('overview')
        # except IndexError:
        #     return render(request, 'skills/skill_setup.html')

        if Skill.objects.filter(user_id=currentUser.id)[0]:
            return redirect('skills:overview')
        else:
            return render(request, 'skills/skill_setup.html')

    else:
        return redirect('account_login')


def skillListView(request):

    if request.user.is_authenticated():
        # Pull all tasks for user
        # Run list utility methods
        # Return dictionary containing tasks and times to be displayed
        return render(request, 'skills/skill_list.html')

    else:
        return redirect('account_login')
