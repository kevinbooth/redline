from .models import Car, Task
from .serializers import CarSerializer, TaskSerializer
from .serializers import CarPostSerializer, TaskPostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CarView(APIView):
    """
    This class handles the GET and POST actions for the Car resource.
    GET - Retrieves a list of all Cars
    POST - Creates a new car
    """
    def get(self, request, version, format=None):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request, version, format=None):
        serializer = CarPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarObjectView(APIView):
    """
    This class handles GET, PUT, and DELETE actions for the Car resource.
    GET - Retrieves a single car
    PUT - Updates a single cars information
    DELETE - Removes a car from the list
    """
    def get_object(self, id):
        try:
            return Car.objects.get(id=id)
        except Car.DoesNotExist:
            return None

    def get(self, request, version, id, format=None):
        car = self.get_object(id)
        serializer = CarSerializer(car)
        return Response(serializer.data)

    def put(self, request, version, id, format=None):
        car = self.get_object(id)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, version, id, format=None):
        car = self.get_object(id)
        if car:
            car.delete()
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_404_NOT_FOUND)


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
