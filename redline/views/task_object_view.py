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
        try:
            return Task.objects.get(id=id)
        except Task.DoesNotExist:
            return None

    def get(self, request, version, id, format=None):
        task = self.get_object(id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, version, id, format=None):
        task = self.get_object(id)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, version, id, format=None):
        task = self.get_object(id)
        if task:
            task.delete()
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_404_NOT_FOUND)
