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
