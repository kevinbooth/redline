
import pdb

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import User
from .serializers import UserSerializer

class UserCreationTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(first_name='',
                     last_name=''
                     ):
        if first_name != '' and last_name != '':
            User.objects.create(first_name=first_name, last_name=last_name)

    def setUp(self):
        self.create_user('Anthony', 'Toscano')
        self.create_user('Kevin', 'Booth')
        self.create_user('Ethan', 'Jarzombek')
