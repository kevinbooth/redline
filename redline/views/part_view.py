from redline.models import Part
from redline.serializers import PartSerializer, PartPostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PartView(APIView):
    """
    This class handles the GET and POST actions for the Part resource.
    GET - Retrieves a list of all Parts
    POST - Creates a new Part
    """
    def get(self, request, format=None):
        parts = Part.objects.all()
        serializer = PartSerializer(parts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PartPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
