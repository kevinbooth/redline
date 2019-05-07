"""
Module that handles all user specific endpoints
account/account_register_view.py
Author: Kevin Booth
Last Updated: 5/7/2019
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

from account.serializers import UserSerializer


class AccountRegisterView(APIView):
    """
    Account specific registration endpoints
    POST - Register a user account
    """
    # Disable auth token
    # Register endpoints do not require it
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, format=None):
        """
        Register a user account
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(username=serializer.data.get('username'),
                                     email=serializer.data.get('email'),
                                     password=serializer.data.get('password'),
                                     first_name=serializer.data.
                                     get('first_name'),
                                     last_name=serializer.data.get('last_name')
                                     )
            return Response(status.HTTP_200_OK)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
