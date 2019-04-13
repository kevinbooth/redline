from .models import Car
from .serializers import CarSerializer
from .serializers import CarPostSerializer
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
    This class handles GET and PUT actions for the Car resource.
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
        return Resonse(serializer.data)

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
            return Response(car, status=status.HTTP_200_OK)
        return Response(status.HTTP_404_NOT_FOUND)
