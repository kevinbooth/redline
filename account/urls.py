"""
Module to define urlpatterns
"""
from django.urls import path
from .views import AccountRegisterView

urlpatterns = [
    path('', AccountRegisterView.as_view(), name="register"),
]
