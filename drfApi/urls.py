from django.urls import path
from .views import TaskOperations, UserOperations
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("tasks/", TaskOperations.as_view(), name="TaskOperations"),
    path("users/", UserOperations.as_view(), name="UserOperations"),
]
