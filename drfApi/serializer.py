from rest_framework import serializers
from .models import Tasks, User


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    tasks = TasksSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "tasks"]
