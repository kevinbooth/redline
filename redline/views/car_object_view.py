from redline.models import Car, Task
from redline.serializers import CarSerializer, CarPostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CarObjectView(APIView):
    """
    This class handles GET, PUT, and Delete actions for the Car resource.
    GET - Retrieves a single car
    PUT - Updates a single cars information
    Delete - Removes a car from the list
    """
    def get_object(self, id):
        try:
            return Car.objects.get(id=id)
        except Car.DoesNotExist:
            return None

    def get(self, request, id, format=None):
        car = self.get_object(id)
        open_task_count = Task.objects.filter(
                                              car_id=id,
                                              completion_date=None
                                              ).count()
        serializer = CarSerializer(car)
        data = dict(serializer.data)
        data['open_task_count'] = open_task_count
        return Response(data)

    def put(self, request, id, format=None):
        car = self.get_object(id)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        car = self.get_object(id)
        if car:
            car.delete()
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_404_NOT_FOUND)
