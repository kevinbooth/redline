"""
Module to test part endpoints in the redline app
"""
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.urls import reverse
from redline.models import Part
from redline.serializers import PartSerializer, PartPostSerializer


class BaseViewTest(APITestCase):
    """
    Class used to test the part endpoints in the redline app.
    """
    client = APIClient()

    def setUp(self):
        """
        Used to create a user with a car and a task for testing purposes.
        """
        ()


class PartEndpointTest(BaseViewTest):
    def test_post_action(self):
        """
        This test ensure that a part is successfully added
        when we make a POST request to the part/ endpoint
        """

        self.assertEquals(True, False)

    def test_put_action(self):
        """
        This test ensure that a part is successfully added
        when we make a POST request to the part/ endpoint
        """

        self.assertEquals(True, False)

    def test_get_action(self):
        """
        This test ensures that all the parts for this account
        are returned without any issues.
        """

        self.assertEquals(True, False)

    def test_delete_action(self):
        """
        This test ensures that a part is deleted from a car.
        """

        self.assertEquals(True, False)
