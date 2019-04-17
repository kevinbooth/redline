from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from django.urls import reverse
# from .models import Task
# from .serializers import TaskSerializer, TaskPostSerializer



class BaseViewTest(APITestCase):
    client = APIClient()

    def setUp(self):
        ()


class TaskEndpointTest(BaseViewTest):
    def test_get_action(self):

        self.assertEquals(True, False)

    def test_post_action(self):

        self.assertEquals(True, False)

    def test_delete_action(self):

        self.assertEquals(True, False)

    def test_put_action(self):

        self.assertEquals(True, False)
