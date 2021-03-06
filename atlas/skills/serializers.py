from rest_framework import serializers

from .models import Skill, Task, Days


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name', 'user')


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'completion_time', 'skill')


class DaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Days
        fields = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'user')
