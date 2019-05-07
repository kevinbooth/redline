# from rest_framework.test import APITestCase, APIClient
# from rest_framework.views import status
# from django.urls import reverse
# from redline.models import Part
# from redline.serializers import PartSerializer, PartPostSerializer


# class BaseViewTest(APITestCase):
#     client = APIClient()
#     part_post_data = {}
#     user_id = 0
#     task_id = 0

#     def setUp(self):
#         User.objects.create_user(username="jsmith",
#                                  email="jsmith@unh.edu",
#                                  password="abc123",
#                                  first_name="John",
#                                  last_name="Smith")
#         user_post_data = {
#             'username': 'jsmith',
#             'password': 'abc123'
#         }
#         response = self.client.post(
#             reverse("auth", kwargs={'version': 'v1'}),
#             user_post_data,
#             format='json'
#         )

#         self.user_id = User.objects.get(username='jsmith').id
#         self.car_post_data = {
#             'user_id': self.user_id,
#             'vin': 'abc1234567890',
#             'year': '2013',
#             'make': 'Toyota',
#             'model': 'Corolla',
#             'color': 'White'
#         }
#         token = Token.objects.get(user__username='jsmith')
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

#         response = self.client.post(
#             reverse("cars", kwargs={'version': 'v1'}),
#             self.car_post_data,
#             format='json'
#         )


# class PartEndpointTest(BaseViewTest):

#     def test_post_action(self):
#         """
#         This test ensure that a part is successfully added
#         when we make a POST request to the part/ endpoint
#         """

#         response = self.client.post(
#             reverse("parts", kwargs={'version': 'v1', 'id': self.task_id}),
#             self.part_post_data,
#             format='json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_put_action(self):
#         """
#         This test ensure that a part is successfully updated
#         when we make a POST request to the part/ endpoint
#         """
#         self.client.post(
#             reverse("tasks", kwargs={'version': 'v1', 'id': self.task_id}),
#             self.part_post_data,
#             format='json'
#         )

#         part_id = Part.objects.get(task_id=self.task_id).id

#         response = self.client.put(
#             reverse("part", kwargs={'version': 'v1', 'id': part_id}),
#             self.part_post_data,
#             format='json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_get_action(self):
#         """
#         This test ensures that all the parts for this task
#         are returned without any issues.
#         """

#         response = self.client.get(
#             reverse("parts", kwargs={'version': 'v1', 'id': self.task_id}),
#             format='json'
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_delete_action(self):
#         """
#         This test ensures that a part is deleted from a task.
#         """
#         self.client.post(
#             reverse("parts", kwargs={'version': 'v1', 'id': self.task_id}),
#             self.part_post_data,
#             format='json'
#         )

#         part_id = Part.objects.get(task_id=self.task_id).id

#         response = self.client.delete(
#             reverse("part", kwargs={'version': 'v1', 'id': part_id}),
#         )
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
