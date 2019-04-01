""" Used to test each function of the Redline API"""
import pdb

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import User, Car
from .serializers import UserSerializer. CarSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(user_name='',first_name='',last_name=''):
        if first_name != '' and last_name != '' and user_name != '':
            Pilot.objects.create(user_name=user_name, first_name=first_name, last_name=last_name)

    def setUp(self):
        self.create_user('atoscano199', 'Anthony', 'Toscano')
        self.create_user('kevinbooth', 'Kevin', 'Booth')
        self.create_user('EZombek', 'Ethan', 'Jarzombek')

class UserEndpointTest(BaseViewTest):
    def test_get_action(self):
        """
        This test ensure that all users added in the setUp method
        exist when we make a GET request to the user/ endpoint
        """
    response = self.client.get(
        reverse("user", kwargs={"version": "v1"})
    )
    expected = User.objects.all()
    serialized = UserSerializer(expected, many=True)
    self.assertEqual(response.data, serialized.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    
