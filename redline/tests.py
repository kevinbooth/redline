""" Used to test each function of the Redline API"""
import pdb

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import User, Car
from .serializers import UserSerializer, CarSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(user_name='',first_name='',last_name=''):
        if first_name != '' and last_name != '' and user_name != '':
            User.objects.create(user_name=user_name, first_name=first_name, last_name=last_name)
    @staticmethod
    def create_car(vin='',year='',make='', model='', color=''):
            if vin != '' and year != '' and make != '' and model != '' and color != '':
                Car.objects.create(vin=vin, year=year, make=make, model=model, color=color)

    def setUpUser(self):
        self.create_user('atoscano199', 'Anthony', 'Toscano')
        self.create_user('kevinbooth', 'Kevin', 'Booth')
        self.create_user('EZombek', 'Ethan', 'Jarzombek')

    def setUpCar(self):
        self.create_car('JTMYFREVXD5002907', '2006', 'Subaru', 'Outback', 'Black')
        self.create_car('3GNGC26U45G236804', '1995', 'GMC', 'Sierra', 'Green')
        self.create_car('1GNDV13E03D183789', '2018', 'Tesla', 'Model S', 'White')

class UserEndpointTest(BaseViewTest):
    def test_get_action(self):
        """
        This test ensure that all users added in the setUpUser method
        exist when we make a GET request to the user/ endpoint
        """
    response = self.client.get(
        reverse("user", kwargs={"version": "v1"})
    )
    expected = User.objects.all()
    serialized = UserSerializer(expected, many=True)
    self.assertEqual(response.data, serialized.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_action(self):
        """
        This test ensures that a new user can be created via a POST request
        to the user/ endpoint
        """
    post_data = {'user_name': 'atoscano199', 'first_name': 'Anthony', 'last_name': 'Toscano'}
    response = self.client.post(
            reverse("user", kwargs={'version': 'v1'}),
            post_data,
            format='json'
        )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CarEndpointTest(BaseViewTest):
    def test_get_action(self):
        """
        This test ensure that all cars added in the setUpCar method
        exist when we make a GET request to the car/ endpoint
        """
    response = self.client.get(
        reverse("car", kwargs={"version": "v1"})
    )
    expected = Car.objects.all()
    serialized = CarSerializer(expected, many=True)
    self.assertEqual(response.data, serialized.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_action(self):
        """
        This test ensures that a new car can be created via a POST request
        to the car/ endpoint
        """
    post_data = {'vin': 'JTMYFREVXD5002907', 'year': '2006', 'make': 'Subaru', 'model': 'Outback', 'color': 'Black'}
    response = self.client.post(
            reverse("car", kwargs={'version': 'v1'}),
            post_data,
            format='json'
        )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserObjectEndpointTest(BaseViewTest):
    def test_get_action(self):
        """
        This test ensures that a single user object can be retrieved
        from the user/<uuid> endpoint
        """
    first_user = User.objects.first()
    uuid = first_user.uuid
    response = self.client.get(
        reverse("user-object", kwargs={"version": "v1", 'uuid': uuid})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    expected = first_user
    serialized = UserSerializer(expected)
    self.assertEqual(response.data, serialized.data)

    def test_put_action(self):
        """
        This test ensures that a single user object can be updated
        from the user/<uuid> endpoint
        """
        first_user = User.objects.first()
        uuid = first_user.uuid
        self.assertEqual('Toscano', first_user.last_name)
        put_data = {'first_name': 'Anthony', 'last_name': 'Toscano'}
        response = self.client.put(
            reverse("user-object", kwargs={'version': 'v1', 'uuid': uuid}),
            put_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        first_user = User.objects.first()
        self.assertEqual('Toscano', first_user.last_name)
