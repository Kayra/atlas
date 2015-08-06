from rest_framework import serializers

from .models import Skill, Task, Days


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('name',)


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('name', 'completion_time',)


class DaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Days
        fields = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',)
