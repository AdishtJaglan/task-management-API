from django.urls import path
from .views import TaskOperations, UserOperations

urlpatterns = [
    path("tasks/", TaskOperations.as_view(), name="TaskOperations"),
    path("users/", UserOperations.as_view(), name="UserOperations"),
]
