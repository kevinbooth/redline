from .models import Car, Part
from .serializers import CarSerializer, PartSerializer
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


class PartView(APIView):
    """
    This class handles the GET and POST actions for the Part resource.
    GET - Retrieves a list of all Parts
    POST - Creates a new Part
    """
    def get(self, request, version, format=None):
        parts = Part.objects.all()
        serializer = PartSerializer(parts, many=True)
        return Response(serializer.data)

    def post(self, request, version, format=None):
        serializer = PartPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PartObjectView(APIView):
    """
    This class handles GET, PUT, and DELETE actions for the Part resource.
    GET - Retrieves a single part
    PUT - Updates a single parts information
    DELETE - Removes a part from the list
    """
    def get_object(self, id):
        try:
            return Part.objects.get(id=id)
        except Part.DoesNotExist:
            return None

    def get(self, request, version, id, format=None):
        part = self.get_object(id)
        serializer = PartSerializer(part)
        return Response(serializer.data)

    def put(self, request, version, id, format=None):
        part = self.get_object(id)
        serializer = artSerializer(part, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, version, id, format=None):
        part = self.get_object(id)
        if part:
            part.delete()
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_404_NOT_FOUND)
