"""
Module to take care of the GET, PUT, and DELETE actions for the Part resource.
"""
from redline.models import Part
from redline.serializers import PartSerializer, PartPostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PartObjectView(APIView):
    """
    This class handles GET, PUT, and DELETE actions for the Part resource.
    GET - Retrieves a single part
    PUT - Updates a single parts information
    Delete - Removes a part from the list
    """
    def get_object(self, id):
        """
        This method takes care of the get_object action for the part resource.
        """
        try:
            return Part.objects.get(id=id)
        except Part.DoesNotExist:
            return None

    def get(self, request, id, format=None):
        """
        This method takes care of the get action for the part resource.
        """
        part = self.get_object(id)
        serializer = PartSerializer(part)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        """
        This method takes care of the put action for the part resource.
        """
        part = self.get_object(id)
        serializer = PartSerializer(part, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        """
        This method takes care of the delete action for the part resource.
        """
        part = self.get_object(id)
        if part:
            part.delete()
            return Response(status.HTTP_200_OK)
        return Response(status.HTTP_404_NOT_FOUND)
