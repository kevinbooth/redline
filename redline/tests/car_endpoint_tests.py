"""
Module to test car endpoints in the redline app
"""
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework.views import status
from django.urls import reverse
from django.contrib.auth.models import User
from redline.models import Car


class BaseViewTest(APITestCase):
    client = APIClient()
    car_post_data = {}
    user_id = 0

    def setUp(self):
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
        self.car_post_data = {
            'user_id': self.user_id,
            'vin': 'abc1234567890',
            'year': '2013',
            'make': 'Toyota',
            'model': 'Corolla',
            'color': 'White'
        }
        token = Token.objects.get(user__username='jsmith')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        response = self.client.post(
            reverse("cars", kwargs={'version': 'v1'}),
            self.car_post_data,
            format='json'
        )


class CarEndpointTest(BaseViewTest):
    def test_get_action(self):
        """
        This test ensures that all the cars for this account
        are returned without any issues.
        """

        response = self.client.get(
            reverse("cars", kwargs={'version': 'v1'}),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_single_car(self):
        """
        This test ensure that a car is successfully added
        when we make a POST request to the cars/ endpoint
        """

        response = self.client.post(
            reverse("cars", kwargs={'version': 'v1'}),
            self.car_post_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_action(self):
        """
        This test ensures that a car is deleted from a user.
        """
        car_id = Car.objects.get(vin='abc1234567890').id

        response = self.client.delete(
            reverse("car", kwargs={'version': 'v1', 'id': car_id}),
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_action(self):
        """
        This test ensure that a car is successfully added
        when we make a POST request to the cars/ endpoint
        """
        car_id = Car.objects.get(vin='abc1234567890').id

        response = self.client.put(
            reverse("car", kwargs={'version': 'v1', 'id': car_id}),
            self.car_post_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
