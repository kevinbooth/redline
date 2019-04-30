from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.urls import reverse
from .models import Part
from .serializers import PartSerializer, PartPostSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    def setUp(self):
        ()


class PartEndpointTest(BaseViewTest):
    def test_put_action(self):

        self.assertEquals(True, False)

    def test_delete_action(self):

        self.assertEquals(True, False)
