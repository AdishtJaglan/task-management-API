from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from .models import Tasks, User
from .serializer import TasksSerializer, UserSerializer


class TaskOperations(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                return Response(
                    {"error": str(e)},
                    serializer.data,
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        pk = request.query_params.get("pk")
        try:
            if pk:
                tasks = get_object_or_404(Tasks, pk=pk)
                serializer = TasksSerializer(tasks)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                tasks = Tasks.objects.all()
                serializer = TasksSerializer(tasks, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return ResourceWarning(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request):
        pk = request.query_params.get("pk")

        try:
            task = get_object_or_404(Tasks, pk=pk)
            seriliazer = TasksSerializer(task, data=request.data)
            if seriliazer.is_valid():
                seriliazer.save()
                return Response(seriliazer.data, status=status.HTTP_205_RESET_CONTENT)
            return Response(seriliazer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def patch(self, request):
        pk = request.query_params.get("pk")

        try:
            task = get_object_or_404(Tasks, pk=pk)
            serializer = TasksSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request):
        pk = request.query_params.get("pk")

        try:
            task = get_object_or_404(Tasks, pk=pk)
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserOperations(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                return Response(
                    {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        pk = request.query_params.get("pk")

        try:
            if pk:
                user = get_object_or_404(User, pk=pk)
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                users = User.objects.all()
                serializer = UserSerializer(users, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request):
        pk = request.query_params.get("pk")

        try:
            user = get_object_or_404(User, pk=pk)
            serializer = UserSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def patch(self, request):
        pk = request.query_params.get("pk")

        try:
            user = get_object_or_404(User, pk=pk)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request):
        pk = request.query_params.get("pk")

        try:
            user = get_object_or_404(User, pk=pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserTasks(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pk = request.query_params.get("pk")

        if pk:
            user = get_object_or_404(User, id=pk)
            tasks = Tasks.objects.filter(user=user)
            serializer = TasksSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "pk is missing in params"}, status=status.HTTP_400_BAD_REQUEST
        )
