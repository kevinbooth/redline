"""
Module to take care of the GET, PUT, and POST actions for the Task resource.
"""
from redline.models import Task
from redline.serializers import TaskSerializer, TaskPostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TaskObjectView(APIView):
    """
    This class handles GET, PUT, and DELETE actions for the Task resource.
    GET - Retrieves a single Task
    PUT - Updates a single Task
    DELETE - Removes a Task from the list
    """

    def get_object(self, id):
        """
        This method takes care of the get_object action for the task resource.
        """
        try:
            return Task.objects.get(id=id)
        except Task.DoesNotExist:
            return None

    def get(self, request, id, format=None):
        """
        This method takes care of the get action for the task resource.
        """
        task = self.get_object(id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        """
        This method takes care of the put action for the task resource.
        """
        task = self.get_object(id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        """
        This method takes care of the delete action for the task resource.
        """
        task = self.get_object(id)
        if task:
            task.delete()
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_404_NOT_FOUND)
