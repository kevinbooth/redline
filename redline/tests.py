""" Used to test each function of the Redline API"""
import pdb
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Car
from .serializers import UserSerializer, CarSerializer
from django.contrib.auth.models import User


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_car(vin='',year='',make='', model='', color=''):
            if vin != '' and year != '' and make != '' and model != '' and color != '':
                Car.objects.create(vin=vin, year=year, make=make, model=model, color=color)

    def setUpCar(self):
        self.create_car('JTMYFREVXD5002907', '2006', 'Subaru', 'Outback', 'Black')
        self.create_car('3GNGC26U45G236804', '1995', 'GMC', 'Sierra', 'Green')
        self.create_car('1GNDV13E03D183789', '2018', 'Tesla', 'Model S', 'White')

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

class CarObjectEndpointTest(BaseViewTest):
    def test_get_action(self):
        """
        This test ensures that a single car object can be retrieved
        from the car/<uuid> endpoint
        """
    first_car = Car.objects.first()
    uuid = first_car.uuid
    response = self.client.get(
        reverse("car-object", kwargs={"version": "v1", 'uuid': uuid})
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    expected = car_user
    serialized = CarSerializer(expected)
    self.assertEqual(response.data, serialized.data)

    def test_put_action(self):
        """
        This test ensures that a single car object can be updated
        from the car/<uuid> endpoint
        """
        first_car = Car.objects.first()
        uuid = first_car.uuid
        self.assertEqual('JTMYFREVXD5002907', first_car.vin)
        put_data = {'vin': 'JTMYFREVXD5002907', 'year': '2006', 'make': 'Subaru', 'model': 'Outback', 'color': 'Black'}
        response = self.client.put(
            reverse("car-object", kwargs={'version': 'v1', 'uuid': uuid}),
            put_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        first_car = Car.objects.first()
        self.assertEqual('JTMYFREVXD5002907', first_car.vin)
