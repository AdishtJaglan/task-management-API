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
        fields = ["id", "username", "email", "tasks", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User(
            email=validated_data["email"],
            username=validated_data["username"],
        )
        user.is_active = True
        user.set_password(validated_data["password"])
        user.save()
        return user
