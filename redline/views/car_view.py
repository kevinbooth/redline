"""
Module to take care of the GET and POST actions for the Car resource.
redline/views/car_view.py
Author: Ethan Jarzombek
Last Updated: 5/7/2019
"""
from redline.models import Car
from redline.serializers import CarSerializer, CarPostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CarView(APIView):
    """
    This class handles the GET and POST actions for the Car resource.
    GET - Retrieves a list of all Cars
    POST - Creates a new car
    """
    def get(self, request, format=None):
        """
        This method takes care of the get action for the car resource.
        """
        cars = Car.objects.filter(user_id=self.request.user.id)
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        This method takes care of the post action for the car resource.
        """
        serializer = CarPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
