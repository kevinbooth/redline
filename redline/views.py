from django.shortcuts import render
from .models import Car, Task
from .serializers import CarSerializer, TaskSerializer
from .serializers import CarPostSerializer, TaskPostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class View(APIView):
    """
    This class handles the GET and POST actions for the Task resource.
    GET - Retrieves a list of all the Tasks
    POST - Creates a new Task
    """
    def get(self, request, version, format=None):
        parts = task.objects.all()
        serializer = TaskSerializer(parts, many=True)
        return Response(serializer.data)

    def post(self, request, version, format=None):
        serializer = TaskPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        serializer = TaskSerializer(part)
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
