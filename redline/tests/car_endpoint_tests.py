"""
Module to test car endpoints in the redline app
"""
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token
from rest_framework.views import status
from django.urls import reverse
from django.contrib.auth.models import User


class BaseViewTest(APITestCase):
    client = APIClient()

    def setUp(self):
        User.objects.create_user(username="jsmith",
                                 email="jsmith@unh.edu",
                                 password="abc123",
                                 first_name="John",
                                 last_name="Smith")
        post_data = {
            'username': 'jsmith',
            'password': 'abc123'
        }
        response = self.client.post(
            reverse("auth", kwargs={'version': 'v1'}),
            post_data,
            format='json'
        )


class CarEndpointTest(BaseViewTest):
    def test_get_action(self):

        self.assertEquals(True, False)

    def test_post_single_car(self):
        """
        This test ensure that a car is successfully added
        when we make a POST request to the cars/ endpoint
        """
        user_id = User.objects.get(username='jsmith').id

        post_data = {
            'user_id': user_id,
            'vin': 'abc123',
            'year': '2013',
            'make': 'Toyota',
            'model': 'Corolla',
            'color': 'White'
        }

        token = Token.objects.get(user__username='jsmith')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        # hit the API endpoint
        response = self.client.post(
            reverse("cars", kwargs={'version': 'v1'}),
            post_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_action(self):

        self.assertEquals(True, False)

    def test_put_action(self):

        self.assertEquals(True, False)
