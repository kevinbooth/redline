"""
Module to define urlpatterns
"""
from django.urls import path, include


urlpatterns = [
    path('user/', include('account.urls')),
]
