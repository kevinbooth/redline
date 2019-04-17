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
