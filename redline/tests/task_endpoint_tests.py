"""
Module to test task endpoints in the redline app
"""
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework.views import status
from django.urls import reverse
from django.contrib.auth.models import User
from redline.models import Car, Task


class BaseViewTest(APITestCase):
    """
    Class used to test the task endpoints in the redline app.
    """
    client = APIClient()
    car_post_data = {}
    task_post_data = {}
    car_id = 0
    user_id = 0

    def setUp(self):
        """
        Used to create a user with a car and a task for testing purposes.
        """
        User.objects.create_user(username="jsmith",
                                 email="jsmith@unh.edu",
                                 password="abc123",
                                 first_name="John",
                                 last_name="Smith")
        user_post_data = {
            'username': 'jsmith',
            'password': 'abc123'
        }
        response = self.client.post(
            reverse("auth", kwargs={'version': 'v1'}),
            user_post_data,
            format='json'
        )

        self.user_id = User.objects.get(username='jsmith').id
        token = Token.objects.get(user__username='jsmith')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        self.car_post_data = {
            'user_id': self.user_id,
            'vin': 'abc1234567890',
            'year': '2013',
            'make': 'Toyota',
            'model': 'Corolla',
            'color': 'White'
        }

        response = self.client.post(
            reverse("cars", kwargs={'version': 'v1'}),
            self.car_post_data,
            format='json'
        )

        self.car_id = Car.objects.get(vin='abc1234567890').id

        self.task_post_data = {
            "car_id": self.car_id,
            "name": "Change oil",
            "estimated_hours": 1,
            "due_date": "2019-05-15",
            "completion_date": None,
            "notes": "Get high viscosity oil"
        }

        response = self.client.post(
            reverse("cars", kwargs={'version': 'v1'}),
            self.car_post_data,
            format='json'
        )


class TaskEndpointTest(BaseViewTest):
    def test_get_action(self):
        """
        This test ensures that all the tasks for this account
        are returned without any issues.
        """

        response = self.client.get(
            reverse("tasks", kwargs={'version': 'v1', 'id': self.car_id}),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_action(self):
        """
        This test ensure that a task is successfully added
        when we make a POST request to the tasks/ endpoint
        """

        response = self.client.post(
            reverse("tasks", kwargs={'version': 'v1', 'id': self.car_id}),
            self.task_post_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_action(self):
        """
        This test ensures that a task is deleted from a user.
        """
        self.client.post(
            reverse("tasks", kwargs={'version': 'v1', 'id': self.car_id}),
            self.task_post_data,
            format='json'
        )

        task_id = Task.objects.get(car_id=self.car_id).id

        response = self.client.delete(
            reverse("task", kwargs={'version': 'v1', 'id': task_id}),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_action(self):
        """
        This test ensure that a task is successfully added
        when we make a POST request to the task/ endpoint
        """
        self.client.post(
            reverse("tasks", kwargs={'version': 'v1', 'id': self.car_id}),
            self.task_post_data,
            format='json'
        )

        task_id = Task.objects.get(car_id=self.car_id).id

        response = self.client.put(
            reverse("task", kwargs={'version': 'v1', 'id': task_id}),
            self.task_post_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
