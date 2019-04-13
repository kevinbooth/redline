"""
Module to test endpoints in the account app
"""
from rest_framework.test import APITestCase, APIClient
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


class UserEndpointTest(BaseViewTest):
    """
    Class to test User specific endpoints
    """
    def test_register_user(self):
        """
        This test ensure that a user is successfully registered
        when we make a POST request to the user/register endpoint
        """
        post_data = {
            'username': 'bobsmith',
            'email': 'bsmith@unh.edu',
            'password': 'abc123',
            'first_name': 'Bob',
            'last_name': 'Smith'
        }
        # hit the API endpoint
        response = self.client.post(
            reverse("register", kwargs={'version': 'v1'}),
            post_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
