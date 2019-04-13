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
    def test_post_action(self):
        self.assertEquals(True, False)
