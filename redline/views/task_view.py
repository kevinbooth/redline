from redline.models import Task
from redline.serializers import TaskSerializer, TaskPostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TaskView(APIView):
    """
    This class handles the GET and POST actions for the Task resource.
    GET - Retrieves a list of all the Tasks for a specified Car
    POST - Creates a new Task
    """
    def get(self, request, id, version, format=None):
        tasks = Task.objects.filter(car_id=id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, id, version, format=None):
        serializer = TaskPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
