from .models import Car
from .serializers import CarSerializer
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


class CarObjectView(APIView):
    """
    This class handles GET and PUT actions for the Car resource.
    GET - Retrieves a single car
    PUT - Updates a single cars information
    DELETE - Removes a car from the list
    """
    def get_object(self, uuid):
        try:
            return Car.objects.get(uuid=uuid)
        except Car.DoesNotExist:
            raise Http404

    def get(self, request, version, uuid, format=None):
        car = self.get_object(uuid)
        serializer = CarSerializer(car)
        return Resonse(serializer.data)

    def post(self, request, version, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, version, uuid, format=None):
        car = self.get_object(uuid)
        serializer = CarSerializer(pilot, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, version, uuid, format=None):
        car = self.get_object(uuid)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
