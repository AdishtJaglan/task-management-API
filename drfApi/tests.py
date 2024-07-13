from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from .models import User, Tasks
from rest_framework_simplejwt.tokens import RefreshToken


class UserOperationsTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

    def test_create_user(self):
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpass123",
        }
        response = self.client.post(reverse("UserOperations"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], data["username"])

    def test_get_users(self):
        response = self.client.get(reverse("UserOperations"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_user(self):
        response = self.client.get(reverse("UserOperations") + f"?pk={self.user.pk}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], self.user.username)

    def test_update_user(self):
        data = {
            "username": "updateduser",
            "email": "updateduser@example.com",
            "password": "updatedpass123",
        }
        response = self.client.put(
            reverse("UserOperations") + f"?pk={self.user.pk}", data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)

    def test_delete_user(self):
        response = self.client.delete(reverse("UserOperations") + f"?pk={self.user.pk}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TaskOperationsTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        self.task = Tasks.objects.create(
            title="Test Task", description="Test Description", user=self.user
        )
        self.token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

    def test_create_task(self):
        data = {
            "title": "New Task",
            "description": "New Description",
            "user": self.user.pk,
        }
        response = self.client.post(reverse("TaskOperations"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], data["title"])

    def test_get_tasks(self):
        response = self.client.get(reverse("TaskOperations"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_task(self):
        response = self.client.get(reverse("TaskOperations") + f"?pk={self.task.pk}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.task.title)

    def test_update_task(self):
        data = {
            "title": "Updated Task",
            "description": "Updated Description",
            "user": self.user.pk,
        }
        response = self.client.put(
            reverse("TaskOperations") + f"?pk={self.task.pk}", data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)

    def test_delete_task(self):
        response = self.client.delete(reverse("TaskOperations") + f"?pk={self.task.pk}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class JWTAuthTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )

    def test_obtain_token(self):
        data = {"username": "testuser", "password": "testpass123"}
        response = self.client.post(reverse("token_obtain_pair"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_refresh_token(self):
        refresh = str(RefreshToken.for_user(self.user))
        data = {"refresh": refresh}
        response = self.client.post(reverse("token_refresh"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
