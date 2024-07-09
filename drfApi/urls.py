from django.urls import path
from .views import TaskOperations, UserOperations

urlpatterns = [
    path("tasks/", TaskOperations.as_view(), name="TaskOperations"),
    path("tasks/<int:pk>/", TaskOperations.as_view(), name="TaskDetailOperations"),
    path("users/", UserOperations.as_view(), name="UserOperations"),
    path("users/<int:pk>/", UserOperations.as_view(), name="UserDetailOperations"),
]
