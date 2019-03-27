from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AccountRegisterView(APIView):
    """

    """

    def post(self, request, version, format=None):
        return Response('response', status=status.HTTP_201_CREATED)
