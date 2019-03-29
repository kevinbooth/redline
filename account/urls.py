"""
Module to define urlpatterns
"""
from django.urls import path
from rest_framework.authtoken import views
from .views import AccountRegisterView

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name="register"),
    path('auth/', views.obtain_auth_token, name= "auth")
]
