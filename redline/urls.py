"""
Module to define urlpatterns
"""
from django.urls import path, include
from rest_framework.authtoken import views


urlpatterns = [
    path('register/', include('account.urls')),
    path('authorize/', views.obtain_auth_token, name= "authorize")
]
