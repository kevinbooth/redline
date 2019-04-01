from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


class AccountRegisterView(APIView):
    """
    Account specific registration endpoints
    """
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, version, format=None):
        """
        Register a user account
        """
        user = User.objects.create_user(username=request.data.get('username'),
                                        email=request.data.get('email'),
                                        password=request.data.get('password'),
                                        first_name=request.data.get('first_name'),
                                        last_name=request.data.get('last_name'))
        if user:
            return Response(status.HTTP_201_CREATED)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
